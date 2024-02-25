def determine(coins):
    right_diagonal = 0
    left_diagonal = 0
    for i in coins:
        if i[0]>=4 or i[1]>=4 or i[0]<=0 or i[1]<=0:
            return 'INVALID INPUT'
        if i[0]==i[1]:
            left_diagonal +=1
        if sum(i)==4:
            right_diagonal +=1
    if right_diagonal == 3 or left_diagonal == 3 :
        return 'WIN'
    if (coins[0][0]==coins[1][0]==coins[2][0]) or (coins[0][1]==coins[1][1]==coins[2][1]):
        return 'WIN'
    return 'LOST'

def main():
    t = int(input('Enter number of inputs: '))
    for _ in range(t):
        coins= []
        a = int(input('Row position of first coin: '))
        b = int(input('Column position of first coin: '))
        coins.append([a,b])
        a = int(input('Row position of second coin: '))
        b = int(input('Column position of second coin: '))
        coins.append([a,b])
        a = int(input('Row position of third coin: '))
        b= int(input('Column position of third coin: '))
        coins.append([a,b])
        print(coins)
        print(determine(coins))
        print('-------------------------------')
if __name__ == "__main__":
    main()