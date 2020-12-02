# sorted

Just a C command to check if a list of words is sorted by words length.

## Usage

To build the tool, just `make` it, it will create a `sorted` executable in your current directory.
You can then use the sorted command to check if a sentence is sorted.

```
    ./sorted [words]
```

## Exemple

If you want to check this sentence: "Another one got caught today, it's all over the papers."

You should do:
```
./sorted another one got caught today it s all over the papers
```

Which should exit with a return value of 0 or 1 if the words are sorted or not.

## Test

There are functionnal tests for the command, to play it, just `make test`.
