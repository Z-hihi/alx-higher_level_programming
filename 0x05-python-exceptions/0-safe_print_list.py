#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    if (x > 0):
        for i in range(x):
            try:
                print(f"{my_list[i]}", end="")
                count = count + 1
            except Exception:
                break
    print()
    return count
