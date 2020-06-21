from django.urls import path
from turniej_app.views.index_view import IndexView
from turniej_app.views.login_view import MyLoginView
from turniej_app.views.logout_view import MyLogoutView
from turniej_app.views.graczes_view import ListaGraczyView, UpdateGraczeView, CreateGraczeView, DeleteGraczeView
from turniej_app.views.turniejes_view import ListaTurniejowView, UpdateTurniejeView, CreateTurniejeView, DeleteTurniejeView
from django_registration.views import RegistrationView

urlpatterns = [
path('', IndexView.as_view(), name='index'),
path('index', IndexView.as_view(), name='index'),
path('turniej_app/logout', MyLogoutView.as_view(), name='logout'),
path('login', MyLoginView.as_view(), name='login'),
path('lista_graczy', ListaGraczyView.as_view(), name='lista_graczy'),
path('index/create_gracz', CreateGraczeView.as_view(), name='create_gracz'),
path('lista_graczy/<int:pk>/update_gracz', UpdateGraczeView.as_view(), name='update_gracz'),
path('lista_graczy/<int:pk>/delete_gracz', DeleteGraczeView.as_view(), name='delete_gracz'),
path('lista_turniejow', ListaTurniejowView.as_view(), name='lista_turniejow'),
path('index/create_turniej', CreateTurniejeView.as_view(), name='create_turniej'),
path('lista_turniejow/<int:pk>/update_turniej', UpdateTurniejeView.as_view(), name='update_turniej'),
path('lista_turniejow/<int:pk>/delete_turniej', DeleteTurniejeView.as_view(), name='delete_turniej'),
]