public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        int[][] stores = new int[nums.Length][];
        for(int i=0 ; i<nums.Length ; i++){
            stores[i] = new int[] {nums[i],i};
        }
        Array.Sort(stores, (a, b) => a[0].CompareTo(b[0]));
        int right = nums.Length-1;
        int left = 0;
        while(right > left){
            if(stores[right][0] + stores[left][0] == target){
                return new int[] { stores[left][1], stores[right][1] };
            }
            else if (stores[right][0] + stores[left][0] > target){
                right -= 1;
            }
            else{
                left +=1;
            }
        }
        return new int []{0,0};
    }
}