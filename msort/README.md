# Msort

This is an implementation of the "merge sort" algorithm in C for learning purpose.
It will be improved over time with my knowledge of C increasing.

It should:
- take a list of words separated by spaces as argument
- output a list of words separated by spaces and sorted by length
- be as performant as possible.
- be cross platform (windows, *nix)

## Usage

To build the tool, just `make` it, it will create an `msort` executable in your current directory.
You can the use the msort command to sort efficiently a bunch of words.

```
    ./msort [words]
```

## Exemple

If you want to sort this sentence: "Another one got caught today, it's all over the papers."

You should do:
```
./msort another one got caught today it s all over the papers
```

Which should output:
```
s it the all got one over today papers caught another
```

## Test

There are functionnal tests for the command, to play it, just `make test`.
