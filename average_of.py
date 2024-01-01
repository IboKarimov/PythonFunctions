def average_of(*args):
    test = [*args]
    length = len(test)
    total_sum = 0
    for i in test:
        total_sum += i
    result = total_sum / length
    return result
