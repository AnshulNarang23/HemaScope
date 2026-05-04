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

print("Heart Super Low:", call_hf('predict_heart', [20, 0, 0, 90, 120, 0, 0, 200, 0, 0.0, 0, 0, 0])) 
print("Diabetes Super Low:", call_hf('predict_diabetes', [20, 0, 18.0, 120, 60, 80, 60, 0.5, 8]))
