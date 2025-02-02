def get_biggest(numbers:list) -> int:
    return int(''.join(sorted(list(map(str, numbers)), reverse=True, key = lambda x: str(x*10)))) if len(numbers)else-1
print(get_biggest([1, 2, 3, 4, 5]))