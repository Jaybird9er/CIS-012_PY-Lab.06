## Asks the user to enter an integer between 1 and 10

print("Enter an integer between 1 and 10: ")
userInt = int(input())
while userInt < 1 or userInt > 10:
    print("Try again. Enter an integer between 1 and 10: ")
    userInt = int(input())

## Prints all even integers between startNumber and endNumber, inclusive
def printEvenNumber(startNumber, endNumber):
    while startNumber <= endNumber:
        if startNumber % 2 == 0:
            print(startNumber)
        startNumber += 1

print("\n")

print("Enter a start number: ")
startNumber = int(input())

print("Enter an end number: ")
endNumber = int(input())

print("\n")
print("From", startNumber, "to", endNumber, "here are all the even numbers:")
printEvenNumber(startNumber, endNumber)
