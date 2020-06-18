from django.urls import path
from .views import *


urlpatterns = [ path('login', log_in, name='login'),
	path('logout', log_out, name='logout'),
	path('signup', sign_up, name='signup'),
	path('', all_blogs, name='all_blogs'),
	path('<int:blog_id>/', get_blog, name='blog_by_id'),
	path('<int:blog_id>/create_post', create_post, name='create_post'),
	path('create_blog/', create_blog, name='create_blog'),
	
	path('delete/<int:post_id>', delete, name='delete')
]
