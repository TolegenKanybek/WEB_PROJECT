from rest_framework import serializers

from django.contrib.auth.models import User

from core.models import Category





class CategorySerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)

    name = serializers.CharField(required=True)



    def create(self, validated_data):

        # {'name': 'new category 4'}

        # name='new category 4'

        category = Category(**validated_data)

        category.save()

        return category



    def update(self, instance, validated_data):

        instance.name = validated_data.get('name', instance.name)

        instance.save()

        return instance





class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = ('id', 'username', 'email',)





class CategorySerializer2(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)

    name = serializers.CharField(required=True)

    created_by = UserSerializer(read_only=True)



    class Meta:

        model = Category

        fields = ('id', 'name', 'created_by',)

        # fields = '__all__'





class ProductSerializer(serializers.Serializer):

    id = serializers.IntegerField()

    name = serializers.CharField()

    price = serializers.FloatField()

    count = serializers.IntegerField()

    category = CategorySerializer()