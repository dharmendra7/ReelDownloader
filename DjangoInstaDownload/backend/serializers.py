from rest_framework import serializers

class LinkSerializer(serializers.Serializer):
    link = serializers.CharField(max_length=255)


# class ImageSerializer(serializers.Serializer):
#     images =

class ReelResponse(serializers.Serializer):
    responseCode = serializers.IntegerField()
    responseMessage = serializers.CharField()
    responseData = serializers.CharField()

class errorResponse(serializers.Serializer):
    responseCode = serializers.IntegerField()
    responseMessage = serializers.CharField()

