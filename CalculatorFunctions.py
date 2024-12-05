import math
import cmath
from sympy import sympify, sqrt, log, sin, cos, tan, exp, I, Number, SympifyError # need to intsall first
from sympy.physics.units import kg, m, G
import numpy as np 
import numpy_financial as npf # need to intsall first
import matplotlib.pyplot as plt # need to intsall first
from datetime import date
import requests # need to intsall first
from HelpFunctions import HelpFunctions

class CalculatorFunctions:

    def __init__(self):
        self.help_func = HelpFunctions()

    def simple_calculation(self):  # No.1
        variables = {}  # Dictionary to store variables
        history = []  # List to store history of calculations

        while True:
            try:
                expression = input("Enter a calculation (type 'help' for instructions or 'back' to return to the main menu): ").strip()

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
                                    
8. Back to menu:
    Type 'back' to simple calculation function in the calculator.
"""
                    self.help_func.text_helper(help_text)



                # Check for quit command
                if expression.lower() == "back":
                    self.help_func.clear_screen()
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
                    break

            except SympifyError:
                self.help_func.clear_screen()
                print("Error: Please enter a valid mathematical expression.")
            except ValueError:
                self.help_func.clear_screen()
                print("Error: Invalid input. Please enter a numerical expression.")

    def shape_calculations(self): # No.2
        text = """
Shape Calculations:

1. Circle Calculation       9. Octagon Calculation
2. Cone Calculation         10. Pentagon Calculation
3. Cylinder Calculation     11. Polygon Calculation
4. Ellipse and Ellipsoid    12. Rectangle Calculation
5. Hexagon Calculation      13. Square Calculation
6. Hyperboloid Calculation  14. Tetrahedron Calculation
7. Kite Calculation         15. Triangle Calculation
8. Lune Calculation         16. Go Back

Enter your choice (1-16): """

        while True:
            choice = input(text).strip()
            self.help_func.clear_screen()
            if choice not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']:
                print("Invalid choice for shape calculations. Please enter (1-16)")
                continue

            if choice == '1': # Circle
                while True:
                    circle_text = """
Circle Calculation.
You can enter any circle calculation:
    1. Circle Circumference (units)
    2. Circle Area (units²)
    3. Calculate Both Area and Perimeter
Enter your choice (1, 2 or 3): """

                    choice = input(circle_text).strip()
                    self.help_func.clear_screen()
                    if choice not in ['1', '2', '3']:
                        print("Invalid choice for circle calculation. Please enter (1-3).")
                        continue
                    
                    radius = self.help_func.get_float_input("Enter the radius of the circle: ", True)

                    circumference = 2 * math.pi * radius
                    area = math.pi * (radius ** 2)

                    if choice in ['1', '3']:
                        print(f"The circumference of the circle with the radius of {radius} is {circumference:.2f} units")

                    if choice in ['2', '3']:
                        print(f"The area of the circle with the radius of {radius} is {area:.2f} units²")
                    break

            elif choice == '2': # Cylinder
                while True:
                    cylinder_text = """
Cylinder Calculation.
You can enter any cylinder calculation:
    1. Circumference of The Cylinder Base (units)
    2. Total Perimeter (Unfolded) (units)
    3. Cylinder Surface Area (units²)
    4. Cylinder Volume (units³)
    5. All Calculations
Enter your choice (1-5): """
                    cylinder_choice = input(cylinder_text).strip()
                    self.help_func.clear_screen()

                    if cylinder_choice in ['1', '2', '3', '4', '5']:
                        # Get the common inputs for radius and height
                        r = self.help_func.get_float_input("Enter the radius of the cylinder: ")
                        h = self.help_func.get_float_input("Enter the height of the cylinder: ") if cylinder_choice in ['2', '3', '4', '5'] else None

                        # Calculation functions
                        calculations = {
                            '1': lambda: f"Circumference: {2 * math.pi * r:.2f} units",
                            '2': lambda: f"Perimeter: {(2 * math.pi * r) + (2 * h):.2f} units",
                            '3': lambda: f"Surface Area: {2 * math.pi * r * (r + h):.2f} units²",
                            '4': lambda: f"Volume: {math.pi * r ** 2 * h:.2f} units³",
                            '5': lambda: (
                                f"Circumference: {2 * math.pi * r:.2f} units\n"
                                f"Perimeter: {(2 * math.pi * r) + (2 * h):.2f} units\n"
                                f"Surface Area: {2 * math.pi * r * (r + h):.2f} units²\n"
                                f"Volume: {math.pi * r ** 2 * h:.2f} units³"
                            )
                        }

                        # Handle choice
                        if cylinder_choice in calculations:
                            self.help_func.clear_screen()
                            print(calculations[cylinder_choice]())
                            break
                    else:
                        self.help_func.clear_screen()
                        print("Invalid choice for cylinder calculation. Please enter (1-5).")

            elif choice == '3': # Cone
                cone_text = """
Cone Calculation.
You can enter any cone calculation:
    1. Cone Volume (units³)
    2. Cone Surface Area (units²)
    3. Calculate Both Volume and Surface Area
Enter your choice (1-3): """
                while True:
                    choice = input(cone_text).strip()
                    self.help_func.clear_screen()
                    if choice not in ['1', '2', '3']:
                        print("Invalid choice for Cone calculation. Please enter (1-3)")
                        continue

                    if choice in ['2', '3']:
                        l_text = """
Slant Height Calculation.
    1. Enter the slant height (l)
    2. Calculate slant height (l) from radius and height
Enter your choice (1-2): """
                        while True:
                            l_choice = input(l_text).strip() 
                            self.help_func.clear_screen()
                            if l_choice not in ['1', '2']:
                                print("Invalid choice for slant height calculation. Please enter (1-2)")
                                continue
                            break

                    r = self.help_func.get_float_input("Enter the radius of the cone: ")
                    h = self.help_func.get_float_input("Enter the height of the cone: ")

                    if choice in ['2', '3'] and l_choice == '1':
                        l = self.help_func.get_float_input("Enter the slant height of the cone: ")
                    
                    self.help_func.clear_screen()

                    volume = (1/3) * (math.pi * (r ** 2)) * h
                    
                    if l_choice == '1':
                        surface_area = (math.pi * r) * (r + l)
                    else:
                        uknown_l = math.sqrt((r ** 2) + (h ** 2))  
                        surface_area = (math.pi * r) * (r + uknown_l)

                    print("Inputs:")
                    print(f"The radius (r): {r}")
                    print(f"The height (h): {h}")
                    if choice in ['2', '3'] and l_choice == '1':
                        print(f"The slant height (l): {l}")
                    else:
                        print(f"The unknown slant height is {uknown_l}\n")
                    print("Result:")
                    if choice in ['1', '3']:
                        print(f"The volume of the cone is {volume:.2f} units³.")

                    if choice in ['2', '3']:
                        print(f"The surface area of the cone is {surface_area:.2f} units².")
                    break

            elif choice == '4': # Ellipse and Ellipsoid
                main_choice_text = """
Ellipse and Ellipsoid Calculations:
    1. Ellipse (2D: Area, Circumference)
    2. Ellipsoid (3D: Volume, Surface Area)
Enter your choice (1-2): """
    
                while True:
                    main_choice = input(main_choice_text).strip()
                    self.help_func.clear_screen()
                    if choice not in ['1', '2']:
                        print("Invalid choice. Please enter (1-2).")
                        continue

                    if main_choice == '1':  # Ellipse
                        ellipse_text = """
Ellipse Calculation:
You can enter any ellipse calculation:
    1. Ellipse Area (units²)
    2. Ellipse Circumference (units)
    3. Calculate Both Area and Circumference
