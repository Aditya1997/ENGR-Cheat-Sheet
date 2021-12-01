import numpy as np
from numpy import linalg
import pandas as pd

# def impres(D, T):
#     dfboltsimp = pd.read_csv(r"C:\Users\adity\Documents\GitHub\ENGR-Cheat-Sheet\FinalProject\data\boltsizingimp.csv", skiprows=7)
#     dfboltsimp.set_index('No. or Dia.', 'Number of Threads Per Inch')
#     impresult = dfboltsimp[dfboltsimp[D,T]]
#     return impresult
#
# dfboltsimp = pd.read_csv(r"C:\Users\adity\Documents\GitHub\ENGR-Cheat-Sheet\FinalProject\data\boltsizingimp.csv", skiprows=7)
# print(dfboltsimp)
# dfx = dfboltsimp.set_index('No. or Dia.', 'Number of Threads Per Inch')
# print(dfboltsimp)
#
# print(dfx.loc[(2, 72),:])
#impresult = dfboltsimp[dfboltsimp.loc[(2, 72),:]]
#print(impresult)


M3="1 2; 3 4"
M2="1 2; 3 4"
#DSM = "determinant"
DDM = "mult"
def DMoperation(M2, M3, DDM): #M2R, M2C,M3R, M3C
    #a = np.fromstring(M2, dtype=int, sep=' ').reshape(M2R, M2C)
    #b = np.fromstring(M3, dtype=int, sep=' ').reshape(M3R, M3C)
    a = np.array(np.mat(M2), subok=True) #format ('1 2; 3 4')
    b = np.array(np.mat(M3), subok=True) #format ('1 2; 3 4')
    if DDM == "add":
        try:
            add = a + b
            res = add.tolist()
            return 'Addition Result: {}'.format([str(x) for x in res])
        except:
            return "The matrices cannot be added"
    elif DDM == "sub":
        try:
            sub = a - b
            res = sub.tolist()
            return 'Subtraction Result: {}'.format([str(x) for x in res])
        except:
            return  "The matrices cannot be subtracted"
    elif DDM == "mult":
        try:
            mult = np.matmul(a,b)
            res = mult.tolist()
            return 'Multiplication Result: {}'.format([str(x) for x in res])
        except:
            return  "The matrices cannot be multiplied"

x = DMoperation(M2, M3, DDM)
print(x)

# a = np.matrix(value)
# ainv = np.linalg.inv(a)
# print(ainv)
#
# y = test(a, DSM)
# print(y)
#
# dimoptions = {
#     'C': ['Radius'],
#     'R': ['Length', 'Height'],
#     'S': ['Side Length'],
#     'I': ['Flange Width', 'Flange Thickness', 'Beam Height','Web Thickness'],
# }
#
# print(dimoptions['C'])
