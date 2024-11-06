from HelpFunctions import HelpFunctions
from CalculatorFunctions import CalculatorFunctions

class CalculatorSetup:

    def __init__(self):
        self.calc_funcs = CalculatorFunctions()
        self.help_func = HelpFunctions()

    def show_main_menu(self):
        while True:
            self.main_menu()
            if not self.ask_to_calc_again():
                print("Thank you for using the calculator. Goodbye!")
                break

    def execute_calculation(self, calc_function): 
        self.help_func.clear_screen()
        calc_function()  # Execute the passed calculation function
        self.help_func.pause()
        self.help_func.clear_screen()

    def main_menu(self):
        menu_text = """
Welcome to the Calculator!
    1. Simple Calculation
    2. Shape Calculation
    3. Percentage Calculation
    4. Quadratic Calculation
    5. Financial Calculations
    6. Age Calculation
    7. Pythagorean Formula
    8. Distance Formula
    9. Exponential Growth Decay Formula
    10. The Law of Cosines
    11. Riemann Zeta Function
    12. Newton's Law of Universal Gravitation
    13. Quit
Enter your choice (1-12): """

        options = {
            '1': self.calc_funcs.simple_calculation,
            '2': self.calc_funcs.shape_calculations,
            '3': self.calc_funcs.percentage_calculation,
            '4': self.calc_funcs.quadratic_calculations,
            '5': self.calc_funcs.financial_calculations,
            '6': self.calc_funcs.age_calculation,
            '7': self.calc_funcs.pythagorean_formula,
            '8': self.calc_funcs.distance_formula,
            '9': self.calc_funcs.exponential_growth_decay_formula,
            '10': self.calc_funcs.the_law_of_cosines,
            '11':self.calc_funcs.riemann_zeta_function,
            '12':self.calc_funcs.newtons_law_of_universal_gravitation,
            '13': exit
        }

        while True:
            choice = input(menu_text).strip()
            if choice in options:
                if choice == '13':
                    self.help_func.clear_screen()
                    print("Thank you for using the calculator. Goodbye!")
                    exit()
                self.execute_calculation(options[choice]) # takes the choice thats in options and pass it to the function called execute_calculation()
                break
            else:
                self.help_func.clear_screen()
                print("Invalid choice. Please enter a number between 1 and 13.")

    def ask_to_calc_again(self): 
        end_text = """
Would you like to calculate again?
    1. Yes
    2. No
Enter your choice (1 or 2): """
        while True:
            choice = input(end_text).strip()
            if choice == '1':
                self.help_func.clear_screen()
                return True
            elif choice == '2':
                self.help_func.clear_screen()
                return False
            else:
                self.help_func.clear_screen()
                print("Invalid choice. Please enter 1 or 2.")
