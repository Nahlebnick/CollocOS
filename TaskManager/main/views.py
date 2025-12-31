from django.core.serializers import serialize
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from .models import Task
from rest_framework.views import APIView
from rest_framework import status

from .serializers import TaskSerializer


class TaskAPIView(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if pk:
            w = get_object_or_404(Task, pk=pk)
            return Response({'post': TaskSerializer(w).data})
        l = Task.objects.all()
        return Response(TaskSerializer(l, many=True).data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "Invalid data passed"}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Task.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exist"})

        serializer = TaskSerializer(data=request.data, instance=instance)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"error": "Invalid data passed"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Task.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exist"},
                            status=status.HTTP_400_BAD_REQUEST)

        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

