from api.models import User, Teacher
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'url',
            'username',
            'first_name',
            'last_name',
            'email',
            'is_student',
            'is_teacher'
        )


    def update(self, instance, validated_data):
        if instance.is_teacher and instance.username != validated_data.get('username'):
            print("got here")
            instance.username = validated_data.get('username')
            instance.save()
            teacher = instance.teacher
            teacher.generate_key()
            teacher.save()

        instance.first_name = validated_data.get("first_name")
        instance.last_name = validated_data.get("last_name")
        instance.email = validated_data.get("email")
        instance.save()
        print(instance.username)
        print(validated_data.get('username'))
        return instance