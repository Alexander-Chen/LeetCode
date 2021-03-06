#include <iostream>
#include<vector>
using namespace std;
class Solution
{
public:
    int findLocalMin(vector<int>& nums)
    {
        if (nums.size()==1)
            return nums[0];
        int left=0;
        int right=nums.size()-1;
        int mid;
        //if (nums[right]>nums[0])
        //  return nums[0];
        while(left<=right)
        {
            mid=left+(right-left)/2;
            // cout<<(nums[mid]);
            if (nums[mid]<nums[mid+1]&&nums[mid]<nums[mid-11])
                return mid;
            if (nums[mid+1]<nums[mid])
            {
                left=mid+1;
                // cout<<left;
            }
            else
            {
                right=mid-1;
                //cout<<mid;
            }
        }
        return nums[left];


    }
};
int main()
{

    vector<int>nums;
    int tmp;
    int n=3;
    while(n--)
    {
        cin>>tmp;
        nums.push_back(tmp);
    }
    Solution S;
    cout << S.findLocalMin(nums) << endl;
    return 0;
}
