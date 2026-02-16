# views.py
from datetime import timedelta
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Session
from .serializers import SessionSerializer


class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

    @action(detail=False, methods=['get'])
    def next_available(self, request):
        # Requirement 4: Display next available slot
        last_session = Session.objects.last()
        if not last_session:
            return Response({"next_slot": "Now"})

        # Simple Logic: 1 hour after the last booked session
        next_slot = last_session.session_time + timedelta(hours=1)
        return Response({"next_slot": next_slot.strftime("%Y-%m-%d %H:%M")})