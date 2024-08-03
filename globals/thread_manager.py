from trumpet.models import Trumpet
from tank.models import Tank

def create_tank_threading(trumpet_names : list, tank_id : int) :
    for trumpet_name in trumpet_names : 
        print("TRUMPET NAME", trumpet_name)
        Trumpet.objects.create(
            name = trumpet_name.get("name"),
            trumpet_number = trumpet_name.get("name"),
            tank = Tank.objects.get(id=tank_id)
            
        ).save()