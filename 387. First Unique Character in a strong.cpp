class Solution {
public:
    int firstUniqChar(string s) {
        if(s.size()==1)return 0;
        for(int i=0;i<s.size();i++){
            bool flag=false;
            for(int j=0;j<s.size();j++){
                if(s[i]==s[j] && i!=j){flag=true;break;}
            }
            if (!flag)return i;
        }
        return -1;
    }
};