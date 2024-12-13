def main():
    file = open('input11.txt', 'r')
    grid = [line.split() for line in file]
    maxProduct = 0
    for r in range(4, len(grid) - 4):
        for c in range(4, len(grid[r]) - 4):
            topLeft = int(grid[r - 1][c - 1]) * int(grid[r - 2][c - 2]) * int(grid[r - 3][c - 3]) * int(grid[r - 4][c - 4])
            up = int(grid[r - 1][c]) * int(grid[r - 2][c]) * int(grid[r - 3][c]) * int(grid[r - 4][c])
            topRight = int(grid[r - 1][c + 1]) * int(grid[r - 2][c + 2]) * int(grid[r - 3][c + 3]) * int(grid[r - 4][c + 4])
            left = int(grid[r][c - 1]) * int(grid[r][c - 2]) * int(grid[r][c - 3]) * int(grid[r][c - 4])
            right = int(grid[r][c + 1]) * int(grid[r][c + 2]) * int(grid[r][c + 3]) * int(grid[r][c + 4])
            bottomLeft = int(grid[r + 1][c - 1]) * int(grid[r + 2][c - 2]) * int(grid[r + 3][c - 3]) * int(grid[r + 4][c - 4])
            down = int(grid[r + 1][c]) * int(grid[r + 2][c]) * int(grid[r + 3][c]) * int(grid[r + 4][c])
            bottomRight = int(grid[r + 1][c + 1]) * int(grid[r + 2][c + 2]) * int(grid[r + 3][c + 3]) * int(grid[r + 4][c + 4])
            maxProduct = max(maxProduct, topLeft, up, topRight, left, right, bottomLeft, down, bottomRight)
    print(maxProduct)


if __name__ == '__main__':
    main()