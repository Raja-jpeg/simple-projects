import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from scapy.all import *
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

class NIDSGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Network Intrusion Detection System")

        # Create UI elements
        self.capture_button = ttk.Button(self.root, text="Capture Traffic", command=self.capture_traffic)
        self.capture_button.grid(row=0, column=0, padx=10, pady=10)

        self.results_label = ttk.Label(self.root, text="Captured Packets:")
        self.results_label.grid(row=1, column=0, padx=10, pady=5)

        self.results_text = tk.Text(self.root, height=10, width=50)
        self.results_text.grid(row=2, column=0, padx=10, pady=5)

        self.train_button = ttk.Button(self.root, text="Train Model", command=self.train_model)
        self.train_button.grid(row=3, column=0, padx=10, pady=10)

        self.detect_button = ttk.Button(self.root, text="Detect Intrusions", command=self.detect_intrusions)
        self.detect_button.grid(row=4, column=0, padx=10, pady=10)

        # Initialize DataFrame for storing captured packets
        self.packet_data = pd.DataFrame()

        # Initialize machine learning model
        self.clf = None

    def extract_features(self, packet):
        features = {}
        if IP in packet:
            features['src_ip'] = packet[IP].src
            features['dst_ip'] = packet[IP].dst
            features['protocol'] = packet[IP].proto
            features['packet_size'] = len(packet)
            # Check for missing or invalid values and handle them
            if any(value is None for value in features.values()):
                # Replace missing or invalid values with defaults
                features = {'src_ip': 'N/A', 'dst_ip': 'N/A', 'protocol': -1, 'packet_size': -1}
        return features

    def preprocess_packets(self, packet_list):
        features_list = []
        for packet in packet_list:
            features = self.extract_features(packet)
            features_list.append(features)
        df = pd.DataFrame(features_list)
        df.dropna(inplace=True)  # Drop rows with NaN values
        return df



    def capture_traffic(self):
        self.results_text.delete(1.0, tk.END)
        packets = sniff(count=10)  # Capture 10 packets
        print("Captured packets:", packets)  # For debugging
        self.packet_data = self.preprocess_packets(packets)
        self.results_text.insert(tk.END, self.packet_data)

    def train_model(self):
        if self.packet_data.empty:
            messagebox.showwarning("Warning", "No packet data available. Capture traffic first.")
            return

        X = self.packet_data.drop(['src_ip', 'dst_ip'], axis=1)  # Exclude IP addresses for training
        y = [0] * len(X)  # Label all packets as benign for training (0 represents benign)
        self.clf = RandomForestClassifier()
        self.clf.fit(X, y)
        messagebox.showinfo("Info", "Model trained successfully.")

    def detect_intrusions(self):
        if self.clf is None:
            messagebox.showwarning("Warning", "Model not trained. Please train the model first.")
            return

        if self.packet_data.empty:
            messagebox.showwarning("Warning", "No packet data available. Capture traffic first.")
            return

        X = self.packet_data.drop(['src_ip', 'dst_ip'], axis=1)  # Exclude IP addresses for detection
        y_pred = self.clf.predict(X)
        intrusion_indices = [i for i, pred in enumerate(y_pred) if pred == 1]  # 1 represents intrusion
        if intrusion_indices:
            messagebox.showwarning("Intrusion Detected", f"Intrusion detected in packets: {intrusion_indices}")
        else:
            messagebox.showinfo("No Intrusion", "No intrusion detected.")

# Main function
def main():
    root = tk.Tk()
    nidsgui = NIDSGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()