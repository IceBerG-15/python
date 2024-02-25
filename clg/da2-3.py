def conditions(hardness,carbon,tensile):
    a,b,c = False,False,False
    if hardness<0 or carbon<0 or tensile<0:
        print('INVALID INPUT')
        return False, False, False
    if hardness>60:
        a = True
    if carbon<0.9:
        b = True
    if tensile>6000:
        c = True
    return a,b,c

def grade(a,b,c):
    if a and b and c:
        return 10
    elif a and b:
        return 9
    elif b and c:
        return 8
    return None

def main():
    n = int(input('Enter n:'))
    for _ in range(n):
        hardness = float(input('Enter hardness: '))
        carbon = float(input('Enter carbon content: '))
        tensile = float(input('Enter tensile strength: '))
        a,b,c = conditions(hardness,carbon,tensile)
        print(f"Grade: {grade(a,b,c)}")
        print('-------------------------------')

if __name__ == '__main__':
    main()