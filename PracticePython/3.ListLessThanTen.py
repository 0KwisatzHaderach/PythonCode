#%%
#Take a list, say for example this one:
#
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#
# and write a program that prints out all the elements of the list that are less than 5.
#
# Extras:
#
#     Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
#     Write this in one line of Python.
#     Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.

def u_input() -> int:
    while True:
        number = input("please input a natural number: ")
        try: 
            return int(number)
        except:
            print("You must print an integer")

def solution(int_list: list, my_number: list) -> list:
    b = [i for i in int_list if i < 10]
    c = [i for i in int_list if i < my_number]
    return b, c

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
my_number = u_input()

il, ul = solution(a, my_number)
print(f"the lists are {il} and {ul}")

# %%
