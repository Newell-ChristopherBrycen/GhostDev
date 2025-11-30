# AppName: Journal            #
# Developer: C. Brycen Newell #


import datetime
import uuid

# Data Container - recieves information from the Interface. Makes interface Entry available as an object to the Journal. 
class Entry:
	# Constructor and core data
from datetime import datetime
import uuid

class Entry():
    def __init__(self, title="", content="" ):
        # Immutable fields
        self.entry_id = str(uuid.uuid4())
        self.date = datetime.now()
        
        # Mutable Fields
        self._title = title
        self._content = content
        
        # State tracking
        self._dirty = False
        

    def update_title(self, new_title):
        if len(new_title) > 20:
            raise ValueError("Title is too long - max 20 characters")
        self._title = new_title
        self.mark_dirty()

    def update_content(self, new_content):
        if len(self.new_content) > 200:
            raise ValueError("Content is too long - max 200 characters")
        self._content = new_content
        self.mark_dirty()

    def mark_dirty(self):
        self._dirty = True

    def is_dirty(self):
        return self._dirty

    def mark_clean(self):
        self._dirty = False 

    def get_summary(self):
        if len(self._content) <= 50:
            return self._content
        else:
            return self._content[:50] + "..."


# provides busines logic and state management (comparing running-config to startup-config for autosave feature)
class Journal:
	pass


# StorageManager is connection to db.
class StorageManager:
    pass

# Interface is for UI concerns only
class Interface:
    pass
