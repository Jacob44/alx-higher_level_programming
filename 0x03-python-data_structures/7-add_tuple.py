#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    ln_a, ln_b = len(tuple_a), len(tuple_b)
    ntuple = ((tuple_a[0] if ln_a >= 1 else 0) +
              (tuple_b[0] if ln_b >= 1 else 0),
              (tuple_a[1] if ln_a >= 2 else 0) +
              (tuple_b[1] if ln_b >= 2 else 0))
    return ntuple
