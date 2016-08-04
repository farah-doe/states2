from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings  

from app import views


urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # class based views:
    
    # delete views
    url(r'^delete_city/(?P<pk>\d+)/$', 'app.views.delete_city'),
    
    # edit views
    url(r'^city_edit/(?P<pk>\d+)/$', 'app.views.city_edit', name='city_edit'),
    url(r'^state_edit/(?P<pk>\d+)/$', 'app.views.state_edit', name='state_edit'),

    

    # url(r'^city_list_class_view/', views.CityListView.as_view()),
    # url(r'^city_detail_class_view/(?P<pk>\d+)', views.CityDetailView.as_view()),
    # url(r'^state_list_class_view/', views.StateListView.as_view()),
    # url(r'^state_detail_class_view/(?P<pk>\d+)', views.StateDetailView.as_view()),

    # form views
    # url(r'^city_search_post/', 'app.views.city_search_post'),
    url(r'^city_search/', 'app.views.city_search'),
    

   # create views
    url(r'^create_city/', 'app.views.create_city'), 
    url(r'^create_state/', 'app.views.create_state'),

    url(r'^capital_detail/(?P<pk>\d+)/', 'app.views.capital_detail'),
    url(r'^capital_list/', 'app.views.capital_list'),
    url(r'^city_listall/', 'app.views.city_listall'),
    url(r'^contact/', 'app.views.contact'),
    url(r'^state_detail/(?P<pk>\d+)/', 'app.views.state_detail'),
    url(r'^state_list/', 'app.views.state_list'),
    url(r'^city_detail/(?P<pk>\d+)/', 'app.views.city_detail'),
    url(r'^city_list/', 'app.views.city_list'),
    # old views
    url(r'^admin/', include(admin.site.urls)),
    url(r'^template_view/', 'app.views.template_view'),
    url(r'^first_view/', 'app.views.first_view'),
    url(r'^detail/(?P<pk>\d+)/', 'app.views.detail'),
    url(r'^list/$', 'app.views.list'),
    

# form view, get post, 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


