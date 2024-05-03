# Simple Network Intrusion Detection System
This project implements a Network Intrusion Detection System (NIDS) with a graphical user interface (GUI) built using Python's tkinter library. The NIDS captures network traffic, preprocesses the captured packets, trains a Random Forest machine learning model, and then uses the trained model to detect potential intrusions or anomalies in the network traffic.

## Features
1. Capture network traffic using the scapy library.
2. Preprocess captured packets and extract relevant features.
3. Train a Random Forest model on the preprocessed packet data.
4. Detect intrusions or anomalies in the network traffic using the trained model.
5. Graphical user interface for easy interaction and visualization.

## Usage
1. Run the main.py script to launch the GUI.
2. Click the "Capture Traffic" button to capture network packets.
3. Click the "Train Model" button to train the Random Forest model on the captured packet data.
4. Click the "Detect Intrusions" button to detect potential intrusions or anomalies in the network traffic using the trained model.

## Snapshot
![image](https://github.com/Raja-jpeg/simple-projects/assets/59841593/4c8b5b79-89f5-4ef7-80e8-139764b18294)


## Requirements
Python 3.x, tkinter, scapy, pandas, scikit-learn

## Disclaimer
Did not test extensively
