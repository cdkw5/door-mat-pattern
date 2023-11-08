if __name__ == '__main__':
    l=input()
    x=l.split()
    a=int(x[0])
    b=int(x[1])
    for i in range(1,a+1):
        if i==int((a+1)/2) :
            print("-"*int(((b-len("WELCOME"))/2)),"WELCOME","-"*int(((b-len("WELCOME"))/2)),sep="")
            break
        else:
            print("-"*int((b-len(".|."*(2*i-1)))/2),".|."*(2*i-1),"-"*int((b-len(".|."*(2*i-1)))/2),sep="")
            
    for j in range(int((a+1)/2)-1,0,-1):
        print("-"*int((b-len(".|."*(2*j-1)))/2),".|."*(2*j-1),"-"*int((b-len(".|."*(2*j-1)))/2),sep="")
