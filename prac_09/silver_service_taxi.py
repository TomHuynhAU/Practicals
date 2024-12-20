from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that includes flagfall and fanciness."""

    flagfall = 4.50  # Class variable for the flagfall charge

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness  # Adjust price per km according to fanciness

    def get_fare(self):
        """Return the price for the taxi trip including flagfall."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return a string like a Taxi but with flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
