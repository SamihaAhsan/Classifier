import json 
import csv 
import http.client 


books_arr=["Romance", "Mystery", "Sci-fi", "Western", "Fiction"]

def adding_csv(genre):
    conn.request("GET", "/genres/"+genre+"/best", headers=headers_api1) 
    res = conn.getresponse() 
    data = res.read() 
    convert=data.decode("utf-8") 
    final_dict=json.loads(convert) 
    for i in final_dict['books']:
        title=i['title']
        with open('books.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([title, genre])
        
for i in books_arr:
    adding_csv(i)



