# Write your solution here
def prime_numbers():
    cur_prime = 2
    yield cur_prime
    cur_prime += 1

    st_pt = 2
    while(True):
        for i in range(st_pt, cur_prime):
            num_prime = True
            #print(f'iterator value is currently {i}')
            #print(f'{cur_prime} is the current value')
            if cur_prime % i == 0:
                #print(f'remainder = {cur_prime % i}')
                cur_prime += 2
                num_prime = False
                break
        if num_prime:
            yield cur_prime
            cur_prime += 2

            
        


    