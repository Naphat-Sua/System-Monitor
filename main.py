import psutil
import time
import os
import subprocess

def get_cpu_temp():
    # Get CPU temp using external tools (requires iStats or osx-cpu-temp)
    try:
        # Using iStats (if not , type 'sudo gem install iStats' in your terminal)
        output = subprocess.check_output(["istats", "cpu"], text=True)
        temp_str = output.split(": ")[1].split("°")[0]
        return float(temp_str)
    except (subprocess.CalledProcessError, FileNotFoundError, IndexError, ValueError):
        try:
            # Using osx-cpu-temp (if not, type 'brew install osx-cpu-temp' in your terminal)
            output = subprocess.check_output(["osx-cpu-temp"], text=True)
            return float(output.strip().replace("°C", ""))
        except:
            return None

def format_bytes(bytes):
    # Convert bytes to human-readable format
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes < 1024:
            return f"{bytes:.2f} {unit}"
        bytes /= 1024
    return f"{bytes:.2f} PB"

def main(interval=1):
    # Main loop
    prev_net_io = psutil.net_io_counters()
    prev_sent = prev_net_io.bytes_sent
    prev_recv = prev_net_io.bytes_recv

    try:
        while True:
            os.system('clear')

            cpu_percent = psutil.cpu_percent(interval=None)
            cpu_per_core = psutil.cpu_percent(interval=None, percpu=True)

            memory = psutil.virtual_memory()

            disk = psutil.disk_usage('/')

            battery = psutil.sensors_battery()

            net_io = psutil.net_io_counters()
            current_sent = net_io.bytes_sent
            current_recv = net_io.bytes_recv
            sent_rate = (current_sent - prev_sent) / interval
            recv_rate = (current_recv - prev_recv) / interval
            prev_sent = current_sent
            prev_recv = current_recv

            temp = get_cpu_temp()

            print("===== System Performance Monitor =====")
            print(f"CPU Usage: {cpu_percent}%")
            print(f"Per Core Usage: {[f'{core}%' for core in cpu_per_core]}")
            
            print("\nMemory Usage:")
            print(f"Total: {format_bytes(memory.total)}")
            print(f"Used: {format_bytes(memory.used)} ({memory.percent}%)")
            
            print("\nDisk Usage:")
            print(f"Total: {format_bytes(disk.total)}")
            print(f"Used: {format_bytes(disk.used)} ({disk.percent}%)")
            
            print("\nNetwork Usage:")
            print(f"Sent Rate: {format_bytes(sent_rate)}/s")
            print(f"Receive Rate: {format_bytes(recv_rate)}/s")
            
            print("\nBattery Status:")
            if battery:
                print(f"Charge: {battery.percent}%")
                print(f"Plugged In: {'Yes' if battery.power_plugged else 'No'}")
            else:
                print("No battery detected")
            
            print("\nTemperature:")
            if temp is not None:
                print(f"CPU: {temp}°C")
            else:
                print("Temperature data unavailable (install iStats or osx-cpu-temp)")

            print("\nPress Ctrl+C to exit...")
            time.sleep(interval)

    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

if __name__ == "__main__":
    try:
        import psutil
    except ImportError:
        print("Error: psutil library not found. Install with: pip install psutil")
        exit(1)

    main(interval=1) 
