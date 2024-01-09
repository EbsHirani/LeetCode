class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split('.')
        version2 = version2.split('.')

        for i in range(min(len(version1), len(version2))):
            v1 = int(version1[i])
            v2 = int(version2[i])
            if v1>v2:
                return 1
            elif v2>v1:
                return -1
        
        if len(version1)>len(version2):
            for i in range(len(version2), len(version1)):
                if int(version1[i]) > 0:
                    return 1
        else:
            for i in range(len(version1), len(version2)):
                if int(version2[i]) > 0:
                    return -1
        return 0