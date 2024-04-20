#!/usr/bin/env python3
"""
    5. Complex types - list of floats
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
        returns the sum as a float.
    """
    return float(sum(input_list))