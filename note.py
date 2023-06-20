import datetime

# Заметка должна содержать идентификатор, заголовок, тело заметки 
# и дату/время создания или последнего изменения заметки.

class Note:
    _id = 0
    def __init__(self, title, body):
        self.note_id = Note._id
        self.title = title
        self.body = body
        self.created_at = datetime.datetime.now().replace(microsecond=0)
        self.last_modified = self.created_at
        Note._id += 1

    def modify(self, title=None, body=None):
        if title:
            self.title = title
        if body:
            self.body = body
        self.last_modified = datetime.datetime.now().replace(microsecond=0)

    def __str__(self):
        return f"ID: {self.note_id}\nTitle: {self.title}\nBody: {self.body}\nCreated at: {self.created_at}\nLast modified: {self.last_modified}"