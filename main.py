class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count]= nums[i] # update in place and removing val
                count += 1
                print(count,i)
            else:
                nums[i]= None

        print(nums)        
        return count        
