from models.user import User
from uuid import uuid4



data = [

        {   "fname": "abebe",
            "id": str(uuid4()),
            "lname": "kebede",
            "username": "gfgff",
            "password": "te12345678",
            "gender":  "male",
            "phone": 987654321,
            "email": "trecghjjggjgjh@gmail.com"
            }
        ]
for i in data:
    p = User(**i)
    p.save()
    

