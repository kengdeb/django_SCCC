from django.db import models

class Transaction(models.Model):
    shipment_id = models.CharField(max_length = 20,verbose_name = 'เลขชิบเม้น')
    pre_do_no = models.CharField(max_length = 20,verbose_name = 'เลขดีโอ')
    # database กะ หน้า web
    delivery_order_no = models.IntegerField(null = True, blank =True)
    net_weight_qty = models.DecimalField(max_digits = 6, decimal_places = 3,null = True, blank =True)
    weight_out_date = models.DateTimeField(null = True, blank =True)

    def __str__(self):
        return self.shipment_id
