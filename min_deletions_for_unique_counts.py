class Solution:
    def minDeletions(self, s: str) -> int:
        dicti = {}
        for i in s:
            dicti[i] = 1 + dicti.get(i, 0)
        
        repeat_set = []
        val_dict = {}
        for key in dicti:
            val_dict[dicti[key]] = 1 + val_dict.get(dicti[key], 0)
            if val_dict[dicti[key]] == 2:
                repeat_set.append(dicti[key])
        repeat_set.sort(reverse = True)
        dels = 0
        while repeat_set:
            curr_count = repeat_set[-1]
            temp_count = curr_count
            while temp_count in val_dict and temp_count>0:
                temp_count-=1
            val_dict[temp_count] = 1
            val_dict[curr_count] -= 1
            dels += curr_count - temp_count
            if val_dict[curr_count] == 1:
                repeat_set.pop()
        return dels