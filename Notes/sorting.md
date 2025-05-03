# Sorting algorithms
```python
    sorted(iterables, key=None, reverse=False)
```
The sorted() function returns a new sorted list from the elements of any iterable (like lists, tuples, etc.). The original iterable remains unchanged.

List of people and sorte them by theri age in ascending order and if ages are same then sorted them according to their comming order

Input format
``` 
people[i] = [name, age, comming order]
```

```pythton  
people = [['pari', 15, 5], ['Anna', 20, 4], ['jack', 21, 1], ['kishan', 23, 6], ['marry', 23, 2], ['jack', 32, 3]]
```

```python
sorted_people = sorted(people, key=lambda x: (x[1], x[2]))
```