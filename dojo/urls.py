from rest_framework.routers import DefaultRouter
from .views import DojoViewSet

router = DefaultRouter()
router.register(r'dojos', DojoViewSet, base_name='dojo')

urlpatterns = router.urls
