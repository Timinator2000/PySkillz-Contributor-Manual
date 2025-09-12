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
    

    def markdown_file(self):
        return 'markdown.md'


    def learner_file(self):
        return 'exercise_name.py'


    def solution_file(self):
        return 'exercise_name_solution.py'


    def test_file(self):
        return 'exercise_name_test.py'


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
            self.send_msg(self.bug_channel, error)
            return
        
        self.send_multiline_text(markdown_channel, template.markdown_file())
        self.send_multiline_text(learner_channel, template.learner_file())
        self.send_multiline_text(solution_channel, template.solution_file())
        self.send_multiline_text(test_channel, template.test_file())


if __name__ == "__main__":
    analyzer = ExerciseTemplateGenerator()
    analyzer.run()