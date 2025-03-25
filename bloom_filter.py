import math
import mmh3
from bitarray import bitarray

class BloomFilter:
    def __init__(self, capacity, error_rate=0.001):
        """
        Initialize a Bloom Filter
        
        Args:
            capacity: Expected number of elements to be inserted
            error_rate: Desired false positive probability
        """
        self.capacity = capacity
        self.error_rate = error_rate
        
        # Calculate optimal size and number of hash functions
        self.size = self._calculate_size(capacity, error_rate)
        self.hash_count = self._calculate_hash_count(self.size, capacity)
        
        self.bit_array = bitarray(self.size)
        self.bit_array.setall(0)
    
    def _calculate_size(self, capacity, error_rate):
        """Calculate optimal bit array size"""
        size = -capacity * math.log(error_rate) / (math.log(2) ** 2)
        return math.ceil(size)
    
    def _calculate_hash_count(self, size, capacity):
        """Calculate optimal number of hash functions"""
        hash_count = size / capacity * math.log(2)
        return math.ceil(hash_count)
    
    def add(self, item):
        """Add an item to the Bloom filter"""
        for i in range(self.hash_count):
            # Use different seeds for each hash function
            index = mmh3.hash(str(item), i) % self.size
            self.bit_array[index] = 1
    
    def contains(self, item):
        """
        Check if an item might be in the Bloom filter
        
        Returns:
            bool: False if item is definitely not in the filter
                  True if item might be in the filter
        """
        for i in range(self.hash_count):
            index = mmh3.hash(str(item), i) % self.size
            if self.bit_array[index] == 0:
                return False
        return True
    
    def __contains__(self, item):
        """Support for 'in' operator"""
        return self.contains(item)
    
    def __str__(self):
        """String representation of the Bloom filter"""
        return (f"BloomFilter(size={self.size}, "
                f"hash_functions={self.hash_count}, "
                f"capacity={self.capacity}, "
                f"error_rate={self.error_rate})")


# Example usage
if __name__ == "__main__":
    # Create a Bloom filter with capacity for 1000 items and 0.1% error rate
    bloom = BloomFilter(1000, 0.001)
    
    # Add some items
    bloom.add("apple")
    bloom.add("banana")
    bloom.add("orange")
    
    print(f"Contains 'apple': {'apple' in bloom}")
    print(f"Contains 'banana': {'banana' in bloom}")
    print(f"Contains 'grape': {'grape' in bloom}")
    
    for i in range(1000):
        bloom.add(f"item{i}")
    
    print(f"False positive test - Contains 'missing_item': {'missing_item' in bloom}")
    
    print(bloom)
