fp1=open("CSEa1.txt","r")
if fp1:
    print("file is opened successfully")

for i in fp1:
    print(i)

content=fp1.readline()
print(content)
content=fp1.readline()
print(content)

fp1.close()