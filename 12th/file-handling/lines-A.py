def check(readtext, num_lines):
    cnt = 0 
    for i in range(1, num_lines):
        rtext = readtext.readline()
        let = rtext[0]
        if let == "A" or let == "a":
            cnt = cnt + 1
        else:
            continue
    return cnt
    
#reading
readtext = open(r"/Users/momeraj/Documents/erum/learning-python-master/12th/file-handling/Lines.txt", "r")
num_lines = sum(1 for line in open(r"/Users/momeraj/Documents/erum/learning-python-master/12th/file-handling/Lines.txt", "r"))
print("Lines with A = ", check(readtext, num_lines))
readtext.close()

