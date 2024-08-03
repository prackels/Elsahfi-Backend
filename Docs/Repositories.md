### Repository

sequence [PK]
product_name [Char]
unit_price [Float]
quantity [Float]
total [Float]
datetime [datetime]
day [choices]
notes [Text]
=======
sequence [PK]
product_name [Char]
unit_price [Float]
quantity [Float]
total [Float]
datetime [datetime]

## Get all Repositories

## Endpoint : /repository/get/

## method : GET

## permissions : admin user

## create a Repository

## Endpoint : /repository/create/

## method : POST

## permissions : admin user

## Update the Repository

## Endpoint : /repository/update/<int:pk>/

## method : PUT

## permissions : admin user

## Delete Repository

## Endpoint : /repository/delete/<int:pk>

## method : DELETE

## permissions : admin user
