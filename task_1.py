def sort(array):
    new_array = []

    for i in array:
        if i not in new_array:
            new_array.append(i)

    return new_array
