import os

class HelpFunctions:

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def pause(self):
        input("Press Enter to continue...")

    def handle_large_numbers(self, num):
    # Automatically converts to scientific notation if too large or too small
        if abs(num) >= 1e6 or abs(num) < 1e-6 and num != 0:
            return f"{num:.2e}"  # Format in scientific notation
        return num

    def formatted_result101(self, result):
        if result >= 1e3:  # Greater than or equal to 1000
            formatted_result = f"{result:.2f}"  # 2 decimal places
        elif result >= 1e1:  # Greater than or equal to 10
            formatted_result = f"{result:.2f}"  # 2 decimal places
        elif result >= 1e-1:  # Greater than or equal to 0.1
            formatted_result = f"{result:.2f}"  # 2 decimal places
        elif result >= 1e-3:  # Greater than or equal to 0.001
            formatted_result = f"{result:.4f}"  # 4 decimal places
        else:  # Less than 0.001
            formatted_result = f"{result:.2e}"  # Scientific notation for very small values
        return formatted_result

    def get_float_input(self, prompt):
        while True:
            user_input = input(prompt).strip()  # Capture user input as a string
            try:
                return float(user_input)  # Try converting the input to a float
            except ValueError:
                self.clear_screen()  # Clear the screen before showing the error
                print("Invalid input. please enter a valid number.")

    def get_int_input(self, prompt):
        while True:
            user_input = input(prompt).strip()  # Capture user input as a string
            try:
                return int(user_input)  # Try converting the input to a int
            except ValueError:
                self.clear_screen()  # Clear the screen before showing the error
                print("Invalid input. Please enter a valid integer number.")

    def get_input_with_condition(self, prompt, input_type, conditions_or_lambda, error_message=None):
        while True:
            # Get input
            if input_type == 'float':
                value = self.get_float_input(prompt)
            elif input_type == 'int':
                value = self.get_int_input(prompt)

            # Handle single or multiple conditions
            conditions = [(conditions_or_lambda, error_message)] if not isinstance(conditions_or_lambda, list) else conditions_or_lambda

            # Validate conditions
            for condition, error in conditions:
                if not condition(value):
                    self.clear_screen()
                    print(error if error else "ERROR: Invalid input.")
                    break
            else:
                return value

    def text_helper(self, prompt):
        print(prompt)
        self.pause()
        self.clear_screen()
