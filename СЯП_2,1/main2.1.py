import random
def is_prime(number):
    if number < 2:  # числа меньше 2 не являются простыми
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:  # если число делится нацело на другое число, оно не является простым
            return False
    return True
random_number = random.randint(1, 1000)

print(is_prime(random_number))