from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from api.views import OnboardingItemsViewset, DepartmentsViewset

router = DefaultRouter()
router.register('onboarding_items', OnboardingItemsViewset, base_name='onboarding_items')
router.register('departments', DepartmentsViewset, base_name='departments')



urlpatterns = [
    url(r'', include(router.urls)),

]
