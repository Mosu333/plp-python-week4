# plp-python-week4
## Files
- grade_reporter.py - loops through a list of scores, assigns a grade to each using if/elif/else, and prints the pass count, fail count, and average.
- bug_hunt.py - a fixed version of a broken while-loop program that sums the numbers 1 to 5.

## Notes on Part B
This program had three bugs: a missing colon (SyntaxError), a string plus integer concatenation in the print statement (TypeError), and a loop condition that stopped one iteration too early. The hardest one to find was the loop condition, since it produced no error at all - the program just printed the wrong total (10 instead of 15). I only caught it by comparing the printed result against the expected answer of 15 rather than trusting that "it ran without crashing" meant it was correct.
