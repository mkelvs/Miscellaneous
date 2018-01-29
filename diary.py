#! python3
#Create a simple Diary app.
from collections import OrderedDict
import datetime
from peewee import *

#Database file
db = SqliteDatabase('diary.db')

#create an OrderedDict that has function values
menu = OrderedDict([
    ('a', add_entry),
    ('v', view_entries),
])


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
        print("Enter 'q' to quit.")
        for key, value in menu.items():
            print('{}) {}'.format(key, value.__doc__)) #prints out the doctstring of the key value
        choice = input('Action: ').lower().strip()

        if choice in menu:
            menu[choice]() #Executes directly the function from the key value
                           # menu[a] = add_entry = add_entry()


def add_entry():
    """Add an entry."""

def view_entries():
    """View preivous entries."""

def delete_entry(entry):
    """Delete an entry."""

if __name__ == "__main__":
    initialize()
    menu_loop()