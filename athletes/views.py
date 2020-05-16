from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import Athlete, Parent, Document
from .serializers import AthleteSerializer, ParentSerializer, \
    DocumentSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10


class StandardResultsSetPaginationLevel2(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 20


class AthleteListFull(generics.ListCreateAPIView):
    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'first_name', 'last_name', 'email',
                        'phone_number', 'medical_information', 'category',
                        'parent', 'document']
    search_fields = ['first_name', 'last_name', 'phone_number', 'email']


class AthleteList(generics.ListCreateAPIView):
    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'first_name', 'last_name', 'email',
                        'phone_number', 'medical_information', 'category',
                        'parent', 'document']
    search_fields = ['first_name', 'last_name', 'phone_number', 'email']

    def delete(self, request, pk=None):
        try:
            athlete = Athlete.objects.get(pk=pk)
            athlete.delete()
        # except ObjectDoesNotExists:
        #     return Response("Not Found", status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response("Internal Error",
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response("deleted", status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        athlete = Athlete.objects.get(pk=pk)
        serializer = AthleteSerializer(athlete, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ParentList(generics.ListCreateAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'name', 'phone_number', 'email', 'athlete_id']
    search_fields = ['name', 'phone_number', 'email', 'athlete_id']

    def delete(self, request, pk=None):
        try:
            parent = Parent.objects.get(pk=pk)
            parent.delete()
        # except Parent.DoesNotExists:
        #     return Response("Not Found", status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response("Internal Error",
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response("deleted", status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        parent = Parent.objects.get(pk=pk)
        serializer = ParentSerializer(parent, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DocumentList(generics.ListCreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    # pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'title', 'document_filename', 'athlete_id']
    search_fields = ['title', 'document_filename', ]

    def delete(self, request, pk=None):
        try:
            document = Document.objects.get(pk=pk)
            document.delete()
        # except Document.DoesNotExists:
        #     return Response("Not Found", status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response("Internal Error",
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response("deleted", status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        document = Document.objects.get(pk=pk)
        serializer = DocumentSerializer(document, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
