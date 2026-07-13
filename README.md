# Greeting CLI

A small command-line program that accepts a name and prints a friendly greeting.

## Requirements

- Python 3.9 or newer

No secrets or credentials are required.

## Usage

Run the program with a name:

```bash
python3 greet.py Ada
```

Output:

```text
Hello, Ada! Nice to meet you.
```

If you omit the name, it greets `friend`:

```bash
python3 greet.py
```

You can also customize the greeting word:

```bash
python3 greet.py --greeting Hi Kota
```

Output:

```text
Hi, Kota! Nice to meet you.
```

## Tests

Run the automated tests from this directory:

```bash
python3 -m unittest -v
```
