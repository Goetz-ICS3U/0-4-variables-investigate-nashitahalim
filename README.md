[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=22615375&assignment_repo_type=AssignmentRepo)
# 0.4-variables-investigation
## Startup

1. Git clone the repository into Unit0, under Investigate
2. Create a new file called var_investigate.py
3. Copy / paste the below code into that file
4. Play around with the file

## Instructions
1. Change the **values** of all of the variable names so that the story reads a bit differently. DO NOT CHANGE ANYTHING IN THE PRINT FUNCTION YET
2. Add 3 new variables in the Input section and then add those variables to the story in the print function!


```python - copy code below
"""
author:
date:
Investigating Variables
"""

# Input
name = "Mr. Nguyen"
grade = 13
favourite_exclamation = "bruh"
least_favourite_colour = "yellow"
is_cool = True
math_test_score = 90.15
sister_name = None

slope = 2
y_intercept = 10
x = 3
y = slope * x + y_intercept

# Processing / Output
print(
    f"Hey guys, my name is {name} and I am currently in grade {grade}. "
    + f"Yesterday, there was a spider in the classroom that made me yell {favourite_exclamation} whiile I was taking a math test with my {least_favourite_colour} pen :/ "
    + f"One of the questions on the test was wether or not I thought Elvis was cool, so I obviously put {is_cool} to get the answer right... "
    + f"Turns out that I only scored a {math_test_score} on the test. One of the qusetions was asking me to write the equation for a line "
    + f"with a slope of {slope} and a y-intercept of {y_intercept} so I wrote y = {slope}x + {y_intercept}, but I did not notice the x value of {x} in the question "
    + f"so I needed to, on the next line, say that the value of y was {y}. "
    + f"I told my sister {sister_name} about this and she just laughed at me 🙄"
    + "Anyway, that's the story of my math test."
)
```
