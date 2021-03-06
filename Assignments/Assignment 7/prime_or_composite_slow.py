def prime_or_composite(number):
    """
    Add code in the defined function to figure out whether or not the given number is a prime number or not. 
    A prime number (or a prime) is a natural number greater than 1 that is not a product of two smaller natural numbers. 
    A natural number greater than 1 that is not prime is called a composite number. - Wikipedia
    Take in a parameter called number and return “Prime” or “Composite”
    """
    temp = number

    if number > 2:
        for x in range (2,temp):
            if (number % x == 0):
                return(str(temp) + " is a composite number.")
                break
        else:
            return(str(temp) + " is a prime number.")
    elif number == 2:
        return(str(temp) + " is a prime number.")
    elif number <= 1:
        return(str(temp) + " is not a prime or composite number")


if __name__ == "__main__":
    numbers = [1, 2, 10, 31, 47, 89, 101, 103, 97, 187, 981, 19201, -7, 47055833459]
    # If you want to test the efficency of your algorithm add this number to the array above -7
    # If you want to test the efficency of your algorithm add this number to the array above 47055833459
    # 1, 2, 10, 31, 47, 89, 101, 103, 97, 187, 981, 19201
    answers = []
    x = 0
    for number in numbers:
        answers.append(prime_or_composite(number))
        print( answers[x])
        x += 1 