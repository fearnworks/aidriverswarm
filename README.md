python3 -m venv venv 
source venv/bin/activate 
pip install -r requirements/requirements.in

Add openai key to .env 
python3 webui/server.py