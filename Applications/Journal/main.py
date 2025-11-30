# AppName: Journal            #
# Developer: C. Brycen Newell #

from datetime import datetime
import uuid
import json

class Entry:
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
	def __init__(self):
		self._entries = {}

	def add_entry(self, entry):
		self._entries[entry.entry_id] = entry
		# TODO: Autosave feature

	def get_entry(self, entry_id):
		if self._entries.get(entry_id) == None:
			raise ValueError("This is not a valid Entry ID")
		return self._entries.get(entry_id) 

	def find_by_title(self, search_title):
		results = []
		for entry in self._entries.values():
			if search_title.lower() in entry._title.lower():
				results.append(entry)
		return results 

	def find_by_date(self, search_date):
		results = []
		for entry in self._entries.values():
			if entry.date.date() == search_date.date():
				results.append(entry)
		return results

	def get_all_entries(self):
		return list(self._entries.values())

	def update_entry(self, entry_id, new_title=None, new_content=None):
		entry = self.get_entry(entry_id)
		if entry is None:
			return False

		if new_title is not None:
			entry.update_title(new_title)
		if new_content is not None:
			entry.update_content(new_content)
	
		# TODO: Autosave feature add 

		return True 

	def delete_entry(self, entry_id):
		if entry_id in self._entries:
			del self._entries[entry_id]
			# TODO, Autosave feature 
			return true 
		return False

	# dirty entry is an entry that has been updated and needs to be saved
	def list_dirty_entries(self):
		dirty_entries = []
		for entry in self._entries.values():
			if entry.is_dirty():
				dirty_entries.append(entry)
		return dirty_entries


# StorageManager is connection to db.
class StorageManager:
	def __init__(self, filename="journal_data.json"):
		self.filename = filename

	def save_journal(self, journal):
		try:
			# convert to dictionary format
			data = {}
			for entry_id, entry in journal._entries.items():
				data[entry_id] = {
					'title': entry._title,
					'content': entry._content,
					'date': entry.date.isoformat(),
					'entry_id': entry.entry_id
				}
			
			# -- TEMPORARY -- simulate write date to file
			json_output = json.dumps(data, indent=2)
			print("=== WOULD SAVE TO FILE ===")
			print(json_output)
			print("=== END FILE CONTENT ===")

			# Mark all entries as clean 
			for entry in journal._entries.values():
				entry.mark_clean()

			return True, "Save successful"
		
		except Exception as e:
			return False, f"Save failed: {str(e)}"
	
	def load_journal(self, journal):
		try:
			# -- TEMPORARY -- simulate loading
			simulated_data = {
				"test-id-123": {
					"title": "Loaded Entry",
					"content": "This entry was loaded from storage",
					"date": "2025-11-29T10:30:00.000000",
					"entry_id": "test-id-123"
				}
			}
		
			print("=== SIMULATING LOAD FROM FILE ===")
			print(json.dumps(simulated_data, indent=2))
		
			for entry_data in simulated_data.values():
				entry = Entry(entry_data['title'], entry_data['content'])
				#override auto gen ID and Date 
				entry.entry_id = entry_data['entry_id']
				entry.date = datetime.fromisoformat(entry_data['date'])
				entry.mark_clean()
				journal.add_entry(entry)

			return True, "Load successful"

		except Exception as e:
			return False, f"Load failed: {str(e)}"


# Interface is for UI concerns only
class Interface:
    pass
