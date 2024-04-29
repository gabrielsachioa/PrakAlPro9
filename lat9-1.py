data = [10, 5, 3, 26, 92, 33, 60]
data.sort()

for i in range(len(data), 0, -1):
    if i == len(data) - 3:
        break
    else:
        print(data[i - 1])
    