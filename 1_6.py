def swap4(e1, e2, e3, e4):
    tmp = e4
    e4 = e3
    e3 = e2
    e2 = e1
    e1 = tmp
    return (e1,e2,e3,e4)


def rotate(M):
    N = len(M)
    for i in range(int(N/2)):
        for j in range(N-i):
            swapped_values = swap4(M[i+j][j], M[i+j][-i-j-1], M[-i-j-1][-i-j-1], M[-i-j-1][i+j])
            (M[i+j][j], M[i+j][-i-j-1], M[-i-j-1][-i-j-1], M[-i-j-1][i+j]) = swapped_values
    return M

test_list = [
	[ [[]],[[]] ],
	[ [[1,2],[3,4]], [[4,1],[3,2]] ],
	[ [[1,2,3],[4,5,6],[7,8,9]], [[7,4,1],[8,5,2],[9,6,3]] ]
]

for test in test_list:
    print(f"Testing rotate {rotate(test[0])}")
