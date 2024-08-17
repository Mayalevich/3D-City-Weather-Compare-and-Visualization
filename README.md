# 3D-City-Weather-Compare-and-Visualization
This Python project visualizes weather data for multiple cities in a 3D bar chart. Users can input city names, and the program fetches real-time weather data for those cities using the OpenWeatherMap API. The visualization includes temperature, humidity, and wind speed parameters for each city.

Video Description: https://youtu.be/YSXGGjW6eDs

## Features

- Fetches real-time weather data from OpenWeatherMap API.
- Displays temperature, humidity, and wind speed in a 3D bar chart.
- Allows comparison of weather data across multiple cities.
- Provides user-friendly input prompts and error handling.
- Exits gracefully if the user decides to cancel the input.

## Prerequisites

- Python 3.x
- The following Python libraries:
  - `requests`
  - `matplotlib`
  - `numpy`
  - `tkinter`

You can install the required libraries using the following command:

```sh
pip install requests matplotlib numpy
```

## main

1. Clone the repository or download the `main.py` file to your local machine.

2. Sign up for an OpenWeatherMap API key if you don't already have one. You can get it from [OpenWeatherMap](https://openweathermap.org/api).

3. Replace `your_api_key` in the `main.py` file with your actual OpenWeatherMap API key.

## Usage

1. Run the `main.py` script:

   ```sh
   python main.py
   ```

2. Enter the city names separated by commas when prompted. For example:

   ```
   Toronto, New York, London, Paris
   ```

3. The program will fetch the weather data for the specified cities and display a 3D bar chart comparing temperature, humidity, and wind speed for each city.

## Error Handling

- If no cities are provided, the program will prompt the user to enter at least one city.
- If the weather data cannot be fetched for a city, a warning will be displayed, and the data for valid cities will be shown.
- If the user cancels the input dialog, the program will exit gracefully.

## Example
<img width="752" alt="WechatIMG626" src="https://github.com/user-attachments/assets/c7ef22ba-42bd-4fc4-a3c6-511ca49c7a39">
