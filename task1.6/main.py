# 9 -1 3 7 -5 -7 1 3 -3 2 1 -8

# selection
def sort(for_sort):
    result = for_sort.copy()
    for number in range(len(result)):
        min = result[number]
        if min <= 0:
            continue
        min_index = number
        for i in range(number + 1, len(result)):
            if result[i] <= 0:
                continue
            if result[i] < min:
                min = result[i]
                min_index = i
        if min_index != number:
            result[number], result[min_index] = result[min_index], result[number]
    return result


if __name__ == '__main__':
    arr = list(map(int, input().split()))
    print("input: ", arr)
    sorted_arr = sort(arr)
    print("sorted: ", sorted_arr)
