class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}

        for num in nums:
            freq_map[num] = freq_map.get(num,0) + 1
        
        buckets = [[] for _ in range(len(nums) + 1)]

        for num in freq_map:
            buckets[freq_map[num]].append(num)
        
        count = 1
        result = []
        for i in range(len(nums), -1,-1):
            if buckets[i] == []:

                continue
            if count <= k:
                for num in buckets[i]:
                    if count > k:
                        return result
                    result.append(num)
                    count += 1
            else:
                break
        return result
