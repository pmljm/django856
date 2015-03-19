from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'profiles.views.home', name='home'),
    url(r'^work/$', 'profiles.views.work', name='work'),
    url(r'^team/$', 'profiles.views.team', name='team'),
    url(r'^plans/$', 'pricing.views.plans', name='plans'),
    url(r'^chat/$', 'blog.views.chat', name='chat'),
    url(r'^contact/$', 'contacts.views.contact', name='contact'),
    #url(r'^contact$', 'contacts.views.signin', name='signin'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'', include('social_auth.urls')),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)