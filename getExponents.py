
def main():
    num = input("Enter a number: ")
    print("The square value is : ", getSquare(float(num)) )
    print("The cube value is : ", getCube(float(num))) 

def getSquare(value) :
    return pow(value, 2)

def getCube(value) :
    return pow(value, 3)

if __name__ == "__main__":
    main()

