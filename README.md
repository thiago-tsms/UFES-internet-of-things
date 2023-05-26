### Seminário 2

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

Comando para coleta de status do container
docker stats --format "{{.CPUPerc}}|{{.MemUsage}}|{{.NetIO}}" > log.txt