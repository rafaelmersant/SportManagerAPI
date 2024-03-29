from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import User, Document
from .serializers import UserSerializer, UserInfoSerializer, DocSerializer
import json
import sys


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 20


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'email', 'name',
                        'user_role', 'user_hash',
                        'creation_date', 'athlete_id']
    search_fields = ['name', 'email']

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


class UserInfo(generics.ListCreateAPIView):
    serializer_class = UserInfoSerializer

    def post(self, request):
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            userId = int(body['id'])

            user = User.objects.get(id=userId)
            if user != None:
                return Response({"id": user.id,
                                 "email": user.email,
                                 "password": user.password,
                                 "name": user.name,
                                 "user_role": user.user_role,
                                 "user_hash": user.user_hash,
                                 "athlete_id": user.athlete_id,
                                 "created_user": user.created_user,
                                 "creation_date": user.creation_date
                                 },
                                status=status.HTTP_200_OK)

            return Response("null", status=status.HTTP_404_NOT_FOUND)

        # except User.DoesNotExist:
        #     return Response("Not Found", status=status.HTTP_404_NOT_FOUND)
        except:
            return Response(sys.exc_info()[0],
                            status=status.HTTP_400_BAD_REQUEST)


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


class DocumentList(generics.ListCreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'description', 'category',
                        'source', 'creation_date', ]

    def delete(self, request, pk=None):
        try:
            doc = Document.objects.get(pk=pk)
            doc.delete()
        except:
            return Response("the document was not found",
                            status=status.HTTP_400_BAD_REQUEST)

        return Response("deleted", status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        doc = Document.objects.get(pk=pk)
        serializer = DocSerializer(doc, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
