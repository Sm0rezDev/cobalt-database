from file_system import FileSystem


class Cobalt:
    """
    This is the main class for Cobalt Database.
    This class provides methods to retrieve and save data to-and-from database.
    """

    def __init__(self, db_path: str, db_name: str):
        """
        Creates a database db object & copies data to a new dictionary.
        """
        self.fs = FileSystem(path=db_path, name=db_name)
        self.data = self.fs.data
        self.save = self.fs.save
        self.table = None

    # Set the database table to use.
    def select(self, table: str = 'DEFAULT'):
        if not (table and table.strip()):
            raise Exception('No table selected')
        
        self.table = table

    def fetch(self, key: str = None, val: str = None) -> list:
        """
        Retieve data from keys and values.
        Returns a list
        """
        data = self.data
        table = self.table

        items = []
        if not data.get(table):
            raise Exception('Table empty')

        for item in data.get(table, []):
            if isinstance(item, dict) and (not key or item.get('id') == int(key)):
                if val:
                    items.append(item.get(val))
                else:
                    items.append(item)
        return items

    def insert(self, item: dict = {}) -> None:
        """
        Inserts new data to table
        """
        data = self.data
        table = self.table
        save = self.save

        if not bool(item):
            raise Exception('No items where provided.')

        if not data.get(table):
            data[table] = [{'id': 1, **item}]
        else:
            data[table].append({
                'id': max(item['id'] for item in data.get(table)) + 1,
                **item
            })

        save()
        
        
