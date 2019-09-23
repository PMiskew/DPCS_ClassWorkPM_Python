import ToolsPM

#Test slowPrint
ToolsPM.slowPrint("Paul",1) #Test 1 second
ToolsPM.slowPrint("A Word",2) #Test 2 second
ToolsPM.slowPrint("monkey",0.5) #Test 0.5 second, confirms float valid

#Test findFactors
listff1 = ToolsPM.findFactorsA(10)
print("Factors of 10 - A:")
print(listff1)
listff2 = ToolsPM.findFactorsB(10)
print("Factors of 10 - B: ")
print(listff2)

listff1 = ToolsPM.findFactorsA(72072)
print(listff1)
listff2 = ToolsPM.findFactorsB(72072)
print(listff2)

