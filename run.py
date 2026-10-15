"""Main file of our application.

When ran with:
$ python run.py
it will reset the database and start the webserver.
"""

from todo import app, db
    
with app.app_context():
    db.drop_all()
    db.create_all()

app.run(host="0.0.0.0", port=5000)
