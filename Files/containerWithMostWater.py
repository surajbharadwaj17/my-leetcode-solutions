"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.


"""

def maxArea(height):

    max_area = 0 
    l = 0
    r = len(height)-1
    while l<r:
        if height[l] < height[r]:
            min_height = height[l]
        else:
            min_height = height[r]
        area = min_height * (r-l)
        if area > max_area :
            max_area = area
        if height[l] < height[r]:
            l+=1
        else:
            r-=1
    return max_area         
    


heights = [1,1]

print(maxArea(heights))