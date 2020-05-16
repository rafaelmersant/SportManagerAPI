from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import User
from .serializers import UserSerializer
import json


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 20


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'email', 'name',
                        'user_role', 'user_hash',
                        'creation_date', 'athlete_id']

    def delete(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
            user.delete()
        # except User.DoesNotExist:
        #     return Response("user does not exist",
        #                     status=status.HTTP_404_NOT_FOUND)
        except:
            return Response("the user was not found",
                            status=status.HTTP_400_BAD_REQUEST)

        return Response("deleted", status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogin(generics.ListCreateAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            email = body['email']
            password = body['password']

            user = User.objects.filter(email=email, password=password)
            if user.count() > 0:
                return Response({"id": user[0].id,
                                 "email": user[0].email,
                                 "name": user[0].name,
                                 "role": user[0].user_role,
                                 "athlete_id": user[0].athlete_id
                                 },
                                status=status.HTTP_200_OK)

            return Response("null", status=status.HTTP_404_NOT_FOUND)

        # except User.DoesNotExist:
        #     return Response("Not Found", status=status.HTTP_404_NOT_FOUND)
        except:
            return Response("Bad Request",
                            status=status.HTTP_400_BAD_REQUEST)
