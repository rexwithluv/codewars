""" Create a function that returns the name of the winner in a fight
between two fighters.

Each fighter takes turns attacking the other and whoever kills the other
first is victorious. Death is defined as having `health <= 0`.

Each fighter will be a `Fighter` object/instance. See the Fighter class
below in your chosen language.

Both `health` and `damagePerAttack` (`damage_per_attack` for python)
will be integers larger than `0`. You can mutate the `Fighter` objects.

Your function also receives a third argument, a string, with the name of
the fighter that attacks first.

## Example:
```
    declare_winner(Fighter("Lew", 10, 2), Fighter("Harry", 5, 4), "Lew")
    => "Lew"
    
    Lew attacks Harry; Harry now has 3 health.
    Harry attacks Lew; Lew now has 6 health.
    Lew attacks Harry; Harry now has 1 health.
    Harry attacks Lew; Lew now has 2 health.
    Lew attacks Harry: Harry now has -1 health and is dead. Lew wins.
```

```javascript
function Fighter(name, health, damagePerAttack) {
        this.name = name;
        this.health = health;
        this.damagePerAttack = damagePerAttack;
        this.toString = function() { return this.name; }
}
```
```python
class Fighter(object):
        def __init__(self, name, health, damage_per_attack):
                self.name = name
                self.health = health
                self.damage_per_attack = damage_per_attack
                
        def __str__(self):
        return "Fighter({}, {}, {})".format(
            self.name,
            self.health,
            self.damage_per_attack
            )
        __repr__=__str__
```
```java
public class Fighter {
    public String name;
    public int health, damagePerAttack;
    public Fighter(String name, int health, int damagePerAttack) {
        this.name = name;
        this.health = health;
        this.damagePerAttack = damagePerAttack;
    }
}
```
```csharp
public class Fighter {
    public string Name;
    public int Health, DamagePerAttack;
    public Fighter(string name, int health, int damagePerAttack) {
        this.Name = name;
        this.Health = health;
        this.DamagePerAttack = damagePerAttack;
    }
}
```
```clojure
Technical note: The second fighter argument (f2) always attacks first.

(defrecord Fighter [name hp attack])
```
```cpp
class Fighter
{
private:
        std::string name;
        
        int health;
        
        int damagePerAttack;

public:
        Fighter(std::string name, int health, int damagePerAttack)
        {
                this->name = name;
                this->health = health;
                this->damagePerAttack = damagePerAttack;
        }
        
        ~Fighter() { };
        
        std::string getName()
        {
                return name;
        }
        
        int getHealth()
        {
                return health;
        }
        
        int getDamagePerAttack()
        {
                return damagePerAttack;
        }
        
        void setHealth(int value)
        {
                health = value;
        }
};
```
```go
type Fighter struct {
    Name            string
    Health          int
    DamagePerAttack int
}
``` """


class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack

    def __str__(self):
        return "Fighter({}, {}, {})".format(
            self.name, self.health, self.damage_per_attack
        )

    __repr__ = __str__


def attack(me, opponent):
    opponent.health -= me.damage_per_attack


def alive(me):
    return me.health > 0


def declare_winner(fighter1, fighter2, first_attacker):
    attacker = fighter1 if fighter1.name == first_attacker else fighter2
    defender = fighter1 if attacker == fighter2 else fighter2

    while alive(attacker) and alive(defender):
        attack(attacker, defender)
        attacker, defender = defender, attacker

    return attacker.name if alive(attacker) else defender.name


print(declare_winner(Fighter("Lew", 10, 2), Fighter("Harry", 5, 4), "Lew"))
