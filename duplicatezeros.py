class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        nums=[]
        for i in arr:
            if(i==0):
                nums.append(i)
                nums.append(0)
                
                
            else:
                nums.append(i)
        
        arr[:]=nums[0:len(arr)]