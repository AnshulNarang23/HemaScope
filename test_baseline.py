import urllib.request
import json

def call_hf(api_name, data):
    url = f'https://anshulnarang23-disease-predictor.hf.space/gradio_api/call/{api_name}'
    req = urllib.request.Request(url, data=json.dumps({"data": data}).encode('utf-8'), headers={'Content-Type': 'application/json'})
    res = urllib.request.urlopen(req)
    j = json.loads(res.read().decode('utf-8'))
    event_id = j['event_id']
    
    stream_url = f'{url}/{event_id}'
    req_stream = urllib.request.Request(stream_url, headers={'Accept': 'text/event-stream'})
    with urllib.request.urlopen(req_stream) as response:
        for line in response:
            line = line.decode('utf-8').strip()
            if line.startswith('data:'):
                return line
    return 0

print("Testing HEART base arrays...")
print("Heart Low:", call_hf('predict_heart', [29, 0, 1, 110, 160, 0, 0, 185, 0, 0.0, 1, 0, 0])) 
print("Heart Med:", call_hf('predict_heart', [50, 1, 2, 130, 210, 0, 1, 155, 0, 0.8, 2, 0, 1])) 
print("Heart High:", call_hf('predict_heart', [67, 1, 4, 175, 310, 1, 2, 105, 1, 4.2, 3, 3, 3]))

print("Testing DIABETES base arrays...")
print("Diabetes Low:", call_hf('predict_diabetes', [26, 0, 20.8, 165, 80, 65, 85, 0.7, 12]))
print("Diabetes Med:", call_hf('predict_diabetes', [44, 1, 27.5, 205, 140, 48, 135, 1.0, 20]))
print("Diabetes High:", call_hf('predict_diabetes', [62, 1, 36.2, 295, 230, 33, 185, 2.1, 34]))
