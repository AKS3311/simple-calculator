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
    2. Shape Calculations
    3. Quadratic Calculations
    4. Financial Calculations
    5. Age Calculations
    6. Unit Calculations
    7. Currency Calculations
    8. Pythagorean Formula
    9. Distance Formula
   10. Exponential Growth Decay Formula
   11. The Closed Form Formula
   12. The Law of Cosines
   13. Riemann Zeta Function
   14. Newton's Law of Universal Gravitation
   15. Quit
Enter your choice (1-15): """

        options = {
            '1': self.calc_funcs.simple_calculation,
            '2': self.calc_funcs.shape_calculations,
            '3': self.calc_funcs.quadratic_calculations,
            '4': self.calc_funcs.financial_calculations,
            '5': self.calc_funcs.age_calculations,
            '6': self.calc_funcs.unit_calculations,
            '7': self.calc_funcs.currency_calculations,
            '8': self.calc_funcs.pythagorean_formula,
            '9': self.calc_funcs.distance_formula,
            '10':self.calc_funcs.exponential_growth_decay_formula,
            '11':self.calc_funcs.The_closed_form_formula,
            '12':self.calc_funcs.the_law_of_cosines,
            '13':self.calc_funcs.riemann_zeta_function,
            '14':self.calc_funcs.newtons_law_of_universal_gravitation,
            '15': exit
        }

        while True:
            choice = input(menu_text).strip()
            if choice in options:
                if choice == '15':
                    self.help_func.clear_screen()
                    print("Thank you for using the calculator. Goodbye!")
                    exit()
                self.execute_calculation(options[choice]) # takes the choice thats in options and pass it to the function called execute_calculation()
                break
            else:
                self.help_func.clear_screen()
                print("Invalid choice. Please enter a number between (1-15).")

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
