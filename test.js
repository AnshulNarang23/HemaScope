const url = 'https://anshulnarang23-disease-predictor.hf.space/gradio_api/call/predict_diabetes';
fetch(url, {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({data: [35, 1, 25, 180, 140, 50, 100, 1.0, 14]})
}).then(r => r.json()).then(j => {
  const event_id = j.event_id;
  const EventSource = require('eventsource');
  const es = new EventSource(url + '/' + event_id);
  es.onmessage = e => console.log('msg:', e.data);
  es.addEventListener('complete', e => { console.log('complete:', e.data); es.close(); });
}).catch(console.error);
