public class Solution {
    public IList<IList<int>> ThreeSum(int[] nums) {
        Array.Sort(nums);
        IList<IList<int>> answer = new List<IList<int>>();
        for(int i=0 ; i < nums.Length - 2; i++){
           if (i > 0 && nums[i] == nums[i - 1])
            {
                continue;
            }
           int middle = i+1;
           int end = nums.Length-1 ;
           while(end > middle )
           {
            int sum = nums[i] + nums[middle]+ nums[end];
            if(sum == 0){
                answer.Add(new List<int>{nums[i],nums[middle],nums[end]});
                end--;
                while( end > middle && nums[end] == nums[end+1]){
                    end-=1;
                }
                middle+=1;
                while( middle < end && nums[middle] == nums[middle-1]){
                    middle+=1;
                }
            }
            else if (sum > 0){
                end -=1;
            }
            else{
                middle +=1;
            }

           }

        }
        return answer ;
    }
}