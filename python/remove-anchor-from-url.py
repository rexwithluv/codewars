""" Complete the function/method so that it returns the url with
anything after the anchor (`#`) removed.

## Examples

~~~if-not:nasm
```
"www.codewars.com#about" --> "www.codewars.com"
"www.codewars.com?page=1" -->"www.codewars.com?page=1"
```
~~~

~~~if:nasm
```
url1:  db    `www.codewars.com#about\0`
url2:  db    `www.codewars.com?page=1\0`
    
    mov rdi, url1
    call rmurlahr    ; RAX <- `www.codewars.com\0`
    
    mov rdi, url2
    call rmurlahr    ; RAX <- `www.codewars.com?page=1\0`
```
~~~ """


def remove_url_anchor(url: str) -> str:
    return url.rsplit("#")[0]
