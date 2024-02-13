import os
if os.path.exists("1.txt") == True:
    ofr = open("1.txt","r")
    rofr = ofr.read()
    print(rofr)