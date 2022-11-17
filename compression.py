import sys

# coding: utf-8
def compress(x):
    count = 1
    ind = 1
    nex = x[ind]
    new = []
    for i in x:
       if i == nex:
           new.append(i)
       else:
           new.append(i)
           new.append(",")
       try:
           nex = x[ind+1]
       except IndexError:
           pass
       ind += 1
       
        
    new = "".join(new)
    new = new.split(",")
    result = []
    for i in range(len(new)):
        if len(new[i]) > 1:
            number = len(new[i])
            result.append([number, new[i][-1]])
            
        else:
            result.append(new[i])


    q = []
    for i in result:
        if type(i) == list:
            w = "".join(str(i))		
        else:
            w = i
        q.append(w)

    return "".join(q)



with open(sys.argv[1], "r", encoding="utf-8") as f:
	txt = f.read()
	result = compress(txt)
	file_name = sys.argv[1].replace(".txt", "")
	with open(file_name + " - compressed.txt", "w", encoding="utf-8") as h:
		h.write(result)
