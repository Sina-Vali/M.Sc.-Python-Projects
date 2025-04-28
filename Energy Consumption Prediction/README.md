# Overview
In Quebec, energy consumption typically peaks daily in the morning, between 6 a.m. and 9 a.m., and in the evening, between 4 p.m. and 7 p.m. These periods, called peak periods, are particularly challenging to manage, especially during extreme weather conditions, whether very hot or very cold. To reduce these peaks, Hydro-Québec offers advantageous rates to encourage users to limit their consumption during these critical periods.

An effective method to reduce consumption during peak periods is to adjust heating or air conditioning, which represent the main sources of energy consumption in a building. Thanks to thermal inertia, it is possible to use energy before the peak period to preheat or precool the building while preserving occupant comfort. To optimize these strategies, it is necessary to predict, a few hours in advance, the consumption of the heating, ventilation, and air conditioning (HVAC) system. These predictions allow anticipating peaks and implementing proactive heating control rather than reactive control.


# Instructions
In this project, you must design a model to predict the consumption in a house located in Montreal. You have one year of data containing the following characteristics:

- Date
- HVAC system consumption (kW)
- Indoor temperature (°C)
- Weather:
  - Outdoor temperature (°C)
  - Humidity (%)
  - Sunshine (W/m²)
  - Wind speed (km/h)
  - Wind direction (°)

Using the method of your choice, develop a model to predict the HVAC system consumption up to 4 hours (16 time steps) in advance.
