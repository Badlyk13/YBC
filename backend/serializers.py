from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

    def get_field_names(self, declared_fields, info):
        expanded_fields = super(ProfileSerializer, self).get_field_names(declared_fields, info)

        if getattr(self.Meta, 'extra_fields', None):
            return expanded_fields + self.Meta.extra_fields
        else:
            return expanded_fields
