import uvicorn
from pymongo import MongoClient

ENTRY_POINT = 'app.api:app'
HOST = '0.0.0.0'
# TODO: configure AWS mongo host when deployed
MONGO_HOST = 'mongodb://localhost:27017/'
PORT = 8000

if __name__ == '__main__':
  client = MongoClient(MONGO_HOST)

  uvicorn.run(ENTRY_POINT, host=HOST, port=PORT, reload=True)