

grid = [['-','-','-','#','#'],
        ['-','#','-','-','-'],
        ['-','-','#','-','-'],
        ['-','#','#','-','-'],
        ['-','-','-','-','-']]

#Check if row and column are within bounds of grid
def checkposition(grid, row, col):
    return 0 <= row < len(grid) and 0<= col < len(grid[0])

#Checking positions around our cell and add count to give no. of bombs
def countmines(grid, row, col):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0
    for dr, dc in directions:
        new_row, new_column = row + dr, col + dc
        if checkposition(grid, new_row, new_column) and grid[new_row][new_column]=="#":
            count += 1
    return count

#Function to transform grid into one that shows mine counts
def minesweepeer(grid):
    result = []
    for row in range(len(grid)):
        result_row = []
        for col in range(len(grid)):
            if grid[row][col]=="#":
                result_row.append("#")
            else:
                result_row.append(str(countmines(grid, row, col)))
        result.append(result_row)
    return result

#Execute and call function 
output_grid = minesweepeer(grid)

for row in output_grid:
    print(" ".join(row))
