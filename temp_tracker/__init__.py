#!/usr/bin/env python

from .temp_tracker import TempTracker
from .temp_tracker import TempTrackerFast

def flatten_array(arr):
    """
    Flatten an array of arbitrarily nested arrays.

    For example: [[1,2,[3]],4] -> [1,2,3,4].

    :param arr: The array to flatten.
    :returns: The flattened array.
    """

    result = []

    for element in arr:
        if isinstance(element, list):
            result += flatten_array(element)
        else:
            result.append(element)

    return result
