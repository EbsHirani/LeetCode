class Solution:
    def minDays(self, n: int) -> int:
        queue = deque([(n,0)])
        visited = set([n])
        while(queue):
            # print(queue)
            num, steps = queue.popleft()
            if num == 1:
                return 1+steps
            if num%3==0 and num//3 not in visited:
                visited.add(num//3)
                queue.append((num//3, steps+1))
            if num%2==0 and num//2 not in visited:
                visited.add(num//2)
                queue.append((num//2, steps + 1))
            queue.append((num-1, steps+1))
            visited.add(num-1)