from note import Note
import csv
import os
import datetime

class Notebook:
    def __init__(self, filename):
        self.filename = filename
        self.notes = []
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    id, title, body, created_at, last_modified = row
                    note = Note(title, body)
                    note.note_id = int(id)
                    note.created_at = datetime.datetime.strptime(created_at, "%Y-%m-%d %H:%M:%S.%f")
                    note.last_modified = datetime.datetime.strptime(last_modified, "%Y-%m-%d %H:%M:%S.%f")
                    self.notes.append(note)
                    Note._id = max(Note._id, note.note_id + 1)

    def add(self, note):
        self.notes.append(note)
        self.save()

    def modify(self, id, title=None, body=None):
        for note in self.notes:
            if note.note_id == id:
                note.modify(title, body)
                self.save()
            else: print("Wrong id!")

    def remove(self, id):
        self.notes = [note for note in self.notes if note.note_id != id]
        self.save()

    def find_by_date(self, date):
        return [note for note in self.notes if note.created_at.date() == date]

    def get(self, id):
        for note in self.notes:
            if note.note_id == id:
                return note
        return None

    def all(self):
        return self.notes

    def save(self):
        with open(self.filename, 'w') as file:
            writer = csv.writer(file)
            for note in self.notes:
                writer.writerow([note.note_id, note.title, note.body, note.created_at, note.last_modified])
