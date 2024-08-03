# Search Endpoint



> endpoint : /search/

> method : POST

> permissions : admin

### body : 
    - keyword [String]
    - categories [list]
    - sub_categories [list]
    - date_from [date field]
    - date_to [date field]
# 
### Description
```
in search endpoint you can make post with specific body .

keyword , date_from and date_to fields is required

categories filed is required and send as a list like : [a,b,c]

sub_categories field is not required only if user choose sub_category in category like Client -> station, and sub_categories must be sent as a list

```


#
### Test sent data

> test search with only categories :
```
{
    "keyword" : "Radwan",
    "date_from" : "<DATE>",
    "date_to" : "<DATE>",
    "categories" : [
        "employees",
        "supplier",
    ],
}

```
#

> test search with categories and sub_categories
```
{
    "keyword" : "Radwan",
    "date_from" : "<DATE>",
    "date_to" : "<DATE>",
    "categories" : [
        "employees",
        "supplier",
        "clients"
    ],
    "sub_categories" : [
        "station"   
    ]
}

```
#
### Avalibable Categories u can sent in list
- cars
- employees
- repository
- supplier
- trumpets

#
### Avalibable Categories that has sub categories on it 
- clients , sub categories in clients is : station, terilla,deina, blocked, disabled

- expenses , sub categories in expenses is : station , government