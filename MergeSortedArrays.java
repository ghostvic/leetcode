/*
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements 
from nums2. 
The number of elements initialized in nums1 and nums2 are m and n respectively.
*/

/*
We assume that the 2 arrays are sorted in ascenting order.
*/
public class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int i = m-1;
        int j = n-1;
        int timeOfMove = 0;
        
        while (i >= 0 && j >= 0)
        {
            if (nums2[j] > nums1[i])
            {
                nums1[m+n-timeOfMove -1] = nums2[j];
                j --;
            }
            else
            {
                nums1[m+n-timeOfMove -1] = nums1[i];
                i --;
            }
            timeOfMove += 1;
        }
        
        if (j>-1)
            for(int x = 0; x < j+1; x++)
                nums1[x] = nums2[x];
    }
}
