#nieskierowany spojny wazony,

#mst to spojny podgraf obejmujacy wszystkie wierzcholki o mininalnej wadze
#miedzy kazdym wierzcholkiem jest 1 sciezka
#mst to podgraf G z brakiem cyckli

#o elogv

def kruskal(G):
    maxedge = max(G, key=lambda x: max(x[0], x[1]))
    n = max(maxedge[0], maxedge[1]) + 1
    parent = list(range(n))
    rank = [0] * n
    def find(u):
        if parent[u] == u:
            return u
        parent[u] = find(parent[u])
        return parent[u]

    def union(u, v):
        ur, vr = find(u), find(v)
        if ur != vr:
            if rank[ur] > rank[vr]:
                parent[vr] = ur
            elif rank[vr] > rank[ur]:
                parent[ur] = vr
            else:
                parent[vr] = ur
                rank[ur] += 1

    G.sort(key=lambda a: a[2])#ew -
    MST = []
    for (u, v, t) in G:
        if find(u) != find(v):
            union(u, v)
            MST.append((u, v, t))
    return MST

g=[(0, 1, 10),(0, 2, 6),(0, 3, 5),(1, 3, 15),(2, 3, 4),(0,1,11)]
G = [(1, 2, 3), (2, 3, 2), (2, 4, 7), (1, 3, 5), (1, 5, 9), (5, 4, 6)]

print(kruskal(g))


