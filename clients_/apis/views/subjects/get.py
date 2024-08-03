from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from ....models import Subjects, NewCustomer
from ...serializers import SubjectsSerializer, CustomersSubjectsSerializer

@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_subjects(request):
    try:
        subjects_data = []
        customers = NewCustomer.objects.all()
        for customer in customers:
            subjects = Subjects.objects.filter(customer=customer)
            subjects_serializer = SubjectsSerializer(subjects, many=True)
            subjects_data.append({
                'customer': customer.customer_name,
                'subjects': subjects_serializer.data
            })
        total_subjects = Subjects.objects.all().count()
        response_data = {
            'subjects_data': subjects_data,
            'total_subjects': total_subjects
        }
        return Response(response_data, status=HTTP_200_OK)
    except Exception as error:
        return Response(f"Sorry, there was a problem while getting the data: {error}", status=HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_all_subjects(request):
    try:
        subjects = Subjects.objects.all()
        total_subjects = Subjects.objects.all().count()
        serializer = CustomersSubjectsSerializer(subjects, many=True)
        return Response({
            "data": serializer.data,
            "total_subjects": total_subjects
        }, status=HTTP_200_OK)
    except Exception as e:
        return Response({
            "message": "an error occurred while getting all subjects"
        }, status=HTTP_400_BAD_REQUEST)