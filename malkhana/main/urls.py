from django.conf.urls import url
from main import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'),  # Notice the URL has been named

    url(r'^addvivechak$', views.AddVivechak.as_view(), name='addvivechak'),
    url(r'^editvivechak/(?P<pk>\d+)$', views.editvivechak, name='editvivechak'),
    url(r'^deletevivechak/(?P<pk>\d+)$', views.deletevivechak, name='deletevivechak'),
    url(r'^vivechaklist$', views.VivechakList.as_view(), name='vivechaklist'),

    url(r'^addreport$', views.AddReport.as_view(), name='addreport'),
    url(r'^reportlist$', views.ReportList.as_view(), name='reportlist'),

    url(r'^stockin$', views.AddStock.as_view(), name='stockin'),
    url(r'^stockinlist$', views.StockInList.as_view(), name='stockinlist'),

    url(r'^stockout$', views.RemoveStock.as_view(), name='stockout'),
    url(r'^stockoutlist$', views.StockOutList.as_view(), name='stockoutlist'),

]
