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

print("DIABETES:")
call_hf('predict_diabetes', [35, 1, 25, 150, 140, 50, 100, 1.0, 14])
call_hf('predict_diabetes', [35, 1, 25, 200, 140, 50, 100, 1.0, 14])
call_hf('predict_diabetes', [35, 1, 25, 300, 140, 50, 100, 1.0, 14])

print("ANEMIA:")
call_hf('predict_anemia', [13.5, 40, 4.5, 90, 30])
call_hf('predict_anemia', [10.5, 40, 4.5, 90, 30])
call_hf('predict_anemia', [8.5, 40, 4.5, 90, 30])

print("HEART:")
call_hf('predict_heart', [50, 1, 2, 130, 180, 0, 1, 150, 0, 1.0, 2, 0, 2])
call_hf('predict_heart', [50, 1, 2, 130, 280, 0, 1, 150, 0, 1.0, 2, 0, 2])
