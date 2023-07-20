def find_indices(string, char_list):
    indices = []
    for i, char in enumerate(string):
        if char in char_list:
            indices.append(i)
    return indices

string = input("Enter a string: ")
char_list = input("Enter a list of characters (without spaces): ")

indices = find_indices(string, char_list)

print("Indices where characters appear:")
print(indices)
