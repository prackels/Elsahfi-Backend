# New Customer:
- `sequence` [PK]
- `customer_name` [Char]
- `phone_number` [PhoneNum]
- `financial_advance` [Float]
- `payment_date` [Date]
- `date_of_payment` [Date]
- `date` [Date] **Auto**
- `time` [Time] **Auto**
- `day` [Day] **Auto**
- `comments` [Text]

## Create a New Customer
### Endpoint : /clients/customer/create/
### method : POST
### permissions : admin user

## Update the data of clients
### Endpoint : /clients/customer/update/<int:pk>/
### method : PUT
### permissions : admin user

## Get All Clients
### Endpoint : /clients/customer/get/
### method : GET
### permissions : admin user

## Delete data from clients
### Endpoint : clients/customer/delete/<int:pk>/
### method : DELETE
### permissions : admin user

***

# Cars Of The Client
- `customer` [Char] **Relation With New Customer**
- `car_code` [Int]
- `car_type` [Char]
- `car_plate` [Char]

## Create Car
### Endpoint : /clients/car/create/
### method : POST
### permissions : admin user

## Update Car
### Endpoint : /clients/car/update/<int:pk>/
### method : PUT
### permissions : admin user

## Get Car
### Endpoint : /clients/car/get/
### method : GET
### permissions : admin user

## Delete Car
### Endpoint : clients/car/delete/<int:pk>/
### method : DELETE
### permissions : admin user

***
# Subjects Of The Client
- `customer` [Char] **Relation With New Customer**
- `subject_name` [Choices] **Premium Gasoline 91, Premium Gasoline 95, Diesel**
- `price_per_liter` [Char]

## Create Subject
### Endpoint : /clients/subject/create/
### method : POST
### permissions : admin user

## Update Subject
### Endpoint : /clients/subject/update/<int:pk>/
### method : PUT
### permissions : admin user

## Get Subject
### Endpoint : /clients/subject/get/
### method : GET
### permissions : admin user

## Delete Subject
### Endpoint : clients/subject/delete/<int:pk>/
### method : DELETE
### permissions : admin user

***
# Blocked & Pended Clients:
### clients/new-customer/block/<int:pk>/
### clients/new-customer/unblock/<int:pk>/
### clients/new-customer/pend/<int:pk>/
### clients/new-customer/unpend/<int:pk>/
### Method: POST
### Permissions : admin user


