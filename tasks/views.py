# add view for task model 
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
# add view for user
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from rest_framework import status
# add permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
#add filter for tasks
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# add view for task model 
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.select_related('category').all()  # optimizing django queries

    serializer_class = TaskSerializer
    # add permission
    permission_classes = [AllowAny]

    #add filter for tasks
    filter_backends = [DjangoFilterBackend,filters.SearchFilter , filters.OrderingFilter]
    #add filter on fields
    filterset_fields = ['completed']
    #add search on title and description
    search_fields = ['title' , 'description']
    #add  filter craeted date
    ordering_fields = ['created_at']
# add view for user
@api_view(['POST'])
def register_user(request):
    serializer = UserSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    



