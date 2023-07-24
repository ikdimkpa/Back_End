#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    sum_up = 0
    for i in range(x):
        try:
            print(f"{my_list[i]}", end="")
            sum_up += 1
        except IndexError:
            break
    print()
    return(sum_up)
