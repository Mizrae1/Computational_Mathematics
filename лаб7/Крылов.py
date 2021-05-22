import numpy as np
A = np.array([
	[1.0, 0.5, -0.5, 1],
	[0.5, -1.0, 2.0, 0],
	[-0.5, 2, 1,  -1.5],
	[1.0, 0, -1.5, 2.0]])
y0 = np.array([1, 0, 0, 0])

y1 = A.dot(y0)
y2 = A.dot(y1)
y3 = A.dot(y2)
y4 = A.dot(y3)

print(y4)

M = np.array([
	y3, y2, y1, y0
	])
M = M.transpose()
print(M)

v = -y4
res = np.linalg.solve(M, v)
print(res)

res = np.append(0, res)
res[0] = 1.0
lambd = np.roots(res)

for i in range(len(lambd)):
	q = [1, 0, 0, 0]
	for j in range(1,3):
	 	q[j] = lambd[i] * q[j - 1] + res[j]
	vect = y3 * q[0] + y2 * q[1] + y1 * q[2] + y0 * q[3]
	print("lambda =", "%.4f" % lambd[i], "Cобственный вектор:", vect)
