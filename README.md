## Goal
This program derives deduplication rate of a file in python and get fingerprints output for future use.

## Steps in this program:
1. Reading files in a folder
2. For each file it chunks in fixed-size method (4KB in example) 
3. Building a hash table
4. Hashing each chunk and insert its fingerprint into this hash table
5. Write its fingerprint into output file
5. Derive dedup rate
