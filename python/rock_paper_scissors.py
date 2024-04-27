"""ID: 5672a98bdbdd995fad00000f

# Rock Paper Scissors

Let's play! You have to return which player won! In case of a draw
return `Draw!`.

**Examples(Input1, Input2 --> Output):**

```
"scissors", "paper" --> "c"
"scissors", "rock" --> "Player 2 won!"
"paper", "paper" --> "Draw!"
```

![rockpaperscissors](http://i.imgur.com/aimOQVX.png)"""


def rps(p1: str, p2: str) -> str:
    rp1 = "Player 1 won!"
    rp2 = "Player 2 won!"

    if p1 == p2:
        return "Draw!"
    if p1 == "rock" and p2 == "paper":
        return rp2
    if p1 == "rock" and p2 == "scissors":
        return rp1
    if p1 == "paper" and p2 == "scissors":
        return rp2
    if p1 == "paper" and p2 == "rock":
        return rp1
    if p1 == "scissors" and p2 == "rock":
        return rp2
    if p1 == "scissors" and p2 == "paper":
        return rp1
