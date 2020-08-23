from django.conf.urls import url
from routing import views

urlpatterns = [
url('/routing/simple_route/', views.simple_route),
url('/routing/slug_route/([0-9a-z_-]{1,16})/', views.slug_route),
url('/routing/sum_route/(\d)/(\d)/', views.sum_route),
url('/routing/sum_get_method/', views.sum_get_method),
url('/routing/sum_post_method/', views.sum_post_method)
]
