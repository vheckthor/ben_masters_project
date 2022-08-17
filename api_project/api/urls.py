from xml.etree.ElementInclude import include
from  django.urls import path, include

from .views import PlatNumberDataView

urlpatterns = [
    path('v1/platenumber', PlatNumberDataView.as_view()),
]