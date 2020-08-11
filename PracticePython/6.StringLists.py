#%%
#Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

def u_input() -> str:
    while True:
        string = input("Insert a word: ")
        if len(string) > 0 and string.isalpha():
            return string

def palindrome_check(string: str) -> bool:
    l_str = list(string)
    if l_str == l_str[::-1]:
        return True
    else:
        return False

my_str = u_input()
result = palindrome_check(my_str)
print(f"Is it a palindrome? {result}")
