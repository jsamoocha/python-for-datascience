def largest_number_divisible_by_n(numbers, n):
    return max([elt for elt in numbers if elt % n == 0])
