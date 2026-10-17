
class Solution(object):
    def minSwaps(self, nums):
        n = len(nums)

        # Step 1: Sort by digit sum, then by number
        sorted_nums = sorted(nums, key=lambda x: (sum(int(d) for d in str(x)), x))

        # Step 2: Store each number's current index
        pos = {nums[i]: i for i in range(n)}

        swaps = 0

        # Step 3: Put each number in its correct position
        for i in range(n):
            if nums[i] != sorted_nums[i]:
                j = pos[sorted_nums[i]]

                # Swap the numbers
                nums[i], nums[j] = nums[j], nums[i]

                # Update their positions
                pos[nums[j]] = j
                pos[nums[i]] = i

                swaps += 1

        return swaps

        
        