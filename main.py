myList = []
average1 = 0
running = True
while running:
  num = input("fdsf")
  if num == "stop":
    running = False
    break
  num = int(num)
  myList.append(num)
for i in range(0, len(myList), 1):
  average1 += myList[i]

average1 /= len(myList)
print(average1)
