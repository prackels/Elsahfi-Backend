### Trumpet
Trumpet:
    sequence [PK]
    tank [ForeigenKey]
    subject_name [Choices]
    trumpet_number [Integer]
    receiving_counter [Float]
    delivery_counter [Float]
    quantity_sold [Float]
    price_per_litre [Float]
    total [Float]


## Get all Trumpets
## Endpoint : /trumpet/get/
## method : GET
## permissions : admin user

## create a Trumpet
## Endpoint : /trumpet/create/
## method : POST
## permissions : admin user

## Update the data of Trumpets
## Endpoint : /trumpet/update/<int:pk>/
## method : PUT
## permissions : admin user

## Delete data from Trumpets
## Endpoint : /trumpet/delete/<int:pk>
## method : DELETE
## permissions : admin user



### Reading Trumpet
ReadingTrumpet:
    subject_name [Choices]
    trumpet_number [ForeigenKey]
    trumpet_caliber [Float]
    receiving_counter [Float]
    delivery_counter [Float]
    quantity_sold [Float]
    price_per_litre [Float]
    total [Float]
    comments [Text]
    datetime [datetime]


## Get all Reading Trumpet:
## Endpoint : /trumpet/reading-trumpet/get/
## method : GET
## permissions : admin user

## create a Reading Trumpet
## Endpoint : /trumpet/reading-trumpet/create/
## method : POST
## permissions : admin user

## Update the data of Reading Trumpet
## Endpoint : /trumpet/reading-trumpet/delete/<int:pk>/
## method : PUT
## permissions : admin user

## Delete data from Reading Trumpet
## Endpoint : /trumpet/reading-trumpet/delete/<int:pk>
## method : DELETE
## permissions : admin user






### Analytics

## Get Daily Reading Trumpets Analytics:
## Endpoint : /trumpet/analytics/daily/
## method : GET
## permissions : admin user

## Get Weekly Reading Trumpets Analytics:
## Endpoint : /trumpet/analytics/weekly/
## method : GET
## permissions : admin user

## Get Monthly Reading Trumpets Analytics:
## Endpoint : /trumpet/analytics/monthly/
## method : GET
## permissions : admin user