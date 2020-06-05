def derOfx1(pred, m, y):
    return (1 / m) * (pred - y)


def derOfx2(pred, m, y, x):
    return (1 / m) * (pred - y) * x


x1 = 0
x2 = 0

data = [
    [1, 1],
    [2, 2],
    [3, 3],
    [4, 4]
]

predList = [

]

lr = 0.05
count = 1

for i in range(len(data)):
    pred = x1 + x2 * data[i][1]
    dataPt = [count, pred]
    predList.append(dataPt)
    count += 1

for i in range(2000):
    for j in range(len(data)):
        temp1 = x1 - lr * derOfx1(predList[j][1], 4, data[j][1])
        temp2 = x2 - lr * derOfx2(predList[j][1], 4, data[j][1], predList[j][0])
        x1 = temp1
        x2 = temp2
        predList[j][1] = x1 + x2 * predList[j][0]

error = sum([0.125 * (predList[i][1] - data[i][1]) ** 2 for i in range(len(data))])

print(error)

for i in predList:
    i[1] = round(i[1], 6)

print(predList)
x2 = round(x2, 6)
x1 = round(x1, 6)
print(f"Equation for line: y = {x2}x + {x1}")


def makePrediction(prediction):
    return x2 * prediction + x1


prediction = int(input("Enter a new data point to get a predicted value: "))
print(f"Predicted Value: {makePrediction(prediction)}")
