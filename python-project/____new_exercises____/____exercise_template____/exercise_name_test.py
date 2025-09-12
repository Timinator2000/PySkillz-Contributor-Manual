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
    print(f'Import Error: pyskillz_tools.py needs to be in the “____tools____” folder, one level deep from python-project.')

###############################################################################################################
# End Setup
###############################################################################################################


success_message = """


"""

success_message += ''
success_message += ''
success_message += ''


class ExerciseName(pyskillz_tools.Exercise):
class ExerciseName(pyskillz_tools.PrintBasedExercise):
    
    def __init__(self):

        super().__init__(__file__, success_message)
        self.parameter_names = ['a', 'b']
        self.num_random_test_cases = 1000

        self.fixed_test_cases = [
            [],
            [],
            [],
            [],
            []
        ]

        # See the contributor guide if you wish to add any optional grading criteria.

        # Optional Exercise Constraints
        # self.max_statement_count =                 # Default is 10_000_000
        # self.max_lines_of_code =                   # Default is 10_000_000

        # Additional PrintBasedExercise Option
        # self.strict_print_usage = True             # Default is False


    def generate_random_test_case(self) -> list:
        return [random.randint(-100, 100), random.randint(-100, 100)]
    

    # Most exercises do NOT need to override the following methods. See
    # the contributor guide if you wish to customize how a test case is
    # displayed to the learner or if you wish to add custom grading
    # criteria to an exercise.

    # def test_case_to_string(self, test_case) -> str:
    #     a, b = test_case
    #     return f'{a = }\n{b = }'


    # def check_additonal_solution_criteria(self) -> bool:
    #     return ''


if __name__ == "__main__":
    exercise = ExerciseName()
    exercise.run()
