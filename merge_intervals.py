
# Merge Intervals Pattern

def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    merged = []
    
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged

# Example usage:
# print(merge_intervals([[1,4], [0,4]])) # Output: [[0, 4]]
# print(merge_intervals([[1,4], [2,5], [7,9]])) # Output: [[1, 5], [7, 9]]
