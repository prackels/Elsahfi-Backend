### Codes
Code:
    sequence [PK]
    category [Char]
    code [Char]
    added_at [datatime]

## Get all Codes
## Endpoint : /codes/code/get/
## method : GET
## permissions : admin user

## create a Codes
## Endpoint : /codes/code/create/
## method : POST
## permissions : admin user

## Update the data of Codes
## Endpoint : /codes/code/update/<int:pk>/
## method : PUT
## permissions : admin user

## Delete data from Codes
## Endpoint : /codes/code/delete/<int:pk>
## method : DELETE
## permissions : admin user

### Encrypted Codes
''' متنساش ترجع في ال request يكون ال value اسمها password علشان لازم ال password يرجع علشان يقدر ينفذ ال methods '''

EncryptedCodes:
    sequence [PK]
    category [Char]
    code [Char]
    added_at [datatime]

## Get all Encrypted Codes
## Endpoint : /codes/encrypted-codes/get/
## method : GET
## permissions : admin user

## create a Encrypted Codes
## Endpoint : /codes/encrypted-codes/create/
## method : POST
## permissions : admin user

## Update the data of Encrypted Codes
## Endpoint : /codes/encrypted-codes/update/<int:pk>/
## method : PUT
## permissions : admin user

## Delete data from Encrypted Codes
## Endpoint : /codes/encrypted-codes/delete/<int:pk>/
## method : DELETE
## permissions : admin user
