class Solution:
    def twoSum(self, nums, target):
        hashmap = {}

        for i in range(len(nums)):
            curr_num = nums[i]
            needed = target - curr_num
            if hashmap.get(needed, 0) == 0:
                hashmap[curr_num] = i+1
            else:
                needed_index = hashmap[needed] - 1
                new_list = []
                new_list.append(needed_index)
                new_list.append(i)
                return sorted(new_list)
