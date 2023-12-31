class Solution:
    def simplifyPath(self, path: str) -> str:
        address = []
        for i in path.split("/"):
            if i != "" and i != ".":
                print(i)
                if i == "..":
                    if address:
                        address.pop()
                else:
                    address.append(i)
        
        ans = "/" + "/".join(address)
        
        
        return ans