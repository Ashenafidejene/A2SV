class Solution {
public:
    vector<int> buildArray(vector<int>& nums) {
         vector<int> answer ;
         for ( int i = 0 ; i < nums.size() ; i ++ ){
            answer.push_back(nums[nums[i]]);
         }
         return answer ;
    }
};