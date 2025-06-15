class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.count = 0
        self.table = [[] for _ in range(self.size)]

    def _hash_function(self, key):
        """simple hash function"""
        return hash(key) % self.size

    def _resize(self):
        """Double the table size and rehash all entries when load factor exceedd it's initial size"""
        old_table = self.table
        self.size *= 2
        self.table = [[] for _ in range(self.size)]
        self.count = 0

        for chain in old_table:
            for key, value in chain:
                self.insert(key, value)

    def insert(self, key, value):
        """Insert or update a key-value pair"""
        index = self._hash_function(key)
        chain = self.table[index]

        for i, (k, _) in enumerate(chain):
            if k == key:
                chain[i] = (key, value)
                return

        chain.append((key, value))
        self.count += 1

        # Resize if load factor exceeds 0.75
        if self.count / self.size > 0.75:
            self._resize()

    def search(self, key):
        """Search for a value by key"""
        index = self._hash_function(key)
        chain = self.table[index]
        for k, v in chain:
            if k == key:
                return v
        return None

    def delete(self, key):
        """Remove a key from the table"""
        index = self._hash_function(key)
        chain = self.table[index]
        for i, (k, _) in enumerate(chain):
            if k == key:
                del chain[i]
                self.count -= 1
                return True
        return False

    def display(self):
        """Print the entire hash table"""
        for i, chain in enumerate(self.table):
            print(f"Index {i}: {chain}")

    def load_factor(self):
        """Returns current load factor"""
        return self.count / self.size


# Example usage
if __name__ == "__main__":
    ht = HashTable(size=7)
    ht.insert("california", 1)
    ht.insert("texas", 2)
    ht.insert("new york", 3)
    ht.insert("georgia", 4)  
    ht.insert("florida", 5)
    ht.insert("virginia", 6)
    ht.insert("maryland", 7)  

    print("Search 'texas':", ht.search("texas"))
    print("Search 'florida':", ht.search("florida"))
    print("Search 'alaska':", ht.search("alaska"))  # Not found

    print("\nFinal Hash Table (after insertions and possible resizing):")
    ht.display()

    print(f"\nLoad Factor: {ht.load_factor():.2f}")
