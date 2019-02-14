from django.urls import path, re_path
from users.views import SignUp


urlpatterns = [
    path('signup/', SignUp.as_view(), name="signup"),
    

]
