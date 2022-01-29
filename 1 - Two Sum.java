class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] returnSize=new int[2];
        for (int i=0;i<nums.length;i++){
            for(int j=i+1;j<nums.length;j++){
                if (nums[i]+nums[j]==target){
                    returnSize[0] = i;
                    returnSize[1] = j;
                    break;
                }
            }
        }
        return returnSize;
    }
}