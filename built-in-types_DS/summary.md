# Dictionary

## Create a dictionary
```Python
dictionary = {
    key1: value1,
    key2: value2,
    key3: value3,
}
```

## Add a key or update the value of the key if already exist
```python
    dictionary[key] = value
```

## Add or update more than one key using update method
```python 
    dictionary.update({
        newkey = newvalue
        key = newvalue
    })
```

## Excess the value of a particular key 
```python
    dictionary[key] 
    dictionary.get(key, fallback)
```

## Getting list of keys or value
```python
    dictionary.keys()
    dictionary.values() 
```