import pandas as pd
from tracking.models import Transaction

excel = pd.read_excel('shipmentTracking.xlsx', sheet_name = 'Sheet1')

col1 = excel['ShipmentID'].tolist()
col2 = excel['PreDONo'].tolist()
col3 = excel['Delivery Order No'].tolist()
col4 = excel['Net Weight Qty'].tolist()
col5 = excel['Weight Out Date'].tolist()

#print(col1[0],col2[0],col3[0],col4[0],col5[0])

for a,b,c,d,e in zip(col1,col2,col3,col4,col5):
    new = Transaction()
    new.shipment_id = a
    new.pre_do_no = b
    new.delivery_order_no = c
    new. net_weight_qty = d
    new.weight_out_date = e
    new.save()
print('success')
