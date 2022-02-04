class Solution {
public:
    vector<string> divideString(string s, int k, char fill) {
        vector<string>a;
        for (int i=0;i<s.length();i++){
            string s1="";
            for(int j=i;j<i+k && j<s.length();j++){
                s1+=s[j];
            }
            i+=(k-1);
            int len = k-s1.length();
            for(int k=0;k<len;k++)s1+=fill;
            a.push_back(s1);
        }
        return a;
    }
};