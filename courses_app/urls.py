from django.urls import path
from . import views

urlpatterns = [

    path('', views.display_home),
    path('addcourse', views.add_course),
    path('course/deletepage', views.display_deletepage),
    path('course/destroy', views.delete_course),
    path('course/destroy/confirm', views.confirm_course_removal),
    path('comments', views.display_comments),
    path('addcomment', views.add_comments),
    path('goback', views.root_button),
    path('redirct/comments', views.redirct_comments),
]
