from rest_framework import serializers
from .models import Session

class SessionSerializer(serializers.ModelSerializer):
    class Meta:  # <--- MUST be capitalized "Meta"
        model = Session
        fields = '__all__'

    def validate_session_time(self, value):
        # Prevent duplicate booking logic
        if Session.objects.filter(session_time=value).exists():
            raise serializers.ValidationError("This slot is already booked!")
        return value