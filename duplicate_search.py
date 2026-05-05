# Contains Duplicate II
# Given an integer array nums and an integer k, return True 
# if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
#  Otherwise, return False.

def dup_search(num,k):
   
    for i in range(len(num)):
        for j in range(i+1,len(list)):
            if num[i]==num[j] and abs(i-j)<=k:
                return True
    return False


def dup_search_hash(nums, k):
    seen = {}                         # value -> most recent index
    
    for i, num in enumerate(nums):
        if num in seen and i - seen[num] <= k:
            return True
        seen[num] = i                 # update to latest index
    print(seen)
    #print(seen[0])
    return False

def dup_search_array(nums, k):
    window = []                        # sliding window of last k elements
    for num in nums:
        if num in window:
            return True
        window.append(num)
        if len(window) > k:
            window.pop(0)              # evict oldest when window exceeds k
    print(window)
    return False

if __name__=="__main__":
    list=[-2.2,4,5,7,8,5,9]
    k=2
    print(dup_search_hash(list,k))
    print(dup_search_array(list,k))