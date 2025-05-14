class HashTable:
    def __init__(self):
        self.table = [None] * 10

    def _hash(self, key):
        return hash(key) % len(self.table)

    def insert(self, key, value):
        h = self._hash(key)
        self.table[h] = value

    def get(self, key):
        h = self._hash(key)
        return self.table[h]
