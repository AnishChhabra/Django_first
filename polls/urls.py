from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$',
    	views.IndexView.as_view(),
    	name='index'
    ),
    url(r'^(?P<pk>[0-9]+)/$',
    	views.DetailView.as_view(),
    	name='detail'
    ),
    url(
    	r'^(?P<pk>[0-9]+)/results/$',
    	views.ResultsView.as_view(),
    	name='results'
    ),
    url(r'^(?P<question_id>[0-9]+)/vote/$',
    	views.vote,
    	name='vote'
    ),
    url(r'^create_user/$',
    	views.create_user,
    	name='create_user'
    ),
    url(r'^user_auth/$',
    	views.user_auth,
    	name='user_auth'
    ),
    url(r'^login/$',
    	views.login,
    	name='login'
    ),
    url(r'^signup/$',
    	 views.signup,
    	 name='signup'
    ),
    url(r'^change_pw/$',
    	views.change_pw,
    	name='change_pw'
    ),
    url(r'^check_pw/$',
    	views.check_pw,
    	name='check_pw'
    ),
    url(r'^log_out/$',
    	views.log_out,
    	name='log_out'
    ),
]