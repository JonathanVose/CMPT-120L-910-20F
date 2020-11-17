import Calculator

x = int(input("Please enter a number: "))
y = int(input("Please enter another number: "))

functions = Calculator.Calculator()

print(functions.addition(x,y))

print(functions.subtraction(x,y))

print(functions.division(x,y))

print(functions.multiplication(x,y))

print(functions.exponent(x,y))

print(functions.square_root(x))
print(functions.square_root(y))

print(functions.negate(x))
print(functions.negate(y))
