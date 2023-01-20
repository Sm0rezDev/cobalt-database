import pickle


class Database:
    """
    A class for saving and fetching python objects to and from a file on disk.
    The objects are saved and accessed via a key (of type str).
    """
    def __init__(self, file_path):
        """
        Initialize the database by loading the data from the file if it exists.
        If the file does not exist, create an empty file.
        """
        self.data = {}
        self.file_path = f'{file_path}_db.pkl'
        try:
            # Tries to read if file exist
            with open(self.file_path, "rb") as f:
                self.data = pickle.load(f)
        except FileNotFoundError:
            # If file doesnt exist, attempt to create one and initialize it
            # with empty dictionary.
            with open(self.file_path, "wb") as f:
                pickle.dump(self.data, f)

    # Write to disk
    def save(self, key, obj):
        """Save an object to the database with the given key."""
        self.data[key] = obj
        with open(self.file_path, "wb") as f:
            pickle.dump(self.data, f)
