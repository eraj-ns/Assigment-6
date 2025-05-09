class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

f = TemperatureConverter.celsius_to_fahrenheit(0)
print("0°C =", f, "°F")

f = TemperatureConverter.celsius_to_fahrenheit(100)
print("100°C =", f, "°F")

