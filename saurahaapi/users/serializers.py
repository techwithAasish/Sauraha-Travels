from rest_framework import serializers
from users.models import NewUser


class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(min_length=8)

    class Meta:
        model = NewUser
        fields = ('email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    # def clean(self):
    #     email = self.clean_data['email']
    #     if NewUser.objects.exclude(pk=self.instance.pk).filter(email=email).exists():        except NewUser.DoesNotExist:
    #         return ("User already exists")


# extra
