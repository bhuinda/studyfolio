import math

def metallic_mean(n):
    """
    Calculate the n-th metallic mean.

    Parameters:
        n (int): The index of the metallic mean (e.g., 1 for the golden ratio, 2 for the silver ratio).

    Returns:
        float: The value of the n-th metallic mean.
    """
    return (n + math.sqrt(n**2 + 4)) / 2

# Example usage:
if __name__ == "__main__":
    n = int(input("Enter the index of the metallic mean (e.g., 1 for golden ratio): "))
    result = metallic_mean(n)
    print(f"The {n}-th metallic mean is: {result}")