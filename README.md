# temp_tracker

Track temperatures and the min, max, and mean values.

This package includes a function to flatten an array.

```python
import temp_tracker

to_flatten = [[1,2,[3]],4]
flattened = temp_tracker.flatten_array(to_flatten)
# flattened == [1, 2, 3, 4]
```

There are also two implementations of the temp tracker: `TempTracker` and `TempTrackerFast`.

`TempTracker` is a straight-forward, easy to read implementation. `TempTrackerFast` caches values for min, max, and mean to speed up `get_min`, `get_max`, and `get_mean` from O(n) time to O(1).

Example:

```python
tracker = temp_tracker.TempTracker()
tracker.insert(1)
tracker.insert(2)
tracker.get_min() # returns 1
tracker.get_max() # returns 2
tracker.get_mean() # returns 1.5
```