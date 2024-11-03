from HelpFunctions import HelpFunctions
from CalculatorFunctions import CalculatorFunctions
from colorama import Fore, Style

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
Welcome to the calculator!
    1. Simple calculation
    2. Shape calculation
    3. Percentage calculation
    4. Quadratic calculation
    5. Age calculation
    6. Pythagorean formula
    7. Distance formula
    8. Exponential growth decay formula
    9. The law of cosines
    10. Riemann Zeta Function
    11. Quit
Enter your choice (1-11): """

        options = {
            '1': self.calc_funcs.simple_calculation,
            '2': self.calc_funcs.shape_calculation,
            '3': self.calc_funcs.percentage_calculation,
            '4': self.calc_funcs.quadratic_calculation,
            '5': self.calc_funcs.age_calculation,
            '6': self.calc_funcs.pythagorean_formula,
            '7': self.calc_funcs.distance_formula,
            '8': self.calc_funcs.exponential_growth_decay_formula,
            '9': self.calc_funcs.the_law_of_cosines,
            '10':self.calc_funcs.riemann_zeta_function,
            '11': exit
        }

        while True:
            choice = input(Fore.GREEN + menu_text).strip()
            if choice in options:
                if choice == '11':
                    self.help_func.clear_screen()
                    print("Thank you for using the calculator. Goodbye!")
                    exit()
                self.execute_calculation(options[choice]) # takes the choice thats in options and pass it to the function called execute_calculation()
                break
            else:
                self.help_func.clear_screen()
                print("Invalid choice. Please enter a number between 1 and 11.")

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
