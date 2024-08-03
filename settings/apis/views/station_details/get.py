from rest_framework import decorators, permissions, status
from rest_framework.response import Response
from ...serializers import StationDetailsSerializers, StationDetails


@decorators.api_view(['GET'])
@decorators.permission_classes([permissions.IsAdminUser])
def GetAllStationDetails (request) :
    try : 
        query = StationDetails.objects.all()
        serializer = StationDetailsSerializers(query,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    except Exception as error : 
        return Response({
            'message' : f'an error accoured : {error}'
        },status=status.HTTP_400_BAD_REQUEST)
    

@decorators.api_view(['GET'])
@decorators.permission_classes([permissions.IsAdminUser])
def GetStationDetails (request,station_details_id) :
    try : 

        try :
            query = StationDetails.objects.get(id=station_details_id)
        except StationDetails.DoesNotExist :
            return Response({
                'message' : 'not found'
            },status=status.HTTP_404_NOT_FOUND)
        
        serializer = StationDetailsSerializers(query)
        return Response(serializer.data,status=status.HTTP_200_OK)
    except Exception as error : 
        return Response({
            'message' : f'an error accoured : {error}'
        },status=status.HTTP_400_BAD_REQUEST)

