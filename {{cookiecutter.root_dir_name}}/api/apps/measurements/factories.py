
"""
Creates fake objects to seed the database for testing. This makes use
of factory boy and Faker modules. For reference on how to create a
one-to-many factory, see: 
https://simpleit.rocks/python/django/setting-up-a-factory-for-one-to-many-relationships-in-factoryboy/
"""

import factory


class StationFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'measurements.Stations'


    id = factory.Sequence(lambda n: "station_%d" % n)
    name = factory.Faker("text", max_nb_chars=20)
    latitude = factory.Faker("latitude")
    longitude = factory.Faker("longitude")
    

class StationWithMeasurementFactory(StationFactory):
    
    @factory.post_generation
    def measurements(obj, create, extracted, **kwargs):
        """
        If called like: StationWithMeasurementFactory(measurements=4) 
        it generates a Station with 4 measurements.  If called without
        `measurements` argument, it generates a random amount of 
        measurements for this station
        """
        if not create:
            # Build, not create related
            return

        if extracted:
            for n in range(extracted):
                MeasurementFactory(station=obj)
        else:
            import random
            number_of_units = random.randint(20, 40)
            for n in range(number_of_units):
                MeasurementFactory(station=obj)


class MeasurementFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = "measurements.Measurements"

    id = factory.Sequence(lambda n: n)
    station = factory.SubFactory(StationFactory)
    product = factory.Faker("random_element", elements=["at", "wt", "st"])
    value = factory.Faker("random_int", max=50)
