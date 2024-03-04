/* ID: 56d49587df52101de70011e4

You have to write a function that describe Leo:
```python
def leo(oscar):
  pass
```
```javascript
function leo(oscar) {

}
```
```elixir
def leo(oscar) do
  # ...
end
```

if oscar was (integer) 88, you have to return "Leo finally won the oscar! Leo is
happy".</br>
if oscar was 86, you have to return "Not even for Wolf of wallstreet?!"</br>
if it was not 88 or 86 (and below 88) you should return "When will you give Leo
an Oscar?"</br>
if it was over 88 you should return "Leo got one already!" */
package kata;

public class LeonardoDicaprioAndOscars {

    public static String leo(final int oscar) {
        if (oscar == 88) {
            return "Leo finally won the oscar! Leo is happy";
        } else if (oscar == 86) {
            return "Not even for Wolf of wallstreet?!";
        } else if (oscar < 88) {
            return "When will you give Leo an Oscar?";
        } else {
            return "Leo got one already!";
        }
    }
}
