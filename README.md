# Grammar Generator

## Description
A program that generates random grammatically correct phrases from a specified grammar. The file client.py demonstrates the use of the GrammarGenerator class. sentence.txt and simple.txt are sample grammar files written in standard BNF format (with '::=' as the separator symbol and '|' as the delimiter symbol), but any grammar format may be used.

## Usage
```python
grammar = gramgen.GrammarGenerator("sentence.txt", separator, delimiter)
"""
Creates an object that can generate phrases from the grammar specified in sentence.txt.
separator is the designated symbol that separates non-terminal symbols from rules.
delimiter is the designated symbol that separates multiple rules for a single non-terminal.
"""
```
```python
grammar.get_non_terminal_symbols()
"""
Returns a list of the non-terminal symbols for the grammar.

Output: [<s>, <np>, <dp>, <adjp>, <adj>, <n>, <pn>, <vp>, <tv>, <iv>]
"""
```
```python
grammar.set_rules("simple.txt", separator, delimiter)
"""
Replaces the grammar stored in the object with the grammar specified in simple.txt.
"""
```
```python
grammar.get_random_phrase(symbol)
"""
Generates a random phrase from the given grammar symbol and returns as a string.

Output: "the faulty big green cat"
"""
```