import sys

from django.conf import settings
from django.http import HttpResponse
from django.conf.urls import url

settings.configure(
    ROOT_URLCONF=__name__,
    DEBUG=True,
)


def index(request):
    return HttpResponse("Hello World")


urlpatterns = (
    url("", index),
)

if __name__ == '__main__':
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
