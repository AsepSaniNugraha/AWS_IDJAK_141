myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]
print(type(myMixedTypeList))
print(type(myMixedTypeList[0]))
print(type(myMixedTypeList[1]))
print(type(myMixedTypeList[2]))
print(type(myMixedTypeList[3]))
print(type(myMixedTypeList[4]))
print(type(myMixedTypeList[5]))

print("-------")
for item in myMixedTypeList:
    print(type(item))

print("-------")
for item in myMixedTypeList:
    print(item, type(item))