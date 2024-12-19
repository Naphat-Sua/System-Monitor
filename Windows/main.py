import tkinter as tk
from tkinter import messagebox
import psutil
import time
from datetime import datetime
import csv
import os
from PIL import ImageGrab
import json
import logging
from pathlib import Path

class SystemMonitor:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("System Resource Monitor")
        self.root.geometry("400x600")
        
        self.log_dir = Path("system_logs")
        self.log_dir.mkdir(exist_ok=True)
        
        logging.basicConfig(
            filename=self.log_dir / "monitor.log",
            level=logging.INFO,
            format='%(asctime)s - %(message)s'
        )
        
        self.setup_gui()
        self.load_settings()
        
    def setup_gui(self):

        self.consent_label = tk.Label(
            self.root, 
            text="This application monitors system resources.\nAll data is stored locally.",
            wraplength=350
        )
        self.consent_label.pack(pady=10)
        
        self.options_frame = tk.LabelFrame(self.root, text="Monitoring Options")
        self.options_frame.pack(pady=10, padx=10, fill="x")
        
        self.cpu_var = tk.BooleanVar(value=True)
        self.memory_var = tk.BooleanVar(value=True)
        self.disk_var = tk.BooleanVar(value=True)
        
        tk.Checkbutton(self.options_frame, text="CPU Usage", variable=self.cpu_var).pack(anchor="w")
        tk.Checkbutton(self.options_frame, text="Memory Usage", variable=self.memory_var).pack(anchor="w")
        tk.Checkbutton(self.options_frame, text="Disk Usage", variable=self.disk_var).pack(anchor="w")
        
        self.status_frame = tk.LabelFrame(self.root, text="Current Status")
        self.status_frame.pack(pady=10, padx=10, fill="x")
        
        self.cpu_label = tk.Label(self.status_frame, text="CPU: ---%")
        self.cpu_label.pack(anchor="w")
        
        self.memory_label = tk.Label(self.status_frame, text="Memory: ---%")
        self.memory_label.pack(anchor="w")
        
        self.disk_label = tk.Label(self.status_frame, text="Disk: ---%")
        self.disk_label.pack(anchor="w")
        
        self.start_button = tk.Button(self.root, text="Start Monitoring", command=self.start_monitoring)
        self.start_button.pack(pady=5)
        
        self.stop_button = tk.Button(self.root, text="Stop Monitoring", command=self.stop_monitoring, state="disabled")
        self.stop_button.pack(pady=5)
        
        self.export_button = tk.Button(self.root, text="Export Data", command=self.export_data)
        self.export_button.pack(pady=5)
        
        self.clear_button = tk.Button(self.root, text="Clear Data", command=self.clear_data)
        self.clear_button.pack(pady=5)
        
        self.monitoring = False
        self.data = []

    def load_settings(self):
        try:
            with open("monitor_settings.json", "r") as f:
                settings = json.load(f)
                self.cpu_var.set(settings.get("cpu", True))
                self.memory_var.set(settings.get("memory", True))
                self.disk_var.set(settings.get("disk", True))
        except FileNotFoundError:
            pass

    def save_settings(self):
        settings = {
            "cpu": self.cpu_var.get(),
            "memory": self.memory_var.get(),
            "disk": self.disk_var.get()
        }
        with open("monitor_settings.json", "w") as f:
            json.dump(settings, f)

    def start_monitoring(self):
        if not messagebox.askyesno("Consent", 
            "Do you consent to monitoring the selected system resources?\n"
            "All data will be stored locally on your machine."):
            return
            
        self.monitoring = True
        self.start_button.config(state="disabled")
        self.stop_button.config(state="normal")
        logging.info("Monitoring started")
        self.update_stats()

    def stop_monitoring(self):
        self.monitoring = False
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")
        logging.info("Monitoring stopped")

    def update_stats(self):
        if not self.monitoring:
            return
            
        timestamp = datetime.now()
        stats = {"timestamp": timestamp}
        
        if self.cpu_var.get():
            cpu_percent = psutil.cpu_percent()
            self.cpu_label.config(text=f"CPU: {cpu_percent}%")
            stats["cpu"] = cpu_percent
            
        if self.memory_var.get():
            memory_percent = psutil.virtual_memory().percent
            self.memory_label.config(text=f"Memory: {memory_percent}%")
            stats["memory"] = memory_percent
            
        if self.disk_var.get():
            disk_percent = psutil.disk_usage('/').percent
            self.disk_label.config(text=f"Disk: {disk_percent}%")
            stats["disk"] = disk_percent
            
        self.data.append(stats)
        self.root.after(1000, self.update_stats)

    def export_data(self):
        if not self.data:
            messagebox.showinfo("Info", "No data to export")
            return
            
        filename = self.log_dir / f"system_stats_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        
        with open(filename, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=self.data[0].keys())
            writer.writeheader()
            writer.writerows(self.data)
            
        messagebox.showinfo("Success", f"Data exported to {filename}")
        logging.info(f"Data exported to {filename}")

    def clear_data(self):
        if messagebox.askyesno("Confirm", "Are you sure you want to clear all collected data?"):
            self.data = []
            logging.info("Data cleared")
            messagebox.showinfo("Success", "Data cleared")

    def run(self):
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def on_closing(self):
        if self.monitoring:
            if messagebox.askyesno("Quit", "Monitoring is still running. Do you want to quit?"):
                self.stop_monitoring()
                self.save_settings()
                self.root.destroy()
        else:
            self.save_settings()
            self.root.destroy()

if __name__ == "__main__":
    app = SystemMonitor()
    app.run()
