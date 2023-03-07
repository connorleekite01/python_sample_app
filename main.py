# use the calculator library to perform the following operations:
# 1. add 2 and 3
# 2. subtract 5 from 10
# 3. multiply 2 and 3
# 4. divide 10 by 2
# 5. square 2
# 6. square root of 4
# 7. cube 2
# 8. cube root of 8
# 9. 2 to the power of 3
# 10. 3 to the power of 2
# 11. 2 to the power of 0.5

import calculatorLibrary

calc = calculatorLibrary.CalculatorLibrary()

# print all the results with a description of what the result is
print("1. add 2 and 3: " + str(calc.add(2, 3)))
print("2. subtract 5 from 10: " + str(calc.subtract(10, 5)))
print("3. multiply 2 and 3: " + str(calc.multiply(2, 3)))
print("4. divide 10 by 2: " + str(calc.divide(10, 2)))
print("5. square 2: " + str(calc.square(2)))
print("6. square root of 4: " + str(calc.squareRoot(4)))
print("7. cube 2: " + str(calc.cube(2)))
print("8. cube root of 8: " + str(calc.cubeRoot(8)))
print("9. 2 to the power of 3: " + str(calc.power(2, 3)))
print("10. 3 to the power of 2: " + str(calc.power(3, 2)))
print("11. 2 to the power of 0.5: " + str(calc.power(2, 0.5)))
