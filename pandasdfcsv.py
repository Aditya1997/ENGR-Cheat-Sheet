import pandas as pd

df = pd.read_csv(r"C:\Users\adity\Documents\GitHub\ENGR-Cheat-Sheet\FinalProject\data\boltsizingimp.csv", skiprows=7)
print(df)
df2 = pd.read_csv(r"C:\Users\adity\Documents\GitHub\ENGR-Cheat-Sheet\FinalProject\data\boltsizingmetric.csv")

def impresult(D, T):
    dfboltsimp = pd.read_csv(r"C:\Users\adity\Documents\GitHub\ENGR-Cheat-Sheet\FinalProject\data\boltsizingimp.csv", skiprows=7)
    dfx = dfboltsimp.set_index(['No. or Dia.', 'Number of Threads Per Inch'])
    impres = dfx.loc[(D,T),:] # print whole row for (D,T) index
    #x = make_dash_table(impres)
    return impres #impres


x = impresult('1', 72)
#print(x)
dfboltsimp = pd.read_csv(r"C:\Users\adity\Documents\GitHub\ENGR-Cheat-Sheet\FinalProject\data\boltsizingimp.csv", skiprows=7)
dfx = dfboltsimp.set_index(['No. or Dia.', 'Number of Threads Per Inch'])
# y = dfboltsimp.loc[(2,72),:]
# print(y)
D = '1'
T = 72
#print((dfboltsimp['No. or Dia.'] == D) & (dfboltsimp['Number of Threads Per Inch'] == T))
#print(dfboltsimp.loc[((dfboltsimp['No. or Dia.'] == D) & (dfboltsimp['Number of Threads Per Inch'] == T)),:])
# x = dfx.loc[(D,T)]
# print(x)
# x = dfx.loc[(D,T),:]
# print(x)
# print(x.count())
# y = dfboltsimp.loc[((dfboltsimp['No. or Dia.'] == D) & (dfboltsimp['Number of Threads Per Inch'] == T))]
# print(y)
# print(y.count())

def impresult(TapSize):
    dfboltsmet = pd.read_csv(r"C:\Users\adity\Documents\GitHub\ENGR-Cheat-Sheet\FinalProject\data\boltsizingmetric.csv", skiprows=7)
    impres = dfboltsmet.loc[((dfboltsmet['Tap size'] == Tapsize)),:] # this method of using loc produces a dataframe using a boolean mask
    x = make_dash_table(impres)
    return x

dfboltsmet = pd.read_csv(r"C:\Users\adity\Documents\GitHub\ENGR-Cheat-Sheet\FinalProject\data\boltsizingmetric.csv", skiprows=7)
#impres = dfboltsmet.loc[((dfboltsmet['Tap size'] == Tapsize)),:]
print(dfboltsmet.columns)
