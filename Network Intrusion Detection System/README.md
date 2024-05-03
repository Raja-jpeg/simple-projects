# Simple Network Intrusion Detection System
This project implements a Network Intrusion Detection System (NIDS) with a graphical user interface (GUI) built using Python's tkinter library. The NIDS captures network traffic, preprocesses the captured packets, trains a Random Forest machine learning model, and then uses the trained model to detect potential intrusions or anomalies in the network traffic.

## Features
Capture network traffic using the scapy library.
Preprocess captured packets and extract relevant features.
Train a Random Forest model on the preprocessed packet data.
Detect intrusions or anomalies in the network traffic using the trained model.
Graphical user interface for easy interaction and visualization.

## Usage
Run the main.py script to launch the GUI.
Click the "Capture Traffic" button to capture network packets.
Click the "Train Model" button to train the Random Forest model on the captured packet data.
Click the "Detect Intrusions" button to detect potential intrusions or anomalies in the network traffic using the trained model.

## Snapshot
![image](https://github.com/Raja-jpeg/simple-projects/assets/59841593/4c8b5b79-89f5-4ef7-80e8-139764b18294)


## Requirements
Python 3.x, tkinter, scapy, pandas, scikit-learn
