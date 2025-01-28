# Provided table data (just the second column values)
sequence_data = [
    0, 1, 0, 0, 0, 2, 0, 1, 0, 0, 0, 2, 0, 1, 0, 0,
    0, 2, 0, 1, 0, 0, 0, 2, 0, 1, 0, 0, 0, 2, 0, 1,
    0, 0, 0, 2, 0, 1, 0, 0, 0, 2, 0, 1, 0, 0, 0, 2,
    0, 1, 0, 0, 0, 2, 0, 1, 0, 0, 0, 2, 0, 1, 0, 0,
    0, 2, 0, 1, 0, 0, 0, 2, 0, 1, 0, 0, 0, 2, 0, 1,
    0, 0, 0, 2, 0, 1, 0, 0, 0, 2, 0, 1, 0, 0, 0, 2,
    0, 1, 0, 0, 0, 2, 0, 1, 0, 0, 0, 2, 0, 1, 0, 0,
    0, 2, 0, 1, 0, 0, 0, 2, 0, 1, 0, 0, 0, 2, 0, 1
]

# The pattern to search for
given_sequence = [0, 2, 0, 1, 0, 0, 0, 2, 0, 1, 0, 0, 0]

# Function to find the pattern in the sequence
def find_pattern_in_sequence(given_sequence, sequence_data):
    # Try to find the given sequence as a sublist within the sequence data
    for i in range(len(sequence_data) - len(given_sequence) + 1):
        if sequence_data[i:i+len(given_sequence)] == given_sequence:
            return i  # Return the index where the pattern is found
    return -1  # Return -1 if no match is found

# Find the pattern in the sequence
pattern_index = find_pattern_in_sequence(given_sequence, sequence_data)

# Print the result
if pattern_index != -1:
    print(f"The given sequence is found starting at index {pattern_index} in the sequence (ignoring the first column).")
else:
    print("The given sequence is not found in the sequence.")

# Optionally, print part of the sequence for inspection
print(f"Given sequence: {given_sequence}")
print(f"Sequence data (first 100 elements, ignoring the first column): {sequence_data[4:1000]}")
