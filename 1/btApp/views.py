from django.shortcuts import render
from btApp.models import Tem
from btApp.models import Moi
from btApp.models import Co2
from btApp.models import Lig
from btApp.models import Datas
# Create your views here.
def index(request):
	result1 = Datas.objects.filter(name = "Tem")
	tem_data = []
	tem_time = []
	for s in result1:
		tem_data.append(s.data)
		tem_time.append(s.time)
	
	result2 = Datas.objects.filter(name = "Moi")
	moi_data = []
	moi_time = []
	for s in result2:
		moi_data.append(s.data)
		moi_time.append(s.time)
	
	result3 = Datas.objects.filter(name = "Co2")
	co2_data = []
	co2_time = []
	for s in result3:
		co2_data.append(s.data)
		co2_time.append(s.time)
	
	result4 = Datas.objects.filter(name = "Lig")
	lig_data = []
	lig_time = []
	for s in result4:
		lig_data.append(s.data)
		lig_time.append(s.time)
	return render(request,'index.htm',{'tem_data':tem_data,'tem_time':tem_time,'moi_data':moi_data,'moi_time':moi_time,'co2_data':co2_data,'co2_time':co2_time,'lig_data':lig_data,'lig_time':lig_time})