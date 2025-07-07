# You are given an integer array height of length n. There are n vertical lines drawn 
# such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container 
# contains the most water. Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

# [1, 8, 6, 5, 3, 2]

# def maxArea(self, height: List[int]) -> int:
#     max_water = 0
#     for i in range(len(height)):
#         for j in range(i, len(height)):
#             container_width = j - i
#             container_height = min(height[j], height[i])
#             water_area = container_width * container_height
#             if water_area > max_water:
#                 max_water = water_area
#     return max_water

def maxArea(self, height: List[int]) -> int:
    max_area = 0
    l = 0
    r = len(height) - 1
    while l < r:
        container_width = r - l
        container_height = min(height[l], height[r])
        area = container_width * container_height
        if area > max_area:
            max_area = area
        if height[l] >= height[r]:
            r -= 1
        else:
            l += 1
    return max_area
        

                
