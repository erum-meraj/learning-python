
def sum67(nums):
  sum1 = 0
  diff = 0
  for i in nums:
    sum1 = sum1 + i

  for i in range(len(nums)):
    if nums[i] == 6:
      pos7 = nums.index(7)
      for ctr in range(1, pos7+1):
        diff = diff + ctr
    else:
      continue
  
          
    
  value = sum1 - diff  
  return value


nums = [1, 2, 2, 6, 99, 99, 7]
print(sum67(nums))
