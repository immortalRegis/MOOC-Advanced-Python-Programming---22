# Write your solution here
# If you use the classes made in the previous exercise, copy them here
class Task:
    id = 0 

    def __init__(self, description : str, programmer:str, workload:int):
        self.description = description
        self.workload = workload
        self.programmer = programmer
        self.id = Task.id + 1
        Task.id = self.id
        self.workdone = False
    
    def is_finished(self):
        return self.workdone

    def mark_finished(self):
        self.workdone = True
    
    def __str__(self):
        if self.is_finished():
            status = f'FINISHED'
        else:
            status = f'NOT FINISHED'
        
        return f'{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {status}'


class OrderBook:
    def __init__(self):
        self.orders = []
        
    
    def add_order(self, description : str, programmer:str, workload:int):
        new_task = Task(description, programmer, workload)
        self.orders.append(new_task)       


    def all_orders(self):
        return self.orders
    
    def programmers(self):
        programmers = [tk.programmer for tk in self.orders]
        return list(set(programmers))
    
    def mark_finished(self, id: int):
        not_found = True
        for ts in self.orders:
            if ts.id == id:
                ts.mark_finished()
                not_found = False
        if not_found:
            raise ValueError('No such task ')
        

    def finished_orders(self):
        return [task for task in self.orders if task.is_finished()]


    def unfinished_orders(self):
        return [task for task in self.orders if not task.is_finished()]
        

    def status_of_programmer(self, programmer: str):
        programmers_list = self.programmers()
        if programmer not in programmers_list:
            raise ValueError('No such programmer ',  programmer)

        finished = 0
        finished_hours = 0

        not_finished = 0
        not_finished_hours = 0

        for task in self.orders:
            if task.programmer == programmer:
                if task.is_finished():
                    finished += 1
                    finished_hours += task.workload
                else:
                    not_finished += 1
                    not_finished_hours += task.workload
        
        return (finished, not_finished, finished_hours, not_finished_hours)



class OrderBookApplication:
    holder = OrderBook()


    print('commands:')
    print('0 exit')
    print('1 add order')
    print('2 list finished tasks')
    print('3 list unfinished tasks')
    print('4 mark task as finished')
    print('5 programmers')
    print('6 status of programmer')


    while(True):
        print()
        command = input('command: ')
        if command == '0':
            break
        elif command == '1':
            desc  = input('description: ')
            details = input('programmer and workload estimate: ')
            details = details.split()
            correct_input_format = True

            if len(details) != 2:
                correct_input_format = False
            else:    
                name = details[0]
                try:
                    work_load = int(details[1])
                except ValueError:
                    correct_input_format = False
            if correct_input_format:
                holder.add_order(desc, name, work_load)
                print('added!')
            else:
                print('erroneous input')
        elif command == '2':
            finished = holder.finished_orders()
            if len(finished) == 0:
                print('no finished tasks')
            else:
                for tsk in finished:
                    print(tsk)
        elif command == '3':
            unfinished = holder.unfinished_orders()
            if len(unfinished) == 0:
                print(0)
            else:
                for tsk in unfinished:
                    print(tsk)
        elif command == '4':
            try:
                id = int(input('id: '))
                size = len(holder.all_orders())
                if id < 1 or id > size:
                    print('erroneous input')
                else:
                    holder.mark_finished(id)
                    print('marked as finished')
            except ValueError:
                print('erroneous input')
           
        elif command == '5':
            current_programmers = holder.programmers()
            for prog in current_programmers:
                print(prog)
        elif command == '6':
            programmer = input('programmer: ')
            current_programmers = holder.programmers()
            if programmer not in current_programmers:
                print('erroneous input')
            else:
                status = holder.status_of_programmer(programmer)
                print(f'tasks: finished {status[0]} not finished {status[1]}, hours: done {status[2]} scheduled {status[3]}')