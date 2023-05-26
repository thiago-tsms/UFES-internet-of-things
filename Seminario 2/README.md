python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

docker stats --format "{{.CPUPerc}}|{{.MemUsage}}|{{.NetIO}}" > log.txt