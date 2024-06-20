import pickle
fp=open('pickle.txt',"wb")
cn=['virat', "sirraj", "plessis"]
pickle.dump(cn,fp)
fp.close()