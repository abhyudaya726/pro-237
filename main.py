import random
with open("hello.txt","w+") as f:
    for i in range(0,10):
        f.write(str(random.randint(100,200)*i))
        f.write("\n")