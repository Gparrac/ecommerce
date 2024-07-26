from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # record or update
        fields = '__all__'
    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user   

    def update(self, instance, validated_data):
        updated_user = super().update(instance, validated_data)
        updated_user.set_password(validated_data['password'])
        updated_user.save()
        return updated_user   


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
            model = User
    def to_representation(self, instance):
        #to show data throught a custom way in serializer
        return {
            'id': instance['id'],
            'username': instance['username'],
            'password': instance['password'],
            'email': instance['email']
        }

class TestUserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 200)
    email = serializers.EmailField()    
    # to create custom validations we should resubcribe validate_[attribute's name]
    def validate_name(self, value):
        if 'develop' in value:
            print('entry')
            raise serializers.ValidationError('Error')        
        return value
    def validate_email(self, value):
        if self.context['name'] in value:
            raise serializers.ValidationError('El nombre no puede estar en el email')
        return value
    def validate(self, data):
        return data
    # Create method to define actions in save model
    
    def create(self, validated_data):
        # All information validated
        print(validated_data)
        ## return a model class with validated data without keys
        # return User(**validated_data)
        return User.objects.create(**validated_data)
    def update(self, instance, validated_data):
        # define custom validations for update actions
        instance.name = validated_data.get('name', instance.name)
        instance.update = validated_data.get('email', instance.email)
        # refer to save method of model
        
        instance.save()
        return instance
    # def save(self):
        # quite useful to handle data without save records or appent logic after validations