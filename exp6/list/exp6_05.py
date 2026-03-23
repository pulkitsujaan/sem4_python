def split_and_swap(lst):
    mid = len(lst) // 2
    return lst[mid:] + lst[:mid]