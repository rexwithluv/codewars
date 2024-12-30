"""ID: 5768a693a3205e1cc100071f

Some people just have a first name; some people have first and last
names and some people have first, middle and last names.

You task is to initialize the middle names (if there is any).

## Examples

```
'Jack Ryan'                   => 'Jack Ryan'
'Lois Mary Lane'              => 'Lois M. Lane'
'Dimitri'                     => 'Dimitri'
'Alice Betty Catherine Davis' => 'Alice B. C. Davis'
```"""


def initialize_names(name: str) -> str:
    full_name: str = name.split(" ")

    if len(full_name) < 3:
        return name

    return f'{full_name[0]} {" ".join(i[0] + "." for i in full_name[1:-1])} {full_name[-1]}'
