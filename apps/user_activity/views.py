from django.shortcuts import render
from django.http import HttpResponse
from .models import User, ActivityPeriod
from .utils import Response, Result

# Create your views here.


def home(request):
    return HttpResponse("<html> <h3>Welcome to Homepage</h3> </html>")


def get_user_activity(request):
    users = User.objects.all()
    members = list()
    for user in users:
        user_info = Response.user_entity(src_object=user)
        activity_periods = list()
        user_log = ActivityPeriod.objects.filter(user_id=user.id)
        if user_log:
            for log in user_log:
                period = Response.log_entity(src_object=log)
                activity_periods.append(period)
            user_info["activity_periods"] = activity_periods
        members.append(user_info)
    result_data = dict()
    result_data["ok"] = True
    result_data["members"] = members
    result = Result(200, "SUCCESS", extra_fields=result_data)
    return result.http_response(result_data.get("pretty"))
