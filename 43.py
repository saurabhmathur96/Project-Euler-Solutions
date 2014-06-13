import itertools

def list_to_int(t):
    return int(''.join([str(i) for i in t]))

s = 0

for nums in itertools.permutations(range(10),10):
    if list_to_int(nums[1:4]) % 2 == 0:
        if list_to_int(nums[2:5]) % 3 == 0:
            if list_to_int(nums[3:6]) % 5 == 0:
                if list_to_int(nums[4:7]) % 7 == 0:
                    if list_to_int(nums[5:8]) % 11 == 0:
                        if list_to_int(nums[6:9]) % 13 == 0:
                            if list_to_int(nums[7:10]) % 17 == 0:
                                s += list_to_int(nums)

print s
