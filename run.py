from app import app
from db import db

db.init_app(app)

#create db if not created
#removing space
@app.before_first_request
def create_tables():
	db.create_all()
