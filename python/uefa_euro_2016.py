"""ID: 57613fb1033d766171000d60

Finish the uefaEuro2016() function so it return string just like in the examples below:
```javascript
uefaEuro2016(['Germany', 'Ukraine'],[2, 0]) // "At match Germany - Ukraine, Germany won!"
uefaEuro2016(['Belgium', 'Italy'],[0, 2]) // "At match Belgium - Italy, Italy won!"
uefaEuro2016(['Portugal', 'Iceland'],[1, 1]) // "At match Portugal - Iceland, teams played draw."
```

```python
uefa_euro_2016(['Germany', 'Ukraine'],[2, 0]) # "At match Germany - Ukraine, Germany won!"
uefa_euro_2016(['Belgium', 'Italy'],[0, 2]) # "At match Belgium - Italy, Italy won!"
uefa_euro_2016(['Portugal', 'Iceland'],[1, 1]) # "At match Portugal - Iceland, teams played draw."
```

```ruby
uefa_euro_2016(['Germany', 'Ukraine'],[2, 0]) # "At match Germany - Ukraine, Germany won!"
uefa_euro_2016(['Belgium', 'Italy'],[0, 2]) # "At match Belgium - Italy, Italy won!"
uefa_euro_2016(['Portugal', 'Iceland'],[1, 1]) # "At match Portugal - Iceland, teams played draw."
```"""


def uefa_euro_2016(teams: list[str], scores: list[int]) -> str:
    string = f"At match {' - '.join(teams)}, "
    if scores[0] > scores[1]:
        string += f"{teams[0]} won!"
    elif scores[1] > scores[0]:
        string += f"{teams[1]} won!"
    else:
        string += "teams played draw."

    return string
