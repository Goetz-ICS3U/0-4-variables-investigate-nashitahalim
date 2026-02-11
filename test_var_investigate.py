import re
import sys
import io

def test_header_comments():
    """Test that student included author and date in header comments"""
    try:
        with open("var_investigate.py", encoding="utf-8") as f:
            kids_code = f.read()
    except FileNotFoundError:
        raise AssertionError("Could not find var_investigate.py file. Make sure the file is named correctly.")
    
    # Get first 500 characters to check header
    header = kids_code[:500]
    
    # Check for author comment
    has_author = bool(re.search(r'author\s*:', header, re.IGNORECASE))
    assert has_author, "Missing 'author:' in header comments. Please add your name in the header."
    
    # Check for date comment
    has_date = bool(re.search(r'date\s*:', header, re.IGNORECASE))
    assert has_date, "Missing 'date:' in header comments. Please add the date in the header."
    
    # Check that author is not empty or still the default
    author_match = re.search(r'author\s*:\s*(.+)', header, re.IGNORECASE)
    if author_match:
        author_value = author_match.group(1).strip()
        assert author_value and author_value.lower() not in ['', 'mr. habib', 'student name'], \
            "Please fill in your actual name for 'author:' in the header"


def test_var_count():
    """Test that student added at least 3 new variables (minimum 14 total: 11 original + 3 new)"""
    try:
        with open("var_investigate.py", encoding="utf-8") as f:
            kids_code = f.read()
    except FileNotFoundError:
        raise AssertionError("Could not find var_investigate.py file. Make sure the file is named correctly.")
    
    # Count all the variables in their code
    found = re.findall(r"^[a-zA-Z_][a-zA-Z0-9_]* ?=", kids_code, re.MULTILINE)
    # Filter out variables inside strings or comments
    # This is a simple check - students shouldn't have assignments in strings for this exercise
    
    assert len(found) >= 14, f"Expected at least 14 variables (11 original + 3 new), but found {len(found)} variables"


def test_story_changed(capsys):
    """Test that student changed at least one variable value"""
    try:
        # Capture the output from running the student's code
        import var_investigate
    except ModuleNotFoundError:
        raise AssertionError("Could not import var_investigate.py. Make sure the file is named correctly.")
    except Exception as e:
        raise AssertionError(f"Error running var_investigate.py: {str(e)}")
    
    captured = capsys.readouterr()
    
    # Original story (with the typos from the original)
    original_story = (
        "Hey guys, my name is Mr. Nguyen and I am currently in grade 13. "
        "Yesterday, there was a spider in the classroom that made me yell bruh whiile I was taking a math test with my yellow pen :/ "
        "One of the questions on the test was wether or not I thought Elvis was cool, so I obviously put True to get the answer right... "
        "Turns out that I only scored a 90.15 on the test. One of the qusetions was asking me to write the equation for a line "
        "with a slope of 2 and a y-intercept of 10 so I wrote y = 2x + 10, but I did not notice the x value of 3 in the question "
        "so I needed to, on the next line, say that the value of y was 16. "
        "I told my sister None about this and she just laughed at me 😔"
        "Anyway, that's the story of my math test.\n"
    )
    
    # Make sure they changed at least one variable value
    assert captured.out != original_story, "You must change at least one variable value to create a different story"
    
    # Verify that the output is not empty
    assert len(captured.out) > 0, "Your program should print output"


def test_new_variables_used():
    """Test that the 3 new variables are actually used in the print statement"""
    try:
        with open("var_investigate.py", encoding="utf-8") as f:
            kids_code = f.read()
    except FileNotFoundError:
        raise AssertionError("Could not find var_investigate.py file.")
    
    # Find all variables defined
    all_vars = re.findall(r"^([a-zA-Z_][a-zA-Z0-9_]*) ?=", kids_code, re.MULTILINE)
    
    # Original 11 variables
    original_vars = {
        'name', 'grade', 'favourite_exclamation', 'least_favourite_colour',
        'is_cool', 'math_test_score', 'sister_name', 'slope', 'y_intercept', 'x', 'y'
    }
    
    # Find new variables (those not in the original set)
    new_vars = [v for v in all_vars if v not in original_vars]
    
    assert len(new_vars) >= 3, f"You should add at least 3 new variables. Found {len(new_vars)} new variables."
    
    # Check that at least some new variables are used in the print statement
    # Find the print statement
    print_match = re.search(r'print\((.*?)\)', kids_code, re.DOTALL)
    if print_match:
        print_content = print_match.group(1)
        # Check if any new variables are referenced in the print statement
        used_new_vars = [v for v in new_vars if f"{{{v}}}" in print_content or f'{{" + {v} + "}}' in print_content]
        assert len(used_new_vars) > 0, "You should use at least one of your new variables in the print statement"


if __name__ == "__main__":
    # This allows running the tests directly
    import pytest
    sys.exit(pytest.main([__file__, "-v"]))
