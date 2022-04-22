FROM python:3.6 AS builder
COPY requirements.txt .

RUN pip install --user -r requirements.txt

FROM python:3.6-slim
WORKDIR /timetable_bot

COPY --from=builder /root/.local /root/.local
COPY . .

ENV PATH=/root/.local:$PATH

CMD ["python", "-u", "./main.py"]