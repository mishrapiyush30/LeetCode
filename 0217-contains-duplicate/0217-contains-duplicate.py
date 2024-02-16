class Solution(object):
    def containsDuplicate(self, nums):
        l=set()
        for i in nums:
            if(i not in l):
                l.add(i)
            else:
                return True
        return False       
        