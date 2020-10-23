from .models import Location, Journey
from haversine import haversine, Unit

class JourneyCalculator:
    def calculate():
        last_journey_location = Location.objects.exclude(carbon_journey_id__exact='').latest('timestamp')
        locations_to_calc = Location.objects.filter(timestamp__gte=last_journey_location.timestamp).order_by('timestamp')
        for location in locations_to_calc:
            time_from_last = (location.timestamp - last_journey_location.timestamp).total_seconds()
            thirty_mins = 30 * 60

            if time_from_last > thirty_mins
                last_journey_location = location
                continue

            last_lat_lng = (last_journey_location.latitude, last_journey_location.longitude)
            metres_from_last = haversine((location.latitude, location.longitude), last_lat_lng, unit=Unit.METERS)

            speed = metres_from_last / time_from_last
            car_speed = 4.47

            if speed > car_speed
                twenty_mins = 20 * 60
                journey_id = last_journey_location.journey_id if time_from_last < twenty_mins else ''
                if time_from_last < twenty_mins
                    location.journey_id = last_journey_location.journey_id
                    location.save()
                else
                    new_journey = Journey.create()
                    location.journey_id = new_journey.journey_id
                    location.save()
                    last_journey_location = location
            else
                location.journey_id
