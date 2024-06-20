def invert_content(dic):
    invert_dic={}
    invert_dic={k:v for k,v in dic.items()}
    return invert_dic
n=int(input("enter no of values"))
dic={}
for i in range(n):
    key=input("enter key")
    value=input("enter value")
    dic[key]=value
print(dic)
print("alter invention")
print(invert_content(dic))
