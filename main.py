Creating a complete Python program for a "carbon-footprint-calculator" involves several steps. The program will help individuals and businesses to calculate their carbon emissions based on various factors such as energy consumption, transportation, and waste. This is a minimal example, and real-world applications would require more detailed calculations, potentially involving external APIs or databases to get real-time data.

Below is a simplified implementation of a carbon footprint calculator in Python. To keep it straightforward, we'll simulate real-time data using fixed values since an actual implementation would need APIs or databases to get dynamic inputs.

```python
import sys

class CarbonFootprintCalculator:
    def __init__(self):
        # Constants for emission factors (in kg CO2 per unit)
        self.electricity_emission_factor = 0.475  # kg CO2/kWh
        self.gasoline_emission_factor = 2.31  # kg CO2/liter
        self.water_emission_factor = 0.3  # kg CO2/cubic meter
        self.travel_emission_factor = 0.255  # kg CO2/passenger-kilometer

    def calculate_electricity_emissions(self, kwh):
        """Calculate emissions from electricity."""
        try:
            emissions = kwh * self.electricity_emission_factor
            return emissions
        except Exception as e:
            print(f"Error calculating electricity emissions: {e}")
            sys.exit(1)

    def calculate_transport_emissions(self, liters):
        """Calculate emissions from gasoline usage."""
        try:
            emissions = liters * self.gasoline_emission_factor
            return emissions
        except Exception as e:
            print(f"Error calculating transport emissions: {e}")
            sys.exit(1)

    def calculate_water_emissions(self, cubic_meters):
        """Calculate emissions from water usage."""
        try:
            emissions = cubic_meters * self.water_emission_factor
            return emissions
        except Exception as e:
            print(f"Error calculating water emissions: {e}")
            sys.exit(1)

    def calculate_travel_emissions(self, kilometers):
        """Calculate emissions from travel."""
        try:
            emissions = kilometers * self.travel_emission_factor
            return emissions
        except Exception as e:
            print(f"Error calculating travel emissions: {e}")
            sys.exit(1)

    def calculate_total_emissions(self, electricity_kwh, gasoline_liters, water_cubic_meters, travel_kilometers):
        """Calculate total emissions from all sources."""
        try:
            electricity_emissions = self.calculate_electricity_emissions(electricity_kwh)
            transport_emissions = self.calculate_transport_emissions(gasoline_liters)
            water_emissions = self.calculate_water_emissions(water_cubic_meters)
            travel_emissions = self.calculate_travel_emissions(travel_kilometers)

            total_emissions = electricity_emissions + transport_emissions + water_emissions + travel_emissions
            return total_emissions
        except Exception as e:
            print(f"Error calculating total emissions: {e}")
            sys.exit(1)

def main():
    calculator = CarbonFootprintCalculator()

    # Get inputs from user
    try:
        electricity_kwh = float(input("Enter electricity usage in kWh: "))
        gasoline_liters = float(input("Enter gasoline usage in liters: "))
        water_cubic_meters = float(input("Enter water usage in cubic meters: "))
        travel_kilometers = float(input("Enter travel distance in kilometers: "))
    except ValueError as e:
        print(f"Invalid input: {e}")
        sys.exit(1)

    # Calculate total emissions
    total_emissions = calculator.calculate_total_emissions(electricity_kwh, gasoline_liters, water_cubic_meters, travel_kilometers)
    print(f"Total carbon emissions: {total_emissions:.2f} kg CO2")

if __name__ == "__main__":
    main()
```

### Explanation:
1. **Constants**: The emission factors are predefined to convert activity data (e.g., kWh of electricity used) into CO2 emissions.

2. **Functions**: Separate functions compute emissions for each type of activity (electricity, transport, water, and travel).

3. **Error Handling**: Each calculation is wrapped in a try-except block to handle potential errors.

4. **User Input**: The program takes activity data from the user, which should be entered as floats.

5. **Main Method**: Calculates and prints the total emissions based on user input.

This program is just a starting point. A real-world application would involve more sophisticated calculations, user interface, data persistence, and integration with external data sources for more accurate and up-to-date conversion factors.