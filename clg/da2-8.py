def print_diagonal_positions(row, col):
    major_diagonal_up = []
    major_diagonal_down = []
    minor_diagonal_up = []
    minor_diagonal_down = []
    for i in range(1, 9):
        next_row = row + i
        next_col = col + i
        if 1 <= next_row <= 8 and 1 <= next_col <= 8:
            major_diagonal_up.append((next_row, next_col))
    for i in range(1, 9):
        next_row = row - i
        next_col = col - i
        if 1 <= next_row <= 8 and 1 <= next_col <= 8:
            major_diagonal_down.append((next_row, next_col))
    for i in range(1, 9):
        next_row = row + i
        next_col = col - i
        if 1 <= next_row <= 8 and 1 <= next_col <= 8:
            minor_diagonal_up.append((next_row, next_col))
    for i in range(1, 9):
        next_row = row - i
        next_col = col + i
        if 1 <= next_row <= 8 and 1 <= next_col <= 8:
            minor_diagonal_down.append((next_row, next_col))
    major_diagonal_up.sort()
    minor_diagonal_up.sort()
    major_diagonal_down.sort(reverse=True)
    minor_diagonal_down.sort(reverse=True)
    for pos in major_diagonal_up:
        print(f"({pos[0]},{pos[1]})")
    for pos in major_diagonal_down:
        print(f"({pos[0]},{pos[1]})")
    for pos in minor_diagonal_up:
        print(f"({pos[0]},{pos[1]})")
    for pos in minor_diagonal_down:
        print(f"({pos[0]},{pos[1]})")

# main function
def main():
    current_row = int(input("Enter current row position of the coin (1-8): "))
    current_col = int(input("Enter current column position of the coin (1-8): "))
    if 1 <= current_row <= 8 and 1 <= current_col <= 8:
        print_diagonal_positions(current_row, current_col)
    else:
        print("Invalid input!")

if __name__ == "__main__":
    main()
