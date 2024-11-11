import math
import cmath
from sympy import sympify, sqrt, log, sin, cos, tan, exp, I, Number, SympifyError # need to intsall first
from sympy.physics.units import kg, m, G
import numpy as np
import numpy_financial as npf
import matplotlib.pyplot as plt
from datetime import date
from HelpFunctions import HelpFunctions

class CalculatorFunctions:

    def __init__(self):
        self.help_func = HelpFunctions()

    def simple_calculation(self):  # No.1
        variables = {}  # Dictionary to store variables
        history = []  # List to store history of calculations

        while True:
            try:
                expression = input("Enter a calculation (or type 'help' for instructions, 'history' for past calculations): ").strip()

                # Display help instructions
                if expression.lower() == "help":
                    self.help_func.clear_screen()
                    help_text = """
    Calculator Instructions:
                        
    1. Basic Operations:
    Use +, -, *, /, and ^ for addition, subtraction, multiplication, division, and exponentiation.
                        
    2. Square Root:
    Use 'sqrt(x)' to calculate the square root of x.
    Example: sqrt(16)
                        
    3. Logarithmic Functions:
    Use 'log(x)' for natural logarithm and 'log10(x)' for base-10 logarithm.
    Example: log(10), log10(100)
                        
    4. Trigonometric Functions:
    Use 'sin(x)', 'cos(x)', and 'tan(x)' for sine, cosine, and tangent calculations.
    Example: sin(45)
                        
    5. Exponential Function:
    Use 'exp(x)' to calculate e^x.
    Example: exp(2)
                        
    6. Variable Assignment:
    Assign values to variables using '='. Example: x = 5, then use 'x' in calculations.
                        
    7. Complex Numbers:
    The calculator supports complex numbers. Example: sqrt(-1) results in 'I'.
                        
    8. View History:
    Type 'history' to view your past calculations.
                        
    9. Back to menu:
    Type 'back' to simple calculation function in the calculator.
    """
                    self.help_func.text_helper(help_text)

                # Check for history command
                elif expression.lower() == "history":
                    self.help_func.clear_screen()
                    if history:
                        print("Calculation History:")
                        for line in history:
                            print(line)
                            self.help_func.pause()
                            self.help_func.clear_screen()
                    else:
                        print("No history available.")
                    continue

                # Check for quit command
                elif expression.lower() == "back":
                    print("Exiting the calculator. Goodbye!")
                    break

                # Check for empty input
                if not expression:
                    self.help_func.clear_screen()
                    print("Error: Please enter a valid mathematical expression.")
                    continue

                # Check if the expression contains only valid characters and functions
                if not all(char.isdigit() or char in "+-*/().^ sqrtlogsincoetanexp " for char in expression.replace("sqrt", "").replace("log", "").replace("sin", "").replace("cos", "").replace("tan", "").replace("exp", "")):
                    self.help_func.clear_screen()
                    print("Error: Only numbers, valid operators, and functions (sqrt, log, sin, cos, tan, exp) are allowed.")
                    continue

                # Handle variable assignment
                if "=" in expression:
                    var, expr = expression.split("=")
                    var = var.strip()
                    expr = expr.strip()
                    variables[var] = sympify(expr, locals=variables)
                    print(f"{var} = {variables[var]}")
                    history.append(f"{var} = {variables[var]}")
                    continue

                # Evaluate expression with variables
                result = sympify(expression, locals=variables)  # Safely parse the expression with variables

                # Check for very large results
                if isinstance(result, Number) and (result >= 10**100 or result <= -10**100):
                    print("Error: The result is too large to display.")
                else:
                    self.help_func.clear_screen()
                    self.help_func.clear_screen()
                    print(f"The result of {expression} is {result}")
                    history.append(f"{expression} = {result}")  # Add to history
                    self.help_func.pause()
                    self.help_func.clear_screen()
                # End menu prompt
                while True:
                    text = """
    Do you want to perform another calculation?
        1. Yes
        2. No
        Enter your choice (1 or 2): """
                    end_choice = input(text).strip()
                    if end_choice == '1':
                        self.help_func.clear_screen()
                        break  # Continue the while loop for another calculation
                    elif end_choice == '2':
                        self.help_func.clear_screen()
                        return  # Exit the function entirely
                    else:
                        self.help_func.clear_screen()
                        print("Please enter 1 or 2.")

            except SympifyError:
                self.help_func.clear_screen()
                print("Error: Please enter a valid mathematical expression.")
            except ValueError:
                self.help_func.clear_screen()
                print("Error: Invalid input. Please enter a numerical expression.")

    def shape_calculations(self): # No.2

        text = """
Shape Calculations.
You can calculate the area and perimeter/circumference of a shape by selecting an option.
    1. Square Calculation
    2. Rectangle Calculation
    3. Kite Calculation
    4. Circle Calculation
    5. Cylinder Calculation
    6. Triangle Calculation
    7. Pentagon Calculation
    8. Hexagon Calculation
    9. Polygon Calculation
    10. Lune Calculation
    11. Go Back
Enter your choice (1-11): """

        while True:
            choice = input(text).strip()
            self.help_func.clear_screen()
            if choice == '1':  # Square
                while True:
                    squar_text = """
Square Calculation.
You can enter any square calculation:
    1. Square Area (units²)
    2. Square Perimeter (units)
    3. Calculate Both Area and Perimeter
Enter your choice (1, 2 or 3):  """
                    squar_choice = input(squar_text).strip()
                    self.help_func.clear_screen()
                    if squar_choice == '1':
                        self.help_func.clear_screen()
                        side = self.help_func.get_float_input("Enter the length of a side of the square: ")
                        area = side ** 2
                        self.help_func.clear_screen()
                        print(f"The area of the square with side length {side} is {area} units²")
                        break
                    elif squar_choice == '2':
                        self.help_func.clear_screen()
                        side = self.help_func.get_float_input("Enter the length of a side of the square: ")
                        perimeter = 4 * side
                        self.help_func.clear_screen()
                        print(f"The perimeter of the square with side length {side} is {perimeter} units")
                        break
                    elif squar_choice == '3':
                        self.help_func.clear_screen()
                        side = self.help_func.get_float_input("Enter the length of a side of the square: ")
                        area = side ** 2
                        perimeter = 4 * side
                        self.help_func.clear_screen()
                        print(f"The area of the square with side length {side} is {area} units²")
                        print(f"The perimeter of the square with side length {side} is {perimeter} units")
                        break
                    else:
                        self.help_func.clear_screen()
                        print("Invalid choice for square calculation. Please enter 1, 2 or 3.")
                break  # Break after the square calculation

            elif choice == '2':  # Rectangle
                while True:
                    rectangle_text = """
Rectangle Calculation.
You can enter any rectangle calculation:
    1. Rectangle Area (units²)
    2. Rectangle Perimeter (units)
    3. Calculate Both Area and Perimeter
Enter your choice (1, 2 or 3): """
                    rectangle_choice = input(rectangle_text).strip()
                    self.help_func.clear_screen()
                    if rectangle_choice == '1':
                        self.help_func.clear_screen()
                        length = self.help_func.get_float_input("Enter the length of the rectangle: ")
                        width = self.help_func.get_float_input("Enter the width of the rectangle: ")
                        area = length * width
                        self.help_func.clear_screen()
                        print(f"The area of the rectangle with length {length} and width {width} is {area} units²")
                        break
                    elif rectangle_choice == '2':
                        self.help_func.clear_screen()
                        length = self.help_func.get_float_input("Enter the length of the rectangle: ")
                        width = self.help_func.get_float_input("Enter the width of the rectangle: ")
                        perimeter = 2 * (length + width)
                        self.help_func.clear_screen()
                        print(f"The perimeter of the rectangle with length {length} and width {width} is {perimeter} units")
                        break
                    elif rectangle_choice == '3':
                        self.help_func.clear_screen()
                        length = self.help_func.get_float_input("Enter the length of the rectangle: ")
                        width = self.help_func.get_float_input("Enter the width of the rectangle: ")
                        area = length * width
                        perimeter = 2 * (length + width)
                        self.help_func.clear_screen()
                        print(f"The area of the rectangle with length {length} and width {width} is {area} units²")
                        print(f"The perimeter of the rectangle with length {length} and width {width} is {perimeter} units")
                        break
                    else:
                        self.help_func.clear_screen()
                        print("Invalid choice for rectangle calculation. Please enter 1, 2 or 3.")
                break  # Break after the rectangle calculation

            elif choice == '3': # Kite
                while True:
                    kite_text = """
Kite Calculation.
You can enter any kite calculation:
    1. Kite Area (units²)
    2. Kite Perimeter (units)
    3. Calculate Both Area and Perimeter
Enter your choice (1, 2 or 3): """
                    kite_choice = input(kite_text).strip()
                    self.help_func.clear_screen()
                    if kite_choice == '1':
                        d1 = self.help_func.get_float_input("Enter the length of the first diagonal (d1): ")
                        d2 = self.help_func.get_float_input("Enter the length of the second diagonal (d2): ")
                        self.help_func.clear_screen()
                        area = 0.5 * d1 * d2
                        print(f"The area of the kite with diagonals {d1} and {d2} is {area:.2f} units².")
                        break
                    elif kite_choice == '2':
                        a = self.help_func.get_float_input("Enter the length of one pair of equal sides (a): ")
                        b = self.help_func.get_float_input("Enter the length of the other pair of equal sides (b): ")
                        self.help_func.clear_screen()
                        perimeter = 2 * (a + b)
                        print(f"The perimeter of the kite with sides {a} and {b} is {perimeter:.2f} units.")
                        break
                    elif kite_choice == '3':
                        d1 = self.help_func.get_float_input("Enter the length of the first diagonal (d1): ")
                        d2 = self.help_func.get_float_input("Enter the length of the second diagonal (d2): ")
                        self.help_func.clear_screen()
                        a = self.help_func.get_float_input("Enter the length of one pair of equal sides (a): ")
                        b = self.help_func.get_float_input("Enter the length of the other pair of equal sides (b): ")
                        self.help_func.clear_screen()
                        area = 0.5 * d1 * d2
                        perimeter = 2 * (a + b)
                        print(f"The area of the kite with diagonals {d1} and {d2} is {area:.2f} units².")
                        print(f"The perimeter of the kite with sides {a} and {b} is {perimeter:.2f} units.")
                        break
                    else:
                        self.help_func.clear_screen()
                        print("Invalid choice for kite calculation. Please enter 1, 2 or 3.")
                break # Break after the kite calculation

            elif choice == '4':  # Circle
                while True:
                    circle_text = """
Circle Calculation.
You can enter any circle calculation:
    1. Circle Circumference (units)
    2. Circle Area (units²)
    3. Calculate Both Area and Perimeter
Enter your choice (1, 2 or 3): """

                    circle_choice = input(circle_text).strip()
                    self.help_func.clear_screen()
                    if circle_choice == '1':
                        radius = self.help_func.get_float_input("Enter the radius of the circle: ")
                        circumference = 2 * math.pi * radius
                        self.help_func.clear_screen()
                        print(f"The circumference of the circle with the radius of {radius} is {circumference} units")
                        break
                    elif circle_choice == '2':
                        radius = self.help_func.get_float_input("Enter the radius of the circle: ")
                        area = math.pi * radius ** 2
                        self.help_func.clear_screen()
                        print(f"The area of the circle with the radius of {radius} is {area} units²")
                        break
                    elif circle_choice == '3':
                        radius = self.help_func.get_float_input("Enter the radius of the circle: ")
                        circumference = 2 * math.pi * radius
                        area = math.pi * radius ** 2
                        self.help_func.clear_screen()
                        print(f"The circumference of the circle with the radius of {radius} is {circumference} units")
                        print(f"The area of the circle with the radius of {radius} is {area} units²")
                        break
                    else:
                        self.help_func.clear_screen()
                        print("Invalid choice for circle calculation. Please enter 1, 2 or 3.")
                break  # Break after the circle calculation

            elif choice == '5':  # Cylinder
                while True:
                    cylinder_text = """
Cylinder Calculation.
You can enter any cylinder calculation:
    1. Circumference of The Cylinder Base (units)
    2. Total Perimeter (Unfolded) (units)
    3. Cylinder Surface Area (units²)
    4. Cylinder volume (units³)
    5. Option 1, 2, 3 and 4
Enter your choice (1-5): """
                    cylinder_choice = input(cylinder_text).strip()
                    self.help_func.clear_screen()
                    if cylinder_choice == '1':  # Circumference of the cylinder base
                        r = self.help_func.get_float_input("Enter the radius of the cylinder: ")
                        c = 2 * math.pi * r
                        self.help_func.clear_screen()
                        print(f"The circumference of the circular base of the cylinder with the radius of {r} is {c} units")
                        break
                    elif cylinder_choice == '2':  # Total perimeter
                        r = self.help_func.get_float_input("Enter the radius of the cylinder: ")
                        h = self.help_func.get_float_input("Enter the height of the cylinder: ")
                        p = (2 * math.pi * r) + (2 * h)
                        self.help_func.clear_screen()
                        print(f"The total perimeter for the cylinder with the radius of {r} and height of {h} when unfolded into a rectangle is {p} units.")
                        break
                    elif cylinder_choice == '3':  # Surface area
                        r = self.help_func.get_float_input("Enter the radius of the cylinder: ")
                        h = self.help_func.get_float_input("Enter the height of the cylinder: ")
                        a = 2 * math.pi * r * (r + h)
                        self.help_func.clear_screen()
                        print(f"The total area covering the outside of the cylinder with the radius of {r} and height of {h} is {a} units².")
                        break
                    elif cylinder_choice == '4':  # Volume calculation
                        r = self.help_func.get_float_input("Enter the radius of the cylinder: ")
                        h = self.help_func.get_float_input("Enter the height of the cylinder: ")
                        volume = math.pi * r ** 2 * h
                        self.help_func.clear_screen()
                        print(f"The volume of the cylinder with the radius of {r} and height of {h} is {volume} units³.")
                        break
                    elif cylinder_choice == '5':  # all in one
                        r = self.help_func.get_float_input("Enter the radius of the cylinder: ")
                        h = self.help_func.get_float_input("Enter the height of the cylinder: ")
                        self.help_func.clear_screen()

                        # Calculate all properties
                        c = 2 * math.pi * r # Circumference of the cylinder base
                        p = (2 * math.pi * r) + (2 * h)  # Total perimeter
                        a = 2 * math.pi * r * (r + h)  # Surface area
                        volume = math.pi * r ** 2 * h  # Volume

                        # Display results
                        print(f"The circumference of the circular base of the cylinder with the radius of {r} is {c} units.")
                        print(f"The total perimeter for the cylinder with the radius of {r} and height of {h} when unfolded into a rectangle is {p} units.")
                        print(f"The total area covering the outside of the cylinder with the radius of {r} and height of {h} is {a} units².")
                        print(f"The volume of the cylinder with the radius of {r} and height of {h} is {volume} units³.")
                        break
                    else:
                        self.help_func.clear_screen()
                        print("Invalid choice for cylinder calculation. Please enter (1-5).")
                break  # Break after the cylinder calculation

            elif choice == '6':  # Triangle
                while True:
                    which_triangle = """
which shape of triangle you want to calculate:
    1. Normal Triangle
    2. Equilateral Triangle
Enter your choice (1 or 2): """
                    which_triangle_choice = input(which_triangle).strip()
                    if which_triangle_choice == '1':
                        self.help_func.clear_screen()
                        while True:
                            triangle_text = """
Normal Triangle Calculation.
You can enter any triangle calculation:
    1. Triangle Area (units²)
    2. Triangle Perimeter (units)
    3. Calculate Both Area and Perimeter
Enter your choice (1, 2 or 3): """
                            triangle_choice = input(triangle_text).strip()
                            self.help_func.clear_screen()
                            if triangle_choice == '1':
                                base = self.help_func.get_float_input("Enter the base of the triangle: ")
                                height = self.help_func.get_float_input("Enter the height of the triangle: ")
                                area = 0.5 * base * height
                                self.help_func.clear_screen()
                                print(f"The area of the triangle with base {base} and height {height} is {area:.2f} units².")
                                break
                            elif triangle_choice == '2':
                                side1 = self.help_func.get_float_input("Enter the length of the first side of the triangle: ")
                                side2 = self.help_func.get_float_input("Enter the length of the second side of the triangle: ")
                                side3 = self.help_func.get_float_input("Enter the length of the third side of the triangle: ")
                                perimeter = side1 + side2 + side3
                                self.help_func.clear_screen()
                                print(f"The perimeter of the triangle with sides {side1}, {side2}, and {side3} is {perimeter:.2f} units.")
                                break
                            elif triangle_choice == '3':
                                base = self.help_func.get_float_input("Enter the base of the triangle: ")
                                height = self.help_func.get_float_input("Enter the height of the triangle: ")
                                side1 = self.help_func.get_float_input("Enter the length of the first side of the triangle: ")
                                side2 = self.help_func.get_float_input("Enter the length of the second side of the triangle: ")
                                side3 = self.help_func.get_float_input("Enter the length of the third side of the triangle: ")
                                area = 0.5 * base * height
                                perimeter = side1 + side2 + side3
                                self.help_func.clear_screen()
                                print(f"The area of the triangle with base {base} and height {height} is {area:.2f} units.²")
                                print(f"The perimeter of the triangle with sides {side1}, {side2}, and {side3} is {perimeter:.2f} units.")
                                break
                            else:
                                self.help_func.clear_screen()
                                print("Invalid choice for triangle calculation. Please enter 1, 2 or 3.")
                        break
                    elif which_triangle_choice == '2':
                        self.help_func.clear_screen()
                        while True:
                            Eq_triangle_text = """
Equilateral Triangle Calculation.
You can enter any equilateral triangle calculation:
    1. Equilateral Triangle Area (units²)
    2. Equilateral Triangle Perimeter (units)
    3. Calculate Both Area and Perimeter
Enter your choice (1, 2 or 3):  """

                            Eq_triangle_choice = input(Eq_triangle_text).strip()
                            self.help_func.clear_screen()
                            if Eq_triangle_choice == '1':
                                s = self.help_func.get_float_input("Enter any side: ")
                                self.help_func.clear_screen()
                                a = (cmath.sqrt(3) / 4) * (s ** 2)
                                area = self.help_func.handle_large_numbers(a)
                                print(f"The area for the equilateral triangle with the sides of {s} is {area:.2f} units².")
                                break
                            elif Eq_triangle_choice == '2':
                                s = self.help_func.get_float_input("Enter any side: ")
                                self.help_func.clear_screen()
                                perimeter = 3 * s
                                print(f"The perimeter for the equilateral triangle with the sides of {s} is {perimeter:.2f} units.")
                                break
                            elif Eq_triangle_choice == '3':
                                s = self.help_func.get_float_input("Enter any side: ")
                                self.help_func.clear_screen()
                                a = (cmath.sqrt(3) / 4) * (s ** 2)
                                perimeter = 3 * s
                                area = self.help_func.handle_large_numbers(a)
                                print(f"The area for the equilateral triangle with the sides of {s} is {area:.2f} units².")
                                print(f"The perimeter for the equilateral triangle with the sides of {s} is {perimeter:.2f} units.")
                                break
                            else:
                                self.help_func.clear_screen()
                                print("Invalid choice for equilateral triangle calculation. Please enter 1, 2, or 3.")
                        break
                    else:
                        self.help_func.clear_screen()
                        print("Invalid choice for which riangle calculation. Please enter 1 or 2.")             
                break  # Break after the triangle calculation

            elif choice == '7': # Pentagon
                while True:
                    pentagon_text = """
Pentagon Calculation.
You can enter any pentagon calculation:
    1. Pentagon Area (units²)
    2. Pentagon Perimeter (units)
    3. Calculate Both Area and Perimeter
Enter your choice (1, 2 or 3): """

                    pentagon_choice = input(pentagon_text).strip()
                    self.help_func.clear_screen()
                    if pentagon_choice == '1':
                        s = self.help_func.get_float_input("Enter the length of a side: ")
                        self.help_func.clear_screen()

                        discriminant =  5 * (5 + 2 * math.sqrt(5))
                        area = (1/4) * math.sqrt(discriminant) * s**2

                        print(f"The area for the pentagon with the length of a side of {s} is {area:.2f} units².")
                        break
                    elif pentagon_choice == '2':
                        s = self.help_func.get_float_input("Enter the length of a side: ")
                        self.help_func.clear_screen()
                        perimeter = 5 * s
                        print(f"The perimeter for the pentagon with the length of a side of {s} is {perimeter:.2f} units.")
                        break     
                    elif pentagon_choice == '3':
                        s = self.help_func.get_float_input("Enter the length of a side: ")
                        self.help_func.clear_screen()  

                        discriminant =  5 * (5 + 2 * math.sqrt(5))
                        area = (1/4) * math.sqrt(discriminant) * s**2   
                        perimeter = 5 * s

                        print(f"The area for the pentagon with the length of a side of {s} is {area:.2f} units².")
                        print(f"The perimeter for the pentagon with the length of a side of {s} is {perimeter:.2f} units.")
                        break  
                    else:
                        self.help_func.clear_screen()
                        print("Invalid choice for pentagon calculation. Please enter 1, 2 or 3.")
                break # Break after the pentagon calculation

            elif choice == '8': # Hexagon
                while True:
                    hexagon_text = """
Hexagon Calculation.
You can enter any Hexagon calculation:
    1. Hexagon Area (units²)
    2. Hexagon Perimeter (units)
    3. Calculate Both Area and Perimeter
Enter your choice (1, 2 or 3): """

                    hexagon_choice = input(hexagon_text).strip
                    self.help_func.clear_screen()
                    if hexagon_choice == '1':
                        s = self.help_func.get_float_input("Enter the length of a side: ")
                        self.help_func.clear_screen()

                        discriminant = 2 / (3 * cmath.sqrt(3))
                        area = discriminant * s ** 2

                        print(f"The area for the hexagon with the length of a side of {s} is {area:.2f} units².")
                        break
                    elif hexagon_choice == '2':
                        s = self.help_func.get_float_input("Enter the length of a side: ")
                        self.help_func.clear_screen()

                        perimeter = 6 * s

                        print(f"The perimeter the for the hexagon with the length of a side of {s} is {perimeter:.2f} units.")
                        break   
                    elif hexagon_choice == '3':
                        s = self.help_func.get_float_input("Enter the length of a side: ")
                        self.help_func.clear_screen()      

                        discriminant = 2 / (3 * cmath.sqrt(3))
                        area = discriminant * s ** 2
                        perimeter = 6 * s

                        print(f"The area for the hexagon with the length of a side of {s} is {area:.2f} units².")
                        print(f"The perimeter for the hexagon with the length of a side of {s} is {perimeter:.2f} units.")
                        break   
                    else:
                        self.help_func.clear_screen()
                        print("Invalid choice for hexagon calculation. Please enter 1, 2 or 3.")
                break # Break after the hexagon calculation

            elif choice == '9':  # Polygon
                while True:
                    polygon_text = """
Polygon Calculation.
You can enter any Polygon calculation:
    1. Polygon Area (units²)
    2. Polygon Perimeter (units)
    3. Calculate Both Area and Perimeter
Enter your choice (1, 2 or 3): """

                    polygon_choice = input(polygon_text).strip()
                    self.help_func.clear_screen()
                    if polygon_choice == '1':
                        n = self.help_func.get_float_input("Enter the number of sides: ")
                        s = self.help_func.get_float_input("Enter the length of a side: ")
                        self.help_func.clear_screen()

                        area = (1/4) * n * (s ** 2) * (1 / math.tan(math.pi / n))

                        print(f"The area for the polygon with {n} sides and the length of a side of {s} is {area:.2f} units².")
                        break
                    elif polygon_choice == '2':
                        n = self.help_func.get_float_input("Enter the number of sides: ")
                        s = self.help_func.get_float_input("Enter the length of a side: ")
                        self.help_func.clear_screen()  

                        perimeter = n * s

                        print(f"The perimeter for the polygon with {n} sides and the length of a side of {s} is {perimeter:.2f} units.")
                        break 
                    elif polygon_choice == '3':
                        n = self.help_func.get_float_input("Enter the number of sides: ")
                        s = self.help_func.get_float_input("Enter the length of a side: ")
                        self.help_func.clear_screen()

                        area = (1/4) * n * (s ** 2) * (1 / math.tan(math.pi / n))
                        perimeter = n * s

                        print(f"For the polygon with {n} sides, each of length {s}:")
                        print(f" - Area: {area:.2f} units²")
                        print(f" - Perimeter: {perimeter:.2f} units")
                        break
                    else:      
                        self.help_func.clear_screen()
                        print("Invalid choice for polygon calculation. Please enter 1, 2 or 3.")                                
                break # Break after the Polygon calculation

            elif choice == '10': # Lune
                lune_text ="""
Lune Area Calculation.

To calculate the area of a lune (the crescent-shaped region formed by two intersecting circles), 
please provide the radius of the larger circle, the radius of the smaller circle, 
and the central angles of the circular segments for each circle.
"""
                self.help_func.text_helper(lune_text)
                    
                R = self.help_func.get_float_input("Enter the radius of the larger circle: ")
                angle1 = self.help_func.get_float_input("Enter the central angle of the circular segment in the larger circle (in radians): ")
                self.help_func.clear_screen()
                r = self.help_func.get_float_input("Enter the radius of the smaller circle: ")
                angle2 = self.help_func.get_float_input("Enter the central angle of the circular segment in the smaller circle (in radians): ")
                self.help_func.clear_screen()

                area = (R ** 2) * (angle1 - math.sin(angle1)) - (r ** 2) * (angle2 - math.sin(angle2))

                print(f"The area of the lune with a larger circle radius of {R}, a smaller circle radius of {r}")
                print(f"and central angles {angle1} and {angle2} (in radians) is approximately {area:.2f} units².")
                break # Break after the lune calculation
            
            elif choice == '11': # back
                break
            
            else: # wrong input
                print("Invalid choice for shape calculations. Please enter (1-11).")

    def percentage_calculation(self): # No.3

        num1 = self.help_func.get_float_input("Enter the number you want to know the percentage of: ")
        num2 = self.help_func.get_float_input("Enter the total number: ")
        result = (num1 / num2) * 100

        self.help_func.clear_screen()
        print(f"The percentage of {num1} from {num2} is {result:.2f}%.")

    def quadratic_calculations(self):  # No.4
        text = """
Quadratic Calculation.
You can calculate the quadratic equation, quadratic function or cubic functions
    1. Quadratic Function
    2. Quadratic Equation
    3. Cubic Function
    4. Go Back
Enter your choice (1-4): """
        while True:
            choice = input(text).strip()
            self.help_func.clear_screen()

            if choice == '1':  # Quadratic function
                quadratic_text = """
Quadratic Function.
The equation is y = x^2.
You will need to input the first number and the last number you want to stop at; these will be the factors for x.
The program will output y for every number between the first number and the last one,
and will output the highest point and the mean of y values.
"""
                self.help_func.text_helper(quadratic_text)

                x_1 = self.help_func.get_float_input("Enter the first number: ")
                x_2 = self.help_func.get_float_input("Enter the second number: ")
                x = list(range(int(x_1), int(x_2) + 1))
                self.help_func.clear_screen()

                y_values = []  # To store y values

                print(" x   |  y = x^2")
                print("---------------")
                for num in x:
                    result = num ** 2  # Calculate y as x squared
                    y_values.append(result)  # Store the y value
                    print(f" {num}   |    {result}")

                highest_point = (x_2, x_2 ** 2)  # Highest point based on the last value
                mean_of_y = sum(y_values) / len(y_values)  # Calculate mean of y values

                print(f"Highest Point: {highest_point}")
                print(f"Mean of y values: {mean_of_y:.2f}")  # Format mean to 2 decimal places
                break

            elif choice == '2':  # Quadratic equation
                root_text = """
This program calculates the solutions of a quadratic equation in the form:
                    
    ax^2 + bx + c = 0
    x = -(b / a*2)

Where:
- a: Coefficient of x^2
- b: Coefficient of x
- c: Constant term

The function computes the discriminant (D = b^2 - 4ac) to determine the nature of the roots:
- If D > 0: Two distinct real solutions.
- If D = 0: One real solution (a double root).
- If D < 0: Two complex solutions.
- and gets the vertex

You will be prompted to input the coefficients a, b, and c.
The program will return the corresponding solutions based on the value of the discriminant.
"""
                self.help_func.text_helper(root_text)

                while True:
                    a = self.help_func.get_float_input("Enter the coefficient a: ")
                    b = self.help_func.get_float_input("Enter the coefficient b: ")
                    c = self.help_func.get_float_input("Enter the constant c: ")
                    self.help_func.clear_screen()
                    if a == 0:
                        print("Coefficient 'a' cannot be zero for a quadratic equation.")
                        continue

                    discriminant = b ** 2 - 4 * a * c
                    x = -b / (2 * a)

                    if discriminant > 0:
                        root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
                        root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
                        result1 = self.help_func.handle_large_numbers(root1)
                        result2 = self.help_func.handle_large_numbers(root2)
                        print(f"There are two distinct real solutions: {result1.real} and {result2.real}")
                        print(f"The vertex of the parabola represented by the quadratic function is {x}")
                        break

                    elif discriminant == 0:
                        root = -b / (2 * a)
                        print(f"There is one real solution (double root): {root}")
                        print(f"The vertex of the parabola represented by the quadratic function is {x}")
                        break

                    else:
                        real_part = -b / (2 * a)
                        imaginary_part = cmath.sqrt(-discriminant) / (2 * a)
                        img_result = self.help_func.handle_large_numbers(imaginary_part)
                        print(f"There are two complex solutions: {real_part} + {img_result.real}i and {real_part} - {img_result.real}i")
                        print(f"The vertex of the parabola represented by the quadratic function is {x}")
                        break

                break

            elif choice == '3':  # Cubic function
                cubic_text = """
Cubic Calculations.
Here you can find all types of cubic function:
    1. General Form
    2. Factor Form
Enter your choice (1 or 2): """

                while True:
                    cubic_choice1 = input(cubic_text).strip()

                    if cubic_choice1 == '1':  # General Form
                        self.help_func.clear_screen()
                        general_form_text = """
This program calculates the solutions of a cubic equation in the form:
    f(x) = ax^3 + bx^2 + cx + d
"""
                        self.help_func.text_helper(general_form_text)

                        def deg3(a, b, c, d, g):  # Newton-Raphson method
                            return a * g**3 + b * g**2 + c * g + d

                        while True:
                            e = self.help_func.get_float_input("Enter the desired error tolerance (e): ")
                            a = self.help_func.get_float_input("Enter coefficient a: ")
                            b = self.help_func.get_float_input("Enter coefficient b: ")
                            c = self.help_func.get_float_input("Enter coefficient c: ")
                            d = self.help_func.get_float_input("Enter constant d: ")
                            self.help_func.clear_screen()

                            count = 1
                            g = 0.01

                            while abs(deg3(a, b, c, d, g)) > e and count <= 100:
                                count += 1
                                g -= deg3(a, b, c, d, g) / (3 * a * g**2 + 2 * b * g + c)

                            if count <= 100:
                                print("Solved. The best guess is:", g)
                            else:
                                print("Maximum iterations exceeded. Current guess:", g)

                            break  # Exit this specific calculation loop
                        break
                    elif cubic_choice1 == '2':  # Factor Form
                        self.help_func.clear_screen()
                        special_forms = """
This program shows solutions of special forms of cubic functions in the factored form.

Formula:
    f(x) = a(x - r1)(x - r2)(x - r3)
"""
                        self.help_func.text_helper(special_forms)

                        while True:
                            a = self.help_func.get_float_input("Enter the factor a: ")
                            r1 = self.help_func.get_float_input("Enter root r1: ")
                            r2 = self.help_func.get_float_input("Enter root r2: ")
                            r3 = self.help_func.get_float_input("Enter root r3: ")

                            self.help_func.clear_screen()

                            A = a
                            B = -a * (r1 + r2 + r3)
                            C = a * (r1 * r2 + r2 * r3 + r3 * r1)
                            D = -a * r1 * r2 * r3

                            coeffs = [A, B, C, D]
                            formatted_coeffs = [f"{coeff:+.2f}" if coeff != int(coeff) else f"{int(coeff):+d}" for coeff in coeffs]

                            terms = []
                            for i, coeff in enumerate(formatted_coeffs):
                                power = len(formatted_coeffs) - i - 1
                                if float(coeff) == 0:
                                    continue
                                elif power == 0:
                                    terms.append(f"{coeff}")
                                elif power == 1:
                                    terms.append(f"{coeff}x")
                                else:
                                    terms.append(f"{coeff}x^{power}")

                            polynomial_string = " ".join(terms).replace("+-", "- ")
                            print(f"Expanded Polynomial: f(x) = {polynomial_string}")
                            
                            break  # Exit this specific calculation loop
                        break
                    else:  # Invalid input handling for cubic choice
                        self.help_func.clear_screen()
                        print("Invalid choice. Please enter (1 or 2).")

            elif choice == '4':  # Back to previous menu
                break

            else:  # Invalid input handling for the main menu
                self.help_func.clear_screen()
                print("Invalid choice. Please enter (1-4).")
            break

    def financial_calculations(self): # No.5
        text = """
Financial Calculations.
Please select a calculation option:
    1. Compound Interest
    2. Simple Interest
    3. Loan Amortization
    4. Future/Present Value of an Investment
    5. Net Present Value
    6. Internal Rate of Return (IRR)
    7. Return on Investment (ROI)
    8. Enhanced Compound Interest Calculator with Monthly Contributions and Inflation Adjustment
    9. Savings Goal Calculator
    10. Effective Annual Rate (EAR)
    11. Go Back
Enter your choice (1-11): """

        while True:
            choice = input(text).strip()
            self.help_func.clear_screen()
            
            if choice == '1': # Compound Interest Formula
                ci_text = """
Compound Interest Formula.
This formula is useful for savings accounts,
investments, or any scenario where money grows over time due to compounded interest.
You'll need to provide the principal amount, the interest rate, the compounding frequency, and the time in years.
"""
                self.help_func.text_helper(ci_text)

                while True: # P
                    P = self.help_func.get_float_input("Enter the Principal (initial amount of money): ")
                    if P <= 0:
                        self.help_func.clear_screen()
                        print("ERROR: The principal must be a positive number.")
                    else:
                        break

                while True: # r
                    annual_rate = self.help_func.get_float_input("Enter the Annual interest rate (as a percentage, e.g., 5 for 5%): ")
                    if annual_rate <= 0:
                        self.help_func.clear_screen()
                        print("ERROR: The interest rate cannot be negative.")
                    else:
                        r = annual_rate / 100  # Convert percentage to decimal
                        break

                while True: # n
                    n = self.help_func.get_int_input("Enter the Number of times that interest is compounded per year: ")
                    if n <= 0:
                        self.help_func.clear_screen()
                        print("ERROR: The compounding frequency must be a positive number.")
                    else:
                        break

                while True: # t
                    t = self.help_func.get_float_input("Enter the Number of years money is invested or borrowed for: ")
                    if t <= 0:
                        self.help_func.clear_screen()
                        print("ERROR: The time in years must be a positive number.")
                    else:
                        break
                self.help_func.clear_screen()

                # Calculate compound interest over time
                years = list(range(1, int(t) + 1))
                amounts = [P * (1 + (r / n)) ** (n * year) for year in years]

                result = P * (1 + (r / n)) ** (n * t)

                print(f"Starting with a principal of ${P:.2f} at an annual interest rate of {r * 100}%,")
                print(f"compounded {n} times per year, the final amount after {t} years is: ${result:.2f}")

                # Plot using Matplotlib
                plt.figure(figsize=(10, 6))
                plt.plot(years, amounts, marker='o', color='b', linestyle='-', linewidth=2, markersize=6)
                plt.title('Compound Interest Growth Over Time')
                plt.xlabel('Years')
                plt.ylabel('Amount ($)')
                plt.grid(True)
                plt.show()
                break

            elif choice == '2': # Simple Interest
                si_text ="""
Simple Interest.
Simple interest is calculated on the initial principal only, and is useful for short-term loans or investments.
"""
                self.help_func.text_helper(si_text)

                while True: # P
                    P = self.help_func.get_float_input("Enter the Principal (initial amount of money): ")
                    if P <= 0:
                        self.help_func.clear_screen()
                        print("ERROR: The principal must be a positive number.")
                    else:
                        break

                while True: # r
                    annual_rate = self.help_func.get_float_input("Enter the Annual interest rate (as a percentage, e.g., 5 for 5%): ")
                    if annual_rate == 0:
                        self.help_func.clear_screen()
                        print("ERROR: The interest rate cannot be negative.")
                    else:
                        r = annual_rate / 100  # Convert percentage to decimal
                        break

                while True: # t
                    t = self.help_func.get_float_input("Enter the Number of years money is invested or borrowed for: ")
                    if t <= 0:
                        self.help_func.clear_screen()
                        print("ERROR: The time in years must be positive number.")
                    else:
                        break
                self.help_func.clear_screen()

                # Calculate simple interest over time
                years = list(range(1, int(t) + 1))
                amounts = [P * (1 + r * year) for year in years]

                result = P * (1 + r * t)

                print(f"Initial investment: {P:.2f}, Annual interest rate: {r*100:.2f}%, for {t} years.")
                print(f"Total amount after {t} years will be: {result:.2f}.")

                # Plot using Matplotlib
                plt.figure(figsize=(10, 6))
                plt.plot(years, amounts, marker='o', color='g', linestyle='-', linewidth=2, markersize=6)
                plt.title('Simple Interest Growth Over Time')
                plt.xlabel('Years')
                plt.ylabel('Amount ($)')
                plt.grid(True)
                plt.show()
                break
            
            elif choice == '3': # Loan Amortization
                la_text = """
Loan Amortization.
This tool helps calculate regular loan payments for mortgages, car loans, or other installment-based loans.
"""
                self.help_func.text_helper(la_text)

                # Get principal amount
                while True:
                    P = self.help_func.get_float_input("Enter the Principal (initial amount of money): ")
                    if P <= 0:
                        self.help_func.clear_screen()
                        print("Error: The principal amount must be a positive number greater than zero.")
                    else:
                        break

                while True: # r
                    annual_rate = self.help_func.get_float_input("Enter the Annual interest rate (as a percentage, e.g., 5 for 5%): ")
                    r = annual_rate / 100  # Convert percentage to decimal
                    if r <= 0:
                        self.help_func.clear_screen()
                        print("Error: The interest rate must be a positive number greater than zero.")
                    else:
                        break

                while True: # n
                    n = self.help_func.get_int_input("Enter the Number of times that interest is compounded per year (e.g., 12 for monthly): ")
                    if n <= 0:
                        self.help_func.clear_screen()
                        print("Error: The compounding frequency must be a positive integer greater than zero.")
                    else:
                        break

                while True: # t
                    t = self.help_func.get_float_input("Enter the Loan term (in years): ")
                    if t <= 0:
                        self.help_func.clear_screen()
                        print("Error: The loan term must be a positive number greater than zero.")
                    else:
                        break

                self.help_func.clear_screen()

                # Calculate the monthly payment
                monthly_rate = r / n
                total_payments = int(n * t)
                monthly_payment = P * (monthly_rate * (1 + monthly_rate) ** total_payments) / ((1 + monthly_rate) ** total_payments - 1)

                # Print the results
                print(f"Monthly payment details:\nPrincipal: ${P:.2f}\nAnnual Rate: {annual_rate:.2f}%\nCompounding: {n} times/year\nLoan Term: {t:.1f} years")
                print(f"Your monthly payment will be: ${monthly_payment:.2f}.")

                # Generate loan balance over time for visualization
                balance = P
                balances = []
                for month in range(1, total_payments + 1):
                    interest = balance * monthly_rate
                    principal_payment = monthly_payment - interest
                    balance -= principal_payment
                    balances.append(balance)

                # Plot the loan balance over time
                plt.figure(figsize=(10, 6))
                plt.plot(range(1, total_payments + 1), balances, marker='o', color='b', linestyle='-', linewidth=2, markersize=3)
                plt.title('Loan Balance Over Time')
                plt.xlabel('Month')
                plt.ylabel('Remaining Balance ($)')
                plt.grid(True)
                plt.show()
                break

            elif choice == '4':  # Future/past Value of an Investment
                text ="""
Future Value:
This is the amount an investment will grow to over a specified period, given a certain interest rate.
It's useful for estimating the worth of savings or investments in the future.

Present Value:
This is the current value of an amount of money that you will receive or invest in the future, discounted at a specific interest rate.
It helps in assessing how much a future amount is worth today."""
                self.help_func.text_helper(text)

                choice_text ="""
Please select the type of Value of an Investment:
    1. Future Value
    2. Present Value
Enter your choice (1 or 2): """

                while True:
                    choice = input(choice_text).strip()
                    self.help_func.clear_screen()
                    if choice == '1': # Future Value
                        
                        fva_text = """
Future Value of an Investment (Annuities).
This calculation determines how much a series of regular, equal payments (or deposits) will grow
over time given a specified interest rate, making it useful for planning savings or understanding
investment growth through compound interest.

The formula depends on whether the payments are made at the beginning or end of each period:
                        
1. Ordinary Annuity (End of Period Payments): 
    P * ((1 + r) ** n - 1) / r

2. Annuity Due (Beginning of Period Payments): 
    P * ((1 + r) ** n - 1) / r * (1 + r)
                    
"""
                        self.help_func.text_helper(fva_text)

                        choice_fva = """
Please select the type of annuity:
    1. Ordinary Annuity (End of Period Payments)
    2. Annuity Due (Beginning of Period Payments)
Enter your choice (1 or 2): """

                        while True:
                            annuity_type = input(choice_fva).strip()
                            self.help_func.clear_screen()

                            if annuity_type not in ['1', '2']:
                                print("Invalid choice for Future Value of an Investment (Annuities). Please enter 1 or 2.")
                                continue

                            # Get payment amount per period (P)
                            while True:
                                P = self.help_func.get_float_input("Enter the payment amount per period: ")
                                if P <= 0:
                                    self.help_func.clear_screen()
                                    print("Error: The payment amount per period must be a positive number.")
                                else:
                                    break

                            # Get interest rate per period (r)
                            while True:
                                annual_rate = self.help_func.get_float_input("Enter the interest rate per period (as a percentage, e.g., 5 for 5%): ")
                                if annual_rate <= 0:
                                    self.help_func.clear_screen()
                                    print("Error: The interest rate per period must be a positive number.")
                                else:
                                    r = annual_rate / 100  # Convert percentage to decimal
                                    break

                            # Get total number of periods (n)
                            while True:
                                n = self.help_func.get_int_input("Enter the total number of periods: ")
                                if n <= 0:
                                    self.help_func.clear_screen()
                                    print("Error: The total number of periods must be a positive number.")
                                else:
                                    break

                            self.help_func.clear_screen()

                            if annuity_type == '1':  # Ordinary Annuity
                                result = npf.fv(r, n, -P, 0)  # Future Value of Ordinary Annuity
                                annuity_name = "Ordinary Annuity"
                            else:  # Annuity Due
                                result = npf.fv(r, n, -P, 0) * (1 + r)  # Future Value of Annuity Due
                                annuity_name = "Annuity Due"

                            # Display the result
                            print(f"The {annuity_name} with a payment amount of ${P:.2f},")
                            print(f"an interest rate of {annual_rate:.2f}%, over {n:.0f} periods, is ${result:.2f}.")

                            # Graph the Future Value over periods (Optional Visualization)
                            periods = list(range(1, n + 1))
                            future_values = [npf.fv(r, period, -P, 0) if annuity_type == '1' else npf.fv(r, period, -P, 0) * (1 + r) for period in periods]
                            
                            plt.plot(periods, future_values, label='Future Value')
                            plt.title(f'{annuity_name} over Time')
                            plt.xlabel('Periods')
                            plt.ylabel('Future Value ($)')
                            plt.legend()
                            plt.grid(True)
                            plt.show()
                            break
                        break
                    
                    elif choice == '2': # Present Value
                        PV_text ="""
Present Value (PV) calculation.
represents the current worth of a future sum of money, discounted at a specific interest rate. 
It helps determine how much a future amount is worth today, taking into account the time value of money.
"""
                        self.help_func.text_helper(PV_text)
                        # Get Future Value (the amount of money in the future) (FV)
                        while True:
                            FV = self.help_func.get_float_input("Enter future value (the amount of money in the future): ")
                            if FV <= 0:
                                self.help_func.clear_screen()
                                print("Error: Future value (the amount of money in the future) must be a positive number.")
                            else:
                                break

                        # Get interest rate per period (r)
                        while True:
                            annual_rate = self.help_func.get_float_input("Enter the discount rate (or interest rate per period) (as a percentage, e.g., 5 for 5%): ")
                            if annual_rate <= 0:
                                self.help_func.clear_screen()
                                print("Error: The interest rate per period must be a positive number.")
                            else:
                                r = annual_rate / 100  # Convert percentage to decimal
                                break

                        # Get total number of periods (t)
                        while True:
                            t = self.help_func.get_float_input("Enter Number of periods (years, months, etc.): ")
                            if t <= 0:
                                self.help_func.clear_screen()
                                print("Error: The total number of periods must be a positive number.")
                            else:
                                break   
                        self.help_func.clear_screen()

                        # Calculate Present Value using numpy_financial
                        result = npf.pv(r, t, 0, FV)  # PV = FV / (1 + r)^t
                        
                        print(f"To achieve a future value of ${FV:.2f} in {t} periods, with an interest rate of {annual_rate:.2f}%")
                        print(f"the present value needed today is: ${result:.2f}")

                        # Create a graph to visualize the present value for varying interest rates or periods

                        # Create a range of interest rates (for graphing)
                        interest_rates = np.linspace(0, 0.2, 100)  # Interest rates from 0% to 20%
                        
                        # Calculate present value for each interest rate
                        pv_values = npf.pv(interest_rates, t, 0, FV)

                        # Plotting the graph
                        plt.figure(figsize=(8, 6))
                        plt.plot(interest_rates * 100, pv_values, label=f"Future Value = ${FV:.2f}", color='b', linestyle='-', marker='o')
                        plt.title('Present Value vs Interest Rate')
                        plt.xlabel('Interest Rate (%)')
                        plt.ylabel('Present Value ($)')
                        plt.grid(True)
                        plt.legend()
                        plt.show()
                        break
                    
                     
                    else: # wrong input
                        self.help_func.clear_screen()
                        print("Invalid choice for the type of Value of an Investment. Please enter (1 or 2).")
                break
            
            elif choice == '5':  # Net Present Value (NPV)
                npv_text = """
Net Present Value calculation.
Calculate the present value of a series of future cash flows, considering a specific discount rate.
You need to gather all the expected cash flows for each time period, the discount rate, and how many periods you're analyzing.
""" 
                self.help_func.text_helper(npv_text)

                # Get total number of periods (n)
                while True:
                    n = self.help_func.get_int_input("Enter the total number of periods: ")
                    if n <= 0:
                        self.help_func.clear_screen()
                        print("Error: The total number of periods must be a positive number.")
                    else:
                        break

                # Get Cash Flows (CF)
                cash_flows = []  # Initialize an empty list to store cash flows
                for i in range(n + 1):  # Including Year 0
                    while True:
                        cash_flow = self.help_func.get_float_input(f"Enter the cash inflow (or outflow) for Year {i}: ")
                        cash_flows.append(cash_flow)
                        break

                # Get Discount Rate (r)
                while True:
                    annual_rate = self.help_func.get_float_input("Enter the discount rate (as a percentage, e.g., 5 for 5%): ")
                    if annual_rate <= 0:
                        self.help_func.clear_screen()
                        print("Error: The discount rate must be a positive number.")
                    else:
                        r = annual_rate / 100  # Convert percentage to decimal
                        break

                self.help_func.clear_screen()

                # Calculate NPV and prepare the graph data
                npv_sum = 0
                npv_values = []  # To store cumulative NPV values for each year
                years = list(range(n + 1))  # X-axis: years (should have n + 1 elements)

                for i in range(n + 1):  # For each year, from 0 to n
                    CF = cash_flows[i]  # Get the cash flow for year i
                    npv_sum += CF / (1 + r) ** i  # Apply the NPV formula
                    npv_values.append(npv_sum)  # Append the cumulative NPV value

                # Output the results
                self.help_func.clear_screen()
                print(f"Discount Rate (r): {r * 100}%")
                print(f"Number of Periods (n): {n}")
                print("Cash Flows (CF):")
                for i in range(n + 1):
                    print(f"  Year {i}: {cash_flows[i]}")
                print(f"\nNet Present Value (NPV): ${npv_sum:.2f}")

                # Plot the graph
                plt.plot(years, npv_values, color='green', marker='o')
                plt.title("NPV vs. Year")
                plt.xlabel("Year")
                plt.ylabel("Cumulative NPV ($)")
                plt.grid(True)
                plt.show()
                break

            elif choice == '6': # Internal Rate of Return (IRR)
                irr_text = """
Internal Rate of Return (IRR) calculation.
This method calculates the rate of return at which the net present value (NPV) of all cash flows equals zero.
You will need to gather the initial investment and all expected future cash flows for each period.
        """
                self.help_func.text_helper(irr_text)

                # Get the total number of periods (n)
                while True:
                    n = int(self.help_func.get_int_input("Enter the total number of periods: "))
                    if n <= 0:
                        self.help_func.clear_screen()
                        print("Error: The total number of periods must be a positive number.")
                    else:
                        break

                # Get Cash Flows (CF)
                cash_flows = []  # Initialize an empty list to store cash flows
                for i in range(n + 1):  # Including Year 0 (initial investment)
                    while True:
                        cash_flow = self.help_func.get_float_input(f"Enter the cash inflow (or outflow) for Year {i}: ")
                        # For Year 0, check if it's negative (initial investment)
                        if i == 0 and cash_flow >= 0:
                            self.help_func.clear_screen()
                            print("ERROR: The initial investment (Year 0) should be negative.")
                        # For future years, check if it's positive (cash inflows)
                        elif i > 0 and cash_flow < 0:
                            self.help_func.clear_screen()
                            print("ERROR: Future years should have positive cash inflows.")
                        else:
                            cash_flows.append(cash_flow)
                            break  # Exit the loop and proceed to the next year
                self.help_func.clear_screen()

                # Calculate IRR using numpy_financial's irr function
                irr = npf.irr(cash_flows)

                # Output the results
                self.help_func.clear_screen()
                print(f"Cash Flows (CF):")
                for i in range(n + 1):
                    print(f"  Year {i}: {cash_flows[i]}")

                if irr is None or irr != irr:  # Check if IRR is NaN
                    print("\nError: Could not calculate IRR. Check if the cash flows are correct.")
                else:
                    print(f"\nInternal Rate of Return (IRR): {irr * 100:.2f}%")
                    
                    # Plot the graph of cumulative cash flows over the years
                    cumulative_cash_flows = [sum(cash_flows[:i+1]) for i in range(len(cash_flows))]  # Cumulative cash flows

                    # Plot the cumulative cash flows
                    plt.plot(range(n + 1), cumulative_cash_flows, color='blue', marker='o', label='Cumulative Cash Flow')

                    # Highlight the IRR point where the cumulative cash flow is closest to zero
                    plt.axhline(0, color='red', linestyle='--', label="IRR (0 crossing)")
                    plt.scatter([n], [cumulative_cash_flows[-1]], color='green', label=f"IRR = {irr * 100:.2f}%")

                    # Adding titles and labels
                    plt.title("Cumulative Cash Flow and IRR")
                    plt.xlabel("Year")
                    plt.ylabel("Cumulative Cash Flow ($)")
                    plt.legend()
                    plt.grid(True)
                    plt.show()
                    break
                
            elif choice == '7': # Return on Investment (ROI)
                roi_text ="""
Return on Investment (ROI) Calculation.
Assess the profitability of an investment by comparing the final value to the initial investment.
Input the amount you invested initially and the value of the investment after a certain period to calculate the return percentage.
"""
                self.help_func.text_helper(roi_text)

                choice_text ="""
Return on Investment (ROI) Calculator
Evaluate the profitability of your investment by comparing its initial value to its final value over a chosen period. 

Choose your Return on Investment (ROI) type:
    1. Single-period ROI Calculate the return for a single investment period.
    2. Annualized ROI Calculate the annualized return, useful for comparing investments of varying durations.
Enter your choice (1 or 2): """

                while True:
                    choice = input(choice_text).strip()
                    self.help_func.clear_screen()

                    if choice in ['1', '2']:

                        # Get Gain from Investment (GFI)
                        while True:
                            GFI = self.help_func.get_float_input("Enter the total amount you gained or earned from the investment: ")
                            if GFI <= 0:
                                self.help_func.clear_screen()
                                print("Error: The total amount you gained or earned must be a positive number.")
                            else:
                                break

                        # Get Initial Investment (II)
                        while True:
                            II = self.help_func.get_float_input("Enter the original amount you invested: ")
                            if II <= 0:
                                self.help_func.clear_screen()
                                print("Error: The original amount you invested must be a positive number.")
                            else:
                                break

                        if choice == '1':  # Basic ROI Calculation
                            result = ((GFI - II) / II) * 100
                            self.help_func.clear_screen()
                            print(f"Basic ROI Calculation:")
                            print(f"  Gain from Investment: {GFI}")
                            print(f"  Initial Investment: {II}")
                            print(f"  ROI: {result:.2f}%")

                            # Plot the Basic ROI Calculation as a bar chart
                            plt.figure(figsize=(6, 4))
                            categories = ['Initial Investment', 'Gain from Investment']
                            values = [II, GFI]
                            plt.bar(categories, values, color=['blue', 'green'])
                            plt.title('Basic ROI Calculation')
                            plt.ylabel('Amount')
                            plt.show()
                            break
                        elif choice == '2':  # Compounded ROI Calculation
                            while True:
                                n = self.help_func.get_int_input("Enter the time period, in years, over which the investment was held: ")
                                if n <= 0:
                                    self.help_func.clear_screen()
                                    print("Error: The time period, in years, must be a positive number.")
                                else:
                                    break

                            compounded_roi = (((GFI / II) ** (1 / n)) - 1) * 100
                            self.help_func.clear_screen()
                            print(f"Compounded ROI Calculation:")
                            print(f"  Gain from Investment: {GFI}")
                            print(f"  Initial Investment: {II}")
                            print(f"  Time Period: {n} years")
                            print(f"  Compounded ROI: {compounded_roi:.2f}%")

                            # Plot the Compounded ROI Calculation over time
                            years = list(range(1, n + 1))
                            roi_values = [(((GFI / II) ** (1 / year)) - 1) * 100 for year in years]

                            plt.figure(figsize=(6, 4))
                            plt.plot(years, roi_values, marker='o', color='purple')
                            plt.title('Compounded ROI Over Time')
                            plt.xlabel('Years')
                            plt.ylabel('Compounded ROI (%)')
                            plt.grid(True)
                            plt.show()
                            break
                        else:
                            self.help_func.clear_screen()
                            print("Invalid choice for Return on Investment (ROI) type. Please enter 1 or 2.")

                    else:
                        self.help_func.clear_screen()
                        print("Invalid choice for Return on Investment (ROI) Calculation. Please enter 1 or 2.")
                break
            
            elif choice == '8': # Advanced Compound Interest with Monthly Contributions with or without inflation
                text_choice ="""
Advanced Compound Interest Calculator
This program helps you calculate the future value of an investment, factoring in compound interest, monthly contributions, and the option to consider inflation.

Choose your calculation mode:
    1. With Inflation Calculate with inflation-adjusted values for a realistic future estimate.
    2. Without Inflation Calculate based solely on compound interest for a straightforward projection.
Enter your choice (1 or 2): """
                
                while True:
                    choise = input(text_choice).strip()
                    self.help_func.clear_screen()

                    if choise == '1':
                        text = """
This program calculates the future value of an investment considering both compound interest and monthly contributions.
"""
                        self.help_func.text_helper(text)

                        while True:  # P
                            P = self.help_func.get_float_input("Enter the Principal (initial amount of money): ")
                            if P <= 0:
                                self.help_func.clear_screen()
                                print("ERROR: The principal must be a positive number.")
                            else:
                                break

                        while True:  # r
                            annual_rate = self.help_func.get_float_input("Enter the Annual interest rate (as a percentage, e.g., 5 for 5%): ")
                            if annual_rate <= 0:
                                self.help_func.clear_screen()
                                print("ERROR: The interest rate cannot be negative.")
                            else:
                                r = annual_rate / 100  # Convert percentage to decimal
                                break

                        while True:  # n
                            n = self.help_func.get_int_input("Enter the number of times interest is compounded per year: ")
                            if n <= 0:
                                self.help_func.clear_screen()
                                print("ERROR: The number of times interest is compounded per year must be greater than 0.")
                            elif n > 365:
                                self.help_func.clear_screen()
                                print("ERROR: The number of times interest is compounded per year cannot be greater than 365.")
                            else:
                                break

                        while True:  # t
                            t = self.help_func.get_int_input("Enter how long the money is invested (in years): ")
                            if t <= 0:
                                self.help_func.clear_screen()
                                print("ERROR: The time investment must be a positive number.")
                            else:
                                break

                        while True:  # PMT
                            PMT = self.help_func.get_float_input("Enter the amount you add each month: ")
                            if PMT <= 0:
                                self.help_func.clear_screen()
                                print("ERROR: The amount you add each month must be a positive number.")
                            else:
                                break
                        self.help_func.clear_screen()

                        A_principal = P * (1 + r/n)**(n * t)
                        A_contributions = PMT * ((1 + r/n)**(n * t) - 1) / (r/n)

                        result = A_principal + A_contributions

                        # After collecting all inputs and result
                        print(f"Inputs:")
                        print(f"  Initial Principal (P): ${P:.2f}")
                        print(f"  Annual Interest Rate (r): {r*100:.2f}%")
                        print(f"  Compounding Frequency (n): {n} times per year")
                        print(f"  Time (t): {t} year{'s' if t > 1 else ''}")
                        print(f"  Monthly Contribution (PMT): ${PMT:.2f}")
                        print(f"\nThe total amount after {t} year{'s' if t > 1 else ''} is: ${result:.2f}")

                        # Create graph
                        years = [i for i in range(1, t + 1)]
                        future_values = []

                        for year in years:
                            A_principal = P * (1 + r/n)**(n * year)
                            A_contributions = PMT * ((1 + r/n)**(n * year) - 1) / (r/n)
                            future_values.append(A_principal + A_contributions)

                        # Plot the graph
                        plt.plot(years, future_values, label="Future Value", color='blue')
                        plt.xlabel("Years")
                        plt.ylabel("Future Value ($)")
                        plt.title("Investment Growth Over Time")
                        plt.grid(True)
                        plt.legend()
                        plt.show()
                        break

                    elif choise == '2':
                        text = """
This program calculates the future value of an investment considering both interest and inflation.
"""
                        self.help_func.text_helper(text)

                        while True:  # P
                            P = self.help_func.get_float_input("Enter the Principal (initial amount of money): ")
                            if P <= 0:
                                self.help_func.clear_screen()
                                print("ERROR: The principal must be a positive number.")
                            else:
                                break

                        while True:  # r
                            annual_rate = self.help_func.get_float_input("Enter the Annual interest rate (as a percentage, e.g., 5 for 5%): ")
                            if annual_rate <= 0:
                                self.help_func.clear_screen()
                                print("ERROR: The interest rate cannot be negative.")
                            else:
                                r = annual_rate / 100  # Convert percentage to decimal
                                break

                        while True:  # i
                            inflation_rate = self.help_func.get_float_input("Enter the annual inflation rate (as a percentage, e.g., 5 for 5%): ")
                            if inflation_rate <= 0:
                                self.help_func.clear_screen()
                                print("ERROR: The annual inflation rate cannot be negative.")
                            else:
                                i = inflation_rate / 100  # Convert percentage to decimal
                                break

                        while True:  # n
                            n = self.help_func.get_int_input("Enter the number of times interest is compounded per year: ")
                            if n <= 0:
                                self.help_func.clear_screen()
                                print("ERROR: The number of times interest is compounded per year must be greater than 0.")
                            elif n > 365:
                                self.help_func.clear_screen()
                                print("ERROR: The number of times interest is compounded per year cannot be greater than 365.")
                            else:
                                break

                        while True:  # t
                            t = self.help_func.get_float_input("Enter how long the money is invested (in years): ")
                            if t <= 0:
                                self.help_func.clear_screen()
                                print("ERROR: The time investment must be a positive number.")
                            else:
                                break

                        while True:  # PMT
                            PMT = self.help_func.get_float_input("Enter the amount you add each month: ")
                            if PMT <= 0:
                                self.help_func.clear_screen()
                                print("ERROR: The amount you add each month must be a positive number.")
                            else:
                                break
                        self.help_func.clear_screen() 

                        A_principal = P * (1 + (r - i)/n)**(n * t)
                        A_contributions = PMT * ((1 + (r - i)/n)**(n * t) - 1) / ((r - i)/n)

                        result = A_principal + A_contributions

                        # After collecting all inputs and result
                        print(f"Inputs:")
                        print(f"  Initial Principal (P): ${P:.2f}")
                        print(f"  Annual Interest Rate (r): {annual_rate:.2f}%")
                        print(f"  Annual Inflation Rate (i): {inflation_rate:.2f}%")
                        print(f"  Compounding Frequency (n): {n} times per year")
                        print(f"  Time (t): {t} year{'s' if t > 1 else ''}")
                        print(f"  Monthly Contribution (PMT): ${PMT:.2f}")
                        print(f"\nThe total amount after {t} year{'s' if t > 1 else ''} is: ${result:.2f}")

                        # Create graph
                        years = [i for i in range(1, int(t) + 1)]
                        future_values = []

                        for year in years:
                            A_principal = P * (1 + (r - i)/n)**(n * year)
                            A_contributions = PMT * ((1 + (r - i)/n)**(n * year) - 1) / ((r - i)/n)
                            future_values.append(A_principal + A_contributions)

                        # Plot the graph
                        plt.plot(years, future_values, label="Future Value (Inflation Adjusted)", color='green')
                        plt.xlabel("Years")
                        plt.ylabel("Future Value ($)")
                        plt.title("Investment Growth Over Time (With Inflation Adjustment)")
                        plt.grid(True)
                        plt.legend()
                        plt.show()
                        break

                    else:
                        self.help_func.clear_screen() 
                        print("Invalid choice Advanced Compound Interest calculation. Please enter 1 or 2.")
                break

            elif choice == '9': # Savings Goal Calculator
                text ="""
Saving Goal Calculation.
Calculates the time (in years) needed to reach a savings goal (FV) with regular monthly contributions (PMT),
an annual interest rate, and a compounding frequency.
"""
                self.help_func.text_helper(text)

                while True:  # FV (Future Value)
                    FV = self.help_func.get_float_input("Enter your future savings goal: ")
                    if FV <= 0:
                        self.help_func.clear_screen()
                        print("ERROR: The future savings goal must be a positive number.")
                    else:
                        break

                while True:  # PMT (Monthly Contribution)
                    PMT = self.help_func.get_float_input("Enter the amount you will contribute each month: ")
                    if PMT <= 0:
                        self.help_func.clear_screen()
                        print("ERROR: The monthly contribution amount must be a positive number.")
                    else:
                        break

                while True:  # r (Interest Rate per Period)
                    annual_rate = self.help_func.get_float_input("Enter the interest rate per period (as a percentage, e.g., enter 5 for 5%): ")
                    if annual_rate <= 0:
                        self.help_func.clear_screen()
                        print("ERROR: The interest rate must be a positive number.")
                    else:
                        r = annual_rate / 100  # Convert percentage to a decimal
                        break

                while True:  # n (Compounding Frequency per Year)
                    n = self.help_func.get_int_input("Enter the number of times interest is compounded per year: ")
                    if n <= 0:
                        self.help_func.clear_screen()
                        print("ERROR: The compounding frequency must be a positive number.")
                    elif n > 365:
                        self.help_func.clear_screen()
                        print("ERROR: The compounding frequency cannot be greater than 365.")
                    else:
                        break

                # Get the time period for the graph
                while True:
                    t= self.help_func.get_float_input("Enter the maximum time period (in years) for the graph: ")
                    if t <= 0:
                        self.help_func.clear_screen()
                        print("ERROR: The time period must be a positive number.")
                    else:
                        break
                    
                self.help_func.clear_screen()

                # Calculate the time required to reach the future savings goal
                part_one = (FV * r) / (PMT * (1 + r))
                finish_one = math.log(part_one)
                part_two = n * math.log(1 + r)
                result = finish_one / part_two

                # Print the results first
                print("Calculation Result:")
                print(f"  Future Savings Goal (FV): {FV}")
                print(f"  Monthly Contribution (PMT): {PMT}")
                print(f"  Interest Rate per Period (r): {annual_rate}%")
                print(f"  Compounding Frequency (n): {n} times per year")
                print(f"  Time required to reach the savings goal: {result:.2f} years")
                break

            elif choice == '10': # Effective Annual Rate (EAR)
                text = """
Effective Annual Rate (EAR) Calculation
The Effective Annual Rate (EAR) accounts for compounding periods within the year, providing an accurate
measure of annual return or cost. This helps in comparing financial products with different compounding intervals.
"""
                self.help_func.text_helper(text)

                while True: # r
                    annual_rate = self.help_func.get_float_input("Enter the Nominal Annual Interest Rate (as a percentage, e.g., 5 for 5%): ")
                    if annual_rate == 0:
                        self.help_func.clear_screen()
                        print("ERROR: The Nominal Annual Interest Rate must be negative.")
                    else:
                        r = annual_rate / 100  # Convert percentage to decimal
                        break

                while True: # n
                    n = self.help_func.get_int_input("Enter the Number of Compounding Periods per Year: ")
                    if n <= 0:
                        self.help_func.clear_screen()
                        print("Error: The Number of Compounding Periods must be a positive integer greater than zero.")
                    else:
                        break
                    
                while True:  # Maximum years for graph
                    max_years = self.help_func.get_int_input("Enter the number of years to display on the graph: ")
                    if max_years <= 0:
                        self.help_func.clear_screen()
                        print("ERROR: The number of years must be a positive integer.")
                    else:
                        break

                self.help_func.clear_screen()

                # Calculate EAR over the user-specified number of years
                years = list(range(1, max_years + 1))
                EAR_values = []

                for year in years:                        
                    result = (1 + (r / n)) ** (n * year) - 1  # EAR formula considering compounding over each year
                    EAR_values.append(result)

                print("Inputs:")
                print(f"- Nominal Annual Interest Rate (r): {annual_rate:.2f}%")
                print(f"- Compounding Periods per Year (n): {n}")
                print(f"- Displayed Years: {max_years}")
                print("\nResult:")
                print(f"- Effective Annual Rate (EAR) at year {max_years}: {result:.4%}")

                # Plot the graph
                plt.plot(years, EAR_values, label="Effective Annual Rate (EAR)", color='blue')
                plt.xlabel("Years")
                plt.ylabel("Annual Rate")
                plt.title("Effective Annual Rate Over Time")
                plt.grid(True)
                plt.legend()
                plt.show()
                break

            elif choice == '11': # back
                break

            else: # wrong input
                self.help_func.clear_screen()
                print("Invalid choice for Financial Calculations. Please enter (1-10).")
            
            # NOTE: please add more of financial calculations
            # NOTE: graph at formula number 9 is not working

    def age_calculation(self): # No.6
        choice_text ="""
Welcome to the Age Calculator!
    1. birthdate Calculation
    2. Age Comparison
    3. Go back
Enter your choice (1-3): """

        while True:
            choice = input(choice_text).strip()
            self.help_func.clear_screen()
            if choice == '1': # birthdate Calculation
        
                text = """
birthdate Calculation.

To use this function:
- Please enter your birthdate in the format YYYY-MM-DD (e.g., 2000-05-15).
- Ensure the date is valid and follows the correct format to avoid errors.
- Once entered, the program will calculate and display:
- Your age in years, months, and days.
- Days remaining until your next birthday.
- A special message if today is your birthday.

Note: Invalid formats will prompt you to re-enter the date.
"""
                self.help_func.text_helper(text)

                while True:
                    try:         
                        # Input birthdate from the user
                        birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
                        year, month, day = map(int, birthdate_str.split('-'))
                        birthdate = date(year, month, day)
                        today = date.today()
                        self.help_func.clear_screen()

                        # Calculate age in years
                        age_years = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

                        # Calculate age in months
                        if today.month < birthdate.month or (today.month == birthdate.month and today.day < birthdate.day):
                            age_months = (12 - birthdate.month) + today.month - 1
                        else:
                            age_months = today.month - birthdate.month

                        # Calculate age in days
                        if today.day < birthdate.day:
                            month_ago = (today.month - 1) if today.month > 1 else 12
                            days_in_month = (date(today.year, today.month, 1) - date(today.year, month_ago, 1)).days
                            age_days = days_in_month - (birthdate.day - today.day)
                        else:
                            age_days = today.day - birthdate.day

                        # Output the age
                        print(f"You are {age_years} years, {age_months} months, and {age_days} days old.")

                        if today.month == birthdate.month and today.day == birthdate.day:
                            print("Congratulations! Happy Birthday!")

                        # Calculate the next birthday
                        next_birthday_year = today.year if (today.month, today.day) < (birthdate.month, birthdate.day) else today.year + 1
                        next_birthday = date(next_birthday_year, birthdate.month, birthdate.day)
                        days_until_birthday = (next_birthday - today).days

                        print(f"Your next birthday is in {days_until_birthday} days on {next_birthday}.")
                        break

                    except ValueError:
                        print("Invalid date format. Please enter your birthdate in YYYY-MM-DD format.")
                    except Exception as e:
                        print(f"An error occurred: {e}. Please try again.")
                break

            elif choice == '2': # Age Comparison
                text ="""
Age Comparison calculation.

Please enter two birthdates in the format YYYY-MM-DD.
- The first birthdate is the one you want to compare.
- The second birthdate is the one you want to compare it with.

For example, if you enter:
    - First birthdate: 2000-05-20
    - Second birthdate: 1998-12-15

The program will tell you who is older and by how many years, months, and days.
"""
                self.help_func.text_helper(text)
                
                while True:
                    try:
                        # Input and validate the first birthdate
                        while True: 
                            birthdate_str1 = input("Enter the first birthdate (YYYY-MM-DD): ")
                            try: 
                                year1, month1, day1 = map(int, birthdate_str1.split('-'))
                                birthdate1 = date(year1, month1, day1)
                                self.help_func.clear_screen()
                                break  # Exit the loop if the date is valid
                            except ValueError:
                                self.help_func.clear_screen()
                                print("Invalid date format. Please enter the date in YYYY-MM-DD format.")

                        # Input and validate the second birthdate
                        while True: 
                            birthdate_str2 = input("Enter the second birthdate (YYYY-MM-DD): ")
                            try:
                                year2, month2, day2 = map(int, birthdate_str2.split('-'))
                                birthdate2 = date(year2, month2, day2)
                                self.help_func.clear_screen()
                                break  # Exit the loop if the date is valid
                            except ValueError:
                                self.help_func.clear_screen()
                                print("Invalid date format. Please enter the date in YYYY-MM-DD format.")

                    except Exception as e:
                        print(f"An error occurred: {e}. Please try again.")
                        continue

                    # Determine which date is older
                    if birthdate1 > birthdate2:
                        birthdate1, birthdate2 = birthdate2, birthdate1
                        older = "younger"
                    else:
                        older = "older"

                    # Calculate the difference in years, months, and days
                    delta_years = birthdate2.year - birthdate1.year
                    delta_months = birthdate2.month - birthdate1.month
                    delta_days = birthdate2.day - birthdate1.day

                    if delta_days < 0:
                        delta_days += (date(birthdate2.year, birthdate2.month, 1) - date(birthdate2.year, birthdate2.month - 1, 1)).days
                        delta_months -= 1

                    if delta_months < 0:
                        delta_months += 12
                        delta_years -= 1

                    # Display the result with the comparison
                    print(f"The first birthdate is {older} than the second birthdate by {delta_years} years, {delta_months} months, and {delta_days} days.")
                    break
                break

            elif choice == '3': # go back
                break

            else: # wrong input
                self.help_func.clear_screen()
                print("Invalid choice. Please enter (1-3)")

    def pythagorean_formula(self): # No.7
        text = """
Pythagorean Equation.
Here we can find c is the length of the hypotenuse (the side opposite the right angle)
Or the a and b are the lengths of the two legs of the right triangle
    1. Find c
    2. Find a and b
    3. Back
Enter your choice (1, 2 or 3): """
        while True:
            choice = input(text).strip()
            if choice == '1':
                self.help_func.clear_screen()  # Ensure this function is defined
                a = self.help_func.get_float_input("Enter the first leg of the triangle: ")
                b = self.help_func.get_float_input("Enter the second leg of the triangle: ")
                c = cmath.sqrt((a ** 2) + (b ** 2))
                result = self.help_func.handle_large_numbers(c)
                self.help_func.clear_screen()
                print(f"The length of the hypotenuse with the first leg of {a} and the second leg of {b} is {result}")
                break

            elif choice == '2':
                self.help_func.clear_screen()
                leg = self.help_func.get_float_input("Enter the known leg of the triangle: ")
                c = self.help_func.get_float_input("Enter the hypotenuse of the triangle: ")
                missing_leg = cmath.sqrt((c ** 2) - (leg ** 2))
                result = self.help_func.handle_large_numbers(missing_leg)
                self.help_func.clear_screen()
                print(f"The length of the missing leg with the known leg of {leg} and the hypotenuse of {c} is {result}")
                break
            elif choice == '3':
                break
                
            else:
                self.help_func.clear_screen()
                print("Invalid choice. Please enter (1-3)")

    def distance_formula(self): # No.8
        text ="""
Distance Formula.
This formula calculates the distance between two points (x'1,y'1) and (x'2,y'2) on a 2D plane.

input "back" to come back to the main menu.
"""
# Menus Class
        self.help_func.text_helper(text)


        x_1 = self.help_func.get_float_input("Enter x from the first point: ")
        y_1 = self.help_func.get_float_input("Enter y from the first point: ")
        self.help_func.clear_screen()
        x_2 = self.help_func.get_float_input("Enter x from the second point: ")
        y_2 = self.help_func.get_float_input("Enter y from the second point: ")
        self.help_func.clear_screen()
        equation_d = cmath.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)
        reslut = self.help_func.handle_large_numbers(equation_d)

        print(f"The distance between ({x_1}, {y_1}) and ({x_2}, {y_2}) is {reslut}")

    def exponential_growth_decay_formula(self): # No.9
        text = """
Exponential Growth/Decay Formula

The formula is: N = N0 * e^(kt)

Example:
- You invest $500 in an account with a continuous growth rate of 3% per year. 
How much will the investment be worth after 10 years?

Given Values:
- Initial amount (N0) = $500
- Growth rate (k) = 0.03 (3% per year, converted to decimal)
- Time (t) = 10 years

Result:
After 10 years, an investment of $500 at a 3% percentage growth rate will be worth approximately $674.95.
"""

        self.help_func.text_helper(text)

        N0 = self.help_func.get_float_input("Enter the initial amount (N0): ")
        k = self.help_func.get_float_input("Enter the growth/decay rate (k): ")
        t = self.help_func.get_float_input("Enter the time (t): ")
        self.help_func.clear_screen()

        N = N0 * math.exp(k * t)
        print(f"For an initial amount of {N0} with a growth rate of {k * 100:.2f} percent over {t} *any time curency*, the final amount is approximately {N:.2f}.")

    def the_law_of_cosines(self): # No.10
        text ="""
Law of Cosines for Triangle Calculation

The Law of Cosines is a fundamental formula in geometry that relates the lengths of the sides of a triangle to the cosine of one of its angles.
This formula is especially useful for calculating unknown side lengths or angles when certain information about the triangle is known.

Formula:
For a triangle with sides a, b, and c, and angles A, B, and C opposite those sides, the Law of Cosines states:
    
c^2 = a^2 + b^2 - 2ab * cos(C)

Applications:
1. **Finding Unknown Sides**: If two sides and the included angle are known, you can calculate the third side using the formula.
2. **Finding Unknown Angles**: If all three sides are known, the formula can be rearranged to find any angle:
    cos(C) = (a^2 + b^2 - c^2) / (2ab)

This law is applicable in various fields such as geometry, physics, engineering, and computer graphics, making it a vital tool for shape calculations, especially in triangular configurations.
"""
        self.help_func.text_helper(text)

        choice_text ="""
Law of Cosines for Triangle Calculation
    1. Finding Unknown Sides
    2. Finding Unknown Angles
    3. Go Back
Enter your choice (1-3): """

        while True:
            choice = input(choice_text).strip()
            self.help_func.clear_screen()
            if choice == '1': # Finding Unknown Sides
                a = self.help_func.get_float_input("Enter the length of one known side: ")
                b = self.help_func.get_float_input("Enter the length of second known side: ")
                c = self.help_func.get_float_input("Enter the angle between sides a and b: ")
                self.help_func.clear_screen()

                # Convert angle from degrees to radians for the calculation
                c_rad = math.radians(c)
                c2 = (a ** 2) + (b ** 2) - (2 * a * b) * math.cos(c_rad)

                # Only take the square root of c2 if it's non-negative
                if c2 < 0:
                    print("The calculation resulted in a negative value, indicating an error in the input values.")
                    break

                result = math.sqrt(c2)
                print(f"The unknown side for side one with {a} and side two with {b} and angle with {c}° is approximately {result:.2f}")
                break
            elif choice == '2': # Finding Unknown Angles
                a = self.help_func.get_float_input("Enter the length of one known side: ")
                b = self.help_func.get_float_input("Enter the length of second known side: ")
                c = self.help_func.get_float_input("Enter the length of third known side: ")
                self.help_func.clear_screen()

                cosc = ((a ** 2) + (b ** 2) - (c ** 2)) / (2 * a * b)

                # Check if cosc is within the valid range
                if cosc < -1 or cosc > 1:
                    print("Invalid input values: The cosine value is out of range.")
                    break
                
                angle_rad = math.acos(cosc)  # Calculate the angle in radians
                result = math.degrees(angle_rad)  # Convert radians to degrees
                print(f"The unknown angle for the first side with {a}, second side with {b}, and third side with {c} is approximately {result:.2f}°")
                break
            elif choice == '3': # back
                break
            else:
                self.help_func.clear_screen()
                print("Invalid choice for Law of Cosines for Triangle Calculation. Please enter (1-3).")

    def riemann_zeta_function(self): # No.11
        text = """
        Riemann Zeta Function.
        To calculate the Riemann Zeta Function, you will need to input s (must be > 1) and n (number of terms).
        """
        self.help_func.text_helper(text)

        # Loop to get a valid value for s
        while True:
            s = self.help_func.get_float_input("Enter a value for s where s > 1: ")
            if s > 1:
                break
            self.help_func.clear_screen()
            print("Error: s must be more than 1. Please try again.")

            self.help_func.clear_screen()

        # Loop to get a valid positive integer for n
        while True:
            n = self.help_func.get_int_input("Enter the number of terms (positive integer): ")
            if n > 0:
                break 
            self.help_func.clear_screen()
            print("Error: The number of terms must be a positive integer. Please try again.")

        self.help_func.clear_screen()

        # Calculate the Riemann Zeta sum
        zeta_sum = 0
        for i in range(1, n + 1):
            zeta_sum += 1 / (i ** s)

        print(f"The Riemann Zeta for s = {s} with {n} terms is approximately {zeta_sum:.5f}.")

    def newtons_law_of_universal_gravitation(self): # No.12
        G = 6.67430e-11  # Gravitational constant in m^3 kg^-1 s^-2 

        text = """
    Newton's Law of Universal Gravitation states that every particle in the universe attracts every other particle with a force 
    that is directly proportional to the product of their masses and inversely proportional to the square of the distance between them.

    There are two ways to calculate this formula:

    First way:
        Calculate the gravitational force using the formula:
            F = G * (m1 * m2) / r^2
        What you need to input:
            - mass for the first object
            - mass for the second object
            - the distance between the two objects

    Second way:
        Calculate the gravitational force using the formula:
            unknown_m = (F * r^2) / (G * known_m^2)
        What you need to input:
            - the result of the calculation
            - second or first mass of the objects
            - the distance between the two objects
    """

        self.help_func.text_helper(text)

        choice_text = """
    Newton's Law of Universal Gravitation.
        1. First way
        2. Second way
        3. Go Back
    Enter your choice (1, 2, or 3): """

        while True:
            choice = input(choice_text).strip()
            self.help_func.clear_screen()

            if choice == '1':
                
                m1 = self.help_func.get_float_input("Enter the mass of the first object (kg): ")
                m2 = self.help_func.get_float_input("Enter the mass of the second object (kg): ")
                while True:
                    r = self.help_func.get_float_input("Enter the distance between the two objects (m): ")
                    if r <= 0:  # Check for less than or equal to zero
                        self.help_func.clear_screen()
                        print("Distance must be greater than zero.")
                    else:
                        break
                self.help_func.clear_screen()

                # Calculate the gravitational force using the formula F = G * (m1 * m2) / r^2
                result = self.help_func.formatted_result101(G * (m1 * m2) / (r ** 2))

                print(f"The gravitational force between masses {m1:.1f} kg and {m2:.1f} kg separated by {r:.1f} m is approximately {result}.")
                break

            elif choice == '2':

                F = self.help_func.get_float_input("Enter the gravitational force (F) in Newtons (N): ")
                known_m = self.help_func.get_float_input("Enter the mass of the known object (kg): ")
                while True:
                    r = self.help_func.get_float_input("Enter the distance between the two objects (m): ")
                    if r <= 0:  # Check for less than or equal to zero
                        self.help_func.clear_screen()
                        print("Distance must be greater than zero.")
                    else:
                        break
                self.help_func.clear_screen()

                result = (F * r ** 2) / (G * known_m)

                print(f"The unknown mass between known mass of {known_m:.1f} kg and gravitational force of {F:.1f} N at a distance of {r:.1f} m is approximately {result:.2e} kg.")
                break

            elif choice == '3':
                break

            else:
                self.help_func.clear_screen()
                print("Invalid choice for  Newton's Law of Universal Gravitation. Please enter (1-3).")
    
    # add more functions here
