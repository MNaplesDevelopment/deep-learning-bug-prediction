file = open("output.txt", "r")
arr = file.readlines()
trainData = []
trainLabel = []
for x in arr:
    temp = x.split(",")

    trainLabel.append(temp[len(temp)-1])
    del temp[len(temp)-1]
    trainData.append(temp)

trainLabel = [item.strip() for item in trainLabel]
trainLabel[len(trainLabel)-1] = "23"
trainData = [list(map(float, x)) for x in trainData]
trainLabel = list(map(int, trainLabel))

print(trainLabel)
print(trainData)
print(len(trainLabel))
print(len(trainLabel))

file2 = open("output2.txt", "r")
arr2 = file2.readlines()
testData = []
testLabel = []

for x in arr2:
    temp = x.split(",")

    testLabel.append(temp[len(temp)-1])
    del temp[len(temp)-1]
    testData.append(temp)

testLabel = [item.strip() for item in testLabel]
testData = [list(map(float, x)) for x in testData]
testLabel[len(testLabel)-1] = "0"
testLabel = list(map(int, testLabel))
testData[len(testData)-1]  = [5,2,2,3,3,0,1,0,17,3,43,1,0,0,2,6,5]
trainData[len(trainData)-1] = [8,2,4,4,780,0,49,20,347,40,25,22,0,0,39,105,100]


print(testLabel)
print(testData)
print(len(testLabel))
print(len(testData))
print(len(testData[len(testData)-1]))
print(len(testData[len(testData)-2]))
print(len(testData[len(testData)-3]))
print(testData[len(testData)-1])
print(len(trainData[len(trainData)-1]))
print(len(trainData[len(trainData)-2]))
print(len(trainData[len(trainData)-3]))