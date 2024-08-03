# Expenses APIs Refs

### Station Expenses
- `sequence` [PK]
- `invoice_sequence`[BigInt]
- `name` [Char]
- `price` [Float]
- `total_price` [Float]
- `quantity` [Int]
- `expense_code` [Choices] **دي هتكون سيرش وفي نفس الوقت choices علشان دي Relation**
- `expense_type` [Char] **ده هيجي اوتوماتيك من ال exp_code علشان الريليشن**
- `photo_of_invoice` [Img] 
- `date` [Date]
- `time` [Time]
- `day` [Char]
- `notes` [Text]
- `expense_type` [Text]
- `edited` [Bool] **اوعى ترجعها في ال get دي هشرحهالك**

## Get all expenses for station
## Endpoint : /expenses/station/get/
## method : GET
## permissions : admin user
<pre>
{
    "total_exp": 3330285.0,
    "data": [
        {
            "sequence": 1,
            "invoice_sequence": 684,
            "name": "بنزين ممتاز 91",
            "price": 24.0,
            "total_price": 475755.0,
            "quantity": 574255,
            "expense_code": 0,
            "expense_type": "type",
            "photo_of_invoice": "/media/Photo_of_invoice/dsa.jpeg",
            "date": null,
            "time": null,
            "day": null,
            "notes": null,
            "created_at": "2024-01-24"
        }
    ]
}
</pre>

## create expenses for station
## Endpoint : /expenses/station/create/
## method : POST
## permissions : admin user

## update data for expenses station
## Endpoint : /expenses/station/update/<station_id>/
## method : PUT
## permissions : admin user

## delete data for expenses government station
## Endpoint : /expenses/station/delete/<station_id>/
## method : DELETE
## permissions : admin user


***

# Governemt Expenses
- `sequence`[PK]
- `invoice_number` [BigInt]
- `profession` [Char]
- `expense_code`= [Char] **Relation With Codes**
- `employee_insurance` [Float]
- `license_cost_photo` [Img]
- `employee_insurance_photo` [Img]
- `car_insurance_photo` [Img]
- `renwal_of_form_photo` [Img]
- `renwal_of_form` [Float]
- `employee_code` [Int]
- `cost_of_license` [Float]
- `car_insurance` [Float]
- `name` [Char]
- `day` [Day]
- `time` [Time]
- `date` [Date]
- `notes` [Text]
- `edited` [Bool]

## Get all expenses for government station
## Endpoint : /expenses/government/station/get/
## method : GET
## permissions : admin user
<pre>
{
    "total_exp": {
        "total_cost_of_license": 31435.0,
        "total_employee_insurance": 333.0,
        "total_car_insurance": 31354.0,
        "total_renwal_of_form": 13435.0
    },
    "data": [
        {
            "sequence": 1,
            "invoice_number": 12,
            "profession": "21",
            "employee_insurance": 21.0,
            "license_cost_photo": "/media/Photo_of_invoice/images.jpg",
            "employee_insurance_photo": "/media/Photo_of_invoice/images_KShRhLh.jpg",
            "car_insurance_photo": "/media/Photo_of_invoice/images_OCc0WmL.jpg",
            "renwal_of_form_photo": "/media/Renwal_of_form/images.jpg",
            "renwal_of_form": 312.0,
            "employee_code": 312,
            "cost_of_license": 123.0,
            "car_insurance": 123.0,
            "name": "312",
            "day": "Friday",
            "time": "21:52:47.423670",
            "date": "2024-01-28",
            "comments": "312",
            "created_at": "2024-01-28"
        }
    ]
}
</pre>
## create expenses for government station
## Endpoint : /expenses/government/station/create/
## method : POST
## permissions : admin user

## update data for expenses government station
## Endpoint : /expenses/government/station/update/<station_id>/
## method : PUT
## permissions : admin user

## delete data for expenses government station
## Endpoint : /expenses/government/station/delete/<station_id>/
## method : DELETE
## permissions : admin user

***
### Cars Expenses
StationCustomerInvoice: 
    invoice_sequence [Int]
    name [Char]
    price [Float]
    car_type [Relation] **هنا هتحط الsequence بتاع السياره وتحطهم في dropdown**
    total_price [Float]
    quantity [Int]
    photo_of_invoice [File]
    date [Date]
    time [Time]
    day [Char]
    comments [Text]


## create a Cars Expenses
## Endpoint : /expenses/cars/create/
## method : POST
## permissions : admin user

## Update the data of Cars Expenses
## Endpoint : /expenses/cars/update/<int:pk>/
## method : PUT
## permissions : admin user

## Get all Cars Expenses 
## Endpoint : /expenses/cars/get/
## method : GET
## permissions : admin user

## Delete Cars Expenses 
## Endpoint : /expenses/cars/delete/<int:pk>/
## method : DELETE
## permissions : admin user
***
# Analytics

## Get Expenses Analytics
## Endpoint: /expenses/analytics/
## Method: GET
## pPermissions: admin user