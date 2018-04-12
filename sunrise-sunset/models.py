class Location:
    state = None
    city = None
    lat = None
    lng = None
    timezone = None

    def __init__(self, city, lat, lng, state="WA", timezone=None):
        self.state = state
        self.city = city
        self.lat = lat
        self.lng = lng
        self.timezone = timezone

    def __str__(self):
        return "{},{} ({}, {})".format(self.state, self.city, self.lat, self.lng)
