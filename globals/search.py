from employee.models import Car, Employee
from employee.apis.serializers import CarSerializer, EmployeeSerializer

from repository_.models import Repository
from repository_.apis.serializers import RepositorySerializer

from new_purchase.models import NewSupplier
from new_purchase.apis.serializers import NewSupplierSerializer

from clients_ import models as client_models
from clients_.apis import serializers as client_serializers

from trumpet import models as trumpet_models
from trumpet.apis.serializers import TrumpetSerializer

from expenses import models as expenses_models
from expenses.apis.serializers import GovernmentExpSerializer, StationExpSerializer

from customer_orders import models as customer_orders_models
from customer_orders.apis import serializers as customer_orders_serializers

from .reports import cars, customer



class Search:
    
    def __init__(self, keyword,category=None, date_from=None,date_to=None) : 
        self.data = []
        self.keyword = keyword
        self.category = category
        self.date_from = date_from
        self.date_to = date_to
        self.count_results = 0
        
    
    def search_all (self) : 
        categories = ["CustomerStation","TrillaCustomer",'DeiannaCustomer']
        for category in categories : 
            self.serach_on_customer_orders(category)
        


    def serach_on_customer_orders (self, category) :

        if category == "CustomerStation" : 
            model = customer_orders_models.CustomerStation

        if category == "TrillaCustomer" :
            model = customer_orders_models.TrillaCustomer

        if category == "DeiannaCustomer" :
            model = customer_orders_models.DeiannaCustomer


        results = model.objects.filter(customer_name__icontains=self.keyword)
        
        for result in results :
            customer_count = customer_orders_models.CustomerStation.objects.filter(customer_name=result.customer_name).count()
            deina_count = customer_orders_models.DeiannaCustomer.objects.filter(customer_name=result.customer_name).count()
            trilla_count = customer_orders_models.TrillaCustomer.objects.filter(customer_name=result.customer_name).count()
            total = customer_count + deina_count + trilla_count

            self.data.append({
                'name' : result.customer_name,
                "CustomerStation" : customer_count,
                "DeiannaCustomer" : deina_count,
                "TrillaCustomer" : trilla_count,
                "total" : total,
            })


    def search_category(self) : 
        if self.category == 'cars' :
            self.send_serialized_data(
                queryset = Car.objects.filter(car_name__icontains=self.keyword),
                serializer_class = CarSerializer,
                array_key = self.category
            )

        if self.category == 'employees' :
            self.send_serialized_data(
                queryset = Employee.objects.filter(name__icontains=self.keyword),
                serializer_class = EmployeeSerializer,
                array_key = self.category
            )
        
        if self.category == 'repository' : 
            self.send_serialized_data(
                queryset = Repository.objects.filter(product_name__icontains=self.keyword),
                serializer_class = RepositorySerializer ,
                array_key = self.category
            )

        if self.category == 'supplier' :
            self.send_serialized_data(
                queryset = NewSupplier.objects.filter(supplier_name__icontains=self.keyword),
                serializer_class = NewSupplierSerializer ,
                array_key = self.category
            )

        if self.category == 'trumpets' : 
            self.trumpets()

        # if self.category == 'final_report' :
        #     self.search_final_reports() 


        return self.data

    def search_category_subcategory (self, sub_category) : 
        
        if self.category == 'clients' : 
            self.clients(sub_category=sub_category)

        if self.category == 'trumpets' : 
            self.trumpets()

        if self.category == 'expenses' : 
            self.expenses(sub_category=sub_category)
        
        return self.data
    
    def clients (self, sub_category) :
        
        if sub_category == 'station' : 
            self.send_serialized_data(
                array_key = sub_category,
                queryset = customer_orders_models.CustomerStation.objects.filter( customer_name__icontains= self.keyword ),
                serializer_class = customer_orders_serializers.CustomerStationSerializer
            )


        if sub_category == 'terilla' : 
            self.send_serialized_data(
                array_key = sub_category,
                queryset = customer_orders_models.TrillaCustomer.objects.filter( customer_name__icontains = self.keyword ),
                serializer_class = customer_orders_serializers.TrillaCustomer
            )


        if sub_category == 'deina': 
            self.send_serialized_data(
                array_key = sub_category,
                queryset = customer_orders_models.DeiannaCustomer.objects.filter( customer_name__icontains = self.keyword ),
                serializer_class = customer_orders_serializers.DeiannaCustomerSerializer
            )
            

        if sub_category == 'blocked': 
            self.send_serialized_data(
                array_key = sub_category,
                queryset = client_models.NewCustomer.objects.filter(status=sub_category,customer_name__icontains = self.keyword,blocked=True),
                serializer_class = client_serializers.NewCustomerSerializer
            )

        if sub_category == 'pending': 
            self.send_serialized_data(
                array_key = sub_category,
                queryset = client_models.NewCustomer.objects.filter(status=sub_category,customer_name__icontains = self.keyword,pending=True),
                serializer_class = client_serializers.NewCustomerSerializer
            )

    def trumpets (self) : 
        self.send_serialized_data(
            array_key = "Trumpets",
            queryset = trumpet_models.Trumpet.objects.filter(name__icontains = self.keyword ),
            serializer_class = TrumpetSerializer
        )


    def expenses (self, sub_category) : 
        if sub_category == 'station' : 
            self.send_serialized_data(
                array_key = sub_category,
                queryset = expenses_models.StationExpense.objects.filter( name__icontains = self.keyword ),
                serializer_class = StationExpSerializer
            )

        if sub_category == 'government' : 
            self.send_serialized_data(
                array_key = sub_category,
                queryset = expenses_models.GovernmentExpense.objects.filter( name__icontains = self.keyword ),
                serializer_class = GovernmentExpSerializer
            )
    

    def send_serialized_data (self, queryset, serializer_class, array_key) : 
        if self.date_from != None and self.date_to != None :
            queryset = queryset.filter(created_at__range=[self.date_from, self.date_to])
        serializer =  serializer_class(queryset,many=True)
        self.data.append(
            { 'data' : serializer.data }
        )