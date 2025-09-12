# Last Edited: Sept 12, 2025 9:55am

from copy import deepcopy
from collections import namedtuple, Counter
import builtins
import sys
import os
import random
import importlib
import ast


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


class Exercise(TechioInteraction):
    
    PRINT_TEST_CASES = False
    CONTAINERS = ['list', 'tuple', 'set']

    def __init__(self, exercise_path, success_message):
        super().__init__(exercise_path)
        self.fixed_test_cases = []
        self.num_random_test_cases = 0
        self.success_message = success_message.strip()
        self.first_failed_test_case = None

        self.success_channel = Channel(f'{random.choice(CONGRATS)} {random.choice(CONGRATS_EMOJIS)}', 'Win🎉>')
        self.bug_channel = Channel(f'{random.choice(BUG)} {random.choice(BUG_EMOJIS)}', 'Bug🐞>')
        self.solution_channel = Channel('Suggested Solution ✅', 'Sol✅>')
        self.std_out_channel = Channel('Standard Output', 'StdOut>')

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
        print('THIS METHOD MUST BE OVERRIDDEN')
        return None

    
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
        return solution(*deepcopy(test_case))

                
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


    def check_additonal_solution_criteria(self):
        return ''


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
                
        error_msg = self.check_additonal_solution_criteria()
        if error_msg:
            self.fail()

            msg = 'You have passed all test cases. However, your '
            msg += 'code does not meet all the required criteria.\n\n' + error_msg
            self.send_multiline_text(self.success_channel, msg)
            return

        self.success()
        self.send_multiline_text(self.success_channel, self.success_message)
        self.send_multiline_text(self.solution_channel, self.suggested_solution_text)


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

    def __init__(self, exercise_path, success_message):
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

        num_expected_lines = len(expected_answer)
        num_user_lines = len(user_answer)
        verb = 'was' if num_expected_lines == 1 else 'were'

        expected_lines_str = f'{num_expected_lines} line' + ('s' if num_expected_lines != 1 else '')
        user_lines_str = f'{num_user_lines} line' + ('s' if num_user_lines != 1 else '')

        msg = ''
        if num_user_calls_to_print > 0 and self.strict_print_usage and num_expected_calls_to_print != num_user_calls_to_print:
            word_expected = 'time' if num_expected_calls_to_print == 1 else 'times'
            word_user = 'time' if num_user_calls_to_print == 1 else 'times'
            
            if expected_answer_string == user_answer_string:
                msg += 'The text you output is correct. However...\n'
            msg += f"Your code called 'print' {num_user_calls_to_print} {word_user}. "
            msg += f"The grader called 'print' {num_expected_calls_to_print} {word_expected}.\n"

        if num_user_lines == 0:
            msg += f'You did not print anything. {expected_lines_str} of printed output {verb} expected.\n'

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



