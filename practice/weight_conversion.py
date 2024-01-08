#weight conversion from kg to lbs and vice versa...
def kg_to_lbs(x):
    return round(x*2.2,2)

def lbs_to_kg(x):
    return round(x/2.2,2)

def main():
    x = int(input('enter weight: '))
    c = input('lbs(l) or kg(k): ')
    if c == 'k' or c == 'K':
        a = kg_to_lbs(x)
    else:
        a = lbs_to_kg(x)
    print('weight is: ',a)
    
if __name__ == '__main__':
    main()