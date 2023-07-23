#from django.conf.urls import url
from tutorials import views
from django.urls import path

urlpatterns = [
#    url(r'^api/tutorials$', views.tutorial_list),
#   url(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
#    url(r'^api/tutorials/published$', views.tutorial_list_published)

#    path('api/', views.apitest, name='apitest')
    path('tutorial-list/', views.listTutorial, name='tutorial-list'),
    path('tutorial-detail/<str:pk>', views.detailTutorial, name='tutorial-detail'),
    path('tutorial-create/', views.createTutorial, name='tutorial-create'),
    path('tutorial-update/<str:pk>', views.updateTutorial, name='tutorial-update'),
    path('tutorial-delete/<str:pk>', views.deleteTutorial, name='tutorial-delete'),
]