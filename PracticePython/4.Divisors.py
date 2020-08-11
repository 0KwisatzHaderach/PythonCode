#%%
#Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

#nums = [25, 50, 101, 151, 203]

def u_input() -> int:
    while True:
        number = input("please input a natural number: ")
        try: 
            return int(number)
        except:
            print("You must print an integer")

def find_divisors() -> list:
    number = u_input()
    divisors = [i for i in range(1,number+1) if number % i == 0 ]
    print(divisors)

find_divisors()
