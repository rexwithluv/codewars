/* ID: 55e8aba23d399a59500000ce

```if:csharp
## Terminal Game - Create Hero Class

In this first kata in the series, you need to define a Hero class to be used in a terminal game. The hero should have the following attributes:

attribute | type | value
---|---|---
Name | string | user argument or "Hero"
Position | string | "00"
Health | float | 100
Damage | float | 5
Experience | int | 0
```

```if-not:csharp
## Terminal Game - Create Hero Prototype

In this first kata in the series, you need to define a Hero prototype to be used in a terminal game. The hero should have the following attributes:

attribute | value
---|---
name | user argument or 'Hero'
position | '00'
health | 100
damage | 5
experience | 0
``` */
package kata;

public class GrasshopperTerminalGameNumber1 {

    public class Hero {

        public String name;
        public String position;
        public int health;
        public int damage;
        public int experience;

        public Hero() {
            this.name = "Hero";
            this.position = "00";
            this.health = 100;
            this.damage = 5;
            this.experience = 0;
        }

        public Hero(String name) {
            this.name = name;
            this.position = "00";
            this.health = 100;
            this.damage = 5;
            this.experience = 0;
        }
    }
}
