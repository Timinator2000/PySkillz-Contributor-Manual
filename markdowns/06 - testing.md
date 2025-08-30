# Testing Your New Exercise

Since your GitHub branch isn’t linked to a playground, you’ll need to test your code locally. The directory structure shown below applies to step one.

📂 python-project<BR>
&nbsp;&nbsp;&nbsp;&nbsp;📂 tools<BR>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🗋 timinator_tools.py<BR>

1. Go to the `tools` directory and set RUNNING_ON_TECH_IO to False inside `timinator_tools.py`.

2. Code a solution in `exercise_name.py` just as a playground user would. Be sure to save your changes.

3. Run `exercise_name_test.py`.

When the exercise runs, you’ll see the same output that users see in the playground. The formatting is adjusted for terminal display, but the content is identical. On Tech.io, all output is sent to a “channel,” which Tech.io neatly organizes and presents. In your terminal, channels are shown on each output line, like this:

```text
Win🎉> Success Channel on Tech.io.
Bug🐞> Bug Channel on Tech.io.
Sol✅> Suggested Solution Channel on Tech.io.
StdOut> Standard Output Channel on Tech.io
```

Users of the playground are encouraged to print debug output to `sys.stderr`. On Tech.io, any output sent to `sys.stderr` is captured in a dedicated "Standard Error" panel. When testing locally, this output will follow your development environment's default behavior.

<BR>

************

[![Skillz Catalog](../graphics/PySkillzFooter.png)](skillz-catalog)
