
import time, requests, random

def schedule_submissions(total=80, hours=24):
    interval = (hours * 3600) / total
    for i in range(total):
        try:
            response = requests.get("http://localhost:5000/submit")
            print(f"[{i+1}/{total}] ✅ Submitted: {response.text}")
        except Exception as e:
            print(f"[{i+1}/{total}] ❌ Error:", e)
        time.sleep(random.uniform(interval * 0.8, interval * 1.2))

if __name__ == "__main__":
    schedule_submissions()
