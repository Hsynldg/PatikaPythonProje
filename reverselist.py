
def revlist(l):
    l.reverse()
    for i in l:
        if isinstance(i,list):
            i.reverse()
            
l1=[[1, 2], [3, 4], [5, 6, 7]]
revlist(l1)
print(l1)