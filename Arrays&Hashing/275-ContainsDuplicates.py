class Solution:
    def containsDuplicate(self, nums) -> bool:
        # if any item occurs more than once, return true
        # iterating over the list, setting each as a value in a dict may work and may perform at N time
        # but constant branching would slow down the code
        # reassigning the list as a set eliminates duplicates in N time
        # memory complexity does go up from this though
        return (len(nums) != len(set(nums)))
