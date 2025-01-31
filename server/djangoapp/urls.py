# Uncomment the imports before you add the code
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # path for registration
    path(route='register', view=views.registration, name='registration'),
    # path for login
    path(route='login', view=views.login_user, name='login'),
    # path for logout
    path(route='logout', view=views.logout_request, name='logout'),
    # path for get_cars
    path(route='get_cars', view=views.get_cars, name ='getcars'),    path(route='get_cars', view=views.get_cars, name ='getcars'),
    # path for get_dealerships
    path(route='get_dealers', view=views.get_dealerships, name='get_dealers'),
        path(route='get_dealers/<str:state>', view=views.get_dealerships, name='get_dealers_by_state'),
    # path for get_dealer_details
    path(route='dealer/<int:dealer_id>', view=views.get_dealer_details, name='dealer_details'),
    # path for dealer reviews view
    path(route='reviews/dealer/<int:dealer_id>', view=views.get_dealer_reviews, name='dealer_details'),
    # path for add a review view
    path(route='add_review', view=views.add_review, name='add_review'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
