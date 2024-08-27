import statistics

def read_numbers_and_find_median(file_path):
    with open(file_path, 'r') as file:
        numbers = [int(line.strip()) for line in file]
    return statistics.median(numbers)

print("Median:", read_numbers_and_find_median('integers.txt'))
