# Last Edited: Oct 2, 2025 5:10am

from copy import deepcopy
from collections import namedtuple, Counter, defaultdict
import builtins
import sys
import os
import random
import importlib
import ast
import re


CONGRATS = ['Kudos!',
            'Well Done!',
            'Bravo!',
            'Perfect!',
            'Nice Job!',
            'Keep It Up!',
            'Attaboy!',
            'Nice Work!',
            'Excellent My Friend!',
            'Excelente Mi Amigo!',
            'Awesome!',
            'Hooray!',
            'Way To Go!',
            'Encore!',
            'Great Effort!',
            'Top Notch!',
            'There You Go!',
            'Take a Bow!',
            'Great Work!',
            'Outstanding!',
            'Exceptional Work!',
            'Superb!',
            'First-Class Effort!',
            'Brilliant!',
            'You are a Champion!',
            'Stellar!',
            'Magnificent Job!',
            'Dazzling Work!',
            'Stupendous!',
            'Marvelous!',
            'B-E-A-UTIFUL!',
            'Congratulations!']

CONGRATS_EMOJIS = '🌟🔥👏💥🎆🎉🥳💓💖💗🤟💯😀🤩😍'

BUG = ['Oops!',
       'Uh-oh!',
       'Oh no!',
       'Hmmm?',
       'Might have to try again!',
       'Ugh!',
       'Egad!']

BUG_EMOJIS = '🐞🐛🪲🦗😔😢😧'


class Channel():

    def __init__(self, full_name, short_name):
        self.full_name = full_name
        self.short_name = short_name


    def name(self, on_tech_io=True):
        return self.full_name if on_tech_io else self.short_name


