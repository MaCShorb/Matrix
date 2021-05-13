import Matrix

def determinant(matrix):
	if (matrix.isSquareMatrix() == False):
		return None;
	if (matrix.rowCount == 2):
		return (matrix.data[0][0] * matrix.data[1][1] - matrix.data[0][1] * matrix.data[1][0]);
	else:
		excludedRow = 0;
		determinantResult = 0;
		for excludedCol in range(matrix.rowCount):
			## Smaller matrix partitioned via Leibniz 
			smallerMatrix = matrix.subMatrix(excludedRow, excludedCol);
			## Leibniz Formula
			determinantResult += (-1) ** (excludedRow + 1 + excludedCol + 1) * matrix.data[excludedRow][excludedCol] * determinant(smallerMatrix);
		return determinantResult;

def transpose(matrix):
	transposeMatrix = Matrix.Matrix(matrix.colCount, matrix.rowCount);
	for r in range(matrix.rowCount):
		for c in range(matrix.colCount):
			transposeMatrix.data[c][r] = matrix.data[r][c];
	return transposeMatrix;

def cofactor(matrix):
	cofactorMatrix = Matrix.Matrix(matrix.rowCount, matrix.colCount);
	for excludedRow in range(matrix.rowCount):
		for excludedCol in range(matrix.colCount):
			m = matrix.subMatrix(excludedRow, excludedCol);
			cofactorMatrix.data[excludedRow][excludedCol] = (-1) * (excludedRow + 1 + excludedCol + 1) * determinant(m);
	return cofactorMatrix

def adjunct(matrix):
	cofactorMatrix = cofactor(matrix);
	return transpose(cofactorMatrix);

def inverse(matrix):
	return adjunct(matrix) * (1 / determinant(matrix));
