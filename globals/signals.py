from django.dispatch import receiver
from django.db.models.signals import post_save
from clients_.models import NewCustomer
from cash_station.models import Cash
from customer_orders. models import DeiannaCustomer, TrillaCustomer, CustomerStation
from django.db.models import F
from cash_station.models import PaymentOfTheDeadLine
from codes.models import EncryptedCodes
from employee.models import Employee
from new_purchase.models import NewPurchase
from tank.models import Tank
from trumpet.models import ReadingTrumpet_K, ReadingTrumpet


@receiver(post_save, sender=NewCustomer)
def create_or_update_cash(sender, instance, created, **kwargs):
    if created:
        Cash.objects.get_or_create(
            customer=instance,
            defaults={
                'financial_advance': instance.financial_advance,
                'the_amount_required': 0
            }
        )
    else:
        Cash.objects.filter(customer=instance).update(
            financial_advance=instance.financial_advance,
            the_amount_required=0
        )

@receiver(post_save, sender=CustomerStation)
def create_or_update_customer_station(sender, instance, created, **kwargs):
    cash = Cash.objects.filter(customer=instance.customer_name).first()
    instance_amount = (instance.quantity * instance.price_per_litre)
    if instance.payment_method == 'Deposit':
        if cash:
            if cash.financial_advance == 0:
                cash.the_amount_required = instance_amount
            elif instance_amount > cash.financial_advance:
                cash.the_amount_required = F('the_amount_required') + instance_amount - cash.financial_advance
                cash.financial_advance = 0
            elif instance_amount <= cash.financial_advance:
                cash.financial_advance = F('financial_advance') - instance_amount
                cash.the_amount_required = 0
            cash.save()

@receiver(post_save, sender=DeiannaCustomer)
def create_or_update_deianna_customer(sender, instance, created, **kwargs):
    cash = Cash.objects.filter(customer=instance.customer_name).first()
    instance_amount = (instance.value_rent + (instance.secret_counter * instance.price_per_litre))
    if instance.payment_method == 'Deposit':
        if cash:
            if cash.financial_advance == 0:
                cash.the_amount_required = instance_amount
            elif instance_amount > cash.financial_advance:
                cash.the_amount_required = F('the_amount_required') + instance_amount - cash.financial_advance
                cash.financial_advance = 0
            elif instance_amount <= cash.financial_advance:
                cash.financial_advance = F('financial_advance') - instance_amount
                cash.the_amount_required = 0
            cash.save()

@receiver(post_save, sender=TrillaCustomer)
def create_or_update_trilla_customer(sender, instance, created, **kwargs):
    cash = Cash.objects.filter(customer=instance.customer_name).first()
    instance_amount = (instance.value_rent + (instance.secret_counter * instance.price_per_litre))
    if instance.payment_method == 'Deposit':
        if cash:
            if cash.financial_advance == 0:
                cash.the_amount_required = instance_amount
            elif instance_amount > cash.financial_advance:
                cash.the_amount_required = F('the_amount_required') + instance_amount - cash.financial_advance
                cash.financial_advance = 0
            elif instance_amount <= cash.financial_advance:
                cash.financial_advance = F('financial_advance') - instance_amount
                cash.the_amount_required = 0
            cash.save()


@receiver(post_save, sender=PaymentOfTheDeadLine)
def create_or_update_payment_of_the_deadline(sender, instance, created, **kwargs):
    cash = Cash.objects.filter(customer=instance.customer_name).first()
    if cash:
        cash.the_amount_required= F('the_amount_required') - instance.payment_amount
        cash.save()



@receiver(post_save, sender=Employee)
def create_or_update_employee_code(sender, instance, created, **kwargs):
    
    if created:
        EncryptedCodes.objects.get_or_create(
            category=instance.name,
            code=instance.code,
            type= 'Employee'
        )




# @receiver(post_save, sender= ReadingTrumpet_K)
# def reduction_tank_trumpet_k_91(sender, instance, created, **kwargs):
#     if instance.subject_name == 'Premium Gasoline 91':
#         if created:
#             Tank.objects.filter(material= 'Premium Gasoline 91').update(
#                 tank_quantity= F('tank_quantity') - instance.quantity_sold,
#             )
#     if instance.subject_name == 'Premium Gasoline 95':
#         if created:
#             Tank.objects.filter(material= 'Premium Gasoline 95').update(
#                 tank_quantity= F('tank_quantity') - instance.quantity_sold,
#             )
#     if instance.subject_name == 'Diesel':
#         if created:
#             Tank.objects.filter(material= 'Diesel').update(
#                 tank_quantity= F('tank_quantity') - instance.quantity_sold,
#             )
