from rest_framework import serializers
from .models import Student


class StudentSerialization(serializers.ModelSerializer):
    #First Priority 
    #Validators
    def starts_with_r(value):
        if value[0].lower() != 'r':
            raise serializers.ValidationError("Name Should be start with R")
    name = serializers.CharField(validators=[starts_with_r]) #this is single field validation
    class Meta:
        model = Student
        fields = ['id','name','roll','city']
        # read_only_fields = ['name','roll'] #this method is apply to the multiple fields for same validation
        # extra_kwargs = {'name':{'read_only':True},'roll':{'read_only':True}} #this method is apply to validate the multiple fields with multiple validation


    #Second Priority
    #Field level Validations
    def validate_roll(self,value):
        if value >= 200:
            raise serializers.ValidationError("Seat Full")
        return value

    #Third priority 
    #Object Level Validation
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm == 'Rohit' and ct != 'Surat':
            raise serializers.ValidationError("City Must be Surat")
        return data



