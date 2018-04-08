// LeetCode.cpp: 定义控制台应用程序的入口点。
//
/*给定一个整数数列，找出其中和为特定值的那两个数。

你可以假设每个输入都只会有一种答案，同样的元素不能被重用。

示例 :

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回[0, 1]
*/

#include "stdafx.h"


int main()
{
    return 0;
}

/**
* Note: The returned array must be malloced, assume caller calls free().
*/
int* twoSum(int* nums, int numsSize, int target) {
	int i = 0; int j = 0;
	//int[] result = new int[2];
	int *result = (int *)malloc(2 * sizeof(int));
	for (i = 0; i<numsSize; i++)
	{
		for (j = i + 1; j<numsSize; j++)
		{
			if (nums[i] + nums[j] == target)
			{
				result[0] = i;
				result[1] = j;
				return result;
			}

		}
	}
	return result;

}