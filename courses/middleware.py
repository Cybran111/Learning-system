class CourseMiddleware(object):
    def process_view(self, request, view_func, view_args, view_kwargs):
        """
        Supplies possible URL args to context processor by adding these to Request
        :param request:
        :param view_func:
        :param view_args:
        :param view_kwargs:
        :return:
        """
        request.course_info = view_kwargs