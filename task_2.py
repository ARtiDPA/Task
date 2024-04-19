def generate_array(mim_num, max_num):
    def check_num(num):

        score = 0
        for i in range(1, num + 1):
            if num % i == 0:
                score += 1

        if score == 2:
            return True
        return False

    new_array = []

    for i in range(mim_num, max_num + 1):
        if check_num(i):
            new_array.append(i)

    return new_array

