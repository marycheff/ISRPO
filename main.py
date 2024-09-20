def check_same_sign(arr):
    if len(arr) == 0:
        return False
    first_sign = -1
    for x in arr:
        if x == 0:
            return False
        
        if first_sign == -1:
            first_sign = x > 0
        elif (x > 0) != first_sign:
            return False
    return True

def process_arrays(arrays):
    found = False
    i = 1
    for arr in arrays:
        if check_same_sign(arr):
            print(f"Массив {i} состоит из элементов одного знака.")
            found = True
        i += 1
    if not found:
        print("Нет массивов, состоящих из элементов одного знака.")

arrays = [
    [1.2, 3.4, 5.6, 7.8],
    [-1.1, -2.2, -3.3],
    [0.0, 1.1, -1.1],
    [4.4, 5.5, 6.6],
    [-7.7, -8.8, -9.9]
]

process_arrays(arrays)
