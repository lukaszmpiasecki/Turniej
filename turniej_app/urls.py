from django.urls import path
from turniej_app.views.index_view import IndexView
from turniej_app.views.login_view import MyLoginView
from turniej_app.views.logout_view import MyLogoutView

urlpatterns = [
path('', IndexView.as_view(), name='index'),
path('index', IndexView.as_view(), name='index'),
path('turniej_app/logout', MyLogoutView.as_view(), name='logout'),
path('login', MyLoginView.as_view(), name='login'),
]