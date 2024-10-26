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
        # can access as a dict's key if use values() in ORM but if it uses just all(), it would be such as obj attribute (instance.id)
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
        print('name', value)
        if 'develop' in value:
            print('entry')
            raise serializers.ValidationError('Error')        
        return value
    def validate_email(self, value):                
        # to use context we need to pass as a further parameter in serializer's instance
        name = self.context['name']        
        name = self.validate_name(name)
        print('attributes===', name, value)
        # the name's called by validate_name to get the validated name
        if name in value:
            raise serializers.ValidationError('El nombre no puede estar en el email')
        return value
    def validate(self, data):
        return data
    
    # Create method to define actions when save() is called
    def create(self, validated_data):
        # All  validated information
        print(validated_data)
        ## return a model class with validated data without keys
        # return User(**validated_data)
        return User.objects.create(**validated_data)
    def update(self, instance, validated_data):
        # define custom validations for update actions
        print('other update?')
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        # refer to save method of model and  .save in view refers to serializer method
        
        instance.save()
        return instance
    # def save(self):
        # quite useful to handle data without save records or append logic after validations