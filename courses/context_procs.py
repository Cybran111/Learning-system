
from courses.models import Course

__author__ = 'cybran'


def course_info(request):
    course_data = dict()

    if "course_id" in request.course_info:
        course_data["course"] = Course.objects.get(pk=request.course_info["course_id"])
    return course_data