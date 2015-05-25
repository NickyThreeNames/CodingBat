"""Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4. """

def array_front9(nums):
  count = len(nums)
  if count>4: 
    count = 4
  for i in range(count):
    if nums[i] == 9:
      return True
  return False      