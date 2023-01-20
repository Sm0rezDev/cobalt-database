import database


class Cobalt:
    """
    This is the main class for Cobalt Database.
    This class provides methods to retrieve and save data to-and-from database.
    """

    def __init__(self, db_path: str = 'db', db_name: str = 'cobalt'):
        """
        Creates a database db object & copies data to a new dict.
        """
        db = database.Database(f'{db_path}/{db_name}')
        self.data = db.data.copy()
        self.save = db.save
        self.table = None

    # Set the database table to use.
    def select_table(self, table: str = None) -> None:
        self.table = table

    # fetch data from database as list.
    def fetch(self, key: str = None, val: str = None) -> list:
        table: str = self.table
        data: dict = self.data

        if not table.strip():
            raise Exception('No table selected.')

        items = []
        for item in data.get(table, []):
            if isinstance(item, dict) and (not key or item.get('id') == key):
                if val:
                    items.append(item.get(val))
                else:
                    items.append(item)
        return items

    # Task #18 Work in Progress
    # def insert(self, val: str):
    #     table: str = self.table
    #     data: dict = self.data

    #     new_item = {'id': str(len(data)+1), }
    #     data[table].append(new_item)
        
