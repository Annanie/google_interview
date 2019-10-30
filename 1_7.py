def setEmpty(rows, cols, mat):
    zeroRow = [0] * len(mat[0])
    for row in rows:
        mat[row] = zeroRow
    if(cols):
        zeroCol = [0]* len(mat)
        for row in range(len(mat)):
            for col in cols:
                mat[row][col] = 0
    return(mat)

def searchZeroes(mat):
    zeroCols = []
    zeroRows = []
    for row in range(len(mat)):
        for col in range(len(mat[0])):
            if mat[row][col] == 0:
                zeroCols.append(col)
                zeroRows.append(row)
    return(zeroRows, zeroCols)


def emptyMat(mat):
    (rows, cols) = searchZeroes(mat)
    return setEmpty(rows,cols,mat)

tests = [
    [[1,2,3], [0,1,2], [1,2,3], [2,1,3]]
]

for test in tests:
    print(f"For test {test} result is {emptyMat(test)}")
