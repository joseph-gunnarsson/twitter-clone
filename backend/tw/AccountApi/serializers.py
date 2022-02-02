from dataclasses import field
import email
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .models import Following


class LoginSerializer(serializers.Serializer):
    password=serializers.CharField()
    email=serializers.CharField()
    class Meta:
        field=["password","email"]
    def validate(self, data):
        self.user=authenticate(username=data["email"],password=data["password"])
        if not self.user:
            raise serializers.ValidationError({"Invalid": ["User with the credentials does not exist"]})


        return data
    def getUser(self):
        return self.user
    
    def create(self, validated_data):
        user=User.objects.get(username=validated_data.username)
        user.set_password(validated_data.password)
        user.save()
        return user

        
    
    
class updateFollow(serializers.ModelSerializer):
    class Meta:
        model=Following
        fields=["user_id","following_user"]
    def create(self, validated_data):
        try:
            following=Following.objects.get(used_id=validated_data.user_id,following_user=validated_data.following_user)
            following.delete()
            
        except:
            following=Following(used_id=validated_data.user_id,following_user=validated_data.following_user)
            following.save()



    

class SignUpUserSerializer(serializers.ModelSerializer):
    confirmemail=serializers.EmailField()
    confirmpassword=serializers.CharField(max_length=50)
    class Meta:
        model=User
        fields=['email', 'username', 'password','confirmemail','confirmpassword']
        extra_kwargs = {'password': {'write_only': True}}
    def validate_email(self,value):
        confirmemail=self.initial_data.get("confirmemail")
        error=None
        if  confirmemail and value==confirmemail:
            try:
                print("hello")
                user=User.objects.get(email__exact=confirmemail)  
                error= serializers.ValidationError(["A user with that email already exists."])
            except Exception as e:
                return value       
        raise serializers.ValidationError(["Email does not match."]) if not error else error
    def validate_password(self,value):
        confirmpassword=self.initial_data.get("confirmpassword")
        if  value==confirmpassword:
            return value
        else:
            raise serializers.ValidationError(["Password does not match."])
    def create(self, validated_data):
        print=(validated_data)
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

