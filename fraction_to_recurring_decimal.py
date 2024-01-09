class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        setSign = False
        if numerator<0 and denominator<0:
            numerator, denominator = -numerator, -denominator
            setSign = False
        elif numerator<0 or denominator<0:
            numerator, denominator = abs(numerator), abs(denominator)
            setSign = True
        num = numerator//denominator
        ans = str(num) 
        rem = numerator%denominator
        frac= ""
        dicti = {}
        while rem != 0:
            id = len(frac)
            if rem in dicti:
                frac = frac[:dicti[rem]] + f"({frac[dicti[rem]:]})"
                break
            else:
                dicti[rem] = id
                frac += str((rem*10)//denominator)
                rem = (rem*10)%denominator
        
        if len(frac)>0:
            ans = ans+'.'+frac
        if setSign and numerator>0:
            ans = '-' + ans
        
        return ans