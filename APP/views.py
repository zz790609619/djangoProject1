from django.http import HttpResponse
from django.shortcuts import render

from APP import models
from APP.tables.table import Table

tables = []


# Create your views here.
def add(request):
    table = Table(request.GET.get("tableName"), request.GET.get("db"), request.GET.get("tables"))
    tables.append(table)
    models.BaseTable.objects.create(tableName=request.GET.get("tableName"), db=request.GET.get("db"),
                                    size=request.GET.get("tables"))
    return HttpResponse("ok")


# Create your views here.
def calOneTable(request):
    table = models.BaseTable.objects.get(tableName=request.GET.get("tableName"))


    if table is not None:
        ids = int(request.GET.get("id"))
        db = int(ids / table.size)
        db = db % table.db
        tableNum = ids % table.size
        return render(request, "../templates/dataBase.html", {"database": str(db), "tables": str(tableNum)})
    return HttpResponse("ok")


# Create your views here.
def calAllTable(request):
    table = models.BaseTable.objects.all()
    result = []
    ids = int(request.GET.get("id"))
    for i in table:
        db = int(ids / i.size)
        db = db % i.db
        tableNum = ids % i.size
        result.append(Table(i.tableName, db, tableNum))
    return render(request, "../templates/dataBaseAll.html", {"result": result})


def init(request):
    tables.append(Table("merchant_base_info", 4, 1))
    tables.append(Table("merchant_setting_info", 4, 1))
    tables.append(Table("merchant_enjoy_king", 4, 1))
    tables.append(Table("merchant_device", 4, 1))
    tables.append(Table("merchant_bank_account", 4, 1))
    tables.append(Table("merchant_account", 4, 1))
    tables.append(Table("merchant_detail_info", 4, 1))
    tables.append(Table("merchant_account_record", 4, 30))
    tables.append(Table("user_pay_order", 4, 30))
    tables.append(Table("merchant_order", 4, 1))
    tables.append(Table("merchant_aggregate_user", 4, 30))
    tables.append(Table("aggregate_user_info", 4, 30))
    tables.append(Table("merchant_chain_integral_record", 4, 2))
    tables.append(Table("merchant_notice", 4, 2))
    tables.append(Table("merchant_consumer", 4, 20))
    tables.append(Table("user_pay_info", 4, 20))
    tables.append(Table("merchant_coupon", 4, 4))
    tables.append(Table("merchant_opt_log", 4, 4))
    tables.append(Table("merchant_with_drawal", 4, 4))
    tables.append(Table("merchant_powder", 4, 4))
    tables.append(Table("merchant_ganged", 4, 4))
    tables.append(Table("merchant_day_record", 4, 30))
    tables.append(Table("merchant_user_coupon", 4, 8))
    tables.append(Table("user_pay_coupon", 4, 15))
    tables.append(Table("user_pay_enjoyment", 4, 15))
    tables.append(Table("user_pay_enjoyment_record", 4, 25))
    tables.append(Table("user_pay_order_coupon", 4, 25))
    tables.append(Table("main_order", 2, 100))
    for i in tables:
        try:
            table = models.BaseTable.objects.get(tableName=i.name.strip())
        except models.BaseTable.DoesNotExist:
            table = None
        if table is None:
            models.BaseTable.objects.create(tableName=i.name.strip(), db=i.db, size=i.size)
    return HttpResponse("ok")


def calAllTablePath(request, searchId):
    tableAll = models.BaseTable.objects.all()
    result = []
    for i in tableAll:
        db = int(searchId / i.size)
        db = db % i.db
        tableNum = id % i.size
        result.append(Table(i.tableName, db, tableNum))
    return render(request, "../templates/dataBaseAll.html", {"result": result})
