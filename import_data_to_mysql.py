import os
from dotenv import load_dotenv
load_dotenv()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'imdb_django_scripx_app.settings')

import django
django.setup()

import pandas as pd
from sqlalchemy import create_engine
from app.models import IMDB

url = os.getenv('URL')
table_name = IMDB._meta.db_table


# Connect to MySQL server
engine = create_engine(url)

# Read CSV file into a pandas DataFrame
df = pd.read_csv('IMDb-movies.csv')

df.to_sql(table_name, engine, if_exists='replace', index=False)

# Close database connection
engine.dispose()

