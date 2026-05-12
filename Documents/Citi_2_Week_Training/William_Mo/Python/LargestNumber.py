class Main:
    def findLargest(nums):
        if not nums:
            return None

        largest = nums[0]

        for num in nums:
            if num > largest:
                largest = num
        return largest

if __name__ == "__main__":
    nums = [3, 7, 2, 15, 9]
    result = Main.findLargest(nums)
    print(f"The largest number in the list is: {result}")
