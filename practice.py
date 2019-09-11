# import datetime as dt
# import json

# dictionary = {'george' : 16, 'amber' : 19}
# khb_dict = {
#         "phone_no1": {
#             "username": "abhi3701",
#             "country": "India",
#             "last_product":"A",
#             "last_key": "Alltest343247328507230",
#             "datetime": "2019-09-29",
#             }
#         }
# # search_age = input("Provide age\n")
# # for name, age in dictionary.items():
# #     if age == search_age:
# #         print(name)
# #     else:
# #         print("No data")

# name = list(dictionary.keys())[list(dictionary.values()).index(19)]
# # namekhb = list(khb_dict.keys())[list(khb_dict.values()).index('India')]
# # print(name)
# khb_dict_val1 = khb_dict['phone_no1']
# print(khb_dict_val1.get("username"))

# namekhb = list(khb_dict_val1.keys())[list(khb_dict_val1.values()).index('India')]
# print(namekhb)
# # print(khb_dict.values())
# print(dt.date.today())

l = ['432432', '3432423']
print([x for x in l if x == '432432'])