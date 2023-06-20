from note import Note
from notebook import Notebook
import datetime

class Presenter:
    def __init__(self):
        self.notebook = Notebook('notes.csv')

    def create(self):
        title = input('Enter title: ')
        body = input('Enter body: ')
        self.notebook.add(Note(title, body))

    def modify(self):
        id = int(input('Enter note ID to modify: '))
        title = input('Enter new title (or leave blank to keep the old one): ')
        body = input('Enter new body (or leave blank to keep the old one): ')
        self.notebook.modify(id, title, body)

    def remove(self):
        id = int(input('Enter note ID to remove: '))
        self.notebook.remove(id)

    def display(self):
        id = int(input('Enter note ID to display: '))
        note = self.notebook.get(id)
        print(note)

    def print_all(self):
        for note in self.notebook.all():
            print(note)

    def search_by_date(self):
        date_str = input('Enter date (YYYY-MM-DD): ')
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        for note in self.notebook.find_by_date(date):
            print(note)