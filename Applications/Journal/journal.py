# AppName: Journal            #
# Developer: C. Brycen Newell #


import datetime

# Entry should contain an entryid (generated on creation), a date, a title, and content. 
class Entry:
	def __init__(self, title, content, entry_id=None, date=None):
		self.title = title 
		self.content = content
		self.entry_id = id(self)
		self.date = datetime.datetime.now().isoformat()

	
	def display(self, date, title, content):
		print(f"Date: {self.date}")
		print(f"Title: {self.title}")
		print(f"Content:\n{self.content}")

	def __repr__(self):
		return "Entry('{}','{}','{}','{}'".format(self.title, self.content, self.entry_id, self.date)
		
## TODO: to_dictionary & from_dictionary


# journal should contain a collection of entries, and should interact with the storage manager to allow for CRUD actions
class Journal:
	def __init__(self, storage_manager):
		self.entries = {}
		self.storage_manager = storage_manager


# StorageManager is the connection to the MongoDB instance. It should connect, then allow for data manipulation
class StorageManager:
    pass

# Interface is the UI with which we'll be able to make interact with the journal object
class Interface:
    pass
