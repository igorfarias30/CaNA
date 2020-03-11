import sys

x = 1000

def asterisco(n: int) -> None:
    if (n > 1):
        for i in range(0, 7 * n):
            pass
        
        #global x
        #x = x + 7 * n
        #print(x)
        
        asterisco(n//5)
        asterisco(n//5)
        asterisco(n//6)
        asterisco(n//6)
        asterisco(n//6)
        asterisco(n//10)



if __name__ == "__main__":
    
    if len(sys.argv) > 1:
        asterisco(int(sys.argv[1]))
    else:
        print("too many arguments. try: python asterisco.py <N>")