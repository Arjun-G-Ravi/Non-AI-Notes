global_list = [1, 2, 3]

def append_to_global_list(value):
    global_list.append(value)
    print(global_list)

append_to_global_list(4)  # Output: [1, 2, 3, 4]
print(global_list)  # Output: [1, 2, 3]
