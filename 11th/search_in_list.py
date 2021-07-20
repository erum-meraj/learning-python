t = eval(input("ENter list"))
ele = int(input("ENter element to search ->   "))
length = len(t)
if ele in t:
    for ctr in range (0, length):
        if ele == t[ctr]:
            print("Index number = ", t.index(ele))
else:
    print("Item not in the given list")
