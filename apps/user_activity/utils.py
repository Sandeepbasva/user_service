import json
import pytz
from django.http import HttpResponse


class Response:

    def __init__(self, data):
        pass

    @classmethod
    def user_entity(cls, src_object):
        
        user = dict()
        user["id"] = src_object.id
        user["real_name"] = src_object.name
        user["tz"] = pytz.country_timezones(src_object.country)[0] #src_object.country
        return user

    @classmethod
    def log_entity(cls, src_object):
        log = dict()
        log["start_time"] = src_object.start_time.strftime("%b %-d %Y  %H:%M%p")
        log["end_time"] = src_object.end_time.strftime("%b %-d %Y  %H:%M%p")
        return log


class Result(object):
    def __init__(self, code, status, message=None, extra_fields=None):
        """
        Base Result class for API responses.
        code - numeric status code
        status - short status code
        message - descriptive message.
        """
        self.code = code
        self.status = status
        self.message = message
        self.extra_fields = extra_fields

    def to_json_dict(self):
        """Convert to a dict for serializing to JSON."""
        result = {"code": self.code, "status": self.status}
        if self.message:
            result["message"] = self.message
        if self.extra_fields:
            result.update(self.extra_fields)
        return result

    def to_json(self, pretty=0):
        """Serialize to JSON."""
        if pretty == 1:
            return json.dumps(self.to_json_dict(), indent=2)
        return json.dumps(self.to_json_dict())

    def http_response(self, pretty=0, status_code=200):
        response = HttpResponse(self.to_json(pretty), content_type='application/json')
        response.status_code = status_code
        return response
