# Genuone


Genuone is a web app aiming to make the classroom more engaging by providing the instructor with real-time feedback from the students, by taking continuous images of the classroom. The images are analyzed by Microsofts Emotion API and the result is sent to the server in json format. Data Analysis is done on the data received using Pandas Library(Python). The app then shows the result on the instructor's screens i.e. feedback of students in class using various emojis. The result is based on the response of the whole class and is calculated using the median. 

Pictures are currently taken by an Android device which is connected to genuone via a pipeline.

Technologies Used
-----
- Microsoft Cognitive Services, Emotion API
- WebSocket servers and clients
- Data Analysis using Python data science libraries
- Android Debugging Tool to capture and retrieve photos
- Bootstrap

Features
------
- Students can ask questions at the question portal which is hosted at a public IP. The question appears on the screen of the instructor and can be asked anonymously. 
- Data from all the classes can be analyzed to get trends.


TODO
----
- Add webcam support in addtion to using the phone's camera.
- Add a script which starts every thing, as of now several scripts are needed to start the web app which makes it very messy and unorganized.
