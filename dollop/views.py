from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import UserSerializer, GetUserSerializer, EntrySerializer, GetEntrySerializer
from .models import Entry


@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = GetUserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        new_user = serializer.save()

        try:
            user = User.objects.create_user(username=new_user['username'],
                                            password=new_user['password'])
        except:
            return Response({"detail": "user with email already exists"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = GetUserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@authentication_classes([TokenAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def logout(request):
    request.auth.delete()
    return Response({"detail": "logged out successfully"}, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def entry_list(request):
    """
    List entries or create a new entry
    """
    if request.method == 'GET':
        entries = Entry.objects.filter(user_id=request.user.id)
        serializer = GetEntrySerializer(entries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "POST":
        serializer = EntrySerializer(data=request.data)
        if serializer.is_valid():
            new_entry = serializer.save()
            entry = Entry.objects.create(user_id=request.user.id,
                                         value=new_entry['value'])
            serializer = GetEntrySerializer(entry)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