Enter your choice (1-3): """
            
                        while True:
                            sub_choice = input(ellipse_text).strip()
                            self.help_func.clear_screen()
                            if sub_choice not in ['1', '2', '3']:
                                print("Invalid choice for ellipse calculation. Please enter (1-3).")
                                continue

                            a = self.help_func.get_float_input("Enter a: Semi-major axis (a): ")
                            b = self.help_func.get_float_input("Enter b: Semi-minor axis (b): ", True)

                            area = math.pi * a * b
                            circumference = math.pi * ((3 * (a + b)) - math.sqrt(((3 * a) + b) * (a + (3 * b))))

                            print("Inputs:")
                            print(f"  Semi-major axis (a): {a}")
                            print(f"  Semi-minor axis (b): {b}\n")
                            print("Result:\n")

                            if sub_choice in ['1', '3']:
                                print(f"The area of the ellipse is {area:.2f} units².")

                            if sub_choice in ['2', '3']:
                                print(f"The circumference of the ellipse is {circumference:.2f} units.")
                            break

                    elif main_choice == '2':  # Ellipsoid
                        p = 1.6075
                        ellipsoid_text = """
Ellipsoid Calculation:
To calculate the volume and surface area of an ellipsoid:
    1. Ellipsoid Volume (units³)
    2. Ellipsoid Surface Area (units²)
    3. Calculate Both Volume and Surface Area
Enter your choice (1-3): """

                        while True:
                            sub_choice = input(ellipsoid_text).strip()
                            self.help_func.clear_screen()
                            if sub_choice not in ['1', '2', '3']:
                                print("Invalid choice for ellipsoid calculation. Please enter (1-3).")
                                continue

                            a = self.help_func.get_float_input("Enter a: Semi-major axis (longest axis): ")
                            b = self.help_func.get_float_input("Enter b: Semi-intermediate axis (middle axis): ")
                            c = self.help_func.get_float_input("Enter c: Semi-minor axis (shortest axis): ", True)

                            volume = (4/3) * math.pi * a * b * c
                            surface_area = 4 * math.pi * (((a ** p) * (b ** p) + (a ** p) * (c ** p) + (b ** p) * (c ** p)) / 3) ** (1/p)

                            if sub_choice == '1':
                                print(f"Ellipsoid Volume: {volume:.2f} units³")
                            elif sub_choice == '2':
                                print(f"Ellipsoid Surface Area: {surface_area:.2f} units²")
                            elif sub_choice == '3':
                                print("Ellipsoid Calculations (Volume and Surface Area):")
                                print(f"  Volume: {volume:.2f} units³")
                                print(f"  Surface Area: {surface_area:.2f} units²")
                            break
                    break
            
            elif choice == '5': # Hexagon
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
                    if hexagon_choice not in ['1', '2', '3']:
                        print("Invalid choice for hexagon calculation. Please enter (1-3)")
                        continue

                    s = self.help_func.get_float_input("Enter the length of a side: ", True)

                    discriminant = 2 / (3 * cmath.sqrt(3))
                    area = discriminant * s ** 2
                    perimeter = 6 * s
                    
                    if hexagon_choice in ['1', '3']:
                        print(f"The area for the hexagon with the length of a side of {s} is {area:.2f} units².")

                    elif hexagon_choice in ['2', '3']:
                        print(f"The perimeter the for the hexagon with the length of a side of {s} is {perimeter:.2f} units.")
                    break

            elif choice == '6': # Hyperboloid
                choice_text ="""
Hyperboloid Calculation.
You can enter any hyperboloid calculation:
    1. Hyperboloid Volume (units³)
    2. Hyperboloid Surface Area (units²)
    3. Calculate Both Volume and Surface Area
Enter your choice (1-3): """
                while True:
                    choice = input(choice_text).strip()
                    self.help_func.clear_screen()
                    if choice not in ['1', '2', '3']:
                        print("Invalid choice for hyperboloid calculations. Please enter (1-3)")
                        continue

                    a1 = self.help_func.get_float_input("Enter the bottom radius: ")
                    a2 = self.help_func.get_float_input("Enter the top radius: ")
                    a = self.help_func.get_float_input("Enter the base radius: ")
                    h = self.help_func.get_float_input("Enter the height: ",  True)

                    volume = (1/3) * math.pi * h * (a1**2 + a1 * a2 + a2**2)
                    surface_area = 2 * math.pi * a**2 * ((h / a) + math.log((h + math.sqrt(h**2 + a**2)) / a))

                    print("Inputs:")
                    print(f"Bottom radius (a₁): {a1}")
                    print(f"Top radius (a₂): {a2}")
                    print(f"Height (h): {h}")
                    print(f"Base radius (a): {a}\n")
                    print("Result:")
                    
                    if choice in ['1', '2']:
                        print(f"Volume of the hyperboloid is {volume:.2f} units³.")

                    if choice in ['2', '3']:
                        print(f"Surface Area of the hyperboloid is {surface_area:.2f} units².")
                    break

            elif choice == '7': # Kite
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
                    if kite_choice not in ['1', '2', '3']:
                        print("Invalid choice for kite calculation. Please enter (1-3).")
                        continue

                    if kite_choice in ['1', '3']:
                        d1 = self.help_func.get_float_input("Enter the length of the first diagonal (d1): ")
                        d2 = self.help_func.get_float_input("Enter the length of the second diagonal (d2): ", True)

                    if kite_choice in ['2', '3']:
                        a = self.help_func.get_float_input("Enter the length of one pair of equal sides (a): ")
                        b = self.help_func.get_float_input("Enter the length of the other pair of equal sides (b): ", True)

                    area = 0.5 * d1 * d2
                    perimeter = 2 * (a + b)

                    if kite_choice in ['1', '3']:
                        print(f"The area of the kite with diagonals {d1} and {d2} is {area:.2f} units².")
                    
                    if kite_choice in ['2', '3']:
                        print(f"The perimeter of the kite with sides {a} and {b} is {perimeter:.2f} units.")
                    break

            elif choice == '8': # Lune
                choice_text ="""
Choose the lune calculation method:
    1. Angle-based: Calculates based on the angles of the sectors.
    2. Crescent-based: Calculates the area difference between two circles.
    3. Distance-based: Calculates based on the distance between circle centers and their radius.
    4. Inverse-base: (Given area and distance, find radii)
Enter your choice (1-4): """
                while True:
                    choice = input(choice_text).strip()
                    self.help_func.clear_screen()
                    if choice not in ['1', '2', '3', '4']: # invalid input
                        print("Invalid choice for lune calculations. Please enter (1-4)")
                        continue

                    if choice in ['1', '2']: # Angle and Crescent-based
                        if choice == '1':  # Angle-based
                            lune_text = """
Angle-based lune calculation.
Provide the radius of the larger circle, the smaller circle, 
and the central angles of the circular segments (in radians) for each circle.
"""
                        elif choice == '2':  # Crescent-based
                            lune_text = """
