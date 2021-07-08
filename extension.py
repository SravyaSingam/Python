n=input("Input the Filename: ")
print(n)
try: #tries if file extension is found
    y=n.rindex('.') #finding the index of dot
    a=y+1
    z=(n[a:])     #getting the extension
    b=z.lower()
    dict={"py":"python",
      "c":"C",
      "cpp":"c++",
      "java":"java"}
    if b in dict.keys():
        print("Extension of file is :",repr(dict[b]))
    else:    #if extension key is not prsent in dictionary
        print("Extension of file is :",repr(b))
except ValueError: # if extension is not found
    print("Extension of file is not found")
