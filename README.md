Przy tym labolatorium przeniosłam się z windowsna na lunuxa (fedora)

W zadaniu 3 użyłam w linii komned cURL:  curl -X POST http://0.0.0.0:8000/predict \
     -H "Content-Type: application/json" \
     -d '{"value": 6}'


i otrzymałam wynik: {"prediction":[12.0]}



W pozostałych zadaniach używałam komend: 

(zbudowanie obrazu) docker build -t ntpdlab4 .

(uruchomienie kontenera) docker run -p 8000:8000 ntpdlab4

(uruchomienie docker compose) docker compose up --build
