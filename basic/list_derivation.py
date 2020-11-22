# 列表推导式生成质数
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numbers_prime = [number for number in range(1, 10) if 0 not in [number % i for i in range(2, number)]]
print(numbers_prime)





