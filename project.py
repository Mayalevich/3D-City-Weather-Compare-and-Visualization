import numpy as np
import requests
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import tkinter as tk
from tkinter import simpledialog, messagebox


def fetch_weather_data(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    print(f"Using URL: {url}")
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred for {city}: {err}")
        print(f"Response content: {response.content}")  # Debugging: Print response content
        return None
    except Exception as err:
        print(f"Other error occurred for {city}: {err}")
        return None

# Function to extract weather data
def extract_weather_data(weather_data):
    try:
        temp = weather_data['main']['temp'] - 273.15  # Convert from Kelvin to Celsius
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        return temp, humidity, wind_speed
    except KeyError as e:
        print(f"KeyError occurred: {e}")
        return None

# Function to create 3D bar chart comparing multiple cities
def create_3d_bar_chart(city_data):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    
    parameters = ['Temperature (°C)', 'Humidity (%)', 'Wind Speed (m/s)']
    parameter_indices = np.arange(len(parameters))
    city_colors = plt.get_cmap('tab10')

    xpos = []
    ypos = []
    zpos = []
    dx = []
    dy = []
    dz = []
    colors = []
    legends = []

    for i, (city, values) in enumerate(city_data.items()):
        if values:
            for j, value in enumerate(values):
                xpos.append(j * 5)  # Increase spacing between parameters
                ypos.append(i * 5)  # Separate cities
                zpos.append(0)
                dx.append(2)
                dy.append(2)
                dz.append(value)
                colors.append(city_colors(i % 10))
            legends.append((city_colors(i % 10), city))
        else:
            print(f"No valid data for {city}")

    ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color=colors)

    # Add labels to bars
    for x, y, z, value in zip(xpos, ypos, dz, dz):
        ax.text(x, y, z, f'{value:.1f}', color='black', ha='center', va='bottom')

    # Set axes labels and titles
    ax.set_xticks(parameter_indices * 5)
    ax.set_xticklabels(parameters, fontsize=8)  # Adjusted font size to 8
    ax.set_yticks(np.arange(len(city_data)) * 5)
    ax.set_yticklabels(list(city_data.keys()), fontsize=10)
    ax.set_xlabel('Parameters')
    ax.set_ylabel('Cities')
    ax.set_zlabel('Values')
    plt.title('3D Weather Comparison Visualization')

    # Add legend
    legend_patches = [plt.Line2D([0], [0], color=color, lw=4) for color, _ in legends]
    legend_labels = [city for _, city in legends]
    plt.legend(legend_patches, legend_labels, loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=3)

    plt.show()

# GUI for user input
def get_user_input():
    root = tk.Tk()
    root.withdraw()
    cities = simpledialog.askstring(title="City Names", prompt="Enter city names separated by commas (e.g., Toronto, New York, London, UK):")
    if cities is None:
        return None  # Handle the case where the user cancels the dialog
        exit
    return cities.split(',')

# Main function
def main():
    api_key = 'your_api_key'  # Replace with your actual API key
    print(f"Using API Key: {api_key}")  # Debugging: Print API key
    
    while True:
        cities = get_user_input()
        if cities is None:
            messagebox.showinfo("Exit", "No cities provided. Exiting the program.")
            return  # Exit the program if the user cancels the input dialog
        if not cities:
            messagebox.showerror("Input Error", "No cities provided. Please enter at least one city.")
            continue
        
        city_data = {}
        invalid_cities = []
        for city in cities:
            city = city.strip()
            weather_data = fetch_weather_data(api_key, city)
            if weather_data:
                data = extract_weather_data(weather_data)
                if data:
                    city_data[city] = data
                else:
                    invalid_cities.append(city)
            else:
                invalid_cities.append(city)
                print(f"Failed to fetch weather data for {city}. Please check the API key and city name.")
        
        if city_data:
            if invalid_cities:
                messagebox.showwarning("Warning", f"No data available for the following cities: {', '.join(invalid_cities)}. Displaying data for valid cities.")
            create_3d_bar_chart(city_data)
            break
        else:
            messagebox.showerror("Data Error", "No valid data to display. Please check the city names and try again.")

if __name__ == "__main__":
    main()
