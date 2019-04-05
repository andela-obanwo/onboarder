from rest_framework import serializers

from api.models import OnboardingItems


class OnboardingItemsSerializer(serializers.ModelSerializer):

    class Meta:
        model = OnboardingItems
        fields = "__all__"