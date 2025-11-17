vehicleList=["Car", "Truck", "Jet"]
print(vehicleList)
print(type(vehicleList))
print(vehicleList[0])
print(vehicleList[1])
print(vehicleList[2])
vehicleList[1]="Boat"
print(vehicleList)

print("----------")

protectorTuple=("Helmet", "Knee Pad", "Glove")
print(protectorTuple)
print(type(protectorTuple))
print(protectorTuple[0])
print(protectorTuple[1])
print(protectorTuple[2])

print("----------")

partDictionary = {
    "control" : "Steering wheel",
    "drive" : "Dynamo",
    "power" : "Battery"
}
print(partDictionary)
print(type(partDictionary))
print(partDictionary["control"])
print(partDictionary["drive"])
print(partDictionary["power"])

print("---------")

myProgList = ["python", "php", "javascript", "c#", "golang"]
print(myProgList[3:])
myComplexDict = {
    "nama" : "Abdul Basri",
    "alamat" : {
        "kota" : "Jakarta Selatan",
        "provinsi" : "DKI Jakarta"
    }
}

print(myComplexDict["nama"] + " Alamat, " + myComplexDict["alamat"]["kota"], myComplexDict["alamat"]["provinsi"])
print(type(myComplexDict))