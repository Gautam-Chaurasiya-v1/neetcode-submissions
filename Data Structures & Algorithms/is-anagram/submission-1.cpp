class Solution {
public:
    bool isAnagram(string s, string t) {
       unordered_map<int,int>mp;

       for(auto i:s){
        mp[i]++;
       } 

       for(auto j:t){
        mp[j]--;
        if(mp[j]<0)return false;
       }
       
       for(auto j:mp){
         if( j.second > 0 )return false;
       }

       return true;
    }
};
