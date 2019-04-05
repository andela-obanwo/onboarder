from rest_framework import viewsets

from api.models import OnboardingItems
from api.serializers import OnboardingItemsSerializer


class OnboardingItemsViewset(viewsets.ModelViewSet):

    queryset = OnboardingItems.objects.all()
    serializer_class = OnboardingItemsSerializer