# Symbols
These are patterns in the charts that are recorded for the Hidden Markov Model. A symbol consists of 3 separate parts:
1. Name: The symbol's name
2. Code: A shortened variant of the symbol's name used by the model
3. Pattern: Actual inputs that makes up the symbol

## Defining a symbol
```
// C-style comments are allowed
# [NAME], [CODE]
[PATTERN]
```

## Patterns
These are the actual inputs that define the symbol. Patterns are built upon the base inputs of maimai these being TAP, HOLD, SLIDE, TOUCH, and TOUCH HOLD. Additionally, there are the base modifiers that can be applied to these notes: EX, BREAK, EACH. Lastly there is the positional element of these inputs that are enclosed in square braces (`[]`) next to the note type.

Note Types:
1. TAP &rarr; `t`
2. HOLD &rarr; `h`
3. SLIDE &rarr; `s`
4. SLIDE track &rarr; `>`
5. TOUCH &rarr; `x`
6. TOUCH HOLD &rarr; `+`
7. Any note type &rarr; `n`

Modifiers:
1. EX &rarr; `x`
2. BREAK &rarr; `b`
3. EACH &rarr; `{n | n}`

Position:
1. `n[pos]` &rarr; note at position `pos` (Example: `n[1]` is a note at position 1)
2. `n[x]` &rarr; save note position to `x`
3. `n[*]` &rarr; note at any position
