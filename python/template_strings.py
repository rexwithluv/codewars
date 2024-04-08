"""ID: 55a14f75ceda999ced000048

<h1>Template Strings</h1>
Template Strings, this kata is mainly aimed at the new JS ES6 Update
introducing Template Strings

<h3>Task</h3>
Your task is to return the correct string using the Template String
Feature.

<h3>Input</h3>
Two Strings, no validation is needed.

<h3>Output</h3>
You must output a string containing the two strings with the word ```'
are '```


Reference:
https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/template_strings
"""


def temple_strings(obj: str, feature: str) -> str:
    return f"{obj} are {feature}"
