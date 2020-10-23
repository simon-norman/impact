from .models import Location, Journey
from haversine import haversine, Unit

class JourneyCalculator:
    def calculate():
        last_journey_location = Location.objects
            .exclude(carbon_journey_id__exact='', confirmed_no_journey=False)
            .latest('timestamp')
        last_location = last_journey_location

        locations_to_calc = Location.objects
            .filter(timestamp__gt=last_journey_location.timestamp)
            .order_by('timestamp')

        for location in locations_to_calc:
            time_from_last = (location.timestamp - last_location.timestamp).total_seconds()
            thirty_mins = 30 * 60

            if time_from_last > thirty_mins
                last_location = location
                continue

            last_lat_lng = (last_location.latitude, last_location.longitude)
            metres_from_last = haversine((location.latitude, location.longitude), last_lat_lng, unit=Unit.METERS)

            speed = metres_from_last / time_from_last
            car_speed = 4.47

            if speed > car_speed
                time_from_last_journey = (location.timestamp - last_journey_location.timestamp).total_seconds()
                twenty_mins = 20 * 60
                if time_from_last_journey < twenty_mins
                    location.journey_id = last_journey_location.journey_id
                    location.save()
                    recent_static_locations = locations_to_calc
                        .filter(timestamp__gt=last_journey_location.timestamp, timestamp__lt=location.timestamp)
                    
                    for static_location in recent_static_locations
                        static_location.journey_id = last_journey_location.journey_id
                        static_location.confirmed_no_journey = False
                        static_location.save()
                else
                    new_journey = Journey.create()
                    location.journey_id = new_journey.journey_id
                    location.save()
                    last_journey_location = location
            else
                location.confirmed_no_journey = True
