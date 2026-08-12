from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class OrderField(models.PositiveIntegerField):
    def __init__(self, for_fields=None, *args, **kwargs):
        self.for_fields = for_fields
        super().__init__(*args, **kwargs)
        
    def pre_save(self, model_intance, add):
        if getattr(model_intance, self.attname):
            try:
                qs = self.model.objects.all()
                
                if self.for_fields:
                    query = {
                        field: getattr(model_intance, field)
                        for field in self.for_fields
                    }
                    qs = qs.filter(**query)
                    
                last_item = qs.latest(self.attname)
                value = getattr(last_item, self.attname) + 1
                                
            except ObjectDoesNotExist:
                value = 0
        
            setattr(model_intance, self.attname, value)
            
            return value
        else:
            return super().pre_save(model_intance, add)
    
    