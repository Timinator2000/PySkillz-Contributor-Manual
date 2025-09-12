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
    print(f'Import Error: pyskillz_tools.py needs to be in the ____tools____ folder, one level deep from python-project.')

###############################################################################################################
# End Setup
###############################################################################################################


class ExerciseTemplateGenerator(pyskillz_tools.TechioInteraction):

    def __init__(self):
        super().__init__(__file__)


    def run(self):
        learner_channel = pyskillz_tools.Channel(f'Learner Code Window 📚', 'Lrn📚>')
        solution_channel = pyskillz_tools.Channel(f'Solution File ✅', 'Sol✅>')
        test_channel = pyskillz_tools.Channel(f'Test File 🧪', 'Tst🧪>')

        self.send_msg(learner_channel, 'learner channel...')
        self.send_msg(solution_channel, 'solution channel...')
        self.send_msg(test_channel, 'test channel...')


if __name__ == "__main__":
    analyzer = ExerciseTemplateGenerator()
    analyzer.run()