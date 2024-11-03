from CalculatorSetup import CalculatorSetup

class CalculatorApp:

    def __init__(self):
        self.setup = CalculatorSetup()

    def run(self):
        self.setup.show_main_menu()

# Run the Calculator
if __name__ == "__main__":
    app = CalculatorApp()
    app.run()
