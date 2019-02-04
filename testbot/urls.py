"""testbot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from regressions.models import Run
from regressions import views
from rest_framework import routers, serializers, viewsets

# move this all into its own files, but go here for now
class RunSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Run
        fields = ('label','status','duration','submitter','created','updated','start','end')

class RunViewSet(viewsets.ModelViewSet):
    queryset = Run.objects.all()
    serializer_class = RunSerializer

router = routers.DefaultRouter()
router.register(r'runs', RunViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^runs/latest', views.latest, name='latest'),
    url(r'^admin/', admin.site.urls),
]
