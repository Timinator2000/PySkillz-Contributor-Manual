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

import ast
import re

class ExerciseTemplate():

    def __init__(self):
        self.syntax_tree = None

    
    def check_function_definition(self, header_line='', syntax_tree=None) -> str:
        """
        Check if the function definition header is valid:
        - every parameter has a type annotation
        - the return type is specified (including -> None for no return)

        Input should be ONLY the header line (e.g., 'def foo(a: int) -> None:').

        Return value indicates the first error. An empty string indicates success.
        """

        if syntax_tree == None:
            try:
                # Append a dummy body to make it valid Python
                syntax_tree = ast.parse(header_line + "\n    pass")
            except SyntaxError as e:
                return f"Syntax error: {e}"

        for node in ast.walk(syntax_tree):
            if isinstance(node, ast.FunctionDef):
                # Check function name
                if not re.fullmatch(r'[a-z0-9_]+', node.name):
                    return f"Invalid function name '{node.name}'. " + \
                           f"Only lowercase letters, digits, and underscores are allowed."

                # Check parameters
                for arg in node.args.args + node.args.kwonlyargs:
                    if arg.annotation is None:
                        return f"Parameter '{arg.arg}' is missing a type annotation."

                if node.args.vararg and node.args.vararg.annotation is None:
                    return f"Vararg parameter '*{node.args.vararg.arg}' is missing a type annotation."

                if node.args.kwarg and node.args.kwarg.annotation is None:
                    return f"Kwarg parameter '**{node.args.kwarg.arg}' is missing a type annotation."

                # Check return type
                if node.returns is None:
                    return f"Function '{node.name}' is missing a return type annotation."

        return ''
    

    def markdown_file(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            text = f.read()

        return text


    def learner_file(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            text = f.read()

        return text


    def solution_file(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            text = f.read()

        return text


    def test_file(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            text = f.read()

        return text


class ExerciseTemplateGenerator(pyskillz_tools.TechioInteraction):

    def __init__(self):
        super().__init__(__file__)


    def run(self):
        markdown_channel = pyskillz_tools.Channel(f'Exercise Markdown 📚', 'Mkd📚>')
        learner_channel = pyskillz_tools.Channel(f'Learner Code Window 📚', 'Lrn📚>')
        solution_channel = pyskillz_tools.Channel(f'Solution File ✅', 'Sol✅>')
        test_channel = pyskillz_tools.Channel(f'Test File 🧪', 'Tst🧪>')

        template = ExerciseTemplate()
        error = template.check_function_definition(syntax_tree=self.code_analysis['tree'])

        if error:
            self.fail()
            self.send_msg(self.bug_channel, error)
            return
        
        self.success()

        path = os.path.join(self.dir_path, '..', '..', '____new_exercises____', '____exercise_template____')
        path = os.path.normpath(path)
        
        filename = os.path.join(path, 'exercise_name.md')
        self.send_multiline_text(markdown_channel, template.markdown_file(filename))

        filename = os.path.join(path, 'exercise_name.py')
        self.send_multiline_text(learner_channel, template.learner_file(filename))

        filename = os.path.join(path, 'exercise_name_solution.py')
        self.send_multiline_text(solution_channel, template.solution_file(filename))

        filename = os.path.join(path, 'exercise_name_test.py')
        self.send_multiline_text(test_channel, template.test_file(filename))


if __name__ == "__main__":
    analyzer = ExerciseTemplateGenerator()
    analyzer.run()