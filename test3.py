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
                print(line)

print("DIABETES varying BMI and TG:")
call_hf('predict_diabetes', [35, 1, 25, 180, 140, 50, 100, 1.0, 14])
call_hf('predict_diabetes', [35, 1, 30, 180, 200, 50, 100, 1.0, 14])
call_hf('predict_diabetes', [50, 1, 35, 180, 250, 50, 100, 1.0, 14])
