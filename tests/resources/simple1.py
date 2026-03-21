def calculate_total(values: list):
    total = 0
    for value in values:
        if value < 0:
            continue
        total += value
    return total