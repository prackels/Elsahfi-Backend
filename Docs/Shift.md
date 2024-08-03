### Body : 
-   branch_number [int]
-   shift_series [Char]
-   responsible_series [Char]
-   user [Char]
-   date [Date]
-   time [Time]
-   shift_time [PM or AM]


#

### Create Shift
> method : POST

> endpoints : /shift/create/

> permissions : admin  

#
### Get Shift
> method : GET

> endpoint : /shift/get/{shift_uid}/

> permissions : admin  

#
### Delete Shift
> method : DELETE

> endpoint : /shift/delete/{shift_uid}/

> permissions : admin 