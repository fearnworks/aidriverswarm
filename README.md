## Swarm UI Demo 

UI Swarm concept. This app refactors a good deal of the parameter passing logic so that values can be modified at runtime for many of the params used in the llm swarm architecture introduced by echohive. 

To run : 

Setup virtual environment 

```bash
cd /wherever_your_project_is_located
python3 -m venv venv 
source venv/bin/activate 
pip install -r requirements/requirements.in
```


Create .env Add openai key to .env file in root of project

```bash
python3 webui/server.py
```