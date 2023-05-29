from models.bus import Bus

data = [
{
"plate_no": 29565,
"sideno": 3535,
"no_seats": 65
},
{
"plate_no": 29566,
"sideno": 3537,
"no_seats": 65
}
]


for d in data:
    p = Bus(**d)
    p.save()
