
import os

class VirtualFile:
    def __init__(self, name, content='', permissions='rw-r--r--', owner='user'):
        self.name = name
        self.content = content
        self.permissions = permissions
        self.owner = owner

class VirtualDirectory:
    def __init__(self, name):
        self.name = name
        self.files = {}

    def add_file(self, file):
        self.files[file.name] = file

    def get_file(self, name):
        return self.files.get(name, None)

root = VirtualDirectory('/')
root.add_file(VirtualFile('readme.txt', 'Welcome to ShellCoach!'))
