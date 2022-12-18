

#####################################################
#######      Simple for loop to do febonacci   ######
#####################################################


r=[0,1]
for x in range(10):
    s=r[x]+r[x+1]
    r.append(s)
print("Febonacci from for loop ")
print(r)

print("$"*50)


#####################################################
###### Febonacci from recursion function     ########
#####################################################


i=0
seq=[0,1]
def febonacci(n):

    global i

    if n<0:
        print("enter positive number ")
        a=input("write 'y' to try agin 'n' to exit ")
        if a.lower() == 'y':
            return febonacci(int(input("Enter number of Repetition : ")))
        elif a.lower() == 'n':
            print("Exit")
        else:
            print("Its not a joke write the fucking true answer : ")
            return febonacci(n)
    elif n==0:
        return seq
    else:
        sum = seq[i] + seq[i+1]
        seq.append(sum)
        i+=1
        return febonacci(n-1)


n = int(input("Enter number of Repetition : "))
x= febonacci(n)
print(x)




































