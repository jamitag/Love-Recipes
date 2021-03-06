import requests
import simpleSearch
import secrets
import random
import sys
from algorithm import Algorithm as A
from baseClasses import Search
from display import Recipes

key = str(secrets.ApiKey())

url = "https://api.spoonacular.com/recipes/"

text = input("What recipes would you like? ")

a = A(url, key)

try:
    search = a.search_by(text)
except:
    sys.exit()

res = Search.get(search)

r = Recipes(res)

id = r.select_recipe()

r.select_ingredients(id, url, key)

showInstructions = input("Show Instruction? Y/N - ")

if showInstructions.upper() == "Y":
    r.select_instructions(id, url, key)
