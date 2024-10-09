# transpose a square matrices (fact: sqr matrices are diagonally transposed)
def transpose(m):
    l = len(m)
    for r in range(l): # each row is an array
        for c in range(r,l): # each column is an index, start from row because of the swap of the two numbers (so they don't swap back)
            m[r][c], m[c][r] = m[c][r], m[r][c] # swap each index
    return m

m = [[1,2,3],[4,5,6],[7,8,9]]
mT = transpose(m)

print(mT)
# output: [1,4,7],[2,5,8],[3,6,9]
