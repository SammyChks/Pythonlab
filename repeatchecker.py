# Testing out my skill to highlight duplicate occurences:
class solution:
    def repeatcheck(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
            return False

    repeatcheck(([1,2,3,3,4,5,5]))
