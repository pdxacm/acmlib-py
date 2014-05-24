from . import DATE_FORMAT, DATETIME_FORMAT
import datetime
import characteristic

class Model(object):
    
    def __init__(self, requestor):
        self._requestor = None
        self.raw_headers = None
        self.resource_uri = None
    
    @staticmethod
    def _makeDatetimeAttribute(value):
        return datetime.datetime.strptime(value, DATETIME_FORMAT)

    @staticmethod
    def _makeDateAttribute(value):
        return datetime.datetime.strptime(value, DATE_FORMAT).date() 

@characteristic.attributes(["event_id", "revision"],
        defaults={"event_id":None, "revision":None})
class Event(Model):

    def __init__(self, requestor):
        super(Event, self).__init__(requestor)
        self.event_id = None
        self.title = None
        self.description = None
        self.speaker = None
        self.editor_id = None
        self.edited_at = None
        self.start = None
        self.end = None
        self.canceled = None
        self.revision = None
        self.resource_uri = None

    @classmethod
    def from_json(cls, requestor, headers, json):

        i = cls(requestor)

        i.headers = headers
        i.event_id = json['event_id']
        i.title = json['title']
        i.description = json['description']
        i.speaker = json['speaker']
        i.editor_id = json['editor_id']
        i.edited_at = Model._makeDatetimeAttribute(json['edited_at'])
        i.start = Model._makeDatetimeAttribute(json['start'])
        i.end = Model._makeDatetimeAttribute(json['end'])
        i.canceled = json['canceled']
        i.revision = json['revision']

        return i

@characteristic.attributes(["post_id", "revision"],
        defaults={'post_id':None, 'revision':None})
class Post(Model):

    def __init__(self, requestor):
        super(Post, self).__init__(requestor)
        self.post_id = None
        self.title = None
        self.description = None
        self.content = None
        self.editor_id = None
        self.edited_at = None
        self.revision = None
        self.resource_uri = None

    @classmethod
    def from_json(cls, requestor, headers, json):

        i = cls(requestor)

        i.headers = headers
        i.post_id = json['post_id']
        i.title = json['title']
        i.description = json['description']
        i.content = json['content']
        i.editor_id = json['editor_id']
        i.edited_at = Model._makeDatetimeAttribute(json['edited_at'])
        i.revision = json['revision']

        return i

@characteristic.attributes(["id", "username"], 
        defaults={'id':None, 'username':None})
class Person(Model):

    def __init__(self, requestor):
        super(Person, self).__init__(requestor)
        self.id = None
        self.name = None
        self.username = None
        self.email = None
        self.website = None

    @classmethod
    def from_json(cls, requestor, headers, json):

        i = cls(requestor)

        i.headers = headers
        i.id = json['id']
        i.name = json['name']
        i.username = json['username']
        i.email = json['email']
        i.website = json['website']

        return i


@characteristic.attributes(["id"], defaults={"id":None})
class Membership(Model):


    def __init__(self, requestor):
        super(Membership, self).__init__(requestor)
        self.id = None
        self.person_id = None
        self.start_date = None
        self.end_date = None

    @classmethod
    def from_json(cls, requestor, headers, json):

        i = cls(requestor)

        i.headers = headers
        i.id = json['id']
        i.person_id = json['person_id']
        i.start_date = Model._makeDateAttribute(json['start_date'])
        i.end_date = json['end_date']
        if i.end_date:
            i.end_date = Model._makeDateAttribute(i.end_date)

        return i


@characteristic.attributes(["id"], defaults={'id':None})
class Officership(Model):

    def __init__(self, requestor):
        super(Officership, self).__init__(requestor)
        self.id = None
        self.title = None
        self.person_id = None
        self.start_date = None
        self.end_date = None

    @classmethod
    def from_json(cls, requestor, headers, json):

        i = cls(requestor)

        i.headers = headers
        i.id = json['id']
        i.title = json['title']
        i.person_id = json['person_id']
        i.start_date = Model._makeDateAttribute(json['start_date'])
        i.end_date = json['end_date']
        if i.end_date:
            i.end_date = Model._makeDateAttribute(i.end_date)

        return i
