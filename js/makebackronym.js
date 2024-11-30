/* ID: 55805ab490c73741b7000064

# back·ro·nym

> An acronym deliberately formed from a phrase whose initial letters spell out a particular word or words, either to create a memorable name or as a fanciful explanation of a word's origin.
>
> "Biodiversity Serving Our Nation", or BISON

*(from https://en.oxforddictionaries.com/definition/backronym)*

Complete the function to create backronyms. Transform the given string (without spaces) to a backronym, using the preloaded dictionary and return a string of words, separated with a single space (but no trailing spaces).

The keys of the preloaded dictionary are **uppercase** letters `A-Z` and the values are predetermined words, for example:

```javascript
dict["P"] == "perfect"
```
```python
dictionary["P"] == "perfect"
```
```ruby
$dict["P"] == "perfect"
```
```csharp
dict['P'] == "perfect"
```
```java
dictionary.get("P") == "perfect"
```
```haskell
dict 'P' == "perfect"
```


## Examples

```
"dgm" ==> "disturbing gregarious mustache"

"lkj" ==> "literal klingon joke"
``` */

function makeBackronym(string) {
    return [...string].map(l => dict[l.toUpperCase()]).join(" ");
}