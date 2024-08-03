# APIs for employee and car




## Emplyee Endpoints
[NOTE]  employee body : 
    name [Char]
    code [Int]
    phone_number [Phone]
    profession [Char]
    driving_license [File]
    salary [Float]
    marital_status [Char]
    type_of_residence [Char]
    beginning_of_residence [Date]
    end_of_residence [Date]
    renewal_of_residence [Char]
    photo_of_residence [FIle]
    beginning_of_the_employment_contract [Date]
    end_of_the_employment_contract [Date]
    photo_of_contract [Date]
    insurance_number [Char]
    beginning_of_insurance [Date]
    end_of_insurance [Date]
    photo_of_insurance [File]
    nationality [Char]
    passport_number [Char]
    photo_of_passport [File]
    company_name [Char]
    day [Char]
    time [Time]
    date [Date]
    comments [Text]

## get cars
### Endpoint : /employee/car/get/
### method : GET
<pre>
{
    "Employees": 1,
    "data": [
        {
            "id": 1,
            "name": "radwan",
            "code": 0,
            "phone_number": "+201018122497",
            "profession": "kl;gf",
            "driving_license": "/media/driving-license-imgs/elec.jpeg",
            "salary": 30000.0,
            "marital_status": "no",
            "type_of_residence": "type",
            "beginning_of_residence": "2024-01-24",
            "end_of_residence": "2024-02-11",
            "renewal_of_residence": "684",
            "photo_of_residence": "/media/photo_of_residence/hypersport.jpg",
            "beginning_of_the_employment_contract": "2024-01-24",
            "end_of_the_employment_contract": "2024-02-11",
            "photo_of_contract": "/media/photo_of_contract/images.jpeg",
            "insurance_number": "222",
            "beginning_of_insurance": "2024-01-24",
            "end_of_insurance": "2024-02-11",
            "photo_of_insurance": "/media/Photo_of_insurance/960x0.webp",
            "nationality": "hh88h",
            "passport_number": "333",
            "photo_of_passport": "/media/Photo_of_passport/download.png",
            "company_name": "ompany",
            "date": "2024-01-24",
            "time": "08:00:28.987874",
            "day": "Wednesday",
            "comments": "comment",
            "created_at": "2024-01-26"
        }
    ]
}
</pre>

## create employee
### Endpoint : /employee/car/create/
### method : POST

## update car
### Endpoint : /employee/car/update/<car-code>/
### method : PUT

## delete car
### Endpoint : /employee/car/delete/<car-code>/
### method : DELETE






# Endpoints for Car

[NOTE]  car body : 
    type_of_car [Char]
    runnig_cost [Float]
    car_code [Char]
    structure_number [Float]
    plate_number [Char]
    car_name [Char]
    model [Char]
    car_owner [Char]
    day [Char]
    time [Time]
    date [Date]
    comments [Text]

## get emplyees
### Endpoint : /employee/get/
### method : GET
<pre>
{
    "Cars": 2,
    "data": [
        {
            "sequence": 1,
            "type_of_car": "Type",
            "runnig_cost": 3.0,
            "car_code": "0151201",
            "structure_number": 151201.0,
            "plate_number": "0151201",
            "car_name": "new",
            "model": "MYL92LL/A",
            "car_owner": "Ahmed",
            "date": "2024-01-26",
            "time": "11:54:26.589170",
            "day": "Friday",
            "comments": "Comment",
            "created_at": "2024-01-26"
        }
    ]
}
</pre>

## create employee
### Endpoint : /employee/create/
### method : POST

## update employee
### Endpoint : /employee/update/<emplyee-id>/
### method : PUT

## delete employee
### Endpoint : /employee/delete/<emplyee-id>/
### method : DELETE

