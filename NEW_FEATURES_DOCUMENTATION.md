# Smart Care Healthcare System - New Features Documentation

## Overview
This documentation covers the new features added to the Smart Care Healthcare System. All existing features remain unchanged and functional.

## Table of Contents
1. [Emergency Section](#1-emergency-section)
2. [Blood Bank Management](#2-blood-bank-management)
3. [Vaccine Management](#3-vaccine-management)
4. [Burn Unit](#4-burn-unit)
5. [Enhanced Patient Module](#5-enhanced-patient-module)
6. [API Endpoints](#api-endpoints)
7. [Installation & Setup](#installation--setup)

---

## 1. Emergency Section

### Features
- **Emergency Request Creation**: Patients can create emergency requests with location
- **Ambulance Management**: Track and manage available ambulances
- **Emergency Contacts**: Maintain emergency contacts and hospitals
- **Real-time Status Tracking**: Track status (Pending, Accepted, On the Way, Completed, Cancelled)

### API Endpoints
- `GET /emergency/requests/` - List all emergency requests
- `POST /emergency/requests/` - Create emergency request
- `POST /emergency/requests/{id}/assign_ambulance/` - Assign ambulance (Admin)
- `POST /emergency/requests/{id}/cancel/` - Cancel request
- `GET /emergency/ambulances/available/` - List available ambulances
- `GET /emergency/contacts/nearby/` - Get nearby emergency contacts

---

## 2. Blood Bank Management

### Features
- **Blood Donor Registration**: Register as donor with blood group
- **Blood Request System**: Request blood with urgency levels
- **Donation Tracking**: Track blood donation history
- **Blood Bank Management**: Manage blood banks with inventory
- **Search by Blood Group**: Find donors by blood group and location

### API Endpoints
- `GET /blood_bank/donors/` - List all donors
- `POST /blood_bank/donors/` - Register as donor
- `GET /blood_bank/donors/by_blood_group/` - Search by blood group
- `GET /blood_bank/donors/available/` - List available donors
- `POST /blood_bank/requests/` - Create blood request
- `POST /blood_bank/requests/{id}/assign_donor/` - Assign donor (Admin)
- `GET /blood_bank/banks/{id}/availability/` - Check blood availability

---

## 3. Vaccine Management

### Features
- **Vaccine Information**: Detailed vaccine info including side effects
- **Vaccination Records**: Track patient vaccination history
- **Dose Scheduling**: Schedule and track multiple doses
- **Vaccine Schedules**: Predefined vaccination schedules by age group
- **Upcoming Vaccinations**: View upcoming scheduled vaccinations

### API Endpoints
- `GET /vaccine/vaccines/` - List all vaccines
- `GET /vaccine/vaccines/by_age_group/` - Get vaccines by age group
- `POST /vaccine/records/` - Create vaccination record
- `GET /vaccine/records/upcoming/` - Get upcoming vaccinations
- `POST /vaccine/records/{id}/mark_completed/` - Mark completed (Admin)
- `GET /vaccine/schedules/recommended/` - Get recommended schedules

---

## 4. Burn Unit

### Features
- **Burn Specialist Management**: Track burn specialist doctors
- **Patient Admission**: Admit burn patients with severity assessment
- **Treatment Tracking**: Record and track burn treatments
- **Bed Management**: Monitor burn unit bed availability
- **Discharge Management**: Track patient discharge

### API Endpoints
- `GET /burn_unit/doctors/` - List burn doctors
- `GET /burn_unit/doctors/available/` - List available doctors
- `POST /burn_unit/patients/` - Admit patient
- `POST /burn_unit/patients/{id}/assign_doctor/` - Assign doctor (Admin)
- `POST /burn_unit/patients/{id}/discharge/` - Discharge patient (Admin)
- `POST /burn_unit/treatments/` - Record treatment
- `GET /burn_unit/units/available_beds/` - Units with available beds

---

## 5. Enhanced Patient Module

### New Fields Added
**Personal Information:**
- Date of birth
- Gender (Male, Female, Other)
- Blood group
- Address
- Emergency contact (name and phone)

**Medical History:**
- Allergies
- Chronic diseases
- Current medications
- Past surgeries
- Family medical history

**Physical Measurements:**
- Height (in cm)
- Weight (in kg)

---

## Installation & Setup

### 1. Database Migration
```bash
python manage.py migrate
```

### 2. Create Superuser
```bash
python manage.py createsuperuser
```

### 3. Access Admin Panel
Navigate to `/admin/` to add:
- Ambulances
- Emergency contacts
- Vaccines
- Blood banks
- Burn units

### 4. Run Server
```bash
python manage.py runserver
```

---

## API Authentication

Most endpoints require Token-based authentication:
```
Authorization: Token <your-auth-token>
```

---

## Admin Panel Features

### Emergency Section
- List and filter emergency requests by status and type
- Manage ambulances and availability
- Maintain emergency contacts

### Blood Bank
- Manage blood donors with search and filter
- Track blood requests by urgency
- Record donations
- Update blood bank inventory

### Vaccine Management
- Add and manage vaccines
- Track vaccination records
- Schedule vaccinations

### Burn Unit
- Manage burn specialist doctors
- Track burn patients and treatment status
- Record treatments
- Monitor unit capacity

---

## Security & Permissions

### Admin Only Actions:
- Assigning ambulances/doctors/donors
- Marking vaccinations as completed
- Discharging patients
- Managing units and banks

### Patient Actions:
- Creating emergency requests
- Creating blood requests
- Viewing own records
- Viewing own medical history

---

## Example API Calls

### Create Emergency Request
```bash
curl -X POST http://localhost:8000/emergency/requests/ \
  -H "Authorization: Token YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "emergency_type": "Ambulance",
    "location": "123 Main St",
    "description": "Medical emergency",
    "contact_number": "+8801712345678"
  }'
```

### Search Blood Donors
```bash
curl -X GET "http://localhost:8000/blood_bank/donors/by_blood_group/?blood_group=O+"
```

### Get Upcoming Vaccinations
```bash
curl -X GET http://localhost:8000/vaccine/records/upcoming/ \
  -H "Authorization: Token YOUR_TOKEN"
```

---

## Database Schema

### New Apps Created:
1. `emergency` - Emergency requests, ambulances, contacts
2. `blood_bank` - Blood donors, requests, donations, banks
3. `vaccine` - Vaccines, vaccination records, schedules
4. `burn_unit` - Burn doctors, patients, treatments, units

### Updated Models:
- `Patient` - Enhanced with 15 new medical history fields

---

## Important Notes

-  All existing features remain **fully functional**
-  No changes to existing doctor, appointment, or service modules
-  All new apps are independent and isolated
-  Database migrations created for all models
-  Admin panel configured for all new features
-  RESTful APIs with proper authentication
-  Comprehensive filtering and search capabilities

---

## Changelog

### Version 2.0 (Current)
-  Added Emergency Section
-  Added Blood Bank Management
-  Added Vaccine Management
-  Added Burn Unit
-  Enhanced Patient Module with medical history
-  All existing features preserved

---

**Support**: Check Django admin panel for data management and review this documentation for API usage.
