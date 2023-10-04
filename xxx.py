import requests, random, pprint
from faker import Faker 
import json            
  
fake = Faker() 
fake.random.seed(69420)

url = 'http://192.168.29.53:6969/api_add_patient'

# Get the CSRF token from your Django application's cookies
# You need to send a GET request to the same domain to obtain the CSRF token
csrf_url = 'http://192.168.29.53:6969'  # Replace with your actual domain
csrf_response = requests.get(csrf_url)
csrf_token = csrf_response.cookies.get('csrftoken')

myobj = {'first_name': fake.first_name(),
         'last_name': fake.last_name(),
         'gender': random.choice(['Male','Female','Transgender']),
         'mobile_number': random.randint(111111111, 9999999999),
         'emergency_contact': random.randint(111111111, 9999999999),
         'address': fake.address(),
         'age': random.randint(0,100),
         'room_no': random.randint(0,50),
         'email': fake.email(),
         'blood_group': random.choice(['A+','A-','B+','B-','AB+','AB-','O+','O-']),
         }

print(myobj)

# headers = {
#     'X-CSRFToken': csrf_token,
#     'Referer': csrf_url,  # Set the Referer header to your application's URL
# }

# x = requests.post(url, json=myobj, headers=headers)

# print(x.text)