"""
Write a function called sumIntervals/sum_intervals that accepts an array of intervals, and returns the sum of all the interval lengths. Overlapping intervals should only be counted once.

Intervals are represented by a pair of integers in the form of an array. The first value of the interval will always be less than the second value. Interval example: [1, 5] is an interval from 1 to 5. The length of this interval is 4.
"""
def sum_of_intervals(intervals):
    intervals.sort()  # Sort intervals by start time
    result_interval = 0
    current_start = intervals[0][0]
    current_end = intervals[0][1]
    
    for start, end in intervals[1:]:
        if start <= current_end:  # If there is an overlap
            current_end = max(current_end, end)  # Merge intervals
        else:
            result_interval += current_end - current_start
            current_start = start
            current_end = end
    
    result_interval += current_end - current_start
    return result_interval
