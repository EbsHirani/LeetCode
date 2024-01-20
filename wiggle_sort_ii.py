class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0]*5001
        for i in nums:
            counts[i]+=1
        arr = []
        # print(counts)
        for i, count in enumerate(counts):
            for _ in range(count):
                arr.append(i)
        if len(arr)%2==0:
            left = arr[:len(arr)//2]
            right = arr[len(arr)//2:]
        else:
            left = arr[:len(arr)//2+1]
            right = arr[len(arr)//2+1:]
        # print(left)
        # print(right)
        idx = 0
        for i in range((min(len(left), len(right)))):
            nums[idx] = left[len(left)-i-1]
            idx+=1
            nums[idx] = right[len(right)-i-1]
            idx+=1
        if len(left)>len(right):
            nums[-1] = left[0]
        


        