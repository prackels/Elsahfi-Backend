### Body : 
- tank_name [Char] 
- tank_weight [Float] 
- tank_height [Float] 
- tank_width [Float] 
- material [Char] 
- trumpets_count [Int] 
- tank_quantity [Int] 
- tank_caliber [Int] 
- saled_quantity [Int] 
- remaining_quantity [Int] 
- trumpets_name [List of trumpet]
    - example
        trumpets_name = [
            {
                'name' : 'test_name',
                'tank' : 'the id of tank'
            }
        ]

#
## Create Tank

> endpoint : /tank/create/

> method : POST

> permissions : admin

```
if only create tank you add trumpets as key and it shoud be list and has all trumpet names like : [t1, t2, t3]
```
#
## Delete Tank

> endpoint : /tank/delete/{tankid}/

> method : DELETE

> permissions : admin

#
## Get all Tanks

> endpoint : /tank/get/

> method : GET

> permissions : admin

#
## Update Tank

> endpoint : /tank/update/{tankid}/

> method : PUT

> permissions : admin


#
## Update Tank [Spacefic update]

```
Diffrent between this endpoint and update endpoint ,
that in this endpoint u update specfic fields in tank
```

### Body : 
- tank_quantity [Int]
- remaining_quantity [Int]
- tank_caliber [Int]

> endpoint : /tank/specify-update/{tankid}/

> method : PUT

> permissions : admin


