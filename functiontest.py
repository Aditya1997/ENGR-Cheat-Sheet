import numpy as np
from numpy import linalg
value="[1 2;3 4]"
DSM = "transpose"

def SMoperation(M1, DSM):
    a = np.matrix(M1)
    if DSM == "inverse":
        try:
            ainv = np.linalg.inv(a)
            return ainv
        except:
            return "The matrix does not have an inverse"
    if DSM == "transpose":
        M1T = np.transpose(M1)
        return M1T
    if DSM == "determinant":
        try:
            det = np.linalg.det(M1)
            return det
        except:
            return "The matrix does not have a determinant"
        return det

x = SMoperation(value, DSM)
M1T = np.transpose(np.matrix(value))
print(x)
