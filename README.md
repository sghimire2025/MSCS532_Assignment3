# MSCS532 Assignment 3
## Author
- Suresh Ghimire
- Email:[sghimire38288@ucumberlands.edu]


##  Contents
-  Part 1: Randomized Quicksort Analysis
-  Part 2: Hash Table with Chaining
-  Performance Analysis
    
---


### 1. Requirements
You only need **Python 3.x** to run this script. No external libraries are required.

### 2. Running the Script

Download and run the script using:

```bash
python randomized_quicksort.py
python deterministic_quicksort.py
python hashing_and_chaining.py
```

## Part 1: Randomized Quicksort Anlysis
This will:
- Execute the `randomized_quicksort` on large arrays (1000 and 2000 elements),
- Repeat sorting 1000 times per test to get an accurate average runtime,
- Print out the input size, average runtime, and a sample of sorted output.

---

## Test Cases

The following datasets are tested:
- `Large Random (1000 elems)`
- `Large Random (2000 elems)`

---

## Findings Summary

- **Performance is efficient and stable** due to randomized pivot selection.
- **Average runtimes** on a typical machine (per 1000 runs):
  - 1000 elements: ~0.0003 - 0.0006 seconds
  - 2000 elements: ~0.0007 - 0.0012 seconds
- **Edge-case robustness**:
  - Works correctly with empty, repeated, sorted, and reversed arrays.
- **Time measurement**:
  - `time.perf_counter()` is used for high-precision timing.
  - Repeated runs help average out CPU scheduling noise.

---

## Part 2: Hash with Chaining

This part of the assignment implements a **Hash Table** using **Chaining** to resolve hash collisions. It supports key operations:

- `insert(key, value)`
- `search(key)`
- `delete(key)`
- **Dynamic resizing** is triggered when the load factor exceeds **0.75**, doubling the table size.

###  Sample Output
```text
Search 'texas': 2
Search 'florida': 5
Search 'alaska': None

Final Hash Table:
Index 0: [('georgia', 4)]
Index 3: [('california', 1)]
Index 4: [('new york', 3)]
Index 6: [('florida', 5), ('virginia', 6)]
Index 12: [('maryland', 7)]
Index 13: [('texas', 2)]

Load Factor: 0.50

