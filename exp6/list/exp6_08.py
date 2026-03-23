def separate_evens(lst):
    evens = [x for x in lst if x % 2 == 0]
    odds = [x for x in lst if x % 2 != 0]
    return odds, evens  # Returns updated original list and the separated list