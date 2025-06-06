class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        SArr1 = sorted(nums1)
        SArr2 = sorted(nums2)
        i,j = 0, 0
        output = []
        while i < len(SArr1) and j < len(SArr2):
            if SArr1[i] < SArr2[j]:
                i += 1
            elif SArr1[i] == SArr2[j]:
                output.append(SArr1[i])
                i+=1
                j+=1
            elif SArr1[i] > SArr2[j]:
                j+=1
        return output
