"""ID: 5700c9acc1555755be00027e

Input:

- a string `strng`
- an array of strings `arr`

Output of function `contain_all_rots(strng, arr) (or containAllRots or
contain-all-rots)`:

- a boolean `true` if all rotations of `strng` are included in `arr`
- `false` otherwise

#### Examples:
```
contain_all_rots(
  "bsjq", ["bsjq", "qbsj", "sjqb", "twZNsslC", "jqbs"]) -> true

contain_all_rots(
  "Ajylvpy", ["Ajylvpy", "ylvpyAj", "jylvpyA", "lvpyAjy", "pyAjylv",
  "vpyAjyl", "ipywee"]) -> false)
```

#### Note:
Though not correct in a mathematical sense

- we will consider that there are no rotations of `strng == ""`
- and for any array `arr`: `contain_all_rots("", arr) --> true`

Ref: <https://en.wikipedia.org/wiki/String_(computer_science)#Rotations>

```if:shell
## Bash:
For bash the array is replaced by a string (see "RUN sample tests").
```"""

from typing import List


def contain_all_rots(string: str, arr: List[str]) -> bool:
    # Create all real rots
    real_all_rots = set([string[i:] + string[:i] for i in range(len(string))])

    for i in arr:
        if i in real_all_rots:
            real_all_rots.remove(i)

    return True if len(real_all_rots) == 0 else False
