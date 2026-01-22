import subprocess

result = subprocess.run(["ls"], capture_output=True, text=True)

if result.returncode == 0:
    print("Files in directory:\n", result.stdout)
else:
    print("Error:", result.stderr)