Crescent-based lune calculation.
Calculate the area of the lune by subtracting the area of the smaller circle 
from the larger circle. Ideal for non-overlapping circles.
"""
                        self.help_func.text_helper(lune_text)

                        R = self.help_func.get_float_input("Enter the radius of the larger circle: ")
                        r = self.help_func.get_float_input("Enter the radius of the smaller circle: ", True)

                        if choice == '1':  # Angle-based calculation
                            angle1 = self.help_func.get_float_input("Enter the central angle for the larger circle (in radians): ")
                            angle2 = self.help_func.get_float_input("Enter the central angle for the smaller circle (in radians): ", True)

                            area = (R ** 2) * (angle1 - math.sin(angle1)) - (r ** 2) * (angle2 - math.sin(angle2))

                            print(f"The area of the lune with radii {R} and {r}, and central angles {angle1:.2f} and {angle2:.2f} radians,")
                            print(f"is approximately {area:.2f} units².")
                        else:  # Crescent-based calculation
                            area = (math.pi * (R ** 2)) - (math.pi * (r ** 2))

                            print(f"The area of the lune with radii {R} and {r} is approximately {area:.2f} units².")
                        break

                    elif choice in ['3', '4']:  # Distance and Inverse-based
                        if choice == '3':
                            lune_text = """
                    Distance-based lune calculation.
                    Calculate the area of the lune using the radii of the circles and the distance between their centers.
                    """
                        elif choice == '4':
                            lune_text = """
                    Inverse-based lune calculation.
                    Calculate the radii of the circles using the area of the lune and the distance between their centers.
                    """

                        self.help_func.text_helper(lune_text)

                        while True:
                            if choice == '3':
                                R = self.help_func.get_float_input("Enter the radius of the first circle:")
                                r = self.help_func.get_float_input("Enter the radius of the second circle:")
                            elif choice == '4':
                                A = self.help_func.get_float_input("Enter the area of the lune")
                            d = self.help_func.get_float_input("Enter the distance between the centers of the circles")

                            if choice == '3':
                                if not (abs(R - r) <= d <= R + r):
                                    print("Error: Invalid distance. Ensure |R - r| <= d <= R + r for intersecting circles.")
                                    continue

                                if not (-1 <= d / (2 * R) <= 1) or not (-1 <= d / (2 * r) <= 1):
                                    print("Error: Invalid argument for acos. Ensure d / (2 * R) and d / (2 * r) are in the range [-1, 1].")
                                    continue

                                expr = (-d + R + r) * (d + r - R) * (d - R + r) * (d + R + r)
                                if expr < 0:
                                    print("Error: Negative value inside the square root. Check your inputs.")
                                    continue

                                ang1 = (R ** 2) * math.acos(d / (2 * R))
                                ang2 = (r ** 2) * math.acos(d / (2 * r))
                                area = ang1 + ang2 - 0.5 * math.sqrt(expr)

                                print("Inputs:")
                                print(f"Distance between centers: {d}")
                                print(f"Radii: {R}, {r}")
                                print("Result:")
                                print(f"The calculated lune area is approximately {area:.2f} units².")

                            elif choice == '4':
                                if (2 * A) < d**2:
                                    print("Error: Invalid values. Ensure the area is large enough for the given distance.")
                                    continue

                                r1_expr = (A + d**2) / (2 * d)
                                r2_expr = (A - d**2) / (2 * d)

                                if r1_expr <= 0 or r2_expr <= 0:
                                    print("Error: Calculated radii are invalid. Ensure the inputs satisfy the lune conditions.")
                                    continue

                                r1 = math.sqrt(r1_expr)
                                r2 = math.sqrt(r2_expr)

                                print("Inputs:")
                                print(f"Distance between centers: {d}")
                                print(f"The area of the lune: {A}")
                                print("Result:")
                                print(f"Calculated radii are approximately:")
                                print(f"Radius 1: {r1:.2f} units")
                                print(f"Radius 2: {r2:.2f} units")
                            break

            elif choice == '9': # Octagon
                octagon_text = """
Octagon Calculation.
You can enter any octagon calculation:
    1. Octagon Area (units²)
    2. Octagon Perimeter (units)
    3. Calculate Both Area and Perimeter
Enter your choice (1-3):  """
                while True:
                    octagon_choice = input(octagon_text).strip()
                    self.help_func.clear_screen()
                    if octagon_choice not in ['1', '2', '3']:
                        print("Invalid choice for Octagon calculation. Please enter (1-3).")
                        continue

                    side = self.help_func.get_float_input("Enter the length of a side of the Octagon: ", True)

                    area = 2 * (1 + math.sqrt(2)) * (side ** 2)
                    perimeter = 8 * side
                    
                    if octagon_choice in ['1', '3']:
                        print(f"The area of the Octagon with side length {side} is {area:.2f} units²")
                    
                    if octagon_choice in ['2', '3']:
                        print(f"The perimeter of the Octagon with side length {side} is {perimeter:.2f} units")
                    break

            elif choice == '10': # Pentagon
                while True:
                    pentagon_text ="""
Pentagon Calculation.
You can enter any pentagon calculation:
    1. Pentagon Area (units²)
    2. Pentagon Perimeter (units)
    3. Calculate Both Area and Perimeter
Enter your choice (1-3): """   
                    pentagon_choice = input(pentagon_text).strip()
                    self.help_func.clear_screen()
                    if choice not in ['1', '2', '3']:
                        print("Invalid choice for pentagon calculation. Please enter (1-3)")
                        continue

                    s = self.help_func.get_float_input("Enter the length of a side: ", True)

                    discriminant =  5 * (5 + 2 * math.sqrt(5))
                    area = (1/4) * math.sqrt(discriminant) * s**2
                    perimeter = 5 * s

                    if pentagon_choice in ['1', '3']:
                        print(f"The area for the pentagon with the length of a side of {s} is {area:.2f} units².")

                    if pentagon_choice in ['2', '3']:
                        print(f"The perimeter for the pentagon with the length of a side of {s} is {perimeter:.2f} units.")
                    break  

            elif choice == '11': # Polygon
                while True:
                    polygon_text = """
Polygon Calculation.
Choose a calculation option:
    1. Polygon Area (units²)
    2. Polygon Perimeter (units)
    3. Calculate Both Area and Perimeter
Enter your choice (1-3): """
                    polygon_choice = input(polygon_text).strip()
                    self.help_func.clear_screen()
                    if polygon_choice not in ['1', '2', '3']:
                        print("Invalid choice for polygon calculation. Please enter (1-3)")
                        continue
                    # Input for number of sides
                    n = self.help_func.get_input_with_condition(
                        "Enter the number of sides (integer ≥ 3): ", 'int', 
                        lambda x: x >= 3, "The number of sides must be an integer ≥ 3."
                    )

                    # Input for side length
                    s = self.help_func.get_input_with_condition(
                        "Enter the length of a side (greater than 0): ", 'float', 
                        lambda x: x > 0, "The length of a side must be greater than 0."
                    )

                    self.help_func.clear_screen()

                    area = (1 / 4) * n * (s ** 2) * (1 / math.tan(math.pi / n))
                    perimeter = n * s

                    print(f"For the polygon with {n} sides, each of length {s} units:")

                    if polygon_choice in ['1', '3']:
                        print(f" - Area: {area:.2f} units²")

                    if polygon_choice in ['2', '3']:
                        print(f" - Perimeter: {perimeter:.2f} units")
                    break

            elif choice == '12': # Rectangle
                Rectangle_text = """
Rectangle Calculation.
You can enter any rectangle calculation:
    1. Rectangle Area (units²)
    2. Rectangle Perimeter (units)
    3. Calculate Both Area and Perimeter
Enter your choice (1-3): """
                while True:
                    choice = input(Rectangle_text).strip()
                    self.help_func.clear_screen()
                    if choice not in ['1', '2', '3']:
                        print("Invalid choice for rectangle calculation. Please enter (1-3).")
                        continue

                    length = self.help_func.get_float_input("Enter the length of the rectangle: ")
                    width = self.help_func.get_float_input("Enter the width of the rectangle: ", True)

                    area = length * width
                    perimeter = 2 * (length + width)

                    if choice in ['1', '3']:
                        print(f"The area of the rectangle with length {length} and width {width} is {area:.2f} units²")

                    if choice in ['2', '3']:
                        print(f"The perimeter of the rectangle with length {length} and width {width} is {perimeter:.2f} units")
                    break

            elif choice == '13': # Square
                while True:
                    squar_text = """
Square Calculation.
You can enter any square calculation:
    1. Square Area (units²)
    2. Square Perimeter (units)
    3. Calculate Both Area and Perimeter
