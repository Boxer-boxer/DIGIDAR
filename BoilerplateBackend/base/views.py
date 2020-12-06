from django.shortcuts import render
from .models import Contest
from .serializers import ContestSerializer 
from rest_framework import permissions, viewsets


class ContestViewSet(viewsets.ModelViewSet):
    queryset = Contest.objects.all()
    serializer_class = ContestSerializer
    #Update permissions so that only owners can update
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)