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


class ExerciseTemplateGeneratorTechio(pyskillz_tools.TechioInteraction):

    def __init__(self):
        super().__init__(__file__)


    def run(self):
        # markdown_channel = pyskillz_tools.Channel(f'Exercise Markdown 📚', 'Mkd📚>')
        # learner_channel = pyskillz_tools.Channel(f'Learner Code Window 📚', 'Lrn📚>')
        # solution_channel = pyskillz_tools.Channel(f'Solution File ✅', 'Sol✅>')
        # test_channel = pyskillz_tools.Channel(f'Test File 🧪', 'Tst🧪>')

        for line in self.code_analysis['source'].split('\n'):
            if line.startswith('def'):
                template = pyskillz_tools.ExerciseTemplate(function_signature=line)
                error = template.check_function_definition(syntax_tree=self.code_analysis['tree'])
                break
        else:
            error = 'No function definition found.'

        if error:
            self.fail()
            self.send_msg(self.bug_channel, error)
            return
        
        self.success()

        markdown_channel = pyskillz_tools.Channel(f'{template.exercise_name}.md 📚', 'Mkd📚>')
        learner_channel = pyskillz_tools.Channel(f'{template.exercise_name}.py 📚', 'Lrn📚>')
        solution_channel = pyskillz_tools.Channel(f'{template.exercise_name}_solution.py ✅', 'Sol✅>')
        test_channel = pyskillz_tools.Channel(f'{template.exercise_name}_test.py 🧪', 'Tst🧪>')

        path = os.path.join(self.dir_path, '..', '..', '____new_exercises____', '____exercise_template____')
        path = os.path.normpath(path)
        
        filename = os.path.join(path, 'exercise_name.md')
        text = template.markdown_file(filename)
        self.send_multiline_text(markdown_channel, '\n'.join(text))

        filename = os.path.join(path, 'exercise_name.py')
        text = template.retrieve_text(filename)
        self.send_multiline_text(learner_channel, '\n'.join(text))

        filename = os.path.join(path, 'exercise_name_solution.py')
        text = template.retrieve_text(filename)
        self.send_multiline_text(solution_channel, '\n'.join(text))

        filename = os.path.join(path, 'exercise_name_test.py')
        text = template.retrieve_test_file(filename)
        self.send_multiline_text(test_channel, '\n'.join(text))


if __name__ == "__main__":
    analyzer = ExerciseTemplateGeneratorTechio()
    analyzer.run()