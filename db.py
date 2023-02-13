from database import DB

db = DB("db.json")

db.insert({"name": "John Doe", "age": 30})
print(db.all())
# db.get("1")
# db.update("1", {"name": "Jane Doe", "age": 30})
# db.delete("1")
# db.delete_all()
