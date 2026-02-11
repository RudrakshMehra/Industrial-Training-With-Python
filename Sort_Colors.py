class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = ones = twos = 0
        for value in nums:
            if value == 0:
                zero += 1
            elif value == 1:
                ones += 1
            else:
                twos += 1

        # zero = nums.count(0)
        # ones = nums.count(1)
        # twos = nums.count(2)

        i = 0
        new_nums = []
        while(i < len(nums)):
            if(zero != 0):
                new_nums.append(0)
                zero -= 1
                continue
            if(ones != 0):
                new_nums.append(1)
                ones -= 1
                continue
            if(twos != 0):
                new_nums.append(2)
                twos -= 1
                continue         
            
            i += 1
        nums[:] = new_nums