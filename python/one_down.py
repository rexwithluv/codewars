""" A very passive-aggressive co-worker of yours was just fired. While
he was gathering his things, he quickly inserted a bug into your system
which renamed everything to what looks like jibberish. He left two notes
on his desk, one reads:
"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz" while the other
reads: "Uif usjdl up uijt lbub jt tjnqmf kvtu sfqmbdf fwfsz mfuufs xjui
uif mfuufs uibu dpnft cfgpsf ju".

Rather than spending hours trying to find the bug itself, you decide to
try and decode it.

If the input is not a string, your function must return "Input is not a
string". Your function must be able to handle capital and lower case
letters. You will not need to worry about punctuation. """


def one_down(txt: str) -> str:
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    if isinstance(txt, str):
        msg = ""
        for i in txt:
            if i in uppercase:
                msg += uppercase[uppercase.index(i) - 1]
            elif i in lowercase:
                msg += lowercase[lowercase.index(i) - 1]
            else:
                msg += i
        return msg
    return "Input is not a string"
