import requests
import time
import json

def get_content(url, pid):
	t_param=time.time()
	t_list=str(t_param).split(".")
	headers={
		"Cookie":"cna=er6NGDGCXgICAT2Q0eIyFiQg; xlly_s=1; lid=%E9%83%91%E5%8D%93%E6%B0%91zzm; enc=sjjYa9IV5G94osY19xZDnFo2fIglDcofov7XcTa%2Bo44K6UwAzgB9%2BaPGfpq85OFA8zQHx52lpZ%2BcUP66AyuPlw%3D%3D; t=e1c796be0642464736cdd135aef1c5d4; tracknick=%5Cu90D1%5Cu5353%5Cu6C11zzm; lgc=%5Cu90D1%5Cu5353%5Cu6C11zzm; _tb_token_=3715634158e1e; cookie2=1b291ebe4639a3732912fceef5981b4a; dnk=%5Cu90D1%5Cu5353%5Cu6C11zzm; uc1=cookie21=UtASsssme%2BBq&cookie14=Uoe1gByWOY9yHw%3D%3D&pas=0&cookie16=W5iHLLyFPlMGbLDwA%2BdvAGZqLg%3D%3D&existShop=false&cookie15=UIHiLt3xD8xYTw%3D%3D; uc3=nk2=tehLDFq%2FvrQI&id2=UU6gaQWAQBRfpA%3D%3D&lg2=WqG3DMC9VAQiUQ%3D%3D&vt3=F8dCuAc4W5b1lHeHK5k%3D; _l_g_=Ug%3D%3D; uc4=nk4=0%40t1wBkRdd5PSHEH0XQVtoO1bYYrw%3D&id4=0%40U2xt8a8jRFZ0DThg3opOlGTnZbhH; unb=2618894675; cookie1=BxUHHr4mJLyy4cqtpqQFQ38DqO2nXJp7hFSA5BXtj5k%3D; login=true; cookie17=UU6gaQWAQBRfpA%3D%3D; _nk_=%5Cu90D1%5Cu5353%5Cu6C11zzm; sgcookie=E100VB6T11SlWizTeg2V5aF3aove%2BU%2FQlGtRimJfeQZl1d0g99NodZeYLE7VvshJh8Cl8U3cwimcWKkD4b0oQ1K3Og%3D%3D; sg=m56; csg=86feabb5; x5sec=7b22726174656d616e616765723b32223a223131613061363837653932396363626565363230323261313538666330343764434a433567344547454b372f6c2b2f7138636e674b426f4d4d6a59784f4467354e4459334e5473784b494b41416a447475662f632f762f2f2f2f3842227d; tfstk=cRWfBAmLXNBrhpVZ3iZr3RWypqpGZX4WfSTVcsW9N0haxFIfi9MeR-SlsVMJ931..; l=eBQy9h7RjEj8bLZaBOfwhurza77tOIRAguPzaNbMiOCPO25e5izlW6ivJYTwCnGVh68wR3-n_Ro3BeYBcIq0x6aNa6Fy_hMmn; isg=BBgYsWqhzNtSzeBfptdvDZAY6UCqAXyLTIBpA1IJQdME7bjX-hAlGRPLJSVdfTRj",
		"referer":"https://detail.tmall.com/item.htm?spm=a220o.1000855.1998025129.12.4b43f4b1G79HB2&id=599270769700&scm=1007.12144.95220.23864_0_0&pvid=06882256-94c3-4003-aba4-aa37bf03efa0&utparam=%7B%22x_hestia_source%22:%2223864%22,%22x_object_type%22:%22item%22,%22x_hestia_subsource%22:%22default%22,%22x_mt%22:0,%22x_src%22:%2223864%22,%22x_pos%22:12,%22wh_pid%22:-1,%22x_pvid%22:%2206882256-94c3-4003-aba4-aa37bf03efa0%22,%22scm%22:%221007.12144.95220.23864_0_0%22,%22x_object_id%22:599270769700%7D&sku_properties=134942334:28316",
		"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
			}
	params={
			"callback":str(int(t_list[1][3:])+1),
			"_ksTS":t_list[0]+t_list[1][:3]+"_"+t_list[1][3:],
			"currentPage":pid
			}
	res=requests.get(url,params=params,headers=headers).text[len(str(int(t_list[1][3:])+1))+3:-1]
	#print(res)
	res2=json.loads(res)
	res3=json.dumps(res2,indent=4)
	result=json.loads(res3)
	for items in range(len(result["rateDetail"]["rateList"])): 
		result_time=result["rateDetail"]["rateList"][items]["rateDate"]
		result_content=result["rateDetail"]["rateList"][items]["rateContent"]
		#print(result_content)
		with open("taobao3.txt", "a") as f:
			f.write(result_time)
			f.write(":\n")
			f.write(result_content)
			f.write("\n\n")
	print(pid)
	time.sleep(6)
	
for i in range(100, 120):
	get_content('https://rate.tmall.com/list_detail_rate.htm?itemId=599270769700&sellerId=2885348004', str(i))
