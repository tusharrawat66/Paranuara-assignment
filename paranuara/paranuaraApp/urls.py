from django.urls import path
from . views import *
from . import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = {

    path('upload_data/', Datatosql.as_view()),
    path('empDetails/', EmpDetails.as_view()),
    path('singleDualEntity/', csrf_exempt(SingleDualEntity.as_view())),

}