Enter your choice (1-3): """
                    square_choice = input(squar_text).strip()
                    self.help_func.clear_screen()
                    if choice not in ['1', '2', '3']:
                        print("Invalid choice for square calculation. Please enter (1-3).")
                        continue

                    side = self.help_func.get_float_input("Enter the length of a side of the square: ", True)

                    area = side ** 2
                    perimeter = 4 * side

                    if square_choice in ['1', '3']:
                        print(f"The area of the square with side length {side} is {area:.2f} units²")

                    if square_choice in ['2', '3']:
                        print(f"The perimeter of the square with side length {side} is {perimeter:.2f} units")
                    break

            elif choice == '14': # Tetrahedron
                Tetrahedron_text = """
Tetrahedron Calculation.
You can enter any Tetrahedron calculation:
    1. Tetrahedron Volume (units³)
    2. Tetrahedron Surface Area (units²)
    3. Calculate Both Volume and Surface Area
Enter your choice (1-3): """
                while True:
                    calc_choice = input(Tetrahedron_text).strip()
                    self.help_func.clear_screen()
                    if calc_choice not in ['1', '2', '3']:
                        print("Invalid choice for tetrahedron calculation. Please enter (1-3).")
                        continue
                    
                    a = self.help_func.get_float_input("Enter the edge length: ", True)

                    volume = (math.sqrt(2) / 12) * (a ** 3)
                    surface_area = math.sqrt(3) * (a ** 2)

                    print(f"Inputs:\nEdge length (a): {a:.2f}\n")
                    print("Result:")

                    if calc_choice in ['1', '3']:
                        print(f"Tetrahedron Volume: {volume:.2f} units³")
                    if calc_choice in ['2', '3']:
                        print(f"Tetrahedron Surface Area: {surface_area:.2f} units²")
                    break

            elif choice == '15': # Triangle
                while True:
                    triangle_text = """
which shape of triangle you want to calculate:
    1. Normal Triangle
    2. Equilateral Triangle
Enter your choice (1 or 2): """
                    triangle_choice = input(triangle_text).strip()
                    self.help_func.clear_screen()
                    if triangle_choice not in ['1', '2']:
                        print("Invalid choice for triangle calculation. Please enter (1-2)")   
                        continue
                    
                    if triangle_choice == '1': # Normal Triangle
                        triangle_text = """
Normal Triangle Calculation.
You can enter any triangle calculation:
    1. Triangle Area (units²)
    2. Triangle Perimeter (units)
    3. Calculate Both Area and Perimeter
Enter your choice (1, 2 or 3): """
                        
                        while True:
                            triangle_choice = input(triangle_text).strip()
                            self.help_func.clear_screen()
                            if triangle_choice not in ['1', '2', '3']:
                                print("Invalid choice for triangle calculation. Please enter (1-3)")
                                continue

                            area = 0.5 * base * height
                            perimeter = side1 + side2 + side3
                        
                            if triangle_choice in ['1', '3']:
                                base = self.help_func.get_float_input("Enter the base of the triangle: ")
                                height = self.help_func.get_float_input("Enter the height of the triangle: ", True)

                            if triangle_choice in ['2', '3']:
                                side1 = self.help_func.get_float_input("Enter the length of the first side of the triangle: ")
                                side2 = self.help_func.get_float_input("Enter the length of the second side of the triangle: ")
                                side3 = self.help_func.get_float_input("Enter the length of the third side of the triangle: ", True)

                            if triangle_choice in ['1','3']:
                                print(f"The area of the triangle with base {base} and height {height} is {area:.2f} units².")
                                
                            if triangle_choice in ['2', '3']:
                                print(f"The perimeter of the triangle with sides {side1}, {side2}, and {side3} is {perimeter:.2f} units.")
                            break
                        break
                    
                    elif triangle_choice == '2': # Equilateral Triangle
                        Eq_triangle_text = """
Equilateral Triangle Calculation.
You can enter any equilateral triangle calculation:
    1. Equilateral Triangle Area (units²)
    2. Equilateral Triangle Perimeter (units)
    3. Calculate Both Area and Perimeter
Enter your choice (1-3):  """

                        while True:
                            Eq_triangle_choice = input(Eq_triangle_text).strip()
                            self.help_func.clear_screen()
                            if Eq_triangle_choice not in ['1', '2', '3']:
                                print("Invalid choice for equilateral triangle calculation. Please enter (1-3)")
                                continue

                            s = self.help_func.get_float_input("Enter any side: ")
                            self.help_func.clear_screen()

                            area = (math.sqrt(3) / 4) * (s ** 2)
                            perimeter = 3 * s

                            if Eq_triangle_choice in ['1', '3']:
                                print(f"The area for the equilateral triangle with the sides of {s} is {area:.2f} units².")
                        
                            if Eq_triangle_choice in ['2', '3']:
                                print(f"The perimeter for the equilateral triangle with the sides of {s} is {perimeter:.2f} units.")
                            break
                        break     

            elif choice == '16': # back
                break
            break

    def quadratic_calculations(self):  # No.3
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
            if choice not in ['1', '2', '3', '4']:
                print("Invalid choice for quadratic calculation. Please enter (1-4)")
                continue

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
                x_2 = self.help_func.get_float_input("Enter the second number: ", True)
                x = list(range(int(x_1), int(x_2) + 1))

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
                    c = self.help_func.get_float_input("Enter the constant c: ", True)

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
                    self.help_func.clear_screen()
                    if choice not in ['1', '2']:
                        print("Invalid choice. Please enter (1 or 2).")
                        continue

                    if cubic_choice1 == '1':  # General Form
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
                            d = self.help_func.get_float_input("Enter constant d: ", True)

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
                            r3 = self.help_func.get_float_input("Enter root r3: ", True)

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

            elif choice == '4':  # Back
                break
            break

    def financial_calculations(self): # No.4
        text = """
Financial Calculations.
Please select a calculation option:
    1. Percentage Calculator
    2. Compound Percentage with Adjustment Calculation
    3. Compound Interest
    4. Simple Interest
    5. Loan Amortization
    6. Future/Present Value of an Investment
    7. Net Present Value
    8. Internal Rate of Return (IRR)
    9. Return on Investment (ROI)
   10. Enhanced Compound Interest Calculator with Monthly Contributions and Inflation Adjustment
   11. Savings Goal Calculator
   12. Effective Annual Rate (EAR)
   13. Go Back
Enter your choice (1-13): """

        while True:
            choice = input(text).strip()
            self.help_func.clear_screen()
            if choice not in ['1', '2', '3', '4', '5', '6', '7', '8', '8', '9', '10', '11', '12', '13']:
                print("Invalid choice for Financial Calculations. Please enter (1-13)")
                continue

            if choice == '1': # Percentage Calculator
                num1 = self.help_func.get_float_input("Enter the number you want to know the percentage of: ")
                num2 = self.help_func.get_float_input("Enter the total number: ")
                self.help_func.clear_screen()
                result = (num1 / num2) * 100
                print(f"The percentage of {num1} from {num2} is {result:.2f}%.")
                
            elif choice == '2': # Compound Percentage with Adjustment Calculation
                text ="""
Compound Percentage with Adjustment Calculation
This formula calculates the adjusted percentage after a series of growth or decay periods, considering a constant adjustment value.
Its used for scenarios like financial projections, population growth, or decay processes.
"""
                self.help_func.text_helper(text)

                # Input collection
                p_base = self.help_func.get_float_input("Enter the initial percentage or base value: ")

                R = self.help_func.get_input_with_condition(
                    "Enter the Growth or Decay rate (as a percentage, e.g., 5 for 5%): ", 'float',
                    lambda x: x >= 0, "ERROR: The growth/decay rate cannot be negative."
                )
                r = R / 100

                n = self.help_func.get_input_with_condition(
                    "Enter the number of periods (iterations): ", 'float',
                    lambda x: x > 0, "ERROR: The number of periods must be greater than zero."
                    )

                c = self.help_func.get_input_with_condition(
                    "Enter the constant adjustment value: ", 'float',
                    lambda x: x != 0, "ERROR: The constant adjustment value cannot be zero."
                )
                
                self.help_func.clear_screen()     
                p_adjustment = (p_base * (1 +  (r ** n))) + c
                p_adjustment2 = (p_base * (1 +  (r ** n))) - c

                print("\nResults:")
                print(f"Adjusted percentage (adding adjustment): {p_adjustment:.2f}")
                print(f"Adjusted percentage (subtracting adjustment): {p_adjustment2:.2f}")

            elif choice == '3': # Compound Interest Formula
                ci_text = """
