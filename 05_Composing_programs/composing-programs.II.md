# Review:

- OOP
- Functions

# Consider the following snippet:

    d = {1: 'hello', 2: 'goodbye'}
    d2 = {True:  "somestring", False: ""}
    if d2.pop(False):
        x = d.pop(1)
    else:
        x = d.pop(2)

1. What will be the value of `x`?
2. What will be the value of `d2`?

# Consider the following snippet:

    def map2(function, arguments):
        result_list = []
        for arg in arguments:
            result_list.append(function(arg))
        return result_list

    def square(n):
        return n * n

1. What will be the result of `map2(square, [1, 2, 3, 4, 5])`

# Consider the following snippet:

    def strange_loop(l):
        out = []

        for item in l:
            if item is None:  # `item is None` evaluates to True when item contains None
                return out
            out.append(item)

        return out

1. What will be the result of `strange_loop([1, 2, 5, 9, None, 3, 1, 1, None])`

# Comments & Docstrings

- What is the purpose of a docstring?
- What is the purpose of a comment?

#Let's write a script!

Requirements:

1. Download tab-delimited data file from `https://goo.gl/H0vV4x`
2. Reshape data into a dictionary whose keys are the column names and whose values
are the columns (in the form of a list).
3. Calculate mean response error for each SOAxCongruency condition
4. Eliminate outlier RT values, and calculate median RT for each SOAxCongruency condition
