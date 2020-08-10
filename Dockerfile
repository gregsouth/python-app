FROM python:3.9.0b5-alpine3.12
LABEL maintainer="greg.south@gmail.com - Greg South"
WORKDIR /app
ADD main.py ./
ADD requirements.txt ./
RUN pip install -r requirements.txt
EXPOSE 5000
ENV PORT=5000
CMD ["python", "main.py"]
