from dataclasses import field
from turtle import st
from rest_framework import serializers

from .models import Hobby, Person, Reunion

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('__all__')


#Serializador sin un modelo ligado
class PersonaSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    full_name=serializers.CharField()
    job = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()

    #agregando un atributo extra al modelo
    activo = serializers.BooleanField(required=False)#Tambien se puede usar default=False


#Si quiero agregar atributos con un serializador enlazado a un modelo
class PersonSerializer(serializers.ModelSerializer):

    activo = serializers.BooleanField(default=False)

    class Meta:
        model = Person
        fields = ('__all__')


#Para modelos con relacion 1:n
class ReunionSerializer(serializers.ModelSerializer):

    persona = PersonSerializer()

    class Meta:
        model = Reunion
        fields = (
            'id',
            'fecha',
            'hora',
            'asunto',
            'persona',
        )


class HobbySerializer(serializers.ModelSerializer):

    class Meta:
        model = Hobby
        fields = ('__all__')

        
#Para modelos con relacion N:M
class PersonSerializer2(serializers.ModelSerializer):

    hobbies = HobbySerializer(many=True)

    class Meta:
        model = Person
        fields = (
            'id',
            'full_name',
            'job',
            'email',
            'phone',
            'hobbies',
        )


# Metodos de los serializer para operar con los atributos del modelo, en este caso, concatenamos la fecha y hora
class ReunionSerializer2(serializers.ModelSerializer):

    fecha_hora = serializers.SerializerMethodField()

    class Meta:
        model = Reunion
        fields = (
            'id',
            'fecha',
            'hora',
            'asunto',
            'persona',
            'fecha_hora'
        )

    #obj hace referencia al registro(objeto) que se esta iterando en el json
    def get_fecha_hora(self,obj):
        return str(obj.fecha) + ' - ' + str(obj.hora)