from django.contrib import admin


class Table(object):
    def __init__(self, name, db, size):
        self.name = name
        self.db = db
        self.size = size
