#importing the libraries
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import numpy
import re

import sqlite3
import pandas as pd
# Create your connection.
cnx = sqlite3.connect('blog.db')

df = pd.read_sql_query("SELECT * FROM blogpost ", cnx)
print(df)
print(df.iloc[0,1])