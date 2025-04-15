class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longestSeq = set()
        for num in set(nums):
            if num - 1 not in set(nums):
                nextNum = num + 1
                seq = set()
                seq.add(num)
                while(True):
                    if nextNum in nums:
                        seq.add(nextNum)
                        nextNum = nextNum + 1
                    else:
                        break;
                if len(seq) > len(longestSeq):
                    longestSeq = seq
        return len(longestSeq)
                    
