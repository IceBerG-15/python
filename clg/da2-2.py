def average(marks):
    for i in marks:
        if i<0 or i>100:
            print("INVALID INPUT")
            return False,None
    return True,(sum(marks)/len(marks))

def main():
    t = int(input("Enter number of students: "))
    for _ in range(t):
        marks = []
        n = int(input('Enter n: '))
        for _ in range(n):
            marks.append(int(input("Enter marks: ")))
        valid,a = average(marks)
        if valid:
            print(f"Average marks: {a:.2f}")
            print('------------------------')

if __name__ == '__main__':
    main()