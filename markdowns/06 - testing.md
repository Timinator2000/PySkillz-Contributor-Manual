# Testing Your New Exercise

Since your GitHub branch isn’t linked to the playground yet, you can only test your code locally using this simple two-step process.

* Write the solution as a learner would

  * Code a solution in `exercise_name.py` just as a playground user would.

  * Be sure to __save your changes__ before running tests.

* Run the exercise tests

  * Run `exercise_name_test.py` in your terminal.

  * When the exercise runs, you’ll see the __same output that users see in the playground__.

  * Formatting is slightly adjusted for terminal display, but the __content is identical__.

Example terminal output:

```text
Win🎉> Success Channel on Tech.io.
Bug🐞> Bug Channel on Tech.io.
Sol✅> Suggested Solution Channel on Tech.io.
StdOut> Standard Output Channel on Tech.io
```

__Channels: Terminal vs Tech.io__

* In the __playground__, Tech.io organizes output into neat, separate channels: Success, Bug, Suggested Solution, and Standard Output.

* Locally, these channels are __simulated in the terminal__ by prefixing each line with the channel name and a symbol (e.g., `Win🎉>`, `Bug🐞>`, `Sol✅>`, `StdOut>`).

* This ensures that the __same information is visible locally__, even if the formatting isn’t as polished as Tech.io.

* Any debug output sent to `sys.stderr` will follow your terminal’s default behavior locally, while Tech.io captures it in a dedicated __Standard Error__ panel.

<BR>

************

[![Skillz Catalog](../graphics/PySkillzFooter.png)](skillz-catalog)
