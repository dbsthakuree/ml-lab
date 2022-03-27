def aStarAlgo(start,stop):
    open_set=set(start)
    close_set=set()
    g={}               
    parents = {}           
    g[start] = 0
    parents[start] = start
    
    while len(open_set)>0:
        
        n=None
        for v in open_set:
            if n==None or g[v] + h(v) < g[n] + h(n):
                n=v
        if n==stop:
            pass
        else:
            for (m, weight) in get_neighbors(n):
                if m not in open_set and m not in close_set:
                    open_set.add(m)
                    parents[m]=n
                    g[m]=g[n]+weight
                else:
                    if g[m]>g[n]+weight:
                        g[m] = g[n] + weight
                        parents[m] = n
                        if m in close_set:
                            close_set.remove(m)
                            open_set.add(m)
        if n==None:
            print('Path does not exist!')
            return None
        
        if n==stop:
            path=[]
            while parents[n]!=n:
                path.append(n)
                n=parents[n]
            path.append(start)
            path.reverse()
            print('Path found: {}'.format(path))
            return path
        open_set.remove(n)
        close_set.add(n)
    print('Path does not exist!')
    return None



def get_neighbors(v):
    if v in nodes:
        return nodes[v]
    else:
        return None
    
    
    
def h(n):
    H={
       'A':1,
       'B':1,
       'C':1,
       'D':1
       }
    return H[n] 
nodes={
    'A':[('B',1),('C',3),('D',7)],
    'B':[('D',5)],
    'C':[{'D',12}]
    }
aStarAlgo('A','D')
     
