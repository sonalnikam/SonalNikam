from django.conf.urls import url



from . import views

urlpatterns = [
    url(r'^$',views.First1.as_view()),
     url(r'^p',views.prin),
     url(r'^link1',views.car),
     url(r'^arc', views.archive),
     url(r'^link',views.demo),
     url(r'^hm', views.HomePageView.as_view()),
     url(r'^archives', views.archive),
     url(r'^login1',views.archive1),
     url(r'^Reg',views.Reg),
     url(r'^su',views.success),
     url(r'^bookinfo',views.book),
      url(r'^lout',views.logout)
   # ex: /polls/5/
  
   
   
]