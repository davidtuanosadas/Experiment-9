import pandas as pd
Math = {"Student":["Ice Bear","Panda","Grizzly"],"Math":[80,95,79]}
Electronics = {"Student":["Ice Bear","Panda","Grizzly"],"Electronics":[85,81,83]}
GE = {"Student":["Ice Bear", "Panda", "Grizzly"],"GEAS":[90,79,93]}
ESAT = {"Student":["Ice Bear", "Panda", "Grizzly"],"ESAT":[93,89,88]}
math = pd.DataFrame(Math, columns = ["Student", "Math"])
electronics= pd.DataFrame(Electronics, columns = ["Student", "Electronics"]) 
geas= pd.DataFrame(GE, columns = ["Student", "GEAS"])
esat=pd.DataFrame(ESAT, columns=["Student","ESAT"])
score1=pd.merge(pd.merge(math,electronics,on="Student"),
                 pd.merge(geas, esat, on="Student"),on="Student")
score2=pd.melt(score1,id_vars=["Student"], var_name="Subject", value_name="Grades")  