class TechioInteraction():

    RUNNING_ON_TECH_IO = __file__.startswith('/project/target')
    # RUNNING_ON_TECH_IO = os.path.split(os.path.normpath(__file__))[0].startswith('/project/target')

    def __init__(self, exercise_path):

        self.success_channel = Channel(f'{random.choice(CONGRATS)} {random.choice(CONGRATS_EMOJIS)}', 'Win🎉>')
        self.bug_channel = Channel(f'{random.choice(BUG)} {random.choice(BUG_EMOJIS)}', 'Bug🐞>')
        self.std_out_channel = Channel('Standard Output', 'StdOut>')

        # Strip the exercise_name out of the full exercise path passed in as an argument.
        self.dir_path, filename = os.path.split(os.path.normpath(exercise_path))
        self.exercise_name = filename[:filename.find('_test.py')]

        # Analyze the code in the learner window.
        filename = os.path.join(self.dir_path, f'{self.exercise_name}.py')
        self.code_analysis = self.analyze_code(filename)

        # Redirect stdin since Tech.io playgrounds do not support stdin.
        builtins.input = self.input_not_supported
        self.input_not_supported_warning_issued = False


    def input_not_supported(self, prompt=''):
        if not self.input_not_supported_warning_issued:
            print('This playground does not support the input function. This line of code is being skipped.', file=sys.stderr, flush=True)
            self.input_not_supported_warning_issued = True


    def send_multiline_text(self, channel, msg):
        for line in msg.split('\n'):
            self.send_msg(channel, line)

        
    def send_msg(self, channel, msg):
        if TechioInteraction.RUNNING_ON_TECH_IO:
            print("TECHIO> message --channel \"{}\" \"{}\"".format(channel.name(), msg))
        else:
            if msg.startswith('> '):
                msg = msg[2:]
            print(f'{channel.name(on_tech_io=False)}{msg}')

            
    def success(self):
        if TechioInteraction.RUNNING_ON_TECH_IO:
            print("TECHIO> success true")

            
    def fail(self):
        if TechioInteraction.RUNNING_ON_TECH_IO:
            print("TECHIO> success false")


    def analyze_code(self, filename: str) -> dict:
        with open(filename, "r", encoding="utf-8") as f:
            source = f.read()

        tree = ast.parse(source, filename)
        categories = []

        def walk_node(node, depth=0):
            # Skip docstrings
            if isinstance(node, ast.Expr) and isinstance(getattr(node, 'value', None), ast.Constant):
                if isinstance(node.value.value, str):
                    categories.append((node, "docstring/string literal", False, depth))
                    return

            # Skip imports
            if isinstance(node, (ast.Import, ast.ImportFrom)):
                categories.append((node, "import", False, depth))
                return

            # Count statements
            if isinstance(node, ast.stmt):
                categories.append((node, type(node).__name__, True, depth))

            # Recurse into statement bodies
            for attr in ('body', 'orelse', 'finalbody', 'handlers', 'decorator_list', 'cases'):
                if hasattr(node, attr):
                    child_nodes = getattr(node, attr)
                    if not isinstance(child_nodes, list):
                        child_nodes = [child_nodes]
                    for child in child_nodes:
                        if isinstance(child, ast.ExceptHandler):
                            walk_node(child, depth + 1)
                        elif isinstance(child, ast.match_case):
                            for stmt in child.body:
                                walk_node(stmt, depth + 1)
                        else:
                            walk_node(child, depth + 1)

        walk_node(tree, depth=0)

        total_count = sum(1 for _, _, keep, _ in categories if keep)
        kept = Counter(cat for _, cat, keep, _ in categories if keep)
        skipped = Counter(cat for _, cat, keep, _ in categories if not keep)

        # Line counts
        lines = source.splitlines()
        total_lines = len(lines)
        non_blank_lines = sum(1 for line in lines if line.strip())
        comment_lines = sum(1 for line in lines if line.strip().startswith("#"))
        effective_code_lines = non_blank_lines - comment_lines

        return {
            "filename": filename,
            "tree": tree,
            "source": source,
            "categories": categories,  # list of (node, category, keep, depth)
            "total_count": total_count,
            "kept": kept,
            "skipped": skipped,
            "total_lines": total_lines,
            "non_blank_lines": non_blank_lines,
            "comment_lines": comment_lines,
            "effective_code_lines": effective_code_lines,
        }


    def get_code_analysis(self, level_of_detail):

        categories = self.code_analysis["categories"]
        kept = self.code_analysis["kept"]
        skipped = self.code_analysis["skipped"]

        text = []
        if level_of_detail == 'basic_stats':

            text.append(f"Lines of Code : {self.code_analysis['effective_code_lines']}")
            text.append(f"Statements    : {self.code_analysis['total_count']}")

        elif level_of_detail == 'summary':

            text.append(f"Total Lines     : {self.code_analysis['total_lines']}")
            text.append(f"Non-Blank Lines : {self.code_analysis['non_blank_lines']}")
            text.append(f"Comment Lines   : {self.code_analysis['comment_lines']}")
            text.append(f"Effective Code  : {self.code_analysis['effective_code_lines']}")

            text.append('')
            text.append("Summary of Statement Categories")
            text.append("---------------- ----------------")
            text.append("Statements Kept (Counted):")
            
            length = 0 if not kept else max(len(key) for key in kept)
            for cat, n in kept.items():
                text.append(f"  {cat:{length}} : {n}")
            if not kept:
                text.append("  (none)")

            text.append('')
            text.append("Statements Skipped:")

            length = 0 if not skipped else max(len(key) for key in skipped)
            for cat, n in skipped.items():
                text.append(f"  {cat:{length}} : {n}")
            if not skipped:
                text.append("  (none)")

            text.append('')
            text.append("Summary Totals:")
            text.append(f"  Total Statements Found : {len(categories)}")
            text.append(f"  Counted Statements     : {self.code_analysis['total_count']}")
            text.append(f"  Skipped Statements     : {len(categories) - self.code_analysis['total_count']}")
            text.append('')
            text.append(f"Final Statement Count    : {self.code_analysis['total_count']}")

        elif level_of_detail == 'details':

            text.append("Detailed Statement Breakdown (Nested)")
            text.append("-------------------------------------")
            for node, cat, keep, depth in sorted(categories, key=lambda x: getattr(x[0], "lineno", 0)):
                lineno = getattr(node, "lineno", None)
                lineinfo = f"line {lineno}" if lineno is not None else "no line"
                status = "COUNTED" if keep else "SKIPPED"

                snippet = ""
                if lineno is not None:
                    try:
                        snippet = self.code_analysis['source'].splitlines()[lineno - 1].strip()
                    except IndexError:
                        snippet = "<source unavailable>"

                indent = "    " * depth
                text.append(f"{indent}{lineinfo:>8} | {cat:<25} | {status:<7} | {snippet}")

        return '\n'.join(text)



