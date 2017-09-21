from django.http import HttpResponse

# Simple view in Django.
# In order to call view we must map it to a URL, with URLconf.
def index(request):
    return HttpResponse("Hello, World. This is the index page for a PollApplication.")