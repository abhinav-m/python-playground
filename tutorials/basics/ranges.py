# ranges are used for extracting number sequences from the number line.

# Usage 1 range(5) Prints numbers from 0 -> 4 (excludes value) shorthand for range(0,5) starting index is 0 by default
for x in range(5):
    print(x)

# Usage 2 range(1,5) same as above, we can specify a different starting index, which is INCLUDED in the iterable.
for x in range(1, 5):
    print(x)

# Usage 3 range(0,20,2) third argument is step value which will print all even numbers from 1 - 20 in this case.
for x in range(2, 21, 2):
    print(x)

# Usage 4 range(-10 , 0, 1) negative ranges can be used with a positive step value
for x in range(-10, 0, 1):
    print(x)
