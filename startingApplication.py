from Database import Database
from menu import Menu
from models.blog import Blog

__author__ = 'samiurrahman98'

Database.initialize()

menu = Menu()

menu.run_menu()
