from rest_framework import decorators, permissions, status
from rest_framework.response import Response
from globals.search import Search


"""
Algo for search :
    1. get the list of choices categories [Cars, employeies, etc...]
    2. get the keyword 
    3. search by category
        - just need keyword and which category to search
    4. if sub_categories not empty then search on each sub_category
"""

"""
When post data in search endpoint
{
    "keyword" : "Radwan",
    "categories" : [
        "employees",
        "supplier",
        "clients"
    ],
    "sub_categories" : [
        "station"   
    ]
}

"""

@decorators.api_view(['POST'])
@decorators.permission_classes([permissions.IsAdminUser])
def SearchView (request) : 
    try : 
        
        categories = request.data.get('categories',None)
        sub_categories = request.data.get('sub_categories',[])
        keyword = request.data.get('keyword',None)
        date_from = request.data.get('date_from',None)
        date_to = request.data.get('date_to',None)
        data = []


        if keyword is None :
            return Response({
                'message' : 'plases insert keyword for search'
            },status=status.HTTP_400_BAD_REQUEST)
        
        
        if not categories : 
            search = Search(
                keyword = keyword,
            )

            search.search_all()
            search_result = {
                'keyword' : keyword,
                'result_counter' :len(search.data),
                'data' : search.data 
            }


            return Response(search_result,status=status.HTTP_200_OK)


        for category in categories :

            data += Search(keyword=keyword, category=category,date_to=date_to,date_from=date_from).search_category()

            if sub_categories != []:
                for  sub_category in sub_categories :
                    data += Search(keyword=keyword,category=category,date_to=date_to,date_from=date_from).search_category_subcategory(sub_category=sub_category)


        data = data if len(data) > 0 else ''
        
        return Response(data,status=status.HTTP_200_OK)


    except Exception as error : 
        return Response({
            'message' : f'an error accured : {error}'
        },status=status.HTTP_400_BAD_REQUEST)