import uuid
from bookings.models import Booking, Payment
from celery import shared_task



@shared_task
def payment_processing(booking_id):
    try:
        booking = Booking.objects.get(id=booking_id)
        transaction_id = str(uuid.uuid4())

        Payment.objects.create(booking=booking, payment_status='COMPLETED', transaction_id=transaction_id)
        booking.confirmed = True
        booking.save()

        print(f'Payment processed for Booking ID {booking_id}. Transaction ID: {transaction_id}')
    except Booking.DoesNotExist:
        priny(f'Booking ID {booking_id} not found.')