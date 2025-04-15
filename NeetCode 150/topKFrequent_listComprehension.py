class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        freq = [[] for i in range(len(nums) +1)]

        [freq[c].append(n) for n, c in count.items()]

        return [n for i in range(len(freq) - 1, 0, -1) for n in freq[i] if (k := k -1) >= 0]
