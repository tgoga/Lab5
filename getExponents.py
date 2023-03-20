
def main():
    num = input("Enter a number: ")
    print("The square is : ", getSquare(float(num)) )

def getSquare(value) :
    return pow(value, 2)
   

if __name__ == "__main__":
    main()

