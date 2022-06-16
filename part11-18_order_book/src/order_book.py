# Write your solution here:
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









