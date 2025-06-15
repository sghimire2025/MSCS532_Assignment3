import time

def deterministic_quicksort(arr):
    # Base case: 0 or 1 element
    if len(arr) <= 1:
        return arr

    # Use the first element as pivot
    pivot = arr[0]
    less_than_or_equal = [x for x in arr[1:] if x <= pivot]
    greater_than = [x for x in arr[1:] if x > pivot]

    # Recursively sort and combine
    return deterministic_quicksort(less_than_or_equal) + [pivot] + deterministic_quicksort(greater_than)

# function to print the array
def print_array(label, array):
    max_display = 10
    if len(array) > max_display:
        print(f"{label}: {array[:max_display]}... (total {len(array)} elements)")
    else:
        print(f"{label}: {array}")

# Function to test sorting performance and correctness
def test_sorting():
    test_cases = [
        ("Repeated Elements", [5, 3, 8, 3, 9, 3, 1, 5, 5, 5, 5, 5, 5, 3, 2, 2, 2, 4, 4, 4, 2, 3, 1, 1, 0]),
        ("Empty Array", []),
        ("Already Sorted", list(range(100))),
        ("Reverse Sorted", list(range(100, 0, -1))),
        ("Large Random Array", [random.randint(0, 10000) for _ in range(100000)])
    ]

    for test_type, test_input in test_cases:
        print(f"\nTest Case Type: {test_type}")
        print(f"Input Size: {len(test_input)}")
        print_array("Original Array", test_input)

        start_time = time.perf_counter()
        sorted_array = deterministic_quicksort(test_input)
        end_time = time.perf_counter()
        execution_time = end_time - start_time

        print(f"Execution Time: {execution_time:.6f} seconds")
        print_array("Sorted Output", sorted_array)

if __name__ == "__main__":
    import random
    test_sorting()
