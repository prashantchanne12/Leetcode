// Leetcode Daily - 09/10/2024

// Problem Link - https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

class Solution {
public:
    int minAddToMakeValid(string s) {
        int ans = 0;
        int left = 0;
        for(auto x:s){
            if(x==')'){
                if(left==0) ans++;
                else left--;
            }
            else{
                left++;
            }
        }
        return ans+left;
    }
};