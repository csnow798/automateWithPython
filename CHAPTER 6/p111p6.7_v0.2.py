tableData=[['apples','oranges','cherries','banana'],['Alice','Bob','Carol','David'],['dogs','cats','moose','goose']]
tableData=str(tableData)
tableData=tableData.replace('[[','')
tableData=tableData.replace(']]','')
tableData=tableData.replace("\'","")
tableData=tableData.replace(","," ")
tableData=tableData.replace("\'","")
tableData=tableData.split(']  [')
print(isinstance(tableData,list))
print(tableData)

colWidth=[]
#print(colWidth)
for i in range(len(tableData)):
              #print(len(tableData[i]))
              colWidth.append(len(tableData[i]))
print(colWidth)
rightWidth=max(colWidth)
#print(rightWidth)

for i in range(len(tableData)):
              print(tableData[i].rjust(rightWidth))


