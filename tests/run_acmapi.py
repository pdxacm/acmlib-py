#!/bin/python2 
from acmapi import create_app, DB
from acmapi.models import Person, Officership
import datetime

app = create_app(SQLALCHEMY_DATABASE_URI='sqlite:///')

with app.test_request_context():
    DB.drop_all()
    DB.create_all()
    person = Person.create(
        name = None,
        username = 'root',
        email = None,
        website = None,
        password = '1234',
    )
    DB.session.add(person)
    DB.session.commit()

    officership = Officership.create(
        person = person,
        title = 'Root',        
        start_date = datetime.date.today(),
        end_date = None,
    )

    DB.session.add(person)
    DB.session.add(officership)
    DB.session.commit()

app.run()
