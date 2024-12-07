#deternine if 2 nodes are adjacent using adjacency matrix in an undirected graph
adj_mat = [
  [ 0, 1, 0, 0 ],
  [ 1, 0, 1, 1 ],
  [ 0, 1, 0, 1 ],
  [ 0, 1, 1, 0 ]
]

adj_mat = [
  [ 0, 1, 0, 1, 1 ],
  [ 1, 0, 1, 0, 0 ],
  [ 0, 1, 0, 1, 0 ],
  [ 1, 0, 1, 0, 1 ],
  [ 1, 0, 0, 1, 0 ]
]

def checkAdjacency(mat, n1, n2):
    return mat[n1][n2] == 1


print(checkAdjacency(adj_mat, 0, 3))
