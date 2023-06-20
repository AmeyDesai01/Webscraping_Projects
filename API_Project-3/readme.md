Hello I am Amey Desai, I am learning python language and building projects from Beginner level to advance level

#Aim of the project:- To build ISS overhead notifier api project.

#Requirements:- Any python IDE and Understanding of API

The ISS (International Space Station) Overhead Notifier API project is a program that provides real-time notifications when
the ISS is passing overhead a specific location. It utilizes the ISS API to fetch the current position of the ISS and determines if it is visible from the given location.

Here's a short theory on how the ISS Overhead Notifier API project works:

1.Location Input: The program takes input from the user for their desired location (latitude and longitude) or uses a default location.

2.ISS API Integration: The program integrates with the ISS API, which provides information about the current position of the ISS.

3.Data Retrieval: The program makes a request to the ISS API to fetch the data, including the current latitude and longitude of the ISS.

4.Calculation: Using the latitude and longitude of the ISS and the user's location, the program calculates the distance between the two points. It also considers other factors like the altitude of the ISS, the viewing angle, and atmospheric conditions to determine if the ISS is visible from the given location.

5.Notification: If the ISS is within the visible range, the program generates a notification or alert to notify the user that the ISS is passing overhead. This notification can be in the form of a text message, email, or any other preferred method.

6.Real-time Updates: The program continuously updates the ISS position by making periodic requests to the ISS API. It recalculates the visibility and sends notifications whenever the ISS comes within range of the given location.