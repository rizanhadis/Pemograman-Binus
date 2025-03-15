input_list = ["apple", "madam", "121", "hello"]
count = 0
for item in input_list:
    i = str(item)
    if len(i) > 0 and i[0] == i[-1]:
        count += 1
print(count)  


list = [1, 2, 2, 3, 4, 4, 5]
unique_list = []
for item in list:
    if item not in unique_list:
        unique_list.append(item)
print(unique_list) 

list2 = [1,1,1,1,1,1,1]
unique_list = []
for item in list2:
    if item not in unique_list:
        unique_list.append(item)
print(unique_list)

string1 = "hello"
frequency = {}
for char in string1:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
print(frequency)

string2 = "semangat"
frequency = {}
for char in string2:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
print(frequency) 