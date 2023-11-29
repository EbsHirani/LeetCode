class Solution {
public:
    int minMovesToMakePalindrome(string s) {
        int low=0;
        int up=s.length()-1;
        int ans = 0;
        while (low<up){
            cout<<s[low]<<" "<<s[up];
            if (s[low]!=s[up]){
                int t =up-1;
                while(s[low]!=s[t]){
                    t--;
                }
                if (low==t){
                    swap(s[low],s[low+1]);
                    ans++;
                        
                }
                else{
                    while (t!=up){
                        swap(s[t],s[t+1]);
                        t++;
                        ans++;
                    }
                }
            }
            else{
                low++;
                up--;
            }
        }
        return ans; 
        
    }
};