class Exercise(TechioInteraction):
    
    PRINT_TEST_CASES = False
    CONTAINERS = ['list', 'tuple', 'set']

    def __init__(self, exercise_path, success_message=''):
        super().__init__(exercise_path)
        self.fixed_test_cases = []
        self.parameter_names = []
        self.num_random_test_cases = 0
        self.success_message = success_message.strip()
        self.first_failed_test_case = None
        self.floating_point_precision = 2

        self.solution_channel = Channel('Suggested Solution ✅', 'Sol✅>')

        # Import the user solution from exercise_name.py
        module = importlib.import_module(self.exercise_name)
        self.user_solution = getattr(module, self.exercise_name)

        # Import the suggested solution from exercise_name_solution.py
        module = importlib.import_module(self.exercise_name + '_solution')
        self.suggested_solution = getattr(module, self.exercise_name)

        # Self defaults for code size parameters to be tested.
        self.max_statement_count = 10_000_000
        self.max_lines_of_code = 10_000_000

        # Read all of exercise_name_solution.py into the suggested solution text.
        suggested_solution_filename = os.path.join(self.dir_path, f'{self.exercise_name}_solution.py')
        with open(suggested_solution_filename, 'r') as f:
            self.suggested_solution_text = f.read()


    def pluralize(self, count: int, label: str) -> str:
        return f'{count} {label}' + ('s' if count != 1 else '')
    

    def container_element_types(self, container) -> str:
        element_types = {self.data_type(element) for element in container}
        
        if len(element_types) > 1:
            return '[multiple types]'
        
        if len(element_types) == 1:
            return f'[{element_types.pop()}]'

        return '[]'
    
    
    def data_type(self, data) -> str:
        string = str(type(data)).split("'")[-2]
        
        if string in Exercise.CONTAINERS:
            string += self.container_element_types(data)
        
        if string == 'dict':
            key_types = self.container_element_types(data.keys())
            value_types = self.container_element_types(data.values())

            if len(data) == 0:
                string += '[]'
            else:
                string += f'[{key_types[1: -1]}, {value_types[1: -1]}]'
            
        return string


    def generate_random_test_case(self) -> list:
        print('THIS METHOD MUST BE OVERRIDDEN')
        return None


    def test_case_to_string(self, test_case) -> str:
        if len(self.parameter_names) != len(test_case):
            return  f'To use default test_case_to_string(), # of parameter names must be equal to # of test case arguments.\n' + \
                    f'   parameter names     = {len(self.parameter_names)}\n' + \
                    f'   test case arguments = {len(test_case)}'
        
        length = max([len(name) for name in self.parameter_names] + [0])

        strings = []
        for name, value in zip(self.parameter_names, test_case):
            if type(value) == str:
                value = f'{[value]}'[1:-1]

            strings.append(f'{name:{length}} = {value}')

        return '\n'.join(strings)

    
    def display_test_case(self, test_case) -> None:
        for line in self.test_case_to_string(test_case).split('\n'):
            self.send_msg(self.bug_channel, f'   {line}')


    def display_first_failed_test_case(self):
        expected_answer = self.generate_answer(self.suggested_solution, self.first_failed_test_case)
        user_answer = self.generate_answer(self.user_solution, self.first_failed_test_case)
            
        expected_answer_format = self.data_type(expected_answer)
        user_answer_format = self.data_type(user_answer)

        if expected_answer != user_answer:
        
            self.send_msg(self.bug_channel, 'First Failed Test Case:')
            self.send_msg(self.bug_channel, '')
            self.send_msg(self.bug_channel, f'Input:')
            self.send_msg(self.bug_channel, '')
            self.display_test_case(self.first_failed_test_case)
            self.send_msg(self.bug_channel, '')
            self.send_msg(self.bug_channel, f'Expected answer = {expected_answer}')
            self.send_msg(self.bug_channel, f'Your answer     = {user_answer}')
            self.send_msg(self.bug_channel, '')
            self.send_msg(self.bug_channel, f'Expected answer format = {expected_answer_format}')
            self.send_msg(self.bug_channel, f'Your answer format     = {user_answer_format}')
            self.send_msg(self.bug_channel, '')
            
            
    def generate_answer(self, solution, test_case):
        answer = solution(*deepcopy(test_case))

        if type(answer) == float:
            answer = round(answer, self.floating_point_precision)

        return answer


    def run_test_case(self, test_case):
        if Exercise.PRINT_TEST_CASES:
            print(f'{test_case=}')

        expected_answer = self.generate_answer(self.suggested_solution, test_case)
        user_answer = self.generate_answer(self.user_solution, test_case)

        expected_answer_format = self.data_type(expected_answer)
        user_answer_format = self.data_type(user_answer)

        if expected_answer_format != user_answer_format:
            if not self.first_failed_test_case:
                self.first_failed_test_case = test_case
            return False

        if expected_answer != user_answer:
            if not self.first_failed_test_case:
                self.first_failed_test_case = test_case
            return False

        return True


    def check_additional_solution_criteria(self):
        return ''
    

    def display_success_message(self):
        if self.success_message:
            self.send_multiline_text(self.success_channel, self.success_message)


    def display_solution(self):
        self.send_multiline_text(self.solution_channel, self.suggested_solution_text)


    def run(self):
        
        count = 0
        for test_case in self.fixed_test_cases:
            if self.run_test_case(test_case):
                count += 1

        self.send_msg(self.std_out_channel, f'{count} of {len(self.fixed_test_cases)} fixed test cases solved correctly.')
        
        count = 0
        for _ in range(self.num_random_test_cases):
            if self.run_test_case(self.generate_random_test_case()):
                count += 1

        if self.num_random_test_cases > 0:
            self.send_msg(self.std_out_channel, f'{count} of {self.num_random_test_cases} random test cases solved correctly.')

        if self.first_failed_test_case != None:
            self.fail()
            self.display_first_failed_test_case()
            return
        
        error_msg = ''
        learner_loc = self.code_analysis['effective_code_lines']
        if learner_loc > self.max_lines_of_code:
            learner_loc_string = self.pluralize(learner_loc, 'line')
            max_loc_string = self.pluralize(self.max_lines_of_code, 'line')
            error_msg = f'Your solution has {learner_loc_string} of code. To successsfully pass this exercise, '
            error_msg += f'your solution must be no more than {max_loc_string} of code.'

        if not error_msg:
            learner_statement_count = self.code_analysis['total_count']
            if learner_statement_count > self.max_statement_count:
                learner_statement_count_string = self.pluralize(learner_statement_count, 'Python statement')
                max_statement_count_string = self.pluralize(self.max_statement_count, 'Python statement')
                error_msg = f'Your solution has {learner_statement_count_string}. To successsfully pass this exercise, '
                error_msg += f'your solution must use no more than {max_statement_count_string}.'
                
        if not error_msg:
            error_msg = self.check_additional_solution_criteria()

        if error_msg:
            self.fail()

            msg = 'You have passed all test cases. However, your '
            msg += 'solution does not meet all the required criteria.\n\n' + error_msg
            self.send_multiline_text(self.bug_channel, msg)
            return

        self.success()
        self.display_success_message()
        self.display_solution()


