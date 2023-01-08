/*
 * @lc app=leetcode id=344 lang=c
 *
 * [344] Reverse String
 */

// @lc code=start
#define SWAP(a, b) { char t = a; a = b; b = t; }


void reverseString(char* s, int sSize){
    int l=0,r=sSize-1;
    while(l<r){
        SWAP(s[l],s[r]);
        l++;
        r--;
    }
    return s;
}
// @lc code=end

