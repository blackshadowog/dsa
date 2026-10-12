# check if num is armsstorng number
def is_armstrong(num):
    original_num = num
    num_of_digits = len(str(num))
    sum_of_powers = 0

    while num > 0:
        digit = num % 10
        sum_of_powers += digit ** num_of_digits
        num //= 10

    return original_num == sum_of_powers