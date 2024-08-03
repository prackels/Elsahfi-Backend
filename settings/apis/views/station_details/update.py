from rest_framework import decorators, status, permissions
from rest_framework.response import Response
from ...serializers import StationDetails, StationDetailsSerializers


@decorators.api_view(['PUT'])
@decorators.permission_classes([permissions.IsAdminUser])
def UpdateStationDetails (request, station_details_id) : 
    try :
        try : 
            query = StationDetails.objects.get(id=station_details_id)
        except StationDetails.DoesNotExist:
            return Response({
                'message' : "not found"
            },status=status.HTTP_404_NOT_FOUND)
        
        serializer = StationDetailsSerializers(query,data=request.data)
        
        if serializer.is_valid() : 
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    except Exception as error :
        return Response({
            'message' : f'an error accured : {error}'
        },status=status.HTTP_400_BAD_REQUEST)