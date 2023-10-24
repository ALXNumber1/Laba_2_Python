def process_input(data):
    if isinstance(data, tuple):
        total_length = 0
        for word in data:
            total_length += len(word)
        return total_length
    elif isinstance(data, list):
        unique_list = list(set(data))
        if unique_list.count(0) >= 2:
            index_first_zero = unique_list.index(0)
            index_second_zero = unique_list.index(0, index_first_zero + 1)
            return unique_list[index_first_zero] * unique_list[index_second_zero]
        else:
            return "Not enough zeros in the list"
    elif isinstance(data, int):
        if is_prime(data):
            return "Prime number"
        else:
            return "Not a prime number"
    elif isinstance(data, str):
        unicode_codes = []
        for char in data:
            unicode_codes.append(ord(char))
        return unicode_codes
    else:
        return "Invalid input"


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True