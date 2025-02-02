from threading import Thread
def square_numbers(numbers):
    for number in numbers:
        print(f"Sqare: {number + number}")
def cube_numbers(numbers):
    for number in numbers:
        print(f"Cube: {number + number + number}")

nums = [1, 2, 3, 4, 5, 6, 7, 8]

t1 = Thread(target=square_numbers, args=(nums,))
t2 = Thread(target=cube_numbers, args=(nums,))

t1.start()
t2.start()

t1.join()
t2.join()