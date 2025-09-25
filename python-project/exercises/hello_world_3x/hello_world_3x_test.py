###############################################################################################################
# Environment Setup - Do not change anything in this section.
###############################################################################################################

import os
import sys
import random

# Normalize path for current OS. Split the path into directory and filename.
dir_path, _ = os.path.split(os.path.normpath(__file__))

# Add tools directory to the OS PATH
sys.path.insert(0, os.path.join(dir_path, '..', '..', '____tools____'))

try:
    import pyskillz_tools

except ImportError:
    print(f"Import Error: pyskillz_tools.py needs to be in the '____tools____' folder, one level deep from python-project.")

###############################################################################################################
# End Setup
###############################################################################################################


success_message = """


"""

success_message += ''
success_message += ''
success_message += ''


class HelloWorld3X(pyskillz_tools.PrintBasedExercise):
    
    def __init__(self):

        super().__init__(__file__, success_message)
        self.fixed_test_cases = [[]]

    
    def test_case_to_string(self, test_case) -> str:
        return 'There are no test cases for this exercise. You just need to print \'Hello, World!\' 3 times.'


    def display_success_message(self):
        stats_channel = pyskillz_tools.Channel(f'Lines of Code and Python Statements #️⃣', 'LOC#️⃣>')
        self.send_multiline_text(stats_channel, self.get_code_analysis('basic_stats'))


    def display_solution(self):
        pass


if __name__ == "__main__":
    exercise = HelloWorld3X()
    exercise.run()
