import Matrix
## Takes a matrix and a list of values that represents the n x 1 result B, solving for x in Ax = B
def solveLinearSystem(matrix, result):
	if (matrix.isSquareMatrix()):
		## Solve using Cramer's Rule
		if (matrix.determinant() != 0):
			return __cramerRule(matrix, result);

def __cramerRule(matrix, result):
	resultList = [];
	denominator = matrix.determinant();
	for c in range(matrix.colCount):
		matrixWithBCol = Matrix.Matrix(matrix.rowCount, matrix.colCount);
		# Copy matrix values into b col matrix
		matrixWithBCol.setMatrix(matrix);
		# Assign b as column in required place
		matrixWithBCol.setColumn(c, result);
		resultList.append(matrixWithBCol.determinant() / denominator);
	return resultList;

# def __gaussJordan(matrix, result):


# def __gaussColumn(rowIndex, column, matrix):