Compound Interest Formula.
This formula is useful for savings accounts,
investments, or any scenario where money grows over time due to compounded interest.
You'll need to provide the principal amount, the interest rate, the compounding frequency, and the time in years.
"""
                self.help_func.text_helper(ci_text)


                P = self.help_func.get_input_with_condition(
                    "Enter the Principal (initial amount of money): ", 'float',
                    lambda x: x >= 0, "ERROR: The principal must be a positive number."
                )

                annual_rate = self.help_func.get_input_with_condition(
                    "Enter the Annual interest rate (as a percentage, e.g., 5 for 5%): ", 'float',
                    lambda x: x >= 0, "ERROR: The interest rate cannot be negative."
                )
                r = annual_rate / 100  # Convert percentage to decimal

                n = self.help_func.get_input_with_condition(
                    "Enter the Number of times that interest is compounded per year: ", 'float'
                )
                while True: # n
                    n = self.help_func.get_int_input("Enter the Number of times that interest is compounded per year: ")
                    if n <= 0:
                        self.help_func.clear_screen()
                        print("ERROR: The compounding frequency must be a positive number.")
                    else:
                        break

                t = self.help_func.get_input_with_condition(
                    "Enter the Number of years money is invested or borrowed for: ", 'float',
                    lambda x: x >= 0, "ERROR: The time in years must be positive number."
                )
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

            elif choice == '4': # Simple Interest
                si_text ="""
Simple Interest.
Simple interest is calculated on the initial principal only, and is useful for short-term loans or investments.
"""
                self.help_func.text_helper(si_text)

                P = self.help_func.get_input_with_condition(
                    "Enter the Principal (initial amount of money): ", 'float',
                    lambda x: x >= 0, "ERROR: The principal must be a positive number."
                )

                annual_rate = self.help_func.get_input_with_condition(
                    "Enter the Annual interest rate (as a percentage, e.g., 5 for 5%): ", 'float',
                    lambda x: x >= 0, "ERROR: The interest rate cannot be negative."
                )
                r = annual_rate / 100  # Convert percentage to decimal

                t = self.help_func.get_input_with_condition(
                    "Enter the Number of years money is invested or borrowed for: ", 'float',
                    lambda x: x >= 0, "ERROR: The time in years must be positive number."
                )
                
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
            
            elif choice == '5': # Loan Amortization
                la_text = """
Loan Amortization.
This tool helps calculate regular loan payments for mortgages, car loans, or other installment-based loans.
"""
                self.help_func.text_helper(la_text)

                # Get principal amount
                P = self.help_func.get_input_with_condition(
                    "Enter the Principal (initial amount of money): ", 'float',
                    lambda x: x >= 0, "Error: The principal amount must be a positive number greater than zero."
                )

                annual_rate = self.help_func.get_input_with_condition(
                    "Enter the Annual interest rate (as a percentage, e.g., 5 for 5%): ", 'float',
                    lambda x: x >= 0, "Error: The interest rate must be a positive number greater than zero."
                )
                r = annual_rate / 100  # Convert percentage to decimal

                n = self.help_func.get_input_with_condition(
                    "Enter the Number of times that interest is compounded per year (e.g., 12 for monthly): ", 'int',
                    lambda x: x >= 0, "Error: The compounding frequency must be a positive integer greater than zero."
                )

                t = self.help_func.get_input_with_condition(
                    "Enter the Loan term (in years): ", 'float',
                    lambda x: x >= 0, "Error: The loan term must be a positive number greater than zero."
                )

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

            elif choice == '6':  # Future/past Value of an Investment
                text ="""
Future Value:
This is the amount an investment will grow to over a specified period, given a certain interest rate.
It's useful for estimating the worth of savings or investments in the future.

Present Value:
This is the current value of an amount of money that you will receive or invest in the future, discounted at a specific interest rate.
It helps in assessing how much a future amount is worth today.
"""
                choice_text ="""
Please select the type of Value of an Investment:
    1. Future Value
    2. Present Value
Enter your choice (1-2): """

                while True:
                    choice = input(choice_text).strip()
                    self.help_func.clear_screen()
                    if choice not in ['1', '2']:
                            print("Invalid choice for the type of Value of an Investment. Please enter (1-2).")                        
                            continue
                    
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
                            P = self.help_func.get_input_with_condition(
                                "Enter the payment amount per period: ", 'float',
                                lambda x: x >= x, "Error: The payment amount per period must be a positive number."
                            )
                            # Get interest rate per period (r)
                            annual_rate = self.help_func.get_input_with_condition(
                                "Enter the interest rate per period (as a percentage, e.g., 5 for 5%): ", 'float',
                                lambda x: x >= 0, "Error: The interest rate per period must be a positive number."
                            )
                            r = annual_rate / 100  # Convert percentage to decimal

                            # Get total number of periods (n)
                            n = self.help_func.get_input_with_condition(
                                "Enter the total number of periods: ", 'int',
                                lambda x: x >= 0, "Error: The total number of periods must be a positive number."
                            )

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
                    
                    elif choice == '2': # Present Value
                        PV_text ="""
Present Value (PV) calculation.
represents the current worth of a future sum of money, discounted at a specific interest rate. 
It helps determine how much a future amount is worth today, taking into account the time value of money.
"""
                        self.help_func.text_helper(PV_text)
                        # Get Future Value (the amount of money in the future) (FV)
                        FV = self.help_func.get_input_with_condition(
                            "Enter future value (the amount of money in the future): ", 'float',
                            lambda x: x >= 0, "Error: Future value (the amount of money in the future) must be a positive number."
                        )

                        # Get interest rate per period (r)
                        annual_rate = self.help_func.get_input_with_condition(
                            "Enter the discount rate (or interest rate per period) (as a percentage, e.g., 5 for 5%): ", 'float',
                            lambda x: x >= 0, "Error: The interest rate per period must be a positive number."
                        )
                        r = annual_rate / 100  # Convert percentage to decimal

                        # Get total number of periods (t)
                        t = self.help_func.get_input_with_condition(
                            "Enter Number of periods (years, months, etc.): ", 'float',
                            lambda x: x >= 0, "Error: The total number of periods must be a positive number."
                        )

                        t = self.help_func.get_input_with_condition(
                            "Enter Number of periods (years, months, etc.): ", 'float',
                            lambda x: x >= 0, "Error: The total number of periods must be a positive number."
                        )

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

            elif choice == '7':  # Net Present Value (NPV)
                npv_text = """
Net Present Value calculation.
Calculate the present value of a series of future cash flows, considering a specific discount rate.
You need to gather all the expected cash flows for each time period, the discount rate, and how many periods you're analyzing.
""" 
                self.help_func.text_helper(npv_text)

                # Get total number of periods (n)
                n = self.help_func.get_input_with_condition(
                    "Enter the total number of periods: ", 'int',
                    lambda x: x >= 0, "Error: The total number of periods must be a positive number."
                )

                # Get Cash Flows (CF)
                cash_flows = []  # Initialize an empty list to store cash flows
                for i in range(n + 1):  # Including Year 0
                    while True:
                        cash_flow = self.help_func.get_float_input(f"Enter the cash inflow (or outflow) for Year {i}: ")
                        cash_flows.append(cash_flow)
                        break

                # Get Discount Rate (r)
                annual_rate = self.help_func.get_input_with_condition(
                    "Enter the discount rate (as a percentage, e.g., 5 for 5%): ", 'float',
                    lambda x: x >= 0, "Error: The discount rate must be a positive number."
                )
                r = annual_rate / 100

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

            elif choice == '8': # Internal Rate of Return (IRR)
                irr_text = """
