# Django-Clinic-Management-API

### How to Use and Test this Application on your computer
- run migrations `python manage.py makemigrations`
- run migrate `python manage.py migrate`
- run `python manage.py createsuperuser` to create superuser
- run tests `python manage.py test`
- Using `api/register`endpoint POST request you can add a patient.
- Using `api/admin`endpoint you can access all doctors and patients and create new doctors.
- Using `api/calender` endpoint to set available days and time as a doctor.
- Using `api/book-appointment` endpoint as a Patient to book an appointment with a specific doctor.

### How to use and Test this application 
#### Using POSTMAN [POST] all the above endpoints to run the API
- Using ` ` endpoint to see swagger documentation.
- Using `/redoc`endpoint you can se redoc swagger documentation.


### Comments
send an email to abhishek3yadav3@gmail.com if there are any questions.


###Documentation
#### Using POSTMAN [POST] all the above endpoints to run the API
POST Login
BODY 
{
    "email": "markessien@gmail.com",
    "password": "patientonereal"
}

POST Set Calender Availability
BODY 
{
    "email": "mudia@gmail.com",
    "day": "wednesday",
    "open": "12:00",
    "closed": "16:00"
}

POST Book Appointment
BODY 
{
    "email": "yinka@gmail.com",
    "doctor_email": "mudia@gmail.com",
    "day": "wednesday",
    "start_time": "15:00",
    "stop_time": "18:00"
}

POST Register
BODY
{
    first_name: 
        "Abhishek"
    ,
    "last_name":
        "Yadav"
    ,
    "email":
        "abhishek3ayadav3@gmail.com"
    ,
    "phone_number": 
        "970285226"
    ,
    "password": 
        "abhishek"
    ,
    "Address": 
        "Bhandup,Mumbai"    
}


