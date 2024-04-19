def sort_array(array_text):
    new_array = []
    for i in range(len(array_text)):
        element = max(array_text)
        new_array.append(element)
        array_text.remove(element)
