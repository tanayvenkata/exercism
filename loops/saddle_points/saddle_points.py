def saddle_points(matrix):
    is_irregular(matrix)

    largest_in_row = get_highest_in_rows(matrix)
    potential_trees = get_smallest_in_column(largest_in_row, matrix)

    return [{"row": tree[0]+1, "column": tree[1]+1} for tree in potential_trees]

def is_irregular(matrix):
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise ValueError("irregular matrix")

def get_highest_in_rows(matrix):
    number_and_location = []

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == max(matrix[i]):
                number_and_location.append([matrix[i][j], i, j])

    # returning [value, row, col]
    return number_and_location

def get_smallest_in_column(num_loc, matrix):
    potential_trees = []
    for point in num_loc:
        column = []
        for i in range(len(matrix)):
            column.append(matrix[i][point[2]])

        if point[0] == min(column):
            potential_trees.append([point[1], point[2]])

    return potential_trees


matrix = [[4, 5, 4], 
          [3, 5, 5], 
          [1, 5, 4]]

#print(saddle_points(matrix))

x = (get_highest_in_rows(matrix))
#print(get_smallest_in_column(x))
print(saddle_points(matrix))