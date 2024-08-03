# There is two endpoint to reset password if user already authenticated



## First Endpoint : 
    - endpoint : /auth/reset-password/
    - Body : email
    - permissions : authenticated


## Secend Endpoint : 
    - endpoint : /auth/reset-password/otp/
    - Body : otp, password
    - permissions : authenticated
