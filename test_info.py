import urllib.request
import json

url = 'https://anshulnarang23-disease-predictor.hf.space/gradio_api/info'
req = urllib.request.Request(url)
res = urllib.request.urlopen(req)
j = json.loads(res.read().decode('utf-8'))
for endpoint, details in j['named_endpoints'].items():
    print(f"Endpoint: {endpoint}")
    print("Parameters:")
    for param in details['parameters']:
        print(f"  - {param['type']} (label: {param.get('label', 'N/A')})")
    print()
