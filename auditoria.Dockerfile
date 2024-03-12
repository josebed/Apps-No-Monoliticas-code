FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && \
  apt-get install -y libpq-dev gcc && \
  apt-get install -y --no-install-recommends gcc python3-dev libssl-dev

COPY . .

RUN pip install -r requirements.txt

EXPOSE 3000

ENV FLASK_APP="./src/auditoriaCompania/api"

ENTRYPOINT ["flask", "run", "-h", "0.0.0.0", "--port=3000"]