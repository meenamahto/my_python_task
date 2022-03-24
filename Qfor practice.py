
# import json,requests
# from bs4 import BeautifulSoup

# res=requests.get("https://www.flipkart.com/womens-skirts/pr?sid=clo%2Cvua%2Ciku%2Cw5t")
# soup=BeautifulSoup(res.content,"html.parser")
# di=soup.find("div",class_="_1YokD2 _3Mn1Gg")
# d=di.find_all("div",class_="_1AtVbE col-12-12")
# final_data=[]
# serial_no=0
# for i in d:
#     div=i.find_all("div",class_="_2B099V")
#     dict={"rank":"","name":"","mrp_price":"","discount":"","original_price":""}
#     for j in div:
#         a=j.find("a",class_="IRpwTa").get_text()
#         b=j.find("div",class_="_30jeq3").get_text()
#         c=j.find("div",class_="_3I9_wc").get_text()
#         d=j.find("div",class_="_3Ay6Sb").get_text()
#         serial_no+=1
#         dict["rank"]=serial_no
#         dict["name"]=a
#         dict["mrp_price"]=c
#         dict["discount"]=d
#         dict["original_price"]=b
#         final_data.append(dict)
# print(final_data)
# with open("flipkart.json","w") as file:
#     json.dump(final_data,file,indent=4)


# import json,requests
# from bs4 import BeautifulSoup
# res=requests.get("https://www.flipkart.com/womens-skirts/pr?sid=clo%2Cvua%2Ciku%2Cw5t")
# soup=BeautifulSoup(res.content,"html.parser")
# di=soup.find("div",class_="_1YokD2 _3Mn1Gg")
# d=di.find_all("div",class_="_1AtVbE col-12-12")
# import csv
# with open ("flipkart.csv","w") as file:
#     ffile=csv.writer(file)
#     ffile.writerow(["rank","name","mrp_price","discount","original_price"])
#     serial_no=1
#     for i in d:
#         div=i.find_all("div",class_="_2B099V")
#         for j in div:
#             a=j.find("a",class_="IRpwTa").get_text()
#             b=j.find("div",class_="_30jeq3").get_text()
#             c=j.find("div",class_="_3I9_wc").get_text()
#             d=j.find("div",class_="_3Ay6Sb").get_text()
#             final_data=[serial_no,a,c,d,b]
#             ffile.writerow(final_data)
#             print(serial_no)
#             serial_no+=1

