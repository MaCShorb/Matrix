import copy

class Matrix(object):
	"""Matrix class"""
	def __init__(self, rowCount = 1, colCount = 1):
		super(Matrix, self).__init__()
		self.rowCount = rowCount;
		self.colCount = colCount;
		self.data = [];
		for r in range(self.rowCount):
			row = [0.0] * (self.colCount);
			self.data.append(row);

	def isSquareMatrix(self):
		if (self.rowCount != self.colCount):
			return False;
		return True;

	def toString(self):
		matrixString = "";
		for r in range(self.rowCount):
			for c in self.data[r]:
				matrixString += str(c);
				matrixString += " ";
			matrixString += "\n";
		return matrixString;

	def determinant(self):
		if (self.isSquareMatrix() == False):
			return None;x
		if (self.rowCount == 2):
			return (self.data[0][0] * self.data[1][1] - self.data[0][1] * self.data[1][0]);
		else:
			excludedRow = 0;
			determinantResult = 0;
			for excludedCol in range(self.rowCount):
				## Smaller self partitioned via Leibniz 
				smallerMatrix = self.subMatrix(excludedRow, excludedCol);
				## Leibniz Formula
				determinantResult += (-1) ** (excludedRow + 1 + excludedCol + 1) * self.data[excludedRow][excludedCol] * smallerMatrix.determinant();
			return determinantResult;	

	# Get a submatrix with excluded row and column
	def subMatrix(self, excludedRow, excludedCol):
		returnMatrix = Matrix(self.rowCount - 1, self.colCount - 1);
		setRow = 0;
		setCol = 0;
		for row in range(self.rowCount):
			if (row != excludedRow):
				setCol = 0;
				for col in range(self.colCount):
					if (col != excludedCol):
						returnMatrix.data[setRow][setCol] = self.data[row][col];
						setCol += 1;
				setRow += 1;
		return returnMatrix;

	# Set values in a matrix using an already created Matrix.
	def setMatrix(self, setMatrix):
		if (self.rowCount == setMatrix.rowCount and self.colCount == setMatrix.colCount):
			self.data = copy.deepcopy(setMatrix.data);

	# Set a column's values using a list of values
	def setColumn(self, columnNumber, columnList):
		if (len(columnList) == self.colCount and columnNumber >= 0 and columnNumber < self.colCount):
			for r in range(self.rowCount):
				self.data[r][columnNumber] = columnList[r];

	# Set a row's values using a list of values
	def setRow(self, rowNumber, rowList):
		if(len(rowList) == self.rowCount and rowNumber >= 0 and rowNumber < self.rowCount):
			for c in range(self.colCount):
				self.data[rowNumber][c] = rowList[c];

	def transpose(self):
		transposeMatrix = Matrix(self.colCount, self.rowCount);
		for r in range(self.rowCount):
			for c in range(self.colCount):
				transposeMatrix.data[c][r] = self.data[r][c];
		return transposeMatrix;

	def __mul__(self, scalar):
		for r in range(self.rowCount):
			for c in range(self.colCount):
				self.data[r][c] *= scalar;

	def __add__(self, otherMatrix):
		for r in range(self.rowCount):
			for c in range(self.colCount):
				self.data[r][c] *= otherMatrix.data[r][c];

	def cofactor(self):
		cofactorMatrix = Matrix(self.rowCount, self.colCount);
		for excludedRow in range(self.rowCount):
			for excludedCol in range(self.colCount):
				m = self.subMatrix(excludedRow, excludedCol);
				cofactorMatrix.data[excludedRow][excludedCol] = (-1) * (excludedRow + 1 + excludedCol + 1) * m.determinant();

	def adjunct(self):
		cofactorMatrix = self.cofactor();
		return cofactorMatrix.transpose();