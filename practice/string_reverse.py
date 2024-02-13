# string reversal
def str_rev():
    n = input("enter the string: ")
    print("reverse of the given string: ", n[-1::-1])
    if n==n[-1::-1]: # palindrome checking.
        print("palindrome.")
    else:
        print("not a palindrome.")
# ---------------------------------------------------------------------------------
# multiple list operations..
def list_max():
    l = [4,6,8,89,3,100,4,4]
    print("length of the list: ",len(l)) # length of the list
    print("max of list: ", max(l))  # max of list
    l = set(l) #set has a property of storing only unique elements in it. It removes duplicates.
    print("unique elements of the list: ",l) # unique elements of the list
# ---------------------------------------------------------------------------------
# factorial
def factorial():
    n = int(input("enter the number: "))
    fact = 1
    for i in range(1,n+1): 
        fact = fact*i
    print(f"factorial of {n} : {fact}")
# ---------------------------------------------------------------------------------
# main function
def main():
    factorial()
# ---------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
    
