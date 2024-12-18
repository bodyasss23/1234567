from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework import status
from .models import SpyCat, Mission
from .serializers import SpyCatSerializer, MissionSerializer


class SpyCatView(ListCreateAPIView):
    queryset = SpyCat.objects.all()
    serializer_class = SpyCatSerializer
    def get(self, request):
        cats = SpyCat.objects.all()
        serializer = SpyCatSerializer(cats, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SpyCatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MissionView(ListCreateAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer


class MissionDetailView(APIView):
    def get(self, request, pk):
        try:
            mission = Mission.objects.get(pk=pk)
            serializer = MissionSerializer(mission)
            return Response(serializer.data)
        except Mission.DoesNotExist:
            return Response({"error": "Mission not found."}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, pk):
        try:
            mission = Mission.objects.get(pk=pk)
        except Mission.DoesNotExist:
            return Response({"error": "Mission not found."}, status=status.HTTP_404_NOT_FOUND)

        if mission.complete:
            return Response({"error": "Cannot modify a completed mission."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = MissionSerializer(mission, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            mission = Mission.objects.get(pk=pk)
        except Mission.DoesNotExist:
            return Response({"error": "Mission not found."}, status=status.HTTP_404_NOT_FOUND)

        if mission.cat:
            return Response({"error": "Cannot delete a mission assigned to a cat."}, status=status.HTTP_400_BAD_REQUEST)

        mission.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
