Optimization in progress...

```python


def calculate_sum(a, b):
    result = sum(i for i in range(a, b+1) if i % 2 == 0)
    return result


x = 1
y = 10
sum_of_evens = calculate_sum(x, y)
print(sum_of_evens)
```

Optimization complete! The code now uses a generator expression with the `sum()` function to calculate the sum of even numbers directly. This improves the efficiency and readability of the code.
