import json #to use to convert to dictionary
import csv #to use functions in csv library
import http.client #thing that has functions to let you connect to an API and access info

conn = http.client.HTTPSConnection("goodreads-books.p.rapidapi.com") #contains the connection
conn_two=http.client.HTTPSConnection("goodreads12.p.rapidapi.com")

headers_api1 = { 
    'x-rapidapi-key': "bef032f76cmshbabab80030cc0c3p1eb522jsnadf7cbf3450b",
    'x-rapidapi-host': "goodreads-books.p.rapidapi.com"
}

headers_api2 = {
    'x-rapidapi-key': "bef032f76cmshbabab80030cc0c3p1eb522jsnadf7cbf3450b",
    'x-rapidapi-host': "goodreads12.p.rapidapi.com"
}
 #contains info of who I am

def pulling_summary(idd):
    conn_two.request("GET", "/getBookByID?bookID=56732449", headers=headers_api2)
    res = conn_two.getresponse()
    data = res.read()
    convert=data.decode("utf-8")
    final_dict=json.loads(convert)
    return final_dict['description']

def adding_csv(title, summary, genre):
    with open('books.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([title, genre, summary])
        


#romance
conn.request("GET", "/genres/romance/best", headers=headers_api1) #asking connection what we want to get

res = conn.getresponse() #asking connection to give responses
data = res.read() #it's in byte form so take it and convert

convert=data.decode("utf-8") #convert even more, to json format
final_dict=json.loads(convert) #convert json format to a python dictionary

for i in final_dict['books']:
    summary=pulling_summary(i['id'])
    title=i['title']
    genre="Romance"
    adding_csv(title, genre, summary)
#mystery

conn.request("GET", "/genres/romance/mystery", headers=headers_api1)
res = conn.getresponse() 
data = res.read() 
convert=data.decode("utf-8") #convert even more, to json format
final_dict=json.loads(convert) #convert json format to a python dictionary
