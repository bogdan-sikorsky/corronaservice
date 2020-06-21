""" File contains global parameters of the project. """

from os import getenv

DATA_FILENAME = 'WHO-COVID-19-global-data.csv'
DATABASE_URL = getenv('DB_URL', 'postgres://postgres@postgres:5432/covid19')
BROKER_URL = getenv('MB_URL', 'amqp://guest:guest@rabbit:5672/')
CELERY_WORKERS = getenv('CELERY_WORKERS', 1)
DEBUG = getenv('DEBUG', '1') in {'1', 'true', 'True'}
