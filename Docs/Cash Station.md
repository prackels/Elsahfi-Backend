### Payment Of The Dead Line
PaymentOfTheDeadLine:
    sequence [PK]
    invoice_sequence [Int]
    customer_name [Char]
    financial_advance [Float]
    the_amount_required [Float]
    date_of_payment [Date]
    payment_amount [Float]
    remaining_for_the_station [Float]
    remaining_for_the_client [Float]
    payment_method [Char]
    receipt_img [Img]
    payment_date [Date]
    time [Time]
    day [Day]
    comments [Text]


## Get all Payment Of The Dead Line:
## Endpoint : /cash-station/payment-of-the-deadline/get/
## method : GET
## permissions : admin user
<pre>
{
    "Total amount required": 369.0,
    "Total paid": 6393.0,
    "Remaining for the station": 936936.0,
    "data": [
        {
            "sequence": 24,
            "time": "04:59 AM",
            "invoice_sequence": 31231,
            "customer_name": "123",
            "financial_advance": 2131.0,
            "the_amount_required": 123.0,
            "date_of_payment": "2024-01-08",
            "payment_amount": 312312.0,
            "remaining_for_the_station": 312312.0,
            "remaining_for_the_client": 123123.0,
            "payment_method": "3213123",
            "receipt_img": "/media/car-cash/payment-of-the-deadline/images_FxDGBeK.jpg",
            "payment_date": "2024-01-28",
            "day": "Sunday",
            "comments": "31321312"
        }
    ]
}
</pre>

## create a Payment Of The Dead Line
## Endpoint : /cash-station/payment-of-the-deadline/create/
## method : POST
## permissions : admin user

## Update the data of Payment Of The Dead Line
## Endpoint : /cash-station/payment-of-the-deadline/update/<int:pk>/
## method : PUT
## permissions : admin user

## Delete data from Payment Of The Dead Line
## Endpoint : /cash-station/payment-of-the-deadline/delete/<int:pk>
## method : DELETE
## permissions : admin user




### Shift Cash
ShiftCash:
    sequence [PK]
    shift [Char]
    shift_sequence [Int]
    petty_cash [Float]
    shift_cash [Float]
    net_total [Float]
    total [Float]
    additions [Float]
    reason [Char]
    total_amount [Float]
    deposit_officer [Char]
    receipt_img [Img]
    payment_date [Date]
    time [Time]
    day [Day]
    comments [Text]


## Get all ShiftCash:
## Endpoint : /cash-station/shift-cash/get/
## method : GET
## permissions : admin user
<pre>
{
    "Cash": 1096.0,
    "Total": 9789486.54,
    "Net": 2291909.0,
    "Data": [
        {
            "sequence": 1,
            "time": "07:23 PM",
            "shift": "وردية1",
            "shift_sequence": 111,
            "petty_cash": 0.0,
            "shift_cash": 222.0,
            "net_total": 450000.0,
            "total": 50000.0,
            "additions": 0.0,
            "reason": "reason",
            "total_amount": 50000.0,
            "deposit_amount": 0.0,
            "deposit_officer": "abdelrahman",
            "receipt_img": "/media/cash-station/shift-cash/960x0.webp",
            "payment_date": "2024-01-26",
            "day": "Friday",
            "comments": "comment"
        }
    ]
}
</pre>

## create a ShiftCash
## Endpoint : /cash-station/shift-cash/create/
## method : POST
## permissions : admin user

## Update the data of ShiftCash
## Endpoint : /cash-station/shift-cash/delete/<int:pk>/
## method : PUT
## permissions : admin user

## Delete data from ShiftCash
## Endpoint : /cash-station/shift-cash/delete/<int:pk>
## method : DELETE
## permissions : admin user
