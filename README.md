![image](https://user-images.githubusercontent.com/95341497/230357459-6e940b17-6157-4691-a2ef-76e084c6f7af.png)

# projectPad

## Introduction

> A great web app for lab project management that allows users to effortlessly create and manage notes for their experiments.

ProjectPad is a web app for lab project management, developed to help research scientists to effortlessly create and manage notes for their experiments. With a strong focus on efficient workflow, ProjectPad streamlines the process of lab project management, making it easier for researchers to focus on their experiments and collect data efficiently. This repository contains the source code of ProjectPad.

This portfolio project was developed as part of the requirements for the Holberton School's foundation in software engineering program. The timeline for the project was two weeks from conception to delivery of the MVP.

**Useful links:** ![rsz_1rsz_642eb85eda4a1](https://user-images.githubusercontent.com/95341497/230377097-5d647aea-0e4c-40c5-809e-d9914c0f47f8.png)

- [Deployed site](https://projectpad.onrender.com/home)
- Link to project [blog article](https://medium.com/@jonyamagiri/introducing-projectpad-754ac88bae9a)
- Author(s) [LinkedIn](https://www.linkedin.com/in/jonyamagiri/)


## Inspiration 
As a former research scientist, I struggled with the challenge of keeping track of my notes on experiments and progress. I used to scribble notes in notebooks, and sometimes I found myself swimming in a sea of papers with my notes scattered all over the lab. It was frustrating and time-consuming to constantly search for some results I had written in a notebook that was nowhere to be found. It made it difficult to manage my projects effectively.

When I started learning software engineering, I remembered the pain-point I experienced, and I decided to find a solution by creating a companion service that would be available on all devices. I wanted to develop an app that would streamline lab project management and make it easier for researchers to keep track of their experiments. The idea was to create a platform that allowed scientists to effortlessly create and manage notes for their experiments with a strong focus on efficient workflow. This led to development of ProjectPad, the ultimate web app for lab project management. The app simplifies the process of lab project management, making it easier for researchers to focus on their experiments and collect data efficiently. Now, researchers can create and manage notes for their experiments, visualize their data, and collaborate with team members to ensure successful research outcomes.


## Features

***Current***

- [x] **Effortless Note-Taking:** Users can effortlessly create and manage notes for their experiments. The app provides a user-friendly interface for note-taking, making it easy to document and organize lab projects' progress and results.

- [x] **Convenient Accessibility:** ProjectPad is accessible to users who have difficulty physically accessing their notes or need to collaborate with others remotely. The app can be accessed from any device with an internet connection, making it easy to manage lab projects on the go.

- [x] **Secure Data Management:** ProjectPad ensures that users' data is secure and protected. The app provides encryption and data backup features, allowing users to safeguard their notes and related information.

***Future***
- [ ] **Streamlined Project Management:** ProjectPad streamlines the lab project management process, enabling users to manage their projects more efficiently. The app provides tools for task management, project tracking, and collaboration, allowing users to focus on their work and achieve their goals.


## Screenshots

![image](https://user-images.githubusercontent.com/95341497/230374341-1279a54e-608d-46df-a672-d480309abd24.png)

![image](https://user-images.githubusercontent.com/95341497/230374917-a450abed-d273-4291-9002-da02a6de876f.png)


## Challenges overcome

- One of the technical challenges I faced while developing ProjectPad was incorporating a rich-text editor for article writing. The app needed to allow users to create articles with advanced formatting options such as bold, italic, headings, lists, images, and links. After reading several articles and documentation, I stumbled upon [Flask CKEditor](https://flask-ckeditor.readthedocs.io/en/latest/), a highly customizable and user-friendly editor. Although I had never used it before, I decided to give it a try. I followed the documentation and tutorials provided by Flask-CKEditor to integrate it into ProjectPad. This involved configuring the editor, adding it to the application, and setting up routes to handle the article creation and editing functionality. The integration of Flask CKEditor into ProjectPad was a success, and users can now create articles with ease using the rich-text editor. This was a significant achievement for me, as it allowed me to enhance the functionality of the app and improve the user experience.

## Languages & Technologies Used

![image](https://user-images.githubusercontent.com/95341497/230384698-b333f827-79df-48c8-9e9e-82c2fea94f5a.png)

- HTML, CSS, and JavaScript
- Bootstrap
- Flask web framework
- Python
- SQLite3 database
- Render.com cloud platform

## Installation
To use ProjectPad on your local machine, you can follow the steps below:

- Clone this repository using the command: ```git clone https://github.com/jonyamagiri/projectPad.git```
- Install the required dependencies using the command: ```pip install -r requirements.txt```
- Create a new virtual environment using the command: ```python3 -m venv myenv```
- Activate the virtual environment using the command: ```source myenv/bin/activate (for Linux/Mac) or myenv\Scripts\activate (for Windows)```
- Run the app using the command: ```python app.py```
- Navigate to http://localhost:5000/ in your web browser to view the app.

## Usage
To use [ProjectPad](https://projectpad.onrender.com/register), you need to create an account and log in. Once logged in, you can create and manage notes for your experiments, categorize notes according to project and experiment, edit and delete notes as needed. You can also visualize your data, collaborate with team members to ensure successful research outcomes, and update your account information using the account management dashboard.

## Contributing
- ProjectPad was developed by Joab O. Nyamagiri, a software engineering student from ALX-Holberton School.
- If you'd like to contribute to ProjectPad, please fork the repository, make changes, and submit a pull request. I welcome all contributions!

## Related projects
None at the moment

## Licensing
ProjectPad is licensed under the MIT License. Please see the LICENSE file for more details.