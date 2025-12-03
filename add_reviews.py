"""
Script to add 10 client reviews to the SmartCare application
"""
import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smart_care.settings')
django.setup()

from doctor.models import Review, Doctor
from patient.models import Patient

# Sample reviews data
reviews_data = [
    {
        "body": "I had an excellent experience at SmartCare. The doctors are highly professional and caring. They took the time to explain my condition thoroughly and provided the best treatment. The staff is friendly and the facilities are top-notch. Highly recommended!",
        "rating": "⭐⭐⭐⭐⭐"
    },
    {
        "body": "SmartCare has been my go-to healthcare provider for years. The appointment booking is seamless, and I never have to wait long. The doctors are knowledgeable and always make me feel comfortable. The modern equipment ensures accurate diagnosis every time.",
        "rating": "⭐⭐⭐⭐⭐"
    },
    {
        "body": "I visited SmartCare for my regular checkup and was impressed by their efficiency. The lab tests were done quickly with accurate results. The doctor was very thorough in explaining the reports. Great service overall!",
        "rating": "⭐⭐⭐⭐"
    },
    {
        "body": "The emergency services at SmartCare saved my life. I was brought in late at night, and the medical team responded immediately with excellent care. The nurses were compassionate and the doctors were skilled. Forever grateful to this hospital!",
        "rating": "⭐⭐⭐⭐⭐"
    },
    {
        "body": "I brought my daughter for vaccination, and the experience was wonderful. The pediatrician was gentle and made my child feel at ease. The clinic is clean and child-friendly. We will definitely return for future checkups.",
        "rating": "⭐⭐⭐⭐⭐"
    },
    {
        "body": "Had a dental procedure done at SmartCare and it was completely painless. The dentist was professional and explained each step of the process. The clinic is well-maintained and hygiene standards are excellent. Very satisfied with the service.",
        "rating": "⭐⭐⭐⭐"
    },
    {
        "body": "SmartCare's maternity services are exceptional. From prenatal care to delivery, everything was handled perfectly. The doctors and nurses were supportive throughout my pregnancy journey. Special thanks to the entire maternity team!",
        "rating": "⭐⭐⭐⭐⭐"
    },
    {
        "body": "I underwent physiotherapy at SmartCare for my sports injury. The therapists are highly skilled and the equipment is modern. They designed a personalized treatment plan that helped me recover quickly. Excellent rehabilitation services!",
        "rating": "⭐⭐⭐⭐⭐"
    },
    {
        "body": "The cardiology department at SmartCare is outstanding. My father had a heart condition and received world-class treatment here. The cardiologists are experienced and use advanced technology for diagnosis and treatment. Thank you for taking such good care!",
        "rating": "⭐⭐⭐⭐⭐"
    },
    {
        "body": "SmartCare provides comprehensive healthcare under one roof. From consultation to lab tests to pharmacy, everything is available. The online appointment system is convenient and the staff is always helpful. A truly modern healthcare facility!",
        "rating": "⭐⭐⭐⭐"
    }
]

def add_reviews():
    """Add 10 client reviews to the database"""
    
    # Get all doctors and patients
    doctors = list(Doctor.objects.all())
    patients = list(Patient.objects.all())
    
    if not doctors:
        print("Error: No doctors found in the database. Please add doctors first.")
        return
    
    if not patients:
        print("Error: No patients found in the database. Please add patients first.")
        return
    
    print(f"Found {len(doctors)} doctors and {len(patients)} patients")
    print("Adding 10 client reviews...")
    
    # Add reviews
    reviews_created = 0
    for i, review_data in enumerate(reviews_data):
        # Alternate between patients and doctors
        patient = patients[i % len(patients)]
        doctor = doctors[i % len(doctors)]
        
        # Check if similar review already exists
        existing_review = Review.objects.filter(
            reviewer=patient,
            doctor=doctor,
            body=review_data["body"]
        ).first()
        
        if not existing_review:
            review = Review.objects.create(
                reviewer=patient,
                doctor=doctor,
                body=review_data["body"],
                rating=review_data["rating"]
            )
            reviews_created += 1
            print(f"✓ Review {reviews_created}: {patient.user.first_name} reviewed Dr. {doctor.user.first_name} - {review_data['rating']}")
        else:
            print(f"✗ Review already exists: {patient.user.first_name} -> Dr. {doctor.user.first_name}")
    
    print(f"\n✅ Successfully created {reviews_created} new reviews!")
    print(f"📊 Total reviews in database: {Review.objects.count()}")

if __name__ == "__main__":
    add_reviews()
