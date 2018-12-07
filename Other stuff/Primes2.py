import ast



def primes(x,primesl):
    root=(x)**(1/2)
    list=1


    while(primesl[list]<=root):
        if x%primes[list]==0:
            #print("{} number is not Prime".format(numb))
            break
        else:
            list+=1
    return(x)




with open('primes.txt', 'r') as f:
    primes = ast.literal_eval(f.read())


print(primes(5,primes))
