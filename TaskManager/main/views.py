from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from .models import Task
from rest_framework.views import APIView
from rest_framework import status

from .serializers import TaskSerializer
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser
)
from .permissions import IsOwnerOrReadOnly

from django.contrib.auth.models import User
import logging

logger = logging.getLogger(__name__)

class RegisterAPIView(APIView):
    permission_classes = []

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({"error": "username and password required"},status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({"error": "user already exists"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password)

        return Response({"message": "user created"}, status=status.HTTP_201_CREATED)

class TaskAPIView(APIView):

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]

        if self.request.method == 'POST':
            return [IsAuthenticated()]

        if self.request.method == 'PUT':
            return [IsAuthenticated(), IsOwnerOrReadOnly()]

        if self.request.method == 'DELETE':
            return [IsAuthenticated(), IsAdminUser()]

        return super().get_permissions()

    def get(self, request, *args, **kwargs):
        logger.info(f"GET /tasks by user={request.user}")
        pk = kwargs.get("pk", None)
        if pk:
            w = get_object_or_404(Task, pk=pk)
            return Response({'post': TaskSerializer(w).data})
        l = Task.objects.all()
        return Response(TaskSerializer(l, many=True).data)

    def post(self, request):
        logger.info(
            f"POST /tasks by user={request.user}"
        )
        serializer = TaskSerializer(
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        task = serializer.save()

        logger.info(f"Task created id={task.id} by user={request.user}")

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        instance = get_object_or_404(Task, pk=pk)

        self.check_object_permissions(request, instance)
        logger.info(f"PUT /tasks/{instance.id} by user={request.user}" )

        serializer = TaskSerializer(instance=instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        instance = get_object_or_404(Task, pk=pk)

        self.check_object_permissions(request, instance)
        logger.warning(f"DELETE task id={instance.id} by user={request.user}")
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

