### Seminário 2

<ul>
<li>python -m venv .venv</li>
<li>source .venv/bin/activate</li>
<li>pip install -r requirements.txt</li>
</ul>

Comando para coleta de status do container
docker stats --format "{{.CPUPerc}}|{{.MemUsage}}|{{.NetIO}}" > log.txt
