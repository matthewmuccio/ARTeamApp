from django.conf.urls import url

from . import views

# Since polls will be in their own URLconf (this file), they can be placed
# under any path root and the app will work correctly.
urlpatterns = [
	# url() is passed four args, two required (regex, view), two optional (kwargs, name).
    # regex: "regular expression"; syntax for matching patterns in strings/url patterns.
	# It makes its way down the list, comparing the requested URL against each regex until
	# it finds one it matches.
	# view: When Django finds a regex match, it calls the specified view function, with
	# an HttpRequest obj as the first arg and any "captured" vals from the regex as args.
	# kwargs: Arbitrary keyword args can be passed in a dictionary to the target view.
	# name: Naming your URL lets you refer to it unambiguously somewhre in Django.
	url(r'^$', views.index, name='index'),
]