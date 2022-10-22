# seq --> 1 + 1/1! + 1/2! + .....

test_val = int(input("Enter the number of terms    "))
num = test_val
mul = test_val
seq_sum = 1

for termCtr in reversed(range(1, num+1)):
    prod = 1
    mul = test_val

    #factorial calc 
    for FactorialCtr in reversed(range(1, test_val+1)):
        prod = prod * mul
        mul = mul - 1 
     
    recp = (1/prod)
    #adding the terms 
    seq_sum = seq_sum + recp
    test_val = test_val - 1

print(seq_sum)