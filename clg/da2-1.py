def minimum(costs):
    for i in costs:
        if i<=0:
            print("INVALID INPUT")
            return False,None
    return True,min(costs)

def main():
    n = int(input("enter n: "))
    for _ in range(n):
        costs = []
        for _ in range(5):
            costs.append(int(input("Enter cost: ")))
        valid,cost = minimum(costs)
        if valid:
            print(f"Minimum cost: {cost}")
            print('------------------------')

if __name__ == '__main__':
    main()