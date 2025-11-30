# AppName: Journal            #
# Developer: C. Brycen Newell #


import datetime
import uuid

# Data Container - recieves information from the Interface. Makes interface Entry available as an object to the Journal. 
class Entry:
	def __init__(self, title, content, entry_id=None, date=None, tags=None):
		self.title = title 
		self.content = content
		self.entry_id = str(uuid.uuid4()) # guaranteed global uniqueness
		self.date = datetime.datetime.now().isoformat()
		self.tags = None

	

# provides busines logic and state management (comparing running-config to startup-config for autosave feature)
class Journal:
	pass


# StorageManager is connection to db.
class StorageManager:
    pass

# Interface is for UI concerns only
class Interface:
    pass
