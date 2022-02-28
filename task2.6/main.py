

def sort(for_sort):
    for number in range(len(for_sort[0])):
        min_index = number
        for i in range(number + 1, len(for_sort[0])):
            if compare(matrix, min_index, i) < 0:
                min_index = i
        if min_index != number:
            swap(for_sort, number, min_index)


def compare(matrix, col1, col2):
    for row in range(len(matrix) - 1):
        if matrix[row][col2] != matrix[row][col1]:
            return matrix[row][col2] - matrix[row][col1]
    return matrix[len(matrix) - 1][col2] - matrix[len(matrix) - 1][col1]


def swap(matrix, col1, col2):
    for row in range(len(matrix)):
        matrix[row][col2], matrix[row][col1] = matrix[row][col1], matrix[row][col2]


if __name__ == '__main__':
    input_str = input()
    matrix = []
    while input_str != '':
        matrix.append([int(j) for j in input_str.split()])
        input_str = input()
    print("input: ")
    for row in matrix:
        print(' '.join([str(elem) for elem in row]))
    sort(matrix)
    print("sorted: ")
    for row in matrix:
        print(' '.join([str(elem) for elem in row]))
