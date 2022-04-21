def checkInclusion(s1: str, s2: str) -> bool:
        l=list(s2)
        m=list(s1)
        l1=len(s1)
        if l1==0:
            return 0
        m.sort()
        
        pos=l.index(m[0])
        print(pos) 
        if pos!=None:
            for i in range(pos-l1,pos+l1):
                t=l[i:i+l1]
                t.sort()
                if t==m:
                    return "true"
                else:
                    continue

        return 
        
x=checkInclusion("ab","hbac")     
print(x)