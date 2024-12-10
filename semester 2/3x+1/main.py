import matplotlib.pyplot as plt

even_nums = [0, 2, 4, 6, 8]
highest_counts = {}

# Generate sequences
for i in range(1, 1001):  # Change range to 1-1000 for full dataset
    num = i
    sequence = []
    while num != 1:
        if num % 10 in even_nums:  # Check if the last digit is even
            num //= 2
        else:
            num = 3 * num + 1
        sequence.append(num)
    highest_counts[i] = sequence

# Plot each sequence
plt.figure(figsize=(12, 8))
for start, sequence in highest_counts.items():
    plt.plot(sequence, label=f"Start: {start}")

# Customize the graph
plt.xlabel("Steps")
plt.ylabel("Value")
plt.title("Collatz Sequence Progressions (1-10)")
plt.legend()
plt.grid(True)
plt.show()
