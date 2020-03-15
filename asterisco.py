import sys

x = 0

def asterisco(n: int, a: int, b: int, c: int, d:int) -> int:
    global x

    if (n > 1):
        for _ in range(0, d * n):
            x += 1

        for _ in range(a): asterisco(n//5, a, b, c, d)
        for _ in range(b): asterisco(n//6, a, b, c, d)
        
        if c > 0:
            asterisco(n//10, a, b, c, d)
    
    return x


if __name__ == "__main__":
    
    if len(sys.argv) > 1:
        print(asterisco(int(sys.argv[1]), a=2, b=3, c=1, d=7))
    else:
        print("too many arguments. try: python asterisco.py <N>")