Internal Rate of Return (IRR) calculation.
This method calculates the rate of return at which the net present value (NPV) of all cash flows equals zero.
You will need to gather the initial investment and all expected future cash flows for each period.
        """
                self.help_func.text_helper(irr_text)

                # Get the total number of periods (n)
                n = self.help_func.get_input_with_condition(
                    "Enter the total number of periods: ", 'int',
                    lambda x: x >= 0, "Error: The total number of periods must be a positive number."
                )

                # Get Cash Flows (CF)
                cash_flows = []  # Initialize an empty list to store cash flows
                for i in range(n + 1):  # Including Year 0 (initial investment)
                    if i == 0:  # For Year 0 (initial investment)
                        cash_flow = self.help_calc.get_input_with_condition(
                            f"Enter the cash inflow (or outflow) for Year {i}: ", 'float', 
                            lambda x: x < 0, "ERROR: The initial investment (Year 0) should be negative."
                        )
                    else:  # For future years
                        cash_flow = self.help_calc.get_input_with_condition(
                            f"Enter the cash inflow (or outflow) for Year {i}: ", 'float', 
                            lambda x: x >= 0, "ERROR: Future years should have positive cash inflows."
                        )
                    cash_flows.append(cash_flow)
                    break

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
                
            elif choice == '9': # Return on Investment (ROI)
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
                    if choice not in ['1', '2']:
                        print("Invalid choice for Return on Investment (ROI) type. Please enter 1 or 2.")
                        continue

                    # Get Gain from Investment (GFI)
                    GFI = self.help_func.get_input_with_condition(
                        "Enter the total amount you gained or earned from the investment: ", 'float',
                        lambda x: x >= 0, "Error: The total amount you gained or earned must be a positive number."
                    )

                    # Get Initial Investment (II)
                    II = self.help_func.get_input_with_condition(
                        "Enter the original amount you invested: ", 'float',
                        lambda x: x >= 0, "Error: The original amount you invested must be a positive number."
                    )

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
                        n = self.help_func.get_input_with_condition(
                            "Enter the time period, in years, over which the investment was held: ", 'int',
                            lambda x: x >= 0, "Error: The time period, in years, must be a positive number."
                        )

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

            elif choice == '10': # Advanced Compound Interest with Monthly Contributions with or without inflation
                text_choice ="""
Advanced Compound Interest Calculator
This program helps you calculate the future value of an investment, factoring in compound interest, monthly contributions, and the option to consider inflation.

Choose your calculation mode:
    1. With Inflation Calculate with inflation-adjusted values for a realistic future estimate.
    2. Without Inflation Calculate based solely on compound interest for a straightforward projection.
Enter your choice (1 or 2): """
                
                while True:
                    choice = input(text_choice).strip()
                    self.help_func.clear_screen()
                    if choice not in ['1', '2']:
                        print("Invalid choice Advanced Compound Interest calculation. Please enter 1 or 2.")                        
                        continue

                    if choice == '1':
                        text = """
This program calculates the future value of an investment considering both compound interest and monthly contributions.
"""
                    else:
                        text = """
This program calculates the future value of an investment considering both interest and inflation.
"""
                    
                    self.help_func.text_helper(text)

                    # Collect inputs for Principal, Interest, etc.
                    P = self.help_func.get_input_with_condition(
                        "Enter the Principal (initial amount of money): ", 'float',
                        lambda x: x >= 0, "ERROR: The principal must be a positive number."
                    )

                    annual_rate = self.help_func.get_input_with_condition(
                        "Enter the Annual interest rate (as a percentage, e.g., 5 for 5%): ", 'float',
                        lambda x: x >= 0, "ERROR: The interest rate cannot be negative."
                    )
                    r = annual_rate / 100

                    if choice == '2':  # If inflation is considered
                        inflation_rate = self.help_func.get_input_with_condition(
                            "Enter the annual inflation rate (as a percentage, e.g., 5 for 5%): ", 'float',
                            lambda x: x >= 0, "ERROR: The annual inflation rate cannot be negative."
                        )
                        i = inflation_rate / 100
                    else:
                        i = 0  # No inflation adjustment for choice '1'

                    n = self.help_func.get_input_with_condition(
                        "Enter the number of times interest is compounded per year: ", 'int',
                        [
                            (lambda x: x >= 0, "ERROR: The number of times interest is compounded per year must be greater than 0."),
                            (lambda x: x < 365, "ERROR: The number of times interest is compounded per year cannot be greater than 365.")
                        ]
                    )

                    t = self.help_func.get_input_with_condition(
                        "Enter how long the money is invested (in years): ", 'int',
                        lambda x: x >= 0, "ERROR: The time investment must be a positive number."
                    )

                    PMT = self.help_func.get_input_with_condition(
                        "Enter the amount you add each month: ", 'float',
                        lambda x: x >= 0, "ERROR: The amount you add each month must be a positive number."
                    )

                    self.help_func.clear_screen()

                    # Calculate future value based on interest and inflation
                    A_principal = P * (1 + (r - i) / n) ** (n * t)
                    A_contributions = PMT * ((1 + (r - i) / n) ** (n * t) - 1) / ((r - i) / n)
                    result = A_principal + A_contributions

                    # After collecting all inputs and result
                    print(f"Inputs:")
                    print(f"  Initial Principal (P): ${P:.2f}")
                    print(f"  Annual Interest Rate (r): {annual_rate:.2f}%")
                    if choice == '2':
                        print(f"  Annual Inflation Rate (i): {inflation_rate:.2f}%")
                    print(f"  Compounding Frequency (n): {n} times per year")
                    print(f"  Time (t): {t} year{'s' if t > 1 else ''}")
                    print(f"  Monthly Contribution (PMT): ${PMT:.2f}")
                    print(f"\nThe total amount after {t} year{'s' if t > 1 else ''} is: ${result:.2f}")

                    # Create graph
                    years = [i for i in range(1, int(t) + 1)]
                    future_values = []

                    for year in years:
                        A_principal = P * (1 + (r - i) / n) ** (n * year)
                        A_contributions = PMT * ((1 + (r - i) / n) ** (n * year) - 1) / ((r - i) / n)
                        future_values.append(A_principal + A_contributions)

                    # Plot the graph
                    plt.plot(years, future_values, label="Future Value", color='blue' if choice == '1' else 'green')
                    plt.xlabel("Years")
                    plt.ylabel("Future Value ($)")
                    plt.title("Investment Growth Over Time" + (" (With Inflation Adjustment)" if choice == '2' else ""))
                    plt.grid(True)
                    plt.legend()
                    plt.show()
                    break
                
            elif choice == '11': # Savings Goal Calculator
                text ="""
