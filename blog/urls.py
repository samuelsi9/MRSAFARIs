from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from . import views

urlpatterns = [
    path('blog-home', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/download/', views.download_file, name='download_file'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('head',views.head,name="head"),
    path('',views.homes,name="HOMES"),
    path('ciu',views.ciu,name="ciu"),
    path('neu',views.neu,name="neu"),
    path('gau',views.gau,name="gau"),
    path('emu',views.emu,name="emu"),
    path('bau',views.bau,name="bau"),
    path('underciu',views.underciu,name="underciu"),
    path('underbau',views.underbau,name="underbau"),
    path('underemu',views.underemu,name="underemu"),
    path('underneu',views.underneu,name="underneu"),
    path('undergau',views.undergau,name="undergau"),
    path('admission',views.admi,name="admissionP"),
    path('services',views.ser,name="services"),
    path('chypre',views.chy,name="chypre"),
    path('masterciu',views.masterciu,name="masterciu"),
    path('masteremu',views.masteremu,name="masteremu"), 
    path('masterneu',views.masterneu,name="masterneu"), 
    path('mastergau',views.mastergau,name="mastergau"),
    path('masterbau',views.masterbau,name="masterbau"),
    path('doctoratciu',views.doctoratciu,name="doctoratciu"),
    path('doctoratemu',views.doctoratemu,name="doctoratemu"),
    path('doctoratbau',views.doctoratbau,name="doctoratbau"),
    path('doctoratneu',views.doctoratneu,name="doctoratneu"),
    path('doctoratgau',views.doctoratgau,name="doctoratgau"),




   
]     
