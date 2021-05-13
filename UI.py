import Matrix
from IO import *
from Linear import *
from Operations import *

matrixFile = raw_input("Enter a matrix file: ");
m = readMatrixFromFile(matrixFile);
print(m.toString());

print(inverse(m).toString());