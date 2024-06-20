import shelve
sh=shelve.open("shelvel")
print(list(sh.keys()))