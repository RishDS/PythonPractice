'''
Return the "centered" average of an array of ints, which we'll say is the mean average of the values,
except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value,
ignore just one copy, and likewise for the largest value. Use int division to produce the final average. 
You may assume that the array is length 3 or more.


centered_average([1, 2, 3, 4, 100]) → 3
centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
centered_average([-10, -4, -2, -4, -2, 0]) → -3
'''

def centered_average(nums):
  nums.sort()
  tot_len = len(nums)
  sum = 0
  count = 0
  for i in (nums[1:tot_len-1]):
    sum +=i
    count+=1
  return sum/count

#or

def centered_average(nums):
    # Remove the smallest and largest elements
    nums.remove(min(nums))
    nums.remove(max(nums))
    # Compute the average of the remaining elements
    return sum(nums) // len(nums)

  
#The first program sorts the input list, then computes the sum of the elements between the first and last elements of the sorted list and divides by the number of elements in that range. Sorting takes O(n log n) time complexity in the worst case, and computing the sum and count takes O(n) time complexity. So, the overall time complexity of the first program is O(n log n). The space complexity of the first program is O(1), as it only uses a few variables to store the sum, count, and the length of the input list.
#The second program removes the smallest and largest elements of the input list, then computes the sum of the remaining elements and divides by the number of elements in that range. Removing the smallest and largest elements takes O(n) time complexity in the worst case, and computing the sum and count takes O(n) time complexity. So, the overall time complexity of the second program is O(n). The space complexity of the second program is also O(1), as it only uses a few variables to store the sum, count, and the input list (which is modified in place).
#Therefore, the second program is better in terms of both time and space complexity, as it has a linear time complexity and uses constant space. However, it should be noted that the first program may be faster for very small input sizes, as the sorting overhead may not be significant.



