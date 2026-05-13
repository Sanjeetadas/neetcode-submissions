class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result=[]
        for i in range(len(arr)):
            maxi = -1
            for j in range(i+1, len(arr)):
                if maxi < arr[j]:
                    maxi = arr[j]
            result.append(maxi)
        return result

        