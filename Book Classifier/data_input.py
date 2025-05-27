import json #to use to convert to dictionary
import csv #to use functions in csv library
import http.client #thing that has functions to let you connect to an API and access info

conn = http.client.HTTPSConnection("goodreads-books.p.rapidapi.com") #contains the connection


headers_api1 = { 
    'x-rapidapi-key': "bef032f76cmshbabab80030cc0c3p1eb522jsnadf7cbf3450b",
    'x-rapidapi-host': "goodreads-books.p.rapidapi.com"
}

 #contains info of who I am
 #contains info of who I am

books_arr=["Romance", "Mystery", "Sci-fi", "Western", "Fiction"]

def adding_csv(genre):
    conn.request("GET", "/genres/"+genre+"/best", headers=headers_api1) #asking connection what we want to get
    res = conn.getresponse() #asking connection to give responses
    data = res.read() #it's in byte form so take it and convert
    convert=data.decode("utf-8") #convert even more, to json format
    final_dict=json.loads(convert) #convert json format to a python dictionary
    for i in final_dict['books']:
        title=i['title']
        with open('books.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([title, genre])
        
for i in books_arr:
    adding_csv(i)


