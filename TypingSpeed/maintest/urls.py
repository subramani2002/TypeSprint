from django.urls import path
from .views import class_view,student_details,test,results,dashboard

urlpatterns = [
    path('',class_view,name='class_page'),
    path('details_page/<str:class_type>/',student_details,name='details_page'),
    path('test_page/',test,name='test_page'),
    path('results_page/',results, name = 'results_page'),
    path('dashboard/', dashboard, name='dashboard'),
]