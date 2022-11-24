from rest_framework import routers

from .views import ProductViewSet


# Register the product viewset into the router and add the URLs
router = routers.DefaultRouter()
router.register(r'', ProductViewSet)
urlpatterns = router.urls
