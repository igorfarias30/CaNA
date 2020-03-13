import sys

x = 0

def asterisco(n: int) -> int:
    global x

    if (n > 1):
        for _ in range(0, 7*n):
            x += 1

        for _ in range(2):
            asterisco(n//5)
        
        for _ in range(3):
            asterisco(n//6)

    return x


if __name__ == "__main__":
    
    if len(sys.argv) > 1:
        print(asterisco(int(sys.argv[1])))
    else:
        print("too many arguments. try: python asterisco.py <N>")