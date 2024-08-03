### Customer Station
- `sequence` [PK]
- `customer_name` [Char]  **Relation With New Customer**
- `phone_number` [Phone-number]
- `previous_quantity` [Float]
- `subject_name` [choices] **Premium Gasoline 91| Premium Gasoline 95| Diesel**
- `quantity` [Float]
- `price_per_litre` [Float] **Price From Customer Relation** 
- `total` [Float]
- `packing_method` [Char]
- `payment_method` [Char] **Cash| Visa| Deposit**
- `car_type` [Char]
- `car_plate` [Char]
- `driver` [Char]
- `car_photo` [Img]
- `invoice_photo` [Img]
- `invoice_number` [Int]
- `date` [Date]
- `time` [Time]
- `day` [Char]
- `comments` [Text]
- `invoice_sequence` [Int]
- `edited` [Bool] **دي اللي شرحتهالك**



## Get all Customer Station:
## Endpoint : /customers-orders/customer-station/get/
## method : GET
## permissions : admin user

## create a Customer Station
## Endpoint : /customers-orders/customer-station/create/
## method : POST
## permissions : admin user

## Update the data of Customer Station
## Endpoint : /customers-orders/customer-station/delete/<int:pk>/
## method : PUT
## permissions : admin user

## Delete data from Customer Station
## Endpoint : /customers-orders/customer-station/delete/<int:pk>
## method : DELETE
## permissions : admin user




### Trilla Customer

- `sequence` [PK]
- `customer_name` [Char] **Relation With New Customer**
- `phone_number` [Phone-number]
- `subject_name` [choices]
- `previous_quantity` [Float]
- `quantity` [Float]
- `secret_counter` [Float]
- `price_per_litre` [Float]
- `total` [Float]
- `payment_method` [Choices]
- `packing_method` [Char]
- `checkout_counter` [Int]
- `time_to_go_out` [Time]
- `client_station_name` [Char]
- `its_location` [Char]
- `coordinates` [Char]
- `car_type` [Relation] **هنا هتحط الsequence بتاع السياره وتحطهم في dropdown**
- `car_plate` [Char]
- `driver_name` [Char]
- `tips` [Float]
- `value_rent` [Float]
- `total_trip` [Float]
- `entry_counter` [Int]
- `entry_time` [TIme]
- `invoice` [Img]
- `invoice_number` [Int]
- `date` [Date]
- `time` [Time]
- `day` [Char]
- `comments` [Text]
- `invoice_sequence` [Int]
- `edited` [Bool] **دي اللي شرحتهالك**



## Get all Trilla Customer:
## Endpoint : /customers-orders/trilla-customer/get/
## method : GET
## permissions : admin user

## create a Trilla Customer:
## Endpoint : /customers-orders/trilla-customer/create/
## method : POST
## permissions : admin user

## Update the data of Trilla Customer:
## Endpoint : /customers-orders/trilla-customer/delete/<int:pk>/
## method : PUT
## permissions : admin user

## Delete data from Trilla Customer:
## Endpoint : /customers-orders/trilla-customer/delete/<int:pk>
## method : DELETE
## permissions : admin user


<!--  -->
### Deianna Customer

- `sequence` [PK]
- `customer_name` [Char] **Relation With New Customer**
- `phone_number` [Phone-number]
- `subject_name` [choices]
- `previous_quantity` [Float]
- `quantity` [Float]
- `secret_counter` [Float]
- `price_per_litre` [Float]
- `total` [Float]
- `payment_method` [Choices]
- `packing_method` [Char]
- `checkout_counter` [Int]
- `time_to_go_out` [Time]
- `client_station_name` [Char]
- `its_location` [Char]
- `coordinates` [Char]
- `car_type` [Relation] **هنا هتحط الsequence بتاع السياره وتحطهم في dropdown**
- `car_plate` [Char]
- `driver_name` [Char]
- `tips` [Float]
- `value_rent` [Float]
- `total_trip` [Float]
- `entry_counter` [Int]
- `entry_time` [TIme]
- `invoice` [Img]
- `invoice_number` [Int]
- `date` [Date]
- `time` [Time]
- `day` [Char]
- `comments` [Text]
- `invoice_sequence` [Int]
- `edited` [Bool] **دي اللي شرحتهالك**


## Get all Deianna Customer:
## Endpoint : /customers-orders/deiann-customer/get/
## method : GET
## permissions : admin user

## create a Deianna Customer:
## Endpoint : /customers-orders/deiann-customer/create/
## method : POST
## permissions : admin user

## Update the data of Deianna Customer:
## Endpoint : /customers-orders/deiann-customer/delete/<int:pk>/
## method : PUT
## permissions : admin user

## Delete data from Deianna Customer:
## Endpoint : /customers-orders/deiann-customer/delete/<int:pk>
## method : DELETE
## permissions : admin user



### Clients Analytics
## 
## Endpoint : /customers-orders/analytics/
## method : GET
## permissions : admin user
<pre> 
{
    "Customer Station": "58.82%",
    "Trilla Customer": "0.00%",
    "Deianna Customer": "0.00%",
    "Blocked Clients": " 35.29%",
    "Pending Clients": " 5.88%"
}
</pre>