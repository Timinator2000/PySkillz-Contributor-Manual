# Floating-Point Precision

When grading exercises that return floating point numbers, **tiny differences in precision can cause correct solutions to fail**. For example, due to the way floating point arithmetic works, a learner might return `3.14159` while the grader expects `3.14`, resulting in a mismatch even though the values are essentially equivalent.

To avoid this, all floating point results are rounded to a fixed number of decimal places before comparison. By default, this is **2 decimal places**, but you can customize this behavior by setting the `floating_point_precision` attribute in your exercise subclass constructor.

```python
self.floating_point_precision = 5
```

This rounding ensures that small, insignificant differences do not prevent otherwise correct solutions from passing, while still enforcing the desired level of precision.

# Complex Answers with Floating Points

By default, **only answers that consist of a single floating point number are automatically rounded** according to `floating_point_precision`. If your exercise returns more complex structures — such as tuples, lists, or dictionaries containing floats — you’ll need to handle rounding yourself.

For example, suppose you want learners to compute **both the circumference and the area of a circle**, returning a tuple of floating point numbers. In this case, you can override the `generate_answer` method and apply custom rounding to each value:

```python
class CalculateCircleCircumferenceAndArea(pyskillz_tools.Exercise):
    
    def generate_answer(self, solution, test_case):

        circumference, area = super().generate_answer(solution, test_case)

        return round(circumference, 5), round(area, 3)
```

This gives you full control over the precision of each element, ensuring that grading remains consistent even when multiple floating point values are involved.

<BR>

************

[![PySkillz](../../graphics/PySkillzFooter.png)](skillz-catalog)
