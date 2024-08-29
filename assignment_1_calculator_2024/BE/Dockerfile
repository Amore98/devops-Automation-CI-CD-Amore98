FROM python:3.12-slim
##WORKDIR /BE
COPY . /BE

RUN pip install  -r requirements.txt
ENTRYPOINT  ["/BE/calculator.py"]
#RUN pip install fastapi pydantic uvicorn numpy argparse opencensus-ext-azure 
#ENTRYPOINT [ "python", "/calculator_helper.py" ]
