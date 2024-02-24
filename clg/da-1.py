#function to convert decimal number to binary 
def dec_to_bin(num:str)->str:  
    num = int(num)
    ans = ''
    while num>0:
        ans += str(num%2)
        num = num//2
    return ans[::-1]
#function to convert decimal number to octal
def dec_to_octal(num:str)->str: 
    num = int(num)
    ans = ''
    while num>0:
        ans += str(num%8)
        num = num//8
    return ans[::-1]
#function to convert decimal number to hexadecimal
def dec_to_hex(num:str)->str:   
    num = int(num)
    ans = ''
    while num>0:
        rem = num%16
        if rem<10:
            ans +=str(rem)
        elif rem == 10:
            ans += 'A'
        elif rem == 11:
            ans += 'B'
        elif rem == 12:
            ans += 'C'
        elif rem == 13:
            ans += 'D'
        elif rem == 14:
            ans += 'E'
        elif rem == 15:
            ans += 'F'
        num = num//16
    return ans[::-1]
#function to convert binary number to decimal
def bin_to_dec(num:str)->str:   
    ans = 0
    count = 0
    for i in num[::-1]:
        if i=='1':
            ans += 2**count
        count +=1
    return str(ans)
#function to convert binary number to octal
def bin_to_octal(num:str)->str:
    return dec_to_octal(bin_to_dec(num))
#function to convert binary number to hexadecimal
def bin_to_hex(num:str)->str:
    return dec_to_hex(bin_to_dec(num))
#function to convert octal to decimal
def octal_to_dec(num:str)->str:
    count = 0 
    ans = 0
    for i in num[::-1]:
        ans += int(i)*(8**count)
        count +=1
    return str(ans)
#function to convert octal to binary
def octal_to_bin(num:str)->str:
    return dec_to_bin(octal_to_dec(num))
#function to convert hexadecimal to decimal
def hex_to_dec(num:str)->str:
    count = 0 
    ans = 0
    for i in num[::-1]:
        if i == 'A':
            j = 10
        elif i == 'B':
            j = 11
        elif i == 'C':
            j = 12
        elif i == 'D':
            j = 13
        elif i == 'E':
            j = 14
        elif i == 'F':
            j = 15
        else:
            j = int(i)
        ans += j*(16**count)
        count +=1
    return str(ans)
#function to convert hexadecimal to binary
def hex_to_bin(num:str)->str:
    return dec_to_bin(hex_to_dec(num))
#----------------------------------------------
#main function
def main():
    ch = 0
    while ch!= 11:
        print("MENU: ")
        print("1- decimal to binary \n2- decimal to octal \n3- decimal to hexadecimal")
        print("4- binary to octal \n5- binary to hexadecimal \n6- binary to decimal ")
        print("7- octal to decimal \n8- octal to binary ")
        print("9- hexadecimal to decimal \n10- hexadecimal to binary ")
        print("11- EXIT")
        print("--------------------------------------")
        ch = int(input("Enter your choice: "))
        match ch:
            case 1:
                print('Answer: '+dec_to_bin(input("Enter the number: ")))
            case 2:
                print('Answer: '+dec_to_octal(input("Enter the number: ")))
            case 3:
                print('Answer: '+dec_to_hex(input("Enter the number: ")))
            case 4:
                print('Answer: '+bin_to_octal(input("Enter the number: ")))
            case 5:
                print('Answer: '+bin_to_hex(input("Enter the number: ")))
            case 6:
                print('Answer: '+bin_to_dec(input("Enter the number: ")))
            case 7:
                print('Answer: '+octal_to_dec(input("Enter the number: ")))
            case 8:
                print('Answer: '+octal_to_bin(input("Enter the number: ")))
            case 9:
                print('Answer: '+hex_to_dec(input("Enter the number: ")))
            case 10:
                print('Answer: '+hex_to_bin(input("Enter the number: ")))
            case 11:
                print('Successfully exited!!')
                exit()
            case default:
                print("Invalid choice")
# -----------------------------------
if __name__ == '__main__':
    main()