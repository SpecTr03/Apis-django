from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, RetrieveUpdateAPIView

from .models import Person, Reunion
from .serializers import PersonSerializer, PersonaSerializer, ReunionSerializer, PersonSerializer2, ReunionSerializer2

class ListaPersonas(ListView):
    template_name = 'persona/list_personas.html'
    context_object_name = 'personas'

    def get_queryset(self):
        return Person.objects.all()


class PersonListApiView(ListAPIView):

    serializer_class = PersonSerializer

    def get_queryset(self):
        return Person.objects.all()


class PersonListView(TemplateView):
    template_name = 'persona/lista.html'


class PersonSearchApiView(ListAPIView):
    serializer_class = PersonSerializer

    def get_queryset(self):
        kword = self.kwargs['kword']
        return Person.objects.filter(
            full_name__icontains=kword
        )


class PersonCreateView(CreateAPIView):
    serializer_class = PersonSerializer


class PersonDetailView(RetrieveAPIView):

    serializer_class = PersonSerializer
    queryset = Person.objects.filter()


class PersonDeleteView(DestroyAPIView):

    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class PersonUpdateView(UpdateAPIView):

    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class PersonRetrieveUpdateView(RetrieveUpdateAPIView):

    serializer_class = PersonSerializer
    queryset = Person.objects.all()


#Serializador sin modelo relacionado
class PersonaApiListView(ListAPIView):

    serializer_class = PersonaSerializer

    def get_queryset(self):

        return Person.objects.all() 


class ReunionApiLista(ListAPIView):
    serializer_class =  ReunionSerializer

    def get_queryset(self):
        return Reunion.objects.all()


class PersonaHobbiesView(ListAPIView):

    serializer_class = PersonSerializer2

    def get_queryset(self):
        return Person.objects.all()


class ReunionApiLista(ListAPIView):
    serializer_class =  ReunionSerializer2

    def get_queryset(self):
        return Reunion.objects.all()