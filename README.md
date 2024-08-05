## airbnb_clone

#### To check for documenation
```python
# check module documentation
python3 -c 'print(__import__("my_module").__doc__)'
# check function documenation
python3 -c 'print(__import__("my_module").my_function.__doc__)'
# check class documentation
python3 -c 'print(__import__("my_module").MyClass.__doc__)'
# check method documenation
python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
```

### Running tests

```python
# running all tests
python3 -m unittest discover tests
#running individual tests
python3 -m unittest tests/[particular_test_directory]/[test_file.py]
```