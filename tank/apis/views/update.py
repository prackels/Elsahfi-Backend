from rest_framework import status, decorators, permissions
from rest_framework.response import Response
from tank.apis.serializer import TankSerializer, Tank, TankSpecificUpdates
from trumpet.models import Trumpet


@decorators.api_view(['PUT'])
@decorators.permission_classes([permissions.IsAdminUser])
def UpdateTank (request, tankid) : 
    try :

        material = request.data.get('material')
        
        try : 
            tank = Tank.objects.get(id=tankid)
        except Tank.DoesNotExist :
            return Response({
                'message' : "tank not found"
            },status=status.HTTP_404_NOT_FOUND)
        
        serializer = TankSerializer(tank,data=request.data)
        old_trumpets_count= tank.trumpets_count
        

        if serializer.is_valid() :
            if Tank.objects.filter(material=material).exclude(id=tankid).exists() : 
                return Response(
                    {"message":"the tank with this material already exists!"}
                ,status=status.HTTP_400_BAD_REQUEST)
            else:
                new_trumpets_count = request.data.get('trumpets_count')
                the_difference= int(new_trumpets_count) - int(old_trumpets_count)
            if the_difference > 0:
                for x in range(1, the_difference + 1):
                    Trumpet.objects.create(
                        name=f'الطرومبه {old_trumpets_count + x}',
                        tank=tank,
                        subject_name=tank.material,
                    )
            elif the_difference < 0:
                    difference = abs(the_difference)
                    trumpets_to_delete = Trumpet.objects.filter(tank=tank, subject_name= tank.material).order_by('trumpet_number')[:difference]
                    for trumpet in trumpets_to_delete:
                        trumpet.delete()

            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Exception as error :
        return Response({
            'message' : f'an error occurred : {error}'
        },status=status.HTTP_400_BAD_REQUEST)
    


@decorators.api_view(['PUT'])
@decorators.permission_classes([permissions.IsAdminUser])
def specify_update (request, tankid) : 
    try : 
        try : 
            tank = Tank.objects.get(id=tankid)
        except Tank.DoesNotExist :
            return Response({
                'message' : 'tank not found'
            },status=status.HTTP_404_NOT_FOUND)
        
        serializer = TankSpecificUpdates(tank,data=request.data)

        if serializer.is_valid() : 
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            

    except Exception as error :
        return Response({
            'message' : f'an error accoured : {error}'
        },status=status.HTTP_400_BAD_REQUEST)
    

@decorators.api_view(['PUT'])
@decorators.permission_classes([permissions.IsAdminUser])
def UpdateTankTwoField (request) : 
    try :

        tank_name = request.data.get('tank_name',None)
        tank_standard = request.data.get('tank_standard',None)
        returned = request.data.get('returned',None) 

        if tank_name is None or tank_standard is None or returned is None: 
            return Response({
                'message' : "tank_name or tank_standard or returned cannot be empty"
            },status=status.HTTP_400_BAD_REQUEST)
        
        try : 
            tank = Tank.objects.get(tank_name=tank_name)
        except Tank.DoesNotExist :
            return Response({
                'message' : "tank with this name not found"
            },status=status.HTTP_404_NOT_FOUND)
        
        tank.returned = returned
        tank.tank_standard = tank_standard
        tank.save()

        serializer = TankSerializer(tank)
        return Response(serializer.data,status=status.HTTP_200_OK)

    except Exception as error :
        return Response({
            'message' : f'an error accured : {error}'
        },status=status.HTTP_400_BAD_REQUEST)
