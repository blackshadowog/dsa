# Store Frequency in Dictionary
nums = [1, 2, 3, 4, 5, 1, 2, 3, 1]
frequency = {}
for num in nums:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1
print(frequency)

# method 2 : using get method 

arr = [1, 2, 3, 4, 5, 1, 2, 3, 1]
frequency = {}
for num in arr:
    frequency[num] = frequency.get(num, 0) + 1
print(frequency)