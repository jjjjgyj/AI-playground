import requests
from bs4 import BeautifulSoup

# Step 1: Send a GET request to the United Airlines website
url = "https://www.united.com/en/us/flight-search/book-a-flight/results/rev?f=SYD&t=LAX&d=2022-01-01&tt=1&sc=1&px=1&taxng=1&idx=1"
response = requests.get(url)

# Step 2: Parse the HTML response
soup = BeautifulSoup(response.text, "html.parser")

# Step 3: Extract flight information
flight_results = soup.find_all("div", class_="flight-block")

for flight in flight_results:
    # Extract flight details
    flight_details = flight.find("div", class_="flight-details")
    departure_time = flight_details.find("div", class_="departure-time").text.strip()
    arrival_time = flight_details.find("div", class_="arrival-time").text.strip()
    flight_number = flight_details.find("div", class_="flight-number").text.strip()

    # Extract flight price
    flight_price = flight.find("span", class_="price-point").text.strip()

    # Print flight information
    print(f"Flight: {flight_number}")
    print(f"Departure: {departure_time}")
    print(f"Arrival: {arrival_time}")
    print(f"Price: {flight_price}")
    print()

# Step 4: Apply filters and sort flight options

# Apply filters
filtered_flights = []
for flight in flight_results:
    # Apply filters based on your criteria
    if flight_price < 600:  # Example filter: only consider flights with price less than $500
        filtered_flights.append(flight)

# Sort flight options
sorted_flights = sorted(filtered_flights, key=lambda x: x.flight_price)  # Sort flights based on price in ascending order

# Step 5: Display the cheapest flight options
print("results: ", sorted_flights)