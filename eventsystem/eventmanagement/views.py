from rest_framework import status

from .models import Event, EventType
from .serializers import EventSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class EventAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        events = Event.objects.all().values()
        return Response({'title': EventSerializer(events, many=True).data})

    def post(self, request):
        event_type_name = request.data['event_type']

        if isinstance(event_type_name, int):
            return Response("incorrect request", status.HTTP_400_BAD_REQUEST)

        if not EventType.objects.filter(name=event_type_name).exists():
            new_event_type = EventType(name=request.data['event_type'])
            new_event_type.save()
            new_event_type_id = new_event_type.pk
            request.data['event_type'] = new_event_type_id
        else:
            event_type_id = EventType.objects.get(name=event_type_name).pk
            request.data['event_type'] = event_type_id

        serializer = EventSerializer(data=request.data)
        serializer.is_valid(raise_exception=False)
        serializer.save(user=request.user)

        return Response({'title': serializer.data})
