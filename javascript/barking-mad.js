/* ID: 54dba07f03e88a4cec000caf

Teach snoopy and scooby doo how to bark using object methods.
Currently only snoopy can bark and not scooby doo.

```javascript
snoopy.bark(); // return "Woof"
scoobydoo.bark(); // undefined
```
```python
snoopy.bark() #return "Woof"
scoobydoo.bark() #undefined
```
```ruby
snoopy.bark() #return "Woof"
scoobydoo.bark() #doesn't work yet
```
Use method prototypes to enable all Dogs to bark. */

class Dog {
    constructor(breed) {
        this.breed = breed;
    }
}

Dog.prototype.bark = () => "Woof";

let snoopy = new Dog("Beagle");
let scoobydoo = new Dog("Great Dane");
