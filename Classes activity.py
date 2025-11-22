class Passenger:
    def __init__(self, name, current_location, destination, date):
        self.name = name
        self.current_location = current_location
        self.destination = destination
        self.date = date
    def get_passenger_info(self):
        return f"Passenger: {self.name}, From: {self.current_location}, To: {self.destination}, Date: {self.date}"
    def get_weight_allowance(self):
        return " Weight limit: 25 kg"
class EconomyPassenger(Passenger):
    pass
class FirstClassPassenger(Passenger):
    def __init__(self,name, current_location, destination, date, weight, lounge_access):
        super().__init__ (name, current_location, destination, date)
        self.weight = weight
        self.lounge_access = lounge_access
    def weight(self, weight):
        self.weight = weight
    def lounge_access(self):
        if self.lounge_access:
            return f"{self.name} has lounge access"
        else:
            return f"{self.name} has no lounge access"
class PremiumClassPassenger(Passenger):
    def __init__(self,name, current_location, destination, date, weight, priority_boarding):
        super().__init__(name, current_location, destination, date)
        self.weight = weight
        self.priority_boarding = priority_boarding
    def weight(self, weight):
        self.weight = weight
    def priority_boarding(self):
        if self.priority_boarding:
            return f"{self.name} has priority boarding"
        else:
            return f"{self.name} has no priority boarding"

    eco = EconomyPassenger("Phillip," "Nairobi," "Kigali," "06-11-2025")
    first = FirstClassPassenger("Davine," "Kigali" "Dubai" "04-05-2025", 25, True)
    premium = PremiumClassPassenger ("Hassanat," "India" "Delhi" "06-05-2025", 30, True)
    print(eco.get_passenger_info())
    print(eco.get_weight_allowance())
    print(first.get_passenger_info())
    print(first.access_lounge())
    print(premium.get_passenger_info())
    print(premium.get_priority_boadring())
