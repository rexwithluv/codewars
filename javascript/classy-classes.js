/* ID: 55a144eff5124e546400005a

# Classy Classes

Basic Classes, this kata is mainly aimed at the new JS ES6 Update introducing classes

### Task

Your task is to complete this Class, the Person class has been created. You must fill in the Constructor method to accept a name as string and an age as number, complete the get Info property and getInfo method/Info getter which should return <code>johns age is 34</code>

```if:javascript
Reference: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes
```
```if:csharp
Reference: https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/using-properties
```
```if:python
Reference: https://docs.python.org/3/tutorial/classes.html
``` */

class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
        this.info = `${this.name}s age is ${this.age}`;
    }
}
