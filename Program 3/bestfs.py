graph={
    '5':['3','7'],
    '3':['2','4'],
    '2':[],
    '4':['8'],
    '7':['8'],
    '8':[],
}

visited=[]
q=[]

def Bestfs(visited,graph,startNode):
    visited.append(startNode)
    q.append(startNode)
    while q:
        m=q.pop(0)
        print(m,end=' ')
        for n in graph[m]:
            if n not in visited:
                visited.append(n)
                q.append(n)

Bestfs(visited=visited,graph=graph,startNode='5')