IOEvent = namedtuple('Event', ['type', 'text', 'line_count'])

# This was created in hopes of handling both input and output. As of Sept 2025,
# Tech.io playgrounds cannot accomodate input from the learner.
class IOLog:

    def __init__(self):
        self.events = []
        self.strict = False


    def __len__(self):
        return len([event for event in self.events if event.type=='print'])
    

    def reset(self, strict=False):
        self.strict = strict
        self.events = []


    def add_event(self, _type, text):
        line_count = text.count('\n') + (0 if text.endswith('\n') else 1)

        if not self.strict and _type == "print":

            # collapse consecutive prints
            if self.events and self.events[-1].type == "print":
                prev_event = self.events[-1]
                combined_text = prev_event.text + text
                combined_lines = combined_text.count('\n') + (0 if text.endswith('\n') else 1)
                self.events[-1] = IOEvent(prev_event.type, combined_text, combined_lines)
                
                return
            
        self.events.append(IOEvent(_type, text, line_count))


    def num_lines_printed(self):
        return sum(event.line_count for event in self.events if event.type == 'print')


    def full_output(self):
        string = ''.join([event.text for event in self.events if event.type == 'print'])
        if string and string[-1] == '\n':
            string = string[:-1]

        return string


    def __eq__(self, other):
        if not isinstance(other, IOLog):
            return False
        
        # Compare events
        return self.events == other.events


