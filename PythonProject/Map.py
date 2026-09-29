import json
import webbrowser

# Taking input from user
source = input("Enter source: ")
destination = input("Enter destination: ")

# Creating JSON data
data = {
    "source": source,
    "destination": destination
}

# Convert to JSON
json_data = json.dumps(data, indent=4)

print("\nJSON Data:")
print(json_data)

# Open Google Maps
url = f"https://www.google.com/maps/dir/{source.replace(' ', '+')}/{destination.replace(' ', '+')}"
webbrowser.open(url)