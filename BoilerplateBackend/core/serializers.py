from django.contrib.auth import get_user_model
from rest_framework import serializers, validators

CustomUser = get_user_model()

class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.CharField(
        write_only=False, validators=[validators.UniqueValidator(
            message='This email already exists',
            queryset=CustomUser.objects.all()
        )]
    )
    password= serializers.CharField(write_only=True)
    birth_date= serializers.CharField(required=False)
    bio= serializers.CharField(required=False)
    gender= serializers.CharField(required=False)
    last_name= serializers.CharField(required=False)
    first_name= serializers.CharField(required=False)
    birth_date= serializers.CharField(required=False)
    user_type= serializers.CharField(required=True)
    especiality_area = serializers.CharField(required=False)

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'password',
                'bio', 'gender', 'birth_date', 'user_type', 'especiality_area', 'id')


class CustomUserRetrieveSerializer(serializers.ModelSerializer):
    birth_date = serializers.CharField(required=False)
    bio = serializers.CharField(required=False)
    gender = serializers.CharField(required=False)
    user_type= serializers.CharField(required=True)
    especiality_area = serializers.CharField(required=False)

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'password',
                'bio', 'gender', 'birth_date', 'user_type', 
                'especiality_area', 'id')
