g={1:[2,3],2:[4,5],3:[6],4:[],5:[],6:[]}
def dls(n,goal,limit):
print(n,end=" ")
if n==goal: return True
if limit==0: return False
for x in g[n]:
if dls(x,goal,limit-1): return True
return False
print("DLS:",end=" ")
dls(1,6,2)
