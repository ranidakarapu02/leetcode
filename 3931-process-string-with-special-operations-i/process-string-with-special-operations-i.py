class Solution:
    def processStr(self, s: str) -> str:
        res=[]
        for ch in s:
            if ch.islower():
                res.append(ch)
            elif ch=="*":
                if res:
                    res.pop()
            elif ch=="#":
                res+=res
            elif ch=="%":
                res.reverse()
        return "".join(res)

                
      
        