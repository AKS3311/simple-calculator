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
                print(f"Invalid input. please enter a valid number.")

    def get_int_input(self, prompt):
        while True:
            user_input = input(prompt).strip()  # Capture user input as a string
            try:
                return int(user_input)  # Try converting the input to a float
            except ValueError:
                self.clear_screen()  # Clear the screen before showing the error
                print(f"Invalid input. please enter a valid number.")

    def text_helper(self, prompt):
        print(prompt)
        self.pause()
        self.clear_screen()
