
# Creation of summation class
class Summation(object):

    # Initializes an instance of the Summation class
    def __init__ (self,number_stop):
        self.number = number_stop

    # Function that sums a list of numbers from 1 to (including) the users input
    def sum (self):
        total = 0
        for num in range(self.number):
            total += num
        total = total + (num + 1)
        return total

# User input that is stored in the Summation class
if __name__ == "__main__":
    user_number = Summation(int(input("Please enter a number to which you would like to sum: ")))
    print(user_number.sum())