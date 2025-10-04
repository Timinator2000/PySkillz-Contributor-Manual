# Test Case to String

When a learner’s solution fails, the **first failed test case** is displayed to help them debug their code. By default, test cases are shown in a simple **parameter = value** format, like this:

```text
param_1 = 4
param_2 = 5
param_3 = 6
```

Sometimes, though, this default format isn’t the clearest way to present the input. If you’d like to display the test case in a more meaningful or structured way, you can override the `test_case_to_string` method and return a custom string.

For example, suppose your exercise asks learners to compute the **distance between two points**. Each test case includes four parameters: `x1`, `y1`, `x2`, and `y2`. By default, the test case would be displayed as:

```text
x1 = 4
y1 = 5
x2 = 10
y2 = 11
```

You might prefer to group the coordinates for clarity:

```text
(x1, y1) = (4, 5)
(x2, y2) = (10, 11)
```

To achieve this, simply override the `test_case_to_string` method:

```python
def test_case_to_string(self, test_case) -> str:
    x1, y1, x2, y2 = test_case
    return f'(x1, y1) = {(x1, y1)}\n(x2, y2) = {(x2, y2)}'
```

This customization makes the feedback clearer and more tailored to the problem you’re presenting.

<BR>

************

[![PySkillz](../../graphics/PySkillzFooter.png)](skillz-catalog)
