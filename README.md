## Execution
`python3 hash.py`

## This program achieves following functions: 
- [x] Derive deduplication rate of input with different chunks size 
- [x] Output fingerprints file for future use (e.g., storage simulator).
- [ ] Estimate metadata overhead produced by dedup under [CAFTL](https://www.usenix.org/conference/fast11/caftl-content-aware-flash-translation-layer-enhancing-lifespan-flash-memory-based) mechanism for SSD.
  * mapping: Primary Mapping Table (PMT) and Secondary Mapping Table (SMT)
  * Out of Band (OOB): implemented by Reverse Mapping for storing metadata
