from flask import Flask, render_template, request
import re

app = Flask(__name__)

# Code Review Function
def review_code(code):

    suggestions = []

    # Check Long Lines
    lines = code.split("\n")

    for i, line in enumerate(lines):

        if len(line) > 80:

            suggestions.append(
                f"Line {i+1}: "
                "Line exceeds 80 characters."
            )

    # Check Print Statements
    if "print(" in code:

        suggestions.append(
            "Avoid unnecessary print statements "
            "in production code."
        )

    # Check TODO Comments
    if "TODO" in code:

        suggestions.append(
            "TODO comments found. "
            "Complete pending tasks."
        )

    # Check Variable Naming
    variable_pattern =
        r'\b[a-zA-Z]{1}\b'

    if re.search(variable_pattern, code):

        suggestions.append(
            "Use meaningful variable names."
        )

    # Check Empty Suggestions
    if not suggestions:

        suggestions.append(
            "Code looks clean and optimized."
        )

    return suggestions

# Home Page
@app.route('/', methods=['GET', 'POST'])
def index():

    suggestions = []

    code = ""

    if request.method == 'POST':

        code = request.form['code']

        suggestions = review_code(code)

    return render_template(
        'index.html',
        suggestions=suggestions,
        code=code
    )

if __name__ == '__main__':
    app.run(debug=True)