class PrintBasedExercise(Exercise):

    def __init__(self, exercise_path, success_message=''):
        super().__init__(exercise_path, success_message)
        self.normal_print = builtins.print
        self.strict_print_usage = False
        self.log = IOLog()


    def logged_print(self, *args, **kwargs):
        sep = kwargs.get('sep', ' ')
        end = kwargs.get('end', '\n')
        text = sep.join(map(str, args)) + end

        if 'file' in kwargs and kwargs['file'] == sys.stderr:
            self.normal_print(*args, **kwargs)
        else:
            self.log.add_event('print', text)


    def generate_answer(self, solution, test_case) -> IOLog:
        builtins.print = self.logged_print
        self.log.reset(self.strict_print_usage)
        solution(*deepcopy(test_case))
        builtins.print = self.normal_print

        return deepcopy(self.log)


    def display_first_failed_test_case(self) -> None:
        expected_io_log = self.generate_answer(self.suggested_solution, self.first_failed_test_case)
        user_io_log = self.generate_answer(self.user_solution, self.first_failed_test_case)

        num_expected_calls_to_print = len(expected_io_log)
        num_user_calls_to_print = len(user_io_log)

        expected_answer_string = expected_io_log.full_output()
        user_answer_string = user_io_log.full_output()

        expected_answer = [] if not expected_answer_string else expected_answer_string.split('\n')
        user_answer = [] if not user_answer_string else user_answer_string.split('\n')

        num_expected_lines = expected_io_log.num_lines_printed()
        num_user_lines = user_io_log.num_lines_printed()
        verb = 'was' if num_expected_lines == 1 else 'were'

        expected_lines_str = self.pluralize(num_expected_lines, 'line')
        user_lines_str = self.pluralize(num_user_lines, 'line')

        msg = ''
        if num_user_calls_to_print > 0 and self.strict_print_usage and num_expected_calls_to_print != num_user_calls_to_print:
            expected_times_str = self.pluralize(num_expected_calls_to_print, 'time')
            learner_times_str = self.pluralize(num_user_calls_to_print, 'time')
            
            if expected_answer_string == user_answer_string:
                msg += 'The text you output is correct. However...\n\n'
            msg += f"Your solution called 'print' {learner_times_str}. "
            msg += f"The grader called 'print' {expected_times_str}.\n"

        if num_user_lines == 0:
            msg += f'You did not print anything. {expected_lines_str} of printed output {verb} expected.\n'

        elif num_expected_lines == 0:
            msg += f'No lines of printed output were expected. You printed {user_lines_str}.\n'

        elif expected_answer != user_answer:
            msg += ('\n' if msg else '') + 'First Failed Test Case:\n\n'

            msg += f'Your Output:'
            if num_expected_lines != num_user_lines:
                msg += f'   You printed {user_lines_str}. {expected_lines_str} {verb} expected.'

            msg += '\n\n'

            error_found = False
            while user_answer and expected_answer:
                user_line = user_answer.pop(0)
                expected_line = expected_answer.pop(0)

                msg += f'> {user_line}\n'
                if user_line == expected_line:
                    continue

                error_found=True
                msg += f'\nThere is a problem with the most recent line of output. '

                trailing_spaces = False
                if user_line.startswith(expected_line):
                    remaining_output = user_line[len(expected_line):]
                    if all(c.isspace() for c in remaining_output):
                        msg += f'It appears you have unnecessary trailing spaces at the end '
                        msg += f'of your output line.\n'
                        trailing_spaces = True

                if not trailing_spaces:
                    msg += f'It should have been...\n\n'
                    msg += f'> {expected_line}\n'

                break

            if not error_found:
                if len(expected_answer) == 0:
                    too_many = len(user_answer)
                    msg += f'\nYour answer should have ended with {expected_lines_str} printed. The following '
                    msg += f'{too_many} line{"s" if too_many > 1 else ""} should not have been printed.\n\n'

                    for line in user_answer:
                        msg += f'> {line}\n'

                if len(user_answer) == 0:
                    missing = len(expected_answer)
                    msg += f'\nYour answer is correct so far, but you are missing the following '
                    msg += f'{missing} line' + 's.'[missing == 1:] + '\n\n'

                    for line in expected_answer:
                        msg += f'> {line}\n'

        msg += f'\nInput:\n'
        self.send_multiline_text(self.bug_channel, msg)
        self.display_test_case(self.first_failed_test_case)


