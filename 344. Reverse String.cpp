class Solution {
public:
    void reverseString(vector<char>& s) {
        int start = 0;
        int end = s.size()-1;
        while(start<end){
            char s1 = s[start];
            s[start] = s[end];
            s[end] = s1;
            start++;
            end--;
        }
    }
};