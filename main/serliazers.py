from rest_framework import serializers
from main.models import Organization, Contact, Product
from main.validators import IfFactoryToZeroValidator


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'model', 'date', 'organization']
        extra_kwargs = {'organization': {'required': True}}


class OrganizationSerializer(serializers.ModelSerializer):
    contact = ContactSerializer()
    """
    Сериализатор Организации
    """
    class Meta:
        model = Organization
        fields = '__all__'
        validators = [IfFactoryToZeroValidator(field='__all__')]

    def create(self, validated_data):
        """
        Создает привычку
        :param validated_data:
        :return:
        """
        contact_data = validated_data.pop('contact')
        try:
            if Contact.objects.get(email=contact_data["email"]):
                contact = Contact.objects.get(email=contact_data["email"])
        except:
            contact = Contact.objects.create(**contact_data)

        user = self.context['request'].user  # получаем авторизированного пользователя
        organization = Organization(contact=contact, **validated_data)
        organization.user = user  # устанавливаем пользователя

        if organization.type_of_organization == "factory":  # если организация - завод, то ранг 0
            organization.rang = 0
        elif organization.parent:       # если нет - ранг на один больше чем ранг поставщика
            organization.rang = organization.parent.rang + 1

        organization.save()  # сохраняем объект
        return organization

    def update(self, instance, validated_data):
        # Удалите поле 'arrears', если оно есть в validated_data
        if 'arrears' in validated_data:
            del validated_data['arrears']

        # Вызовите родительский метод update() для обновления модели
        return super().update(instance, validated_data)
