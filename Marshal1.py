import marshal
src='''
a=10
b=29
print("Multiplication=",a*b)
'''
code = compile(src,"src","exec")
fp=open("marshal.txt","wb")
marshal.dump(code,fp)
fp.close()
