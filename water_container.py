# Container With Most Water (LeetCode 11)
#
# You are given an integer array `heights` of length n. There are n vertical lines
# drawn such that the two endpoints of the i-th line are (i, 0) and (i, heights[i]).
#
# Find two lines that together with the x-axis form a container that holds the most water.
# Return the maximum amount of water a container can store.
#
# The container cannot be slanted.
#
# Example:
#   Input:  heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
#   Output: 49
#   Explanation: The lines at index 1 (height 8) and index 8 (height 7) form a container
#                with width 7 and height min(8, 7) = 7, giving area = 49.
#
# Constraints:
#   - n == heights.length
#   - 2 <= n <= 10^5
#   - 0 <= heights[i] <= 10^4

def max_area(hights):
    max_area=0
    for i in range(len(hights)):
        for j in range(i+1, len(hights)):
            width= j-i
            hight= min(hights[i], hights[j])
            area= width*hight
            max_area=max(max_area,area)
    return max_area

def das_max_area(hights):
    left=0
    right=len(hights)-1
    max_area=0
    while left<right:
        width=right-left
        hight=min(hights[left], hights[right])
        max_area=max(max_area, width*hight)

        if hights[left] < hights[right]:
            left+=1
        else:
            right-=1
    return max_area

if __name__ == "__main__":
    hights=[1,8,6,2,5,4,8,3,7]
    print(das_max_area(hights))