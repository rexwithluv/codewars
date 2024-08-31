/* ID: 56214b6864fe8813f1000019

## Terminal game bug squashing

You are creating a text-based terminal version of your favorite board game. In the board game, each turn has six steps that must happen in this order: roll the dice, move, combat, get coins, buy more health, and print status.

---

You are using a library that already has the functions below. Create a function named `main` that calls the functions in the proper order.

```javascript
- combat
- buyHealth
- getCoins
- printStatus
- rollDice
- move
```
```ruby
- `combat`
- `buy_health`
- `get_coins`
- `print_status`
- `roll_dice`
- `move`
```
```python
- `combat`
- `buy_health`
- `get_coins`
- `print_status`
- `roll_dice`
- `move`
```
```csharp
- `Combat`
- `BuyHealth`
- `GetCoins`
- `PrintStatus`
- `RollDice`
- `Move`
``` */

var health = 100
var position = 0
var coins = 0

function main() {
    rollDice();
    move();
    combat();
    getCoins();
    buyHealth();
    printStatus();
}