class ExerciseTemplate():

    def __init__(self, function_signature=''):
        self.syntax_tree = None
        self.type = 'Exercise'
        self.parameters = []
        self.function_signature = function_signature
        self.class_name = ''
        self.exercise_name = ''

    
    def check_function_definition(self, syntax_tree=None) -> str:
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
                syntax_tree = ast.parse(self.function_signature + "\n    pass")
            except SyntaxError as e:
                return f"Syntax error: {e}"

        self.syntax_tree = syntax_tree
        for node in ast.walk(self.syntax_tree):
            if isinstance(node, ast.FunctionDef):
                # Check function name
                if not re.fullmatch(r'[a-z0-9_]+', node.name):
                    return f"Invalid function name '{node.name}'. " + \
                           f"Only lowercase letters, digits, and underscores are allowed."

                # Check parameters
                for arg in node.args.args + node.args.kwonlyargs:
                    if arg.arg in self.parameters:
                        return f'All parameter names must be unique. \'{arg.arg}\' appears more than once.'
                    
                    self.parameters.append(arg.arg)
                    if arg.annotation is None:
                        return f"Parameter '{arg.arg}' is missing a type annotation."

                if node.name == 'exercise_name':
                    return f"Your function cannot be named 'exercise_name'."

                if node.args.vararg and node.args.vararg.annotation is None:
                    return f"Vararg parameter '*{node.args.vararg.arg}' is missing a type annotation."

                if node.args.kwarg and node.args.kwarg.annotation is None:
                    return f"Kwarg parameter '**{node.args.kwarg.arg}' is missing a type annotation."

                # Check return type
                if node.returns is None:
                    return f"Function '{node.name}' is missing a return type annotation."
                
                self.exercise_name = node.name
                self.class_name = node.name.replace('_', ' ').title().replace(' ', '')

                return_type = ast.unparse(node.returns)
                self.type = ['Exercise', 'PrintBasedExercise'][return_type == 'None']

                return ''
            
        return 'No function definition found.'
    

    def markdown_file(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            text = f.read().split('\n')

        return text
    

    def retrieve_text(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            file_text = f.read().split('\n')

        template = ''
        template_text = defaultdict(list)
        for line in file_text:
            if line.startswith('def'):
                template = ['Exercise', 'PrintBasedExercise'][line.endswith('None:')]
                line = self.function_signature

            if 'a, b' in line:
                line = line.replace('a, b', ', '.join(self.parameters))

            if template and (line == '' or line[0] != '#'):
                template_text[template].append(line)

        text = template_text[self.type]
        while text[-1] == '':
            text.pop()

        return text
    

    def retrieve_test_file(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            file_text = f.read().split('\n')

        text = []
        for line in file_text:
            if line.startswith('class'):
                template = ['Exercise', 'PrintBasedExercise'][line.endswith('PrintBasedExercise):')]
                if template != self.type:
                    continue

            if (idx := line.find("['a', 'b']")) != -1:
                params = ', '.join([f'{str([p])[1:-1]}' for p in self.parameters])
                line = line[:idx] + f'[{params}]'

            if 'a, b' in line:
                params = ', '.join(self.parameters)
                line = line.replace('a, b', params)

            target = 'random.randint(-100, 100)'
            if target in line:
                line = line.replace(', '.join([target] * 2), ', '.join([target] * len(self.parameters)))


            text.append(line.replace('ExerciseName', self.class_name))

        return text
