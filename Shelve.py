import shelve
with shelve.open("shelvel")as sh:
    sh['one']=1
    sh['two']=2
    sh['three']=3
sh.close