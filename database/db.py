import json

class DB:
    """Database class"""
    
    def __init__(self, path: str) -> None:
        """Initialize the database connection"""
        try:
            f = open(path)
            self.file = f
            if f.read() == "":
                self.data = []
            else:
                self.data = json.load(f)
        except FileNotFoundError:
            f = open(path, "x")
            self.file = f
            self.data = []

    def insert(self, data: dict) -> None:
        """Insert data into the database"""
        self.data.append(data)
        json.dump(self.data, self.file, indent=4)

    def all(self) -> list:
        """Get all data from the database"""
        return self.data

    def get(self, id: str) -> dict:
        """Get data from the database"""
        pass

    def update(self, id: str, data: dict) -> None:
        """Update data in the database"""
        pass

    def delete(self, id: str) -> None:
        """Delete data from the database"""
        pass

    def delete_all(self) -> None:
        """Delete all data from the database"""
        pass
