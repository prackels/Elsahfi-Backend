



class CreateInvoice :

    def __init__(self, model_class , **fields) : 
        
        model_class.objects.create(**fields).save()

