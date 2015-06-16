/*
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.

This solution is from https://leetcode.com/discuss/19151/solution-computation-space-problem-can-extended-situation, thanks for the author.
The main idea is for the majority element, if we remove or take away the majority element, then remove another element,
at the end, the left element should be the majority one.

*/

public class Solution {
    public int majorityElement(int[] nums) {
        int candidate = 0;
        int count = 0;
        int i = 0;
        
        for(i = 0; i < nums.length; i++)
        {
            if (count == 0)
            {
                candidate = nums[i];
                count = 1;
            }
            else
            {
                if (candidate == nums[i])
                    count ++;
                else
                    count --;
            }
        }
        
        return candidate;
    }
}
