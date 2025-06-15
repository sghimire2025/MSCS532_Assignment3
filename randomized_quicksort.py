import random
import time

def randomized_quicksort(arr):
    # Base case: an array of 0 or 1 elements is already sorted
    if len(arr) <= 1:
        return arr

    # Pick a random pivot index and get the pivot value
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]

    # Partition the array into two lists:
    # - less_than_or_equal: all elements less than or equal to pivot (excluding the pivot itself)
    # - greater_than: all elements greater than pivot
    less_than_or_equal = []
    greater_than = []

    for i, value in enumerate(arr):
        if i == pivot_index:
            continue  # skip the pivot element itself
        if value <= pivot:
            less_than_or_equal.append(value)
        else:
            greater_than.append(value)

    # Recursively sort both partitions and combine with pivot in the middle
    return randomized_quicksort(less_than_or_equal) + [pivot] + randomized_quicksort(greater_than)

#function to print the array
def print_array(label, array):
    max_display = 10
    if len(array) > max_display:
        print(f"{label}: {array[:max_display]}... (total {len(array)} elements)")
    else:
        print(f"{label}: {array}")


#function to call sorting
def test_sorting():
    test_cases = [
        ("Repeated Elements", [5,3,8,3,9,3,1,5,5,5,5,5,5,3,2,2,2,4,4,4,2,3,1,1,0]),
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
        sorted_array = randomized_quicksort(test_input)
        end_time = time.perf_counter()
        execution_time = end_time - start_time

        print(f"Execution Time: {execution_time:.6f} seconds")
        print_array("Sorted Output", sorted_array)

if __name__ == "__main__":
    test_sorting()
