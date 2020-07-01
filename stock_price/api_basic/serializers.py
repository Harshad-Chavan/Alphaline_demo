from rest_framework import serializers


class PriceSerializer(serializers.Serializer):
    nseprice = serializers.FloatField()
    bseprice = serializers.FloatField()
    diffprice = serializers.FloatField()
    timestamp = serializers.CharField()
    
    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            print(field,value)
            setattr(instance, field, value)
        return instance