### New Purchase
NewPurchase: 
    sequence [PK]
    supplier_name [Char]
    supplier_location [Char]
    phone_number [PhoneNum]
    order_number [Int]
    order_date [Date]
    order_time [Time]
    subject_name [Char]
    price_per_litre [Float]
    required_quantity [Float]
    quantity_received [Float]
    actual_quantity [Float]
    trumpet_t [Float]
    actual_quantity_price [Float]
    the_difference_per_quantity [Float]
    the_amount_of_evaporation [Float]
    car_type [Char]
    car_plate [Char]
    driver_name [Char]
    checkout_counter [Int]
    time_to_go_out [Time]
    delivery_location [Char]
    receiving_location [Char]
    entry_counter [Int]
    entry_time [Time]
    tips [Float]
    value_rent [Float]
    total_trip [Float]
    invoice [Img]
    date [Date]
    time [Time]
    day [Char]
    comments [Text]

## Get all New Purchase
## Endpoint : new-purchase/new-purchase/get/
## method : GET
## permissions : admin user

## create a New Purchase
## Endpoint : new-purchase/new-purchase/create/
## method : POST
## permissions : admin user

## Update the data of New Purchase
## Endpoint : new-purchase/new-purchase/update/<int:pk>
## method : PUT
## permissions : admin user

## Delete data from New Purchase
## Endpoint : new-purchase/new-purchase/delete/<int:pk>
## method : DELETE
## permissions : admin user


### New Supplier
NewSupplier: 
    sequence [PK]
    supplier_name [Char]
    supplier_location [Char]
    phone_number [PhoneNum]
    purchase_tax [Float]
    subject_name [Choices]
    purchase_price_per_litre [Float]
    liter_selling_price [Float]
    sales_tax [Float]
    date [Date]
    time [Time]
    day [Char]
    comments [Text]

## Get all New Supplier
## Endpoint : new-purchase/new-supplier/get/
## method : GET
## permissions : admin user
<pre>
{
    "suppliers": 1,
    "data": [
        {
            "sequence": 1,
            "time": "07:32 AM",
            "supplier_name": "3132",
            "supplier_location": "3123",
            "phone_number": "+201228120928",
            "purchase_tax": 312.0,
            "subject_name": "Premium Gasoline 91",
            "purchase_price_per_litre": 31.0,
            "liter_selling_price": 31.0,
            "sales_tax": 31.0,
            "date": "2024-01-28",
            "day": "Sunday",
            "comments": "313232"
        }
    ]
}</pre>

## create a New Supplier
## Endpoint : new-purchase/new-supplier/create/
## method : POST
## permissions : admin user

## Update the data of New Supplier
## Endpoint : new-purchase/new-supplier/update/<int:pk>
## method : PUT
## permissions : admin user

## Delete data from New Supplier
## Endpoint : new-purchase/new-supplier/delete/<int:pk>
## method : DELETE
## permissions : admin user
