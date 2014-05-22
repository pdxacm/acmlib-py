from . import DEFAULT_BASE_URL
from .models import Event, Post, Person, Membership, Officership
from .requester import Requester

class AcmLib:

    def __init__(self, username=None, password=None, 
            base_url=DEFAULT_BASE_URL):
        """
        :param: username: str
        :param: password: str
        :param: base_url: str
        """

        self.__requester = Requester(username, password, base_url)

    def get_person(self, id_or_username):
        """
        :calls: `GET /person/`
        :param id_or_username: str or int
        :rtype: :class: `Person`
        """
        response = self.__requester.get(["/people/", id_or_username])
        return self.__process_response(response, Person)

    def get_people(self):
        """
        :calls: `GET /person/`
        :rtype: :class: [`Person`]
        """
        response = self.__requester.get("/people/")
        return self.__process_list_response(response, Person)
        
    def add_person(self, username, password, name=None, email=None,
            website=None):
        """
        :calls: `POST /person/`
        :param: username: str
        :param: password: str
        :param: name: str
        :param: email: str
        :param: website: str
        :rtype: :class: [`Person`]
        """
        
        data = dict(
            username = username,
            password = password,
            name = name,
            email = email,
            website = website,
            )

        response = self.__requester.post("/people/", data)
        
        return self.__process_response(response, Person)
    
    def update_person(self, id_or_username, password=None, name=None, 
            email=None, website=None):
        """
        :calls: `PUT /person/`
        :param: id_or_username: int or str
        :param: password: str
        :param: name: str
        :param: email: str
        :rtype: :class: [`Person`]
        """

        data = dict(
            username = username,
            password = password,
            name = name,
            email = email,
            website = website,
            )

        response = self.__requester.put(
                ["/people/", id_or_username], data)

        return self.__process_response(response, Person)

    def delete_person(self, id_or_username):
        """
        :calls: `DELETE /person/`
        :param: id_or_username: int or str
        """

        response = self.__requester.delete(["/people/", id_or_username])

    def get_event(self, event_id):
        """
        :calls: `GET /events/`
        :param code: int
        :rtype: :class: `Event`
        """
        response = self.__requester.get(["/events/", event_id])
        
        return map(lambda entry: 
            Event.from_json(
                self.__requester, response.headers, entry),
            response.json())
        
    def get_events(self):
        """
        :calls: `GET /events/`
        :rtype: :class: [`Event`]
        """
        response = self.__requester.get("/events/")
        return self.__process_list_response(response, Event)

    def add_event(self, start, end, title=None, description=None, 
            location=None, speaker=None):
        """
        :calls: `POST /event/`
        :param: start: datetime
        :param: end: datetime
        :param: title: str
        :param: description: str
        :param: location: str
        :param: speaker: str
        :rtype: :class: [`Event`]
        """
        
        data = dict(
            start = start,
            end = end,
            title = title,
            description = description,
            location = location,
            speaker = speaker,
            )

        response = self.__requester.post("/events/", data)
        
        return self.__process_response(response, Event)
    
    def update_event(self, event_id, start=None, end=None, title=None, 
            description=None, location=None, speaker=None):
        """
        :calls: `PUT /event/`
        :param: event_id: int
        :param: start: datetime
        :param: end: datetime
        :param: title: str
        :param: description: str
        :param: location: str
        :param: speaker: str
        :rtype: :class: [`Event`]
        """

        data = dict(
            start = start,
            end = end,
            title = title,
            description = description,
            location = location,
            speaker = speaker,
            )

        response = self.__requester.put(["/events/", event_id], data)

        return self.__process_response(response, Event)

    def get_post(self, post_id):
        """
        :calls: `GET /posts/`
        :param code: int
        :rtype: :class: `Post`
        """
        response = self.__requester.get(["/posts/", post_id])
        return self.__process_list_response(response, Post)
        
    def get_posts(self):
        """
        :calls: `GET /posts/`
        :rtype: :class: [`Post`]
        """
        response = self.__requester.get("/posts/")
        return self.__process_list_response(response, Post)

    def add_post(self, title=None, description=None, content=None):
        """
        :calls: `POST /posts/`
        :param: title: str
        :param: description: str
        :param: content: str
        :rtype: :class: [`Post`]
        """
        
        data = dict(
            title = title,
            description = description,
            content = content,
            )

        response = self.__requester.post("/posts/", data)
        
        return self.__process_response(response, Event)
    
    def update_event(self, post_id, title=None, description=None, 
            content=None):
        """
        :calls: `PUT /posts/`
        :param: post_id: int
        :param: title: str
        :param: description: str
        :param: content: str
        :rtype: :class: [`Post`]
        """

        data = dict(
            title = title,
            description = description,
            content = content,
            )

        response = self.__requester.put(["/posts/", post_id], data)

        return self.__process_response(response, Post)

    def get_membership(self, membership_id):
        """
        :calls: `GET /memberships/`
        :param code: int
        :rtype: :class: `Membership`
        """
        response = self.__requester.get(["/membership/", membership_id])
        return self.__process_response(response, Membership)
        
    def get_memberships(self):
        """
        :calls: `GET /memberships/`
        :rtype: :class: [`Membership`]
        """
        response = self.__requester.get("/membership/")
        return self.__process_list_response(response, Membership)

    def add_membership(self, person_id, start, end=None):
        """
        :calls: `POST /membership/`
        :param: person_id: int
        :param: start: datetime
        :param: end: datetime
        :rtype: :class: [`Membership`]
        """

        data = dict(
            person_id = person_id,
            start = start,
            end = end,
            )

        response = self.__requester.post("/memberships/", data)
        
        return self.__process_response(response, Membership)
    
    def update_membership(self, membership_id, start=None, end=None):
        """
        :calls: `PUT /membership/`
        :param: id_or_username: int
        :rtype: :class: [`Membership`]
        """

        data = dict(
            person_id = person_id,
            start = start,
            end = end,
            )
        response = self.__requester.put(
                ["/memberships/", membership_id], data)

        return self.__process_response(response, Membership)

    def delete_membership(self, membership_id):
        """
        :calls: `DELETE /membership/`
        :param: id_or_username: int
        """

        response = self.__requester.delete(["/memberships/", membership_id])

    def get_officership(self, officership_id):
        """
        :calls: `GET /officerships/`
        :param code: int
        :rtype: :class: `Officership`
        """
        response = self.__requester.get(["/officerships/", officership_id])
        return self.__process_response(response, Officership)
        
    def get_officerships(self):
        """
        :calls: `GET /officerships/`
        :rtype: :class: [`Officership`]
        """
        response = self.__requester.get("/officerships/")
        return self.__process_list_response(response, Officership)

    def add_officership(self, person_id, title, start, end=None):
        """
        :calls: `POST /officership/`
        :param: person_id: int
        :param: title: str
        :param: start: datetime
        :param: end: datetime
        :rtype: :class: [`Officership`]
        """
        
        data = dict(
            person_id = person_id,
            title = title,
            start = start,
            end = end,
            )

        response = self.__requester.post("/officerships/", data)
        
        return self.__process_response(response, Officership)
     
    def update_officership(self, officership_id, title=None, start=None,
            end=None):
        """
        :calls: `PUT /officership/`
        :param: officership_id: int
        :param: title: str
        :param: start: date
        :param: end: date
        :rtype: :class: [`Officership`]
        """

        data = dict(
            person_id = person_id,
            title = title,
            start = start,
            end = end,
            )

        response = self.__requester.put(
                ["/officerships/", officership_id])

        return self.__process_response(response, Officership)

    def delete_officership(self, officership_id):
        """
        :calls: `DELETE /officership/`
        :param: id_or_username: int
        """

        response = self.__requester.delete(["/officerships/", officership_id])

    def __process_list_response(self, response, model):
        return map(lambda entry: 
            model.from_json(
                self.__requester, response.headers, entry),
            response.json())

    def __process_response(self, response, model):
        return model.from_json(self.__requester, response.headers,
                response.json()[0])
