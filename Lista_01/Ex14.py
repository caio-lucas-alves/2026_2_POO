x = int(input())
y = int(input())

def MDC(x, y):
    while y != 0:
        x, y = y, x % y
    return x


print("MDC=", MDC(x, y))
