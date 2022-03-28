
def createMatrix():
    matrix = []
    row = int(input("Enter number of rows of matrix: "))
    col = int(input("Enter number of columns of matrix: "))
    for i in range(row):
        rowappend = []
        for j in range(col):
            print("Enter the number in index",i+1,j+1)
            number = int(input())
            rowappend.append(number)
        matrix.append(rowappend)
        rowappend = []
    return matrix




def printMatrix(matrix, resultVector, elementary, oldMat):
    for i in range(len(matrix)):
        print(elementary[i], "                                        *",oldMat[i], "=                                             ",matrix[i], "                                  vectorB-->[",resultVector[i][0],"]")
    print("-----------------------------------------------------------------------------------------------------")



def createResultVector():
    resultVector = []
    temp = []
    row = int(input("Enter number of rows of vector b: "))
    for i in range(row):
        for j in range(1):
            number=int(input("Enter the numbers: "))
            temp.append(number)
        resultVector.append(temp)
        temp = []
    return resultVector




def unitMatrix(matrix):
    unit = []
    temp = []
    size = len(matrix)
    for i in range(size):
        for j in range(size):
            if i == j:
                temp.append(1)
            else:
                temp.append(0)
        unit.append(temp)
        temp = []
    return unit

def zeroMatrix(matrix):
    zeromat = []
    temp = []
    size = len(matrix)
    for i in range(size):
        for j in range(size):
            temp.append(0)
        zeromat.append(temp)
        temp = []
    return zeromat

def multiplymatrix(elementary, matrix):
    newMatrix=zeroMatrix(matrix)
    for i in range(len(elementary)):
        for j in range(len(matrix[0])):
            for k in range(len(matrix)):
                newMatrix[i][j] += elementary[i][k] * matrix[k][j]
    return newMatrix


def elimination(matrix, vectorB):
    flag = 1
    while flag == 1:
        flag = 0
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if i == j and matrix[i][j] == 0:
                    for k in range(len(matrix)):
                        if matrix[k][j] != 0:
                            elementary = unitMatrix(matrix)
                            elementary[i],elementary[k] = elementary[k], elementary[i]
                            oldMat=matrix
                            matrix = multiplymatrix(elementary, matrix)
                            vectorB=multiplymatrix(elementary, vectorB)
                            printMatrix(matrix, vectorB, elementary, oldMat)
                            flag = 1
                            break


    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == j:
                elementary=unitMatrix(matrix)
                elementary[i][j]=(1/matrix[i][j])
                oldMat = matrix
                vectorB = multiplymatrix(elementary, vectorB)
                matrix = multiplymatrix(elementary, matrix)
                printMatrix(matrix, vectorB, elementary, oldMat)
            else:
                elementary = unitMatrix(matrix)
                elementary[j][i] = (matrix[j][i]/matrix[i][i])*(-1)
                oldMat = matrix
                vectorB = multiplymatrix(elementary, vectorB)
                matrix = multiplymatrix(elementary, matrix)
                printMatrix(matrix, vectorB, elementary, oldMat)







matrix = createMatrix()
vectorB = createResultVector()
result = elimination(matrix,vectorB)


