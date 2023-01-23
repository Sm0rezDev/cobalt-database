# cobalt-database

A school group project

A very simple database library written in Python

Basic usage:

```python
from cobalt import Cobalt

cobalt = Cobalt(db_path='db', db_name='cobalt') # Init cobalt

cobalt.select(str) # Selects the table to use

cobalt.insert(dict) # Inserts data to table

cobalt.fetch(str, str) -> list # Retrieve data as list from keys (row, column)
```

