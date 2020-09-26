def variance(numbers):
    mu = sum(numbers) / len(numbers)
    return sum([(n - mu) ** 2 for n in numbers]) / len(numbers)
