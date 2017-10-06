from bs4 import BeautifulSoup
import requests
import os
import pandas as pd

def get_name_year_ext(original):
    name_and_year, extension = original.split(".")
    movie_name, movie_year = name_and_year.split("(")
    movie_name = movie_name.strip()
    movie_year = movie_year.strip(")")
    return movie_name, movie_year, extension

# from https://stackoverflow.com/questions/32380631/using-os-walk-in-python
path = r"D:\External Hard Drive Videos\Movies & Films\Testing Python"
for root, dirs, files in os.walk(path):  # parse through file list in the current directory
    for filename in files:
        if filename[-4:] is not ".srt": # I want to make this exclude .srt files, but it isn't working
            print(get_name_year_ext(filename))
