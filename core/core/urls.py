
from django.contrib import admin
from django.urls import path, include
from django.urls import path
from home.views import *
from vege.views import *
from django.conf import settings 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static 


urlpatterns = [

path('' ,login_page, name="login_page"),
path('receipes/' , receipes , name="receipes"),
path('delete_receipe/<int:id>/', delete_receipe, name="delete_receipe"),
path('update_receipe/<int:id>/', update_receipe, name='update_receipe'),
path('about/' , about , name="about"),
path('login_page/' , login_page, name="login_page"),
path('login1_page/' , login1_page, name="login1_page"),
path('register/' , register, name="register"),
path('contact/' , contact , name="contact"),
path('logout_page/' , logout_page , name="logout_page"),
path('success_page/' , success_page , name="success_page"),
path('students/' , get_student , name="get_students"),
path('see_marks/<student_id>/', see_marks, name='see_marks'),
path('rate_receipe/<int:receipe_id>/', rate_receipe, name='rate_receipe'),
path('user_receipe/', user_receipe, name='user_receipe'),
path('burger/', burger, name='burger'),
path('pizza/', pizza, name='pizza'),
path('delete_receipe1/<int:id>/', delete_receipe1, name="delete_receipe1"),
path('update_receipe1/<int:id>/', update_receipe1, name='update_receipe1'),
path('rate_receipe1/<int:receipe_id>/', rate_receipe1, name='rate_receipe1'),
path('delete_receipe_pizza/<int:id>/', delete_receipe_pizza, name="delete_receipe_pizza"),
path('update_receipe_pizza/<int:id>/', update_receipe_pizza, name="update_receipe_pizza"),
path('user_burger/', user_burger, name='user_burger'),
path('user_pizza/', user_pizza, name='user_pizza'),
path('payment/', payment, name='payment'),
path('addcart/<int:id>/', addcart, name='addcart'),
path('register1/' , register1, name="register1"),



    path('admin/', admin.site.urls),
 ]
if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

   urlpatterns += staticfiles_urlpatterns()


