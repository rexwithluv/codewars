/* ID: 5c44b0b200ce187106452139

Write a function that returns the number of arguments it received.

```
args_count() --> 0
args_count('a') --> 1
args_count('a', 'b') --> 2
```


```if:python,ruby
The function must work for keyword arguments too:
```

```if:python
~~~
args_count(x=10, y=20, 'z') --> 3
~~~
```

```if:ruby
~~~
args_count(x:10, y:20, 'z') --> 3
~~~
``` */

const args_count = (...args) => args.length;