#! python3
#Create a simple Diary app.
from collections import OrderedDict
import datetime
import sys

from peewee import *


#Database file
db = SqliteDatabase('diary.db')

class Entry(Model):
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db

def initialize():
    """Create the database and the table if they don't exist."""
    db.connect()
    db.create_tables([Entry], safe=True)


def menu_loop():
    """Show the Menu."""
    choice = None

    while choice != 'q':
        print("\n--- Main menu ---")
        print("Enter 'q' to quit.")
        for key, value in menu.items():
            print('{}) {}'.format(key, value.__doc__)) #prints out the doctstring of the key value
        choice = input('Action: ').lower().strip()

        if choice in menu:
            menu[choice]() #Executes directly the function from the key value
                           # menu[a] = add_entry = add_entry()


def add_entry():
    """Add an entry."""
    entry = ""
    print("Log your idea, type 'done' when finished,")
    while True:
        data = input('> ')
        if data.lower() != 'done':
            entry += data + '\n'
        else:
            break

    # data = sys.stdin.read().strip()

    if entry:
        if input('Save entry? [Yn]').lower() != 'n':
            Entry.create(content=data)
            print("Saved Successfully!")

def view_entries(search_query=None):
    """View preivous entries."""
    entries = Entry.select().order_by(Entry.timestamp.desc())
    if search_query:
        entries = entries.where(Entry.content.contains(search_query))

    for entry in entries:
        timestamp = entry.timestamp.strftime(' %A %B %d, %Y %I: %M%p')
        print(timestamp)
        print('='*len(timestamp))
        print(entry.content)
        print('n) next entry')
        print('d) delete entry.')
        print('q) return to main menu')

        next_action = input("Action: [Ndq] ").lower().strip()
        if next_action == 'q':
            break
        elif next_action == 'd':
            delete_entry(entry)


def search_entries():
    """Search Entries."""
    view_entries(input('Search query: '))


def delete_entry(entry):
    """Delete an entry."""
    if input("Are you sure? [yN] ").lower() == 'y':
        Entry.delete_instance(entry)


#create an OrderedDict that has function values
menu = OrderedDict([
    ('a', add_entry),
    ('v', view_entries),
    ('s', search_entries)
])
if __name__ == "__main__":
    initialize()
    menu_loop()
