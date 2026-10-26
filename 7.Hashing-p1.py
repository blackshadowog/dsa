# hashing optimal solution 


n = [1, 1, 2, 4, 8, 8, 2, 3, 4, 4, 4, 4, 9, 10]
m = [5, 1, 2, 8, 9, 10, 87, 55, 111]

hash_list = [0] * 11

for num in n:
    hash_list[num] += 1

for num in m:
    if num < 0 or num >= len(hash_list):
        print(0)
    else:
        print(hash_list[num])



#using dict for hashing 


hf = {}
for num in n :
    hf[num] = hf.get(num, 0) +1

for nums in m :
    if nums in hf :
        print(hf[nums])
    else:
        print(0)