from django.shortcuts import render
from django.http import HttpResponse
from .models import Transaction
from django.core.paginator import Paginator
from .query_from_db import sql_execute_query
import json

# Create your views here.

# def Home(request):
#     return HttpResponse('<h1> HelloWorld </h1>')

# def Home(request):
#
#     data = ['TS1001','TS1002','TS1003','TS1004']
#     context = {'kengdata':data}
#
#     # ส่งเป็น dict
#     return render(request,'tracking/home.html',context)

# def Home(request):
#
#     data = Transaction.objects.all()
#     paginator = Paginator(data,10)
#     page = request.GET.get('page')
#     data = paginator.get_page(page)
#
#     context = {'data':data}
#
#     # ส่งเป็น dict
#     return render(request,'tracking/home.html',context)

def searchShipment(ID, field_list = ['ShipmentID','PreDONo','Delivery Order No','Net Weight Qty','Weight Out Date']):
    query= f"select * from shipmenttracking where ShipmentID = '{ID}' "
    df = sql_execute_query('sqldb-datawarehouse',query,None,True)

    data_field =[]
    for fl in field_list:
        fld = df[fl].tolist()
        data_field.append(fld)

    data = []
    for dt in zip(*data_field):
        data.append(list(dt))

    return data

def Home(request):
    query='select top 10 * from shipmenttracking'
    df = sql_execute_query('sqldb-datawarehouse',query,None,True)
    print(df)

    col1 = df['ShipmentID'].tolist()
    col2 = df['PreDONo'].tolist()
    col3 = df['Delivery Order No'].tolist()
    col4 = df['Net Weight Qty'].tolist()
    col5 = df['Weight Out Date'].tolist()

    print(col1[0],col2[0],col3[0],col4[0],col5[0])
    data = []

    for dt in zip(col1,col2,col3,col4,col5):
        data.append(list(dt))
    print(data)

    paginator = Paginator(data,10)
    page = request.GET.get('page')
    data = paginator.get_page(page)

    context = {'data':data}
    return render(request,'tracking/home.html',context)


def About(request):
    return render(request,'tracking/about.html')

def Test1(request):
    query='select top 10 * from shipmenttracking'
    df = sql_execute_query('sqldb-datawarehouse',query,None,True)

    # json_records = df.reset_index().to_json(orient ='records')
    # data = []
    # data = json.loads(json_records)
    # context = {'d': data}

    return HttpResponse(df.to_html())

def Search(request):
    context = {}

    if request.method == 'POST':
        data = request.POST.copy()
        print('DATA:', data)
        search = data.get('search')
        alldata = []
        field_list = ['ShipmentID','PreDONo','Delivery Order No','Net Weight Qty','Weight Out Date']
        context['field'] = field_list
        for sc in search.split(','):
            data = searchShipment(ID = sc.strip(),field_list = field_list)
            alldata.extend(data)
        print(alldata)
        context['data'] = alldata
        if len(alldata) ==0:
            context['nodata'] = True

    return render(request, 'tracking/search.html',context)
