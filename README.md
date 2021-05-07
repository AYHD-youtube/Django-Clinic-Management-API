# Django-Clinic-Management-API

Task Description: Implement Backend for Clinic Management
exposing REST API
The candidate has to build an application using Django meeting following requirements:
1. There will 3 types of users
a. Practitioners: The doctors who treat within the clinic.
b. Visitors: The clients who visit a doctor.
c. Super Admins: Users who can add Doctors and Manage the whole clinic.
2. Practitioners can change their available time from the mobile/web application. Eg: 9 a.m.
to 1 p.m., 2 p.m. to 6 p.m.
3. Practitioners can specify the time slot period for which a visitor can book, eg: 10 minutes,
30 minutes, 120 minutes, etc.
4. Practitioners can see the list of appointments already booked by the patient and the
mode of the appointment:
a. Telephone
b. Video Conference
c. Physical Meeting
5. Practitioners can manage their profile information:
a. Name
b. Profile Picture
c. Specialization
d. Appointment Successfully completed (computed)
e. Date Joined
f. Phone Number
g. Is Available (computed from the available time and time slots)
h. Bank Account Details
i. PAN Number
ii. Bank Account Number
iii. IFSC Code
6. Visitors can register at the system by providing:
a. Email ID (primary field)
b. Name
c. Address
i. Address Line 1
ii. Address Line 2
iii. Postal Code
iv. City
v. State
vi. Country
d. Nationality
e. Gender
f. Date of Birth
g. Type:
i. Patient
ii. Visitor
7. Visitor can check the available time slots for a practitioner by giving:
a. Date
b. Time Slot Duration
For that day
8. Visitors can book a particular slot and that slot should be blocked for 15 minutes until the
visitor completes the payment.
a. If visitors do not make the payment, then the system should automatically make
that slot available.
b. If visitor makes the payment, then send notification to Practitioner via:
i. Email
ii. SMS (Dummy Function)
9. Only Super Admins can add Practitioners.
10. Visitors need to verify the Email using OTP before creating or updating their profile or
booking the appointment.
11. For payment the candidate can use a dummy endpoint that accepts the order_id,
payment_id, amount and appointment id. And should mark payment as successful upon
hitting.
