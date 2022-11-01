FROM python:3.8-slim

WORKDIR /predict-app

COPY ["requirements.txt", "./"]

RUN pip install -r requirements.txt

COPY ["pred_file.bin", "predict.py", "./"]

EXPOSE 9696 

ENTRYPOINT ["waitress-serve", "--listen=0.0.0.0:9696", "predict:app"]