from django.shortcuts import render
import json

ch = {"user":"ООО \"АГРОТОРГ\"","retailPlaceAddress":"344039, 61- г.Ростов-на-Дону,ул.Мечникова,зд.31/106,пом.1,12,13,14,15 на 1 эт.,21,21а,21б,21в,21г,21д,21е на 2 эт.","userInn":"7825706086  ","requestNumber":107,"shiftNumber":29,"operationType":1,"totalSum":63518,"cashTotalSum":0,"ecashTotalSum":63518,"kktRegId":"0006504690023376    ","fiscalDriveNumber":"9960440301797887","fiscalDocumentNumber":3625,"fiscalSign":852113512,"items":[{"name":"Морковь весовая             1кг","price":3289,"sum":2151,"quantity":0.654,"paymentType":4,"productType":1,"nds":2},{"name":"Хлеб тостовый пшеничный в/с570г","price":4989,"sum":4989,"quantity":1.0,"paymentType":4,"productType":1,"nds":2},{"name":"АЮТИНСКИЙ ХЛЕБ ХлебТОСТ.нар280г","price":2399,"sum":2399,"quantity":1.0,"paymentType":4,"productType":1,"nds":2},{"name":"*ПАПА МОЖ.Колб.ЧЕСНОЧ.п/к 420г","price":14990,"sum":14990,"quantity":1.0,"paymentType":4,"productType":1,"nds":2},{"name":"*ПАПА МОЖ.Колб.ЧЕСНОЧ.п/к 420г","price":14990,"sum":14990,"quantity":1.0,"paymentType":4,"productType":1,"nds":2},{"name":"*HOCHL.Сыр 55% с ветч.ванн. 400г","price":23999,"sum":23999,"quantity":1.0,"paymentType":4,"productType":1,"nds":2}],"nds10":5776,"code":3,"fiscalDocumentFormatVer":4,"machineNumber":"0166830006111416","retailPlace":"31D3    18762 - Пятёрочка","prepaidSum":0,"creditSum":0,"provisionSum":0,"dateTime":1658850060,"taxationType":1,"localDateTime":"2022-07-26T18:41"}

def checks(request):
	#return render(request, 'General/home_temp.html', {"nj": json.dumps(nj)})
	#return render(request, 'checks.html', {"ch": json.dumps(ch)})
	return render(request, 'checks.html', context=ch)
