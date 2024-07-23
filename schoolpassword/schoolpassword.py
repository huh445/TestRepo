import itertools
import time

def generate_and_write_combinations():
    letters = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    suffix = "PC"

    with open('output.txt', 'w') as f:
        # Generate all combinations of 3 letters
        for combo in itertools.product(letters, repeat=3):
            combo_str = ''.join(combo)
            # Generate all combinations of 3 numbers
            for nums in itertools.product(numbers, repeat=3):
                password = combo_str + ''.join(nums) + suffix
                f.write(password + '\n')  # Write each password to file

def measure_generation_time():
    start_time = time.time()
    generate_and_write_combinations()  # Generate and write to file
    end_time = time.time()
    return end_time - start_time

if __name__ == '__main__':
    iterations = 3  # Set to 1 for a single run
    times = []

    for _ in range(iterations):
        elapsed_time = measure_generation_time()
        times.append(elapsed_time)
        print(f"List generation time: {elapsed_time:.2f} seconds")

    average_time = sum(times) / iterations
    print(f"Average generation time: {average_time:.2f} seconds")
