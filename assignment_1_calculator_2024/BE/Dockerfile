FROM python:3.12-slim
##WORKDIR /BE
COPY . .
RUN pip install  -r requirements.txt
ENTRYPOINT  ["/BE/calculator.py"]

#ENTRYPOINT [ "python", "/calculator.py" ]
