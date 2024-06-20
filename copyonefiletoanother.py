fp1=open("CSEa1.txt","r")
fp2=open("CSEa2.txt","w+")
if fp1:
    print("file opened successfully")
for i in fp1:
    fp2.write(i)
print("file is copied succesfully")
fp2.seek(0,0)
cont=fp2.read()
print(cont)
fp1.close