Saving Goal Calculation.
Calculates the time (in years) needed to reach a savings goal (FV) with regular monthly contributions (PMT),
an annual interest rate, and a compounding frequency.
"""
                self.help_func.text_helper(text)

                FV = self.help_func.get_input_with_condition(
                    "Enter your future savings goal: ", 'float',
                    lambda x: x >= 0, "ERROR: The future savings goal must be a positive number."
                )

                PMT = self.help_func.get_input_with_condition(
                    "Enter the amount you will contribute each month: ", 'float',
                    lambda x: x >= 0, "ERROR: The monthly contribution amount must be a positive number."
                )

                annual_rate = self.help_func.get_input_with_condition(
                    "Enter the interest rate per period (as a percentage, e.g., enter 5 for 5%): ", 'float',
                    lambda x: x >= 0, "ERROR: The interest rate must be a positive number."
                )
                r = annual_rate / 100

                n = self.help_func.get_input_with_condition(
                    "Enter the number of times interest is compounded per year: ", 'int',
                    [
                        (lambda x: x >= 0, "ERROR: The compounding frequency must be a positive number."),
                        (lambda x: x <= 365, "ERROR: The compounding frequency cannot be greater than 365.")
                    ]
                )

                t = self.help_func.get_input_with_condition(
                    "Enter the maximum time period (in years) for the graph: ", 'float',
                    lambda x: x >= 0, "ERROR: The time period must be a positive number."
                )
                    
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

            elif choice == '12': # Effective Annual Rate (EAR)
                text = """
Effective Annual Rate (EAR) Calculation
The Effective Annual Rate (EAR) accounts for compounding periods within the year, providing an accurate
measure of annual return or cost. This helps in comparing financial products with different compounding intervals.
"""
                self.help_func.text_helper(text)

                R = self.help_func.get_input_with_condition(
                    "Enter the Growth or Decay rate (as a percentage, e.g., 5 for 5%): ", 'float',
                    lambda x: x >= 0, "ERROR: The growth/decay rate cannot be negative."
                )
                r = R / 100

                n = self.help_func.get_input_with_condition(
                    "Enter the Number of Compounding Periods per Year: ", 'int',
                    lambda x: x > 0, "Error: The Number of Compounding Periods must be a positive integer greater than zero."
                )

                max_years = self.help_func.get_input_with_condition(
                    "Enter the number of years to display on the graph: ", 'int',
                    lambda x: x >= 0, "ERROR: The number of years must be a positive integer."
                )

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

            elif choice == '13': # back
                break
            break
        
            # NOTE: please add more of financial calculations
            # NOTE: graph at formula number 9 is not working

    def age_calculations(self): # No.5
        choice_text ="""
Welcome to the Age Calculator!
    1. birthdate Calculation
    2. Age Comparison
    3. Go back
Enter your choice (1-3): """

        while True:
            choice = input(choice_text).strip()
            self.help_func.clear_screen()
            if choice not in ['1', '2', '3']:
                print("Invalid choice. Please enter (1-3)")            
                continue

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

            elif choice == '3': # go back
                break
            break

    def unit_calculations(self): # No.6
        text = """
Welcome to the Distance Converter! 
This tool helps you convert between various units of distance, volume, and weight.
Follow the instructions to enter the number you wish to convert, select the units, 
and see the results instantly!
"""
        self.help_func.text_helper(text)

        # Dictionary of direct conversion factors between units
        conversion_factors = {
            ("Km", "m"): 1000, ("m", "Km"): 1 / 1000,
            ("Cm", "m"): 0.01, ("m", "Cm"): 100,
            ("mm", "m"): 0.001, ("m", "mm"): 1000,
            ("mi", "m"): 1609.34, ("m", "mi"): 1 / 1609.34,
            ("yd", "m"): 0.9144, ("m", "yd"): 1 / 0.9144,
            ("ft", "m"): 0.3048, ("m", "ft"): 1 / 0.3048,
            ("in", "m"): 0.0254, ("m", "in"): 1 / 0.0254,
            ("L", "mL"): 1000, ("mL", "L"): 1 / 1000,
            ("gal", "L"): 3.78541, ("L", "gal"): 1 / 3.78541,
            ("lb", "kg"): 0.453592, ("kg", "lb"): 1 / 0.453592,
            ("g", "kg"): 0.001, ("kg", "g"): 1000,
            ("mg", "g"): 0.001, ("g", "mg"): 1000,
            # Add more conversions as needed
        }

        # Map of choice numbers to unit symbols
        symbol_map = {
            "1": "Km", "2": "m", "3": "Cm", "4": "mm", "5": "mi",
            "6": "yd", "7": "ft", "8": "in", "9": "L", "10": "mL",
            "11": "gal", "12": "lb", "13": "kg", "14": "g", "15": "mg"
        }

        def convert_unit(value, from_unit, to_unit):
            """Convert value directly from one unit to another using conversion_factors."""
            if (from_unit, to_unit) in conversion_factors:
                return value * conversion_factors[(from_unit, to_unit)]
            elif (to_unit, from_unit) in conversion_factors:
                return value / conversion_factors[(to_unit, from_unit)]
            else:
                return None  # Return None if no conversion factor exists

        # Main code

        num = self.help_func.get_float_input("Step 1: Enter the number you want to convert.\nEnter the number you want to convert: ", True)
        
        # Loop until valid conversion choices are made
        while True:

            # Choose the original unit
            while True:
                print("Step 2: Choose the unit you want to convert from.")
                symbol_text = """
Enter the symbol of your number:
    1. Kilometers (Km)       2. Meters (m)             3. Centimeters (Cm)
    4. Millimeters (mm)      5. Miles (mi)             6. Yards (yd)
    7. Feet (ft)             8. Inches (in)            9. Liters (L)
   10. Milliliters (mL)     11. Gallons (gal)         12. Pounds (lb)
   13. Kilograms (kg)       14. Grams (g)             15. Milligrams (mg)
Enter your choice (1-15): """
                
                symbol_choice1 = input(symbol_text).strip()
                if symbol_choice1 in symbol_map:
                    from_symbol = symbol_map[symbol_choice1]
                    break
                else:
                    self.help_func.clear_screen()
                    print("Invalid choice. Please enter a number between 1 and 15.")

            self.help_func.clear_screen()
                 
            # Choose the target unit
            while True:

                print("Step 3: Choose the unit you want to convert to.")
                symbol_text = """
Enter the symbol you want to convert to:
    1. Kilometers (Km)       2. Meters (m)             3. Centimeters (Cm)
    4. Millimeters (mm)      5. Miles (mi)             6. Yards (yd)
    7. Feet (ft)             8. Inches (in)            9. Liters (L)
   10. Milliliters (mL)     11. Gallons (gal)         12. Pounds (lb)
   13. Kilograms (kg)       14. Grams (g)             15. Milligrams (mg)
Enter your choice (1-15): """
                
                symbol_choice2 = input(symbol_text).strip()
                if symbol_choice2 in symbol_map:
                    to_symbol = symbol_map[symbol_choice2]
                    break
                else:
                    self.help_func.clear_screen()
                    print("Invalid choice. Please enter a number between 1 and 15.")

            self.help_func.clear_screen()

            # Perform the conversion and handle invalid conversions
            result = convert_unit(num, from_symbol, to_symbol)
            if result is not None:
                print(f"{num} {from_symbol} is equal to {result:.2f} {to_symbol}")
                break  # Exit loop if conversion is successful
            else:
                self.help_func.clear_screen()
                print(f"Conversion from {from_symbol} to {to_symbol} is not available. Please try again.")

    def currency_calculations(self): # No.7
        text = """
Please enter the currency you want to exchange, followed by the amount.
If you want to see a list of supported currency names, enter 'HELP' at any currency input prompt.
"""

        help_text = """
