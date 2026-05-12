class Main:

    def LargestNumber(nums):
        result = 0
        for num in nums:
            if num > result:
                result = num
        return result
if __name__ == "__main__":
    nums = [3, 2, 5, 8, 6, 10]
    print(f"{Main.LargestNumber(nums)}")
