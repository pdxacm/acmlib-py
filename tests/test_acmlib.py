import unittest
import datetime
import os
from acmapi import create_app, DB
from acmapi.models import Person, Officership
from acmlib import AcmLib
import subprocess
import time

class test_acmlib(unittest.TestCase):

    def setUp(self):

        self.process = subprocess.Popen(['python2', 'tests/run_acmapi.py'])

        time.sleep(1)

        self.lib = AcmLib('root', '1234', 'http://localhost:5000/')
    
    def tearDown(self):

        self.process.terminate()

    def test_init_get_person(self):

        person = self.lib.get_person(1)

        self.assertEqual(person.id, 1)         
        self.assertIsNone(person.name)         
        self.assertEqual(person.username, 'root')         
        self.assertIsNone(person.website)         
        self.assertIsNone(person.email)         

    def test_init_get_unknown_person(self):
        
        try:
            self.lib.get_person(2)
        except LookupError as e:
            pass
        else:
            raise Exception()

    def test_init_get_people(self):
        
        people = self.lib.get_people()

        self.assertEqual(len(people), 1)
        
        person = people[0]

        self.assertEqual(person.id, 1)         
        self.assertIsNone(person.name)         
        self.assertEqual(person.username, 'root')         
        self.assertIsNone(person.website)         
        self.assertIsNone(person.email)         

    def test_init_get_membership(self):
        
        try:
            self.lib.get_membership(1)
        except LookupError as e:
            pass
        else:
            raise Exception()

    def test_init_get_memberships(self):
        
        memberships = self.lib.get_memberships()

        self.assertEqual(len(memberships), 0)

    def test_init_get_events(self):
        
        events = self.lib.get_events()

        self.assertEqual(len(events), 0)

    def test_init_get_event(self):
        
        try:
            self.lib.get_event(1)
        except LookupError as e:
            pass
        else:
            raise Exception()

    def test_init_get_posts(self):
        
        posts = self.lib.get_posts()

        self.assertEqual(len(posts), 0)

    def test_init_get_post(self):
        
        try:
            self.lib.get_post(1)
        except LookupError as e:
            pass
        else:
            raise Exception()

    def test_init_get_officerships(self):

        officerships = self.lib.get_officerships()

        self.assertEqual(len(officerships), 1)
        
        officership = officerships[0]

        self.assertEqual(officership.id, 1)         
        self.assertEqual(officership.title, "Root")         
        self.assertIsNone(officership.end_date)         

    def test_init_get_officership(self):

        officership = self.lib.get_officership(1)

        self.assertEqual(officership.id, 1)         
        self.assertEqual(officership.title, "Root")         
        self.assertIsNone(officership.end_date)         

    def test_init_get_unknown_officership(self):
        
        try:
            self.lib.get_officership(2)
        except LookupError as e:
            pass
        else:
            raise Exception()

    def test_add_valid_person(self):

        person = self.lib.add_person(
            username='username',
            password='password')
        
        self.assertEqual(person.id, 2)
        self.assertEqual(person.username, 'username')

        person = self.lib.get_person(2)

        self.assertEqual(person.id, 2)
        self.assertEqual(person.username, 'username')

    def test_valid_add_person(self):

        person = self.lib.add_person(
            username='username',
            password='password')
        
        self.assertEqual(person.id, 2)
        self.assertEqual(person.username, 'username')

        person = self.lib.get_person(2)

        self.assertEqual(person.id, 2)
        self.assertEqual(person.username, 'username')

    def test_valid_update_person(self):

        person = self.lib.add_person(
            username='username',
            password='password')

        person = self.lib.update_person(
            'username',
            name='name')
        
        self.assertEqual(person.id, 2)
        self.assertEqual(person.username, 'username')
        self.assertEqual(person.name, 'name')

        person = self.lib.get_person(2)

        self.assertEqual(person.id, 2)
        self.assertEqual(person.username, 'username')

    def test_valid_delete_person(self):

        person = self.lib.add_person(
            username='username',
            password='password')
        
        self.assertEqual(person.id, 2)
        self.assertEqual(person.username, 'username')

        self.lib.delete_person('username')
        
        try:
            person = self.lib.get_person(2)
        except LookupError:
            pass
        else:
            raise Exception()
    
    def test_add_membership(self):

        membership = self.lib.add_membership(
            person_id = 1,
            start_date = datetime.datetime.now().date())
        
        self.assertEqual(membership.id, 1)
        self.assertEqual(membership.person_id, 1)

        membership = self.lib.get_membership(1)

        self.assertEqual(membership.id, 1)
        self.assertEqual(membership.person_id, 1)
    
    def test_update_membership(self):
        
        end = datetime.datetime.now().date() + datetime.timedelta(1000)

        membership = self.lib.add_membership(
            person_id = 1,
            start_date = datetime.datetime.now().date())

        membership = self.lib.update_membership(
            1,
            end_date = end)
        
        membership = self.lib.get_membership(1)

        self.assertEqual(membership.end_date, end)

    def test_delete_membership(self):

        end = datetime.datetime.now().date() + datetime.timedelta(1000)

        membership = self.lib.add_membership(
            person_id = 1,
            start_date = datetime.datetime.now().date())
        
        self.lib.delete_membership(1)

        memberships = self.lib.get_memberships()

        self.assertEqual(len(memberships), 0)

    def test_add_officership(self):

        officership = self.lib.add_officership(
            person_id = 1,
            title = "Foo",
            start_date = datetime.datetime.now().date())
        
        self.assertEqual(officership.id, 2)
        self.assertEqual(officership.person_id, 1)

        officership = self.lib.get_officership(2)

        self.assertEqual(officership.id, 2)
        self.assertEqual(officership.person_id, 1)
    
    def test_update_officership(self):
        
        end = datetime.datetime.now().date() + datetime.timedelta(1000)

        officership = self.lib.add_officership(
            person_id = 1,
            title = "Foo",
            start_date = datetime.datetime.now().date())

        officership = self.lib.update_officership(
            2,
            end_date = end)
        
        officership = self.lib.get_officership(2)

        self.assertEqual(officership.end_date, end)

    def test_delete_officership(self):

        end = datetime.datetime.now().date() + datetime.timedelta(1000)

        officership = self.lib.add_officership(
            person_id = 1,
            title = "Foo",
            start_date = datetime.datetime.now().date())
        
        self.lib.delete_officership(2)

        officerships = self.lib.get_officerships()

        self.assertEqual(len(officerships), 1)

    def test_add_event(self):

        event = self.lib.add_event(
            start = datetime.datetime(2000, 10, 1, 10, 10, 10),
            end = datetime.datetime(2000, 10, 1, 11, 10, 10),
            title="FOO",
            description="FOO",
            location="FOO")
        
        self.assertEqual(event.event_id, 1)

        events = self.lib.get_event(1) 

        self.assertEqual(len(events), 1)
    
    def tests_update_event(self):

        event = self.lib.add_event(
            start = datetime.datetime(2000, 10, 1, 10, 10, 10),
            end = datetime.datetime(2000, 10, 1, 11, 10, 10),
            title="FOO",
            description="FOO",
            location="FOO")

        event = self.lib.update_event(1, description="BAR")

        events = self.lib.get_event(1)

        self.assertEqual(len(events), 2)

    def test_add_post(self):

        post = self.lib.add_post()
        
        self.assertEqual(post.post_id, 1)

        posts = self.lib.get_post(1) 

        self.assertEqual(len(posts), 1)
    
    def tests_update_post(self):

        post = self.lib.add_post()

        post = self.lib.update_post(1, description="BAR")

        posts = self.lib.get_post(1)

        self.assertEqual(len(posts), 2)
