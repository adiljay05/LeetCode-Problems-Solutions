class Solution {
public:
    int romanToInt(string s) {
        vector<int>mp(26);
        mp['I' - 'A'] = 1;
        mp['V' - 'A'] = 5;
        mp['X' - 'A'] = 10;
        mp['L' - 'A'] = 50;
        mp['C' - 'A'] = 100;
        mp['D' - 'A'] = 500;
        mp['M' - 'A'] = 1000;
        int res = mp[s[s.size() - 1] - 'A'];
        for(int i = 0; i < s.size() - 1; i++){
            if(mp[s[i] - 'A'] < mp[s[i + 1] - 'A']) res -= mp[s[i] - 'A'];
            else res += mp[s[i] - 'A'];
        }
        return res;
    }
};