# Intersections Counter App

Welcome to the Intersections Counter v1.3 app! This simple web application allows you to count intersections in a set of chords. You can use preset chord sets or input your custom chords in the format (1, 2, 3, 4).

![App Image](./app.png)

## Table of Contents
- [Big-O Runtime](#big-o-runtime)
- [Features](#features)
- [Installation and Running](#installation-and-running)
    - [Using Flask](#using-flask)
    - [Using Dockerfile](#using-dockerfile)
- [old_main.py](#old_mainpy-file)

## Big-O Runtime
The algorithm has a linear time complexity O(n), where n is the length of the 'chords' list. It iterates through the list once using a two-pointer strategy. The overall efficiency is linear, making it suitable for moderate-sized inputs.

## Features

- Count intersections in chord sets.
- Choose from preset chord sets or input custom chords.

## Installation and Running

### Using Flask

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
2. Run the Flask application locally:
   ```bash
   python app.py

### Using Dockerfile
1. For convinience I include dockerfile, Build the Docker image:
    ```bash
    docker build -t intersections-counter .

2. Run the Docker container:
    ```bash
    docker run -p 5001:5001 intersections-counter
3. Access the application in your browser at http://localhost:5001

## old_main.py file

If you prefer to use the original solution without going through the installation process, you can run the following command:

```bash
python3 old_main.py