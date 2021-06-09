from django.urls import path
from .views import Portfolioiew, MyView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('portfolio', Portfolioiew)
urlpatterns = router.urls
urlpatterns += [
    path('login/', MyView.as_view())
]
app_name = 'portfolio'
