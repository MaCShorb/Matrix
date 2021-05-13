import csv
import Matrix
import os

def readMatrixFromFile(fileName):
	fileAddress = os.path.join("/Users/macs/Matrix/", fileName);
	with open(fileAddress, 'r') as file:
		reader = csv.reader(file, delimiter=",");
		dimensionLine = reader.next();
		matrixRowAmount = int(dimensionLine[0]);
		matrixColAmount = int(dimensionLine[1]);
		readMatrix = Matrix.Matrix(matrixRowAmount, matrixColAmount);
		for r in range(int(matrixRowAmount)):
			matrixRow = reader.next();
			for c in range(int(matrixColAmount)):
				readMatrix.data[r][c] = int(matrixRow[c]);
		return readMatrix;
	