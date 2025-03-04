def funcThree():
    print('Three')
    
    
def funcTwo():
    funcThree()
    print('Two')
    
def funcOne():
    funcTwo()
    print('One')
    
    
    
funcOne()

print("---------------------------")


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(4))