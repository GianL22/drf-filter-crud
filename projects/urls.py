from django.urls import path
from rest_framework import routers
from .api import ProjectViewSet
from .views import ProductView
# router = routers.DefaultRouter()

# router.register('api/projects', ProjectViewSet, 'projects')

urlpatterns = [
    path('api/products', ProductView.as_view())
    
]