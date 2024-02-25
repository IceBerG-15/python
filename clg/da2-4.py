def main():
    t = int(input("Number of inputs: "))
    for _ in range(t):
        n = float(input('Enter Ritcher scale number: '))
        if n<0:
            print('INVALID INPUT')
        elif n<5.0:
            print('Little or no damage')
        elif 5.0<=n<5.5:
            print('Some damage')
        elif n>5.5:
            print('Serious damage')
        print('----------------------------')
if __name__ == "__main__":
    main()