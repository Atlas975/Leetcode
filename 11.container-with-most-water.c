/*
 * @lc app=leetcode id=11 lang=c
 *
 * [11] Container With Most Water
 */

// @lc code=start


int maxArea(int* height, int heightSize){
    int l=0,r=heightSize-1;
    int mxarea = 0;
    while (l<r){
        if (height[l]<height[r]){
            mxarea = fmax(mxarea, height[l]*(r-l));
            l++;
        } else{
            mxarea = fmax(mxarea, height[r]*(r-l));
            r--;
        }
    }
    return mxarea;
}
// @lc code=end

