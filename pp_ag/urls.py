from django.urls import path
from . import views
from django.conf.urls import re_path

app_name = 'ag'

urlpatterns = [
    path('', views.index, name="home"),
    re_path('signup/', views.signup, name='signup'),
    path('case/', views.PostCreateView.as_view(), name="case_post"),
    path('list/', views.PostListView.as_view(), name="case_list"),
    path('case/<int:pk>/', views.CaseDetail.as_view(), name="case_detail"),
    path('about/', views.AboutView.as_view(), name="about"),
    path('case/<int:pk>/edit', views.CaseUpdateView.as_view(), name="case_update"),

    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            views.activate_account, name='activate'),
    
]