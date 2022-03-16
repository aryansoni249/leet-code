class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        new =list()
        l=len(nums1)
        m=len(nums2)
        o=0
        i=0
        while o<=l-1 and i<=m-1:
            
            if nums1[o]<nums2[i]:
                    new.append(nums1[o])
                    o=o+1
            elif nums2[i]<nums1[o]:
                      new.append(nums2[i])
                      i=i+1
            else:
                new.append(nums1[o])
                o=o+1
                new.append(nums2[i])
                i=i+1
        if o<(l-1):
            for k in range(o,l):
                new.append(nums1[k])
        if i<(m-1):
            for j in range(i,m):
                new.append(nums2[j])
                
        if l==1 and m==1:
            return (nums1[0]+nums2[0])/2
        elif (l+m)%2==0:
            return (new[int((l+m-2)/2)]+new[int((l+m)/2)])/2
        elif (l==0 and m==1):
            
             return nums2[0]
        elif (m==0 and l==1):
             return nums1[0]
        else:
            return new[int((l+m)/2)]
#nums1: List[int], nums2: List[int]            