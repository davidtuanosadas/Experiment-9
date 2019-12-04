import pandas as pd
A = {"Box": ["Box 1", "Box 1","Box 1","Box 2","Box 2","Box 2"],
     "Dimension":["Length","Width","Height","Length","Width","Height"],
     "Value": [6,4,2,5,3,4]}
Box= pd.DataFrame(A, columns = ["Box", "Dimension", "Value"])
Boxtidy = Box.pivot_table(index = "Box", columns = "Dimension", values = "Value")
Boxtidy['Volume'] = Boxtidy.Length * Boxtidy.Width * Boxtidy.Height