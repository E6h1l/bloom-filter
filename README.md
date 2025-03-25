# Bloom Filter Implementation

This repository contains an implementation of a Bloom filter, a space-efficient probabilistic data structure used to test whether an element is a member of a set.

## Problem Description

A Bloom filter is a probabilistic data structure that allows for efficient set membership testing. It consists of a bit array with multiple hash functions that map elements to positions in the array. The filter may yield false positives (incorrectly indicate an element is in the set) but never false negatives. This property makes Bloom filters useful in applications where space efficiency is critical and occasional false positives are acceptable.

## Usage

```bash
# Clone the repository
git clone https://github.com/username/bloom_filter.git
cd bloom_filter

# Install libs
pip install mmh3
pip install bitarray

# Run the Bloom filter implementation
python bloom_filter.py
```

## Implementation Details

The solution is implemented in Python, with key components:
- Bit array for storing the filter
- Multiple hash functions to reduce collision probability
- Methods for adding elements and querying membership
- Configurable filter size and number of hash functions

## Code author

Prystaichuk Dmytro
