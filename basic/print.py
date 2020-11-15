import random
li = [random.randint(1,100) for _ in range(10)]
print(li)
count = 0
for i in li:
    print(i,end = ",")
    count += 1
    if count % 3 == 0:
        print()



