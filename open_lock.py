class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(deadends)
        if "0000" in deadends:
            return -1
        if "0000" == target:
            return 0
        queue = deque()
        queue.append(("0000",0)) 
        visited.add("0000")
        while queue:
            s, steps = queue.popleft()
            for id in range(4):
                for x in (-1,1):
                    new = s[0:id] + str((int(s[id])+x)%10) + s[id+1:]
                    # print(new)
                    if new == target:
                        return steps+1
                    elif new not in visited:
                        visited.add(new)
                        queue.append((new, steps+1))
        
        return -1
            

