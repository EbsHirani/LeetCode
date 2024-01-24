typedef pair<int, int> pi; 
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int, int> mp;
        vector<int> ans;
        priority_queue<pi, vector<pi>, greater<pi> > pq; 
        pi p;
        for (auto iterator = nums.begin(); iterator<nums.end(); iterator++){
            mp[*iterator]++;
        }
        for (auto iter = mp.begin(); iter!=mp.end(); iter++){
            // cout<<iter->second<<"Val - Key "<<iter->first<<"\n";
            pq.push(make_pair(iter->second, iter->first));
            if (pq.size() > k)
                pq.pop();
        }
        // cout<<"end\n";   
        while (pq.size()){
            p = pq.top();
            // cout<<p.second<<" "<<p.first<<"\n";
            ans.push_back(p.second);
            pq.pop();
        }
        return ans;
    }
};