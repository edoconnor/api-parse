import subprocess

subprocess.run(["python3", "scrape/edina.py"])

subprocess.run(["python3", "scrape/hopkins.py"])

subprocess.run(["python3", "scrape/south-wash.py"])

subprocess.run(["python3", "scrape/white-bear.py"])

subprocess.run(["python3", "multi_upload.py"])
