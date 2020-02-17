def dim(a):
    return [len(a),len(a[0])]
def scalmul(t,a):
    nul = [[] for i in range(len(a))]
    for j in range(len(a)):
        for k in range(len(a[0])):
            nul[j].append(t*a[j][k])
    return nul
def trans(a):
    nul = [[] for i in range(len(a[0]))]
    for j in range(len(a[0])):
        for k in range(len(a)):
            nul[j].append(a[k][j])
    return nul
def add(a,b):
    if dim(a) != dim(b):
        raise Exception('Input matrices must have same dimensions')
    nul = [[] for i in range(len(a))]
    for j in range(len(a)):
        for k in range(len(a[0])):
            nul[j].append(a[j][k] + b[j][k])
    return nul
def sub(a,b):
    if dim(a) != dim(b):
        raise Exception('Input matrices must have same dimensions')
    nul = [[] for i in range(len(a))]
    for j in range(len(a)):
        for k in range(len(a[0])):
            nul[j].append(a[j][k] - b[j][k])
    return nul
def dot(a,b):
    if dim(a) != dim(b):
        raise Exception('Input vectors must be of same dimension')
    nul = []
    for i in range(len(a)):
        nul.append(a[i][0]*b[i][0])
    return sum(nul)
def mdot(a,b):
    if len(a) != len(b):
        raise Exception('Input vectors must be of same dimension')
    nul = []
    for i in range(len(a)):
        nul.append(a[i]*b[i])
    return sum(nul)
def cross(a,b):
    if dim(a) != [3,1] or dim(b) != [3,1]:
        raise Exception('Input vectors must be 3 dimensional')
    return [[a[1][0]*b[2][0]-a[2][0]*b[1][0]],[a[2][0]*b[0][0]-a[0][0]*b[2][0]],
        [a[0][0]*b[1][0]-a[1][0]*b[0][0]]]
def mcross(a,b):
    if len(a) != 3 or len(b) != 3:
        raise Exception('Error: Input vectors must be 3 dimensional')
    return [[a[1]*b[2]-a[2]*b[1]],[a[2]*b[0]-a[0]*b[2]],[a[0]*b[1]-a[1]*b[0]]]
def mul(a,b):
    if dim(a)[1] != dim(b)[0]:
        raise Exception('Error: Input matrices must have dim of [a,b] * [b,c]')
    nul = [[] for i in range(len(a))]
    for j in range(len(a)):
        for k in range(len(b[0])):
            nul[j].append(mdot(a[j],(trans(b))[k]))
    return nul
def submat(a,x,y):
    nul = [[] for i in range(len(a))]
    for j in range(len(a)):
        for k in range(len(a[0])):
            nul[j].append(a[j][k])  
    del nul[x]
    for l in range(len(a)-1):
        del nul[l][y]
    return nul
def det(a):
    if dim(a)[0] != dim(a)[1]:
        raise Exception('Matrix must be square to have a determenent')
    nul = []
    if dim(a) == [2,2]:
        return a[0][0]*a[1][1] - a[0][1]*a[1][0]
    for i in range(len(a)):
        nul.append(a[0][i]*((-1)**i)*det(submat(a,0,i)))
    return sum(nul)
def inv(a):
    if dim(a)[0] != dim(a)[1]:
        raise Exception('Matrix must be square to be inverted')
    if det(a) == 0:
        raise Exception('Matrix is singular')
    if dim(a) == [2,2]:
        return scalmul(1.0/det(a),[[a[1][1],-a[0][1]],[-a[1][0],a[0][0]]])
    nul = [[] for i in range(len(a))]
    for j in range(len(a)):
        for k in range(len(a)):
            nul[j].append(((-1)**j)*((-1)**k)*det(submat(a,j,k)))
    return scalmul((1.0/det(a)),trans(nul))
#use these to make it easier to test
w = [[-12,8,24,0],[-3,-1,24,0],[12,4,24,24],[6,1,48,24]]
x = [[1,2,0,-3,4],[4,2,-2,1,7],[1,0,3,0,-2],[3,-3,1,5,1],[1,0,8,0,-4]]
y = [[1,2,5],[3,4,0],[2,0,1]]
z = [[1,4],[0,-3]]
A = [[] for i in range(10)]
for j in range(10):
    for k in range(1,11):
        A[j].append(abs(k**2 -j**2) - k -j +1)
v1 = [[1],[0],[3]]
v2 = [[3],[1],[12]]
v3 = [[-48],[-6],[24],[6]]