Here are some example currency codes with their respective countries:
- USD (United States Dollar) - United States
- EUR (Euro) - Eurozone countries
- GBP (British Pound) - United Kingdom
- JPY (Japanese Yen) - Japan
- CAD (Canadian Dollar) - Canada
- AUD (Australian Dollar) - Australia
- CNY (Chinese Yuan) - China
- INR (Indian Rupee) - India
- MXN (Mexican Peso) - Mexico
- BRL (Brazilian Real) - Brazil
- RUB (Russian Ruble) - Russia
- CHF (Swiss Franc) - Switzerland
- SEK (Swedish Krona) - Sweden
- NZD (New Zealand Dollar) - New Zealand
- ZAR (South African Rand) - South Africa
- KRW (South Korean Won) - South Korea
- SGD (Singapore Dollar) - Singapore
- MYR (Malaysian Ringgit) - Malaysia
- HKD (Hong Kong Dollar) - Hong Kong
- IDR (Indonesian Rupiah) - Indonesia
- TRY (Turkish Lira) - Turkey
- SAR (Saudi Riyal) - Saudi Arabia
- AED (United Arab Emirates Dirham) - United Arab Emirates
- KWD (Kuwaiti Dinar) - Kuwait
- QAR (Qatari Rial) - Qatar
- PKR (Pakistani Rupee) - Pakistan
- EGP (Egyptian Pound) - Egypt
- THB (Thai Baht) - Thailand
- PHP (Philippine Peso) - Philippines
- VND (Vietnamese Dong) - Vietnam
- ARS (Argentine Peso) - Argentina
- COP (Colombian Peso) - Colombia
- CLP (Chilean Peso) - Chile
- PEN (Peruvian Nuevo Sol) - Peru
- JOD (Jordanian Dinar) - Jordan
- BDT (Bangladeshi Taka) - Bangladesh
- TWD (New Taiwan Dollar) - Taiwan
- HUF (Hungarian Forint) - Hungary
- PLN (Polish Zloty) - Poland
- DKK (Danish Krone) - Denmark
- NOK (Norwegian Krone) - Norway
- ISK (Icelandic Krona) - Iceland
"""

        valid_currency_codes = [
            "USD", "EUR", "GBP", "JPY", "CAD", "AUD", "CNY", "INR", "MXN", "BRL", 
            "RUB", "CHF", "SEK", "NZD", "ZAR", "KRW", "SGD", "MYR", "HKD", "IDR", 
            "TRY", "SAR", "AED", "KWD", "QAR", "PKR", "EGP", "THB", "PHP", "VND", 
            "ARS", "COP", "CLP", "PEN", "JOD", "BDT", "TWD", "HUF", "PLN", "DKK", 
            "NOK", "ISK"
        ]

        self.help_func.text_helper(text)

        while True:

            while True: # the converted currency
                from_currency = self.help_func.get_input_user_text("Enter the currency to exchange: ", 'capital')  
                if from_currency == "HELP":
                    self.help_func.text_helper(help_text)
                    continue
                if from_currency not in valid_currency_codes:
                    self.help_func.clear_screen()
                    print(f"Error: {from_currency} is not a valid currency code. Please try again.")
                    continue
                break

            amount = self.help_func.get_float_input("Enter the amount: ")

            while True: # the converting currency
                to_currency = self.help_func.get_input_user_text("Enter the target currency: ", 'capital', True)
                if to_currency == "HELP":
                    self.help_func.text_helper(help_text)
                    continue
                if to_currency not in valid_currency_codes:
                    self.help_func.clear_screen()
                    print(f"Error: {to_currency} is not a valid currency code. Please try again.")
                    continue
                break

            # API request
            url = f"https://v6.exchangerate-api.com/v6/c99ed7cee48065c263699967/latest/{from_currency}"
            try:
                response = requests.get(url)
                data = response.json()

                self.help_func.clear_screen()

                if response.status_code == 200:
                    if to_currency in data['conversion_rates']:
                        conversion_rate = data['conversion_rates'][to_currency]
                        converted_amount = amount * conversion_rate
                        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
                        break
                    else:
                        print("Error: Invalid target currency.")
                else:
                    print(f"Error {response.status_code}: Unable to fetch exchange rates.")
                    break
            except requests.exceptions.RequestException as e:
                print(f"Error occurred: {e}")
                break

    def pythagorean_formula(self): # No.8
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
            self.help_func.clear_screen()
            if choice not in ['1', '2', '3']:
                print("Invalid choice. Please enter (1-3)")
                continue

            if choice == '1':
                a = self.help_func.get_float_input("Enter the first leg of the triangle: ")
                b = self.help_func.get_float_input("Enter the second leg of the triangle: ", True)

                c = math.sqrt((a ** 2) + (b ** 2))
                result = self.help_func.handle_large_numbers(c)

                print(f"The length of the hypotenuse with the first leg of {a} and the second leg of {b} is {result:.2f}")

            elif choice == '2':
                leg = self.help_func.get_float_input("Enter the known leg of the triangle: ")
                c = self.help_func.get_float_input("Enter the hypotenuse of the triangle: ", True)

                missing_leg = math.sqrt((c ** 2) - (leg ** 2))
                result = self.help_func.handle_large_numbers(missing_leg)

                print(f"The length of the missing leg with the known leg of {leg} and the hypotenuse of {c} is {result:.2f}")
            
            elif choice == '3':
                break
            break

    def distance_formula(self): # No.9
        text ="""
Distance Formula.
This formula calculates the distance between two points (x'1,y'1) and (x'2,y'2) on a 2D plane.

input "back" to come back to the main menu.
"""
# Menus Class
        self.help_func.text_helper(text)


        x_1 = self.help_func.get_float_input("Enter x from the first point: ")
        y_1 = self.help_func.get_float_input("Enter y from the first point: ", True)
        x_2 = self.help_func.get_float_input("Enter x from the second point: ")
        y_2 = self.help_func.get_float_input("Enter y from the second point: ", True)

        equation_d = cmath.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)
        reslut = self.help_func.handle_large_numbers(equation_d)

        print(f"The distance between ({x_1}, {y_1}) and ({x_2}, {y_2}) is {reslut}")

    def exponential_growth_decay_formula(self): # No.10
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
        while True:

            self.help_func.text_helper(text)

            N0 = self.help_func.get_float_input("Enter the initial amount (N0): ")
            k = self.help_func.get_float_input("Enter the growth/decay rate (k): ")
            t = self.help_func.get_float_input("Enter the time (t): ", True)

            # Check if the exponential calculation will overflow
            if k * t > 700:  # Arbitrarily large number threshold (exp function limit)
                print("The value is too large for the exponential calculation.")
                return False  # Return False to indicate failure

            N = N0 * math.exp(k * t)

            print(f"For an initial amount of {N0} with a growth rate of {k * 100:.2f} percent over {t} (any time curency), the final amount is approximately {N:.2f}.")
            break

    def The_closed_form_formula(self): # No.11
        text = """
The closed-form formula calculates Fibonacci numbers using Binet's formula:
F(n) = (phi^n - (1 - phi)^n) / sqrt(5)
where phi = (1 + sqrt(5)) / 2 is the golden ratio.

This method works well for small values of n, but becomes inaccurate for large n due to floating-point precision limitations.
"""
        self.help_func.text_helper(text)
        
        while True:
            n = self.help_func.get_input_with_condition(
                "Enter the n-th Fibonacci number: ", 'int',
                [
                    (lambda x: x > 0, "Fibonacci number is not defined for negative indices."),
                    (lambda x: x <= 500, "Fibonacci number is very big to handle.")
                ]
            )
            self.help_func.clear_screen()
            
            # Binet's formula for Fibonacci
            phi = (1 + math.sqrt(5)) / 2
            fib_num = (phi ** n - (1 - phi) ** n) / math.sqrt(5)

            # Round the result to the nearest integer
            fib_num = round(fib_num)

            print(f"Fibonacci number F({n}) = {fib_num}")
            break
        
    def the_law_of_cosines(self): # No.12
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
                c = self.help_func.get_float_input("Enter the angle between sides a and b: ", True)

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
                c = self.help_func.get_float_input("Enter the length of third known side: ", True)

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

    def riemann_zeta_function(self): # No.13
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

    def newtons_law_of_universal_gravitation(self): # No.14
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
            if choice not in ['1', '2', '3']:
                print("Invalid choice for  Newton's Law of Universal Gravitation. Please enter (1-3)")
                continue

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

            elif choice == '3':
                break
            break

    # add more functions here
