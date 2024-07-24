import itertools
import time

def generate_combinations():
    letters = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    suffix = "PC"
    
    # Generate all combinations of 3 letters
    all_combinations = []
    for combo in itertools.product(letters, repeat=3):
        combo_str = ''.join(combo)
        for nums in itertools.product(numbers, repeat=3):
            all_combinations.append(combo_str + ''.join(nums) + suffix)
    
    return all_combinations

def write_combinations_to_file(combinations):
    with open('output.txt', 'w') as f:
        f.write('\n'.join(combinations) + '\n')

def measure_generation_time():
    start_time = time.time()
    all_combinations = generate_combinations()  # Generate all combinations
    write_combinations_to_file(all_combinations)  # Write to file
    end_time = time.time()
    return end_time - start_time

if __name__ == '__main__':
    iterations = 3  # Number of iterations for timing
    times = []

    for _ in range(iterations):
        elapsed_time = measure_generation_time()
        times.append(elapsed_time)
        print(f"List generation time: {elapsed_time:.2f} seconds")

    average_time = sum(times) / iterations
    print(f"Average generation time: {average_time:.2f} seconds")
