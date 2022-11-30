FROM python
EXPOSE 5000
WORKDIR /app
COPY requirements.txt .
RUN python -m venv venv
RUN pip install --upgrade pip \
    pip install -r requirements.txt 
COPY . /app/    
CMD [ "flask" , "run" , "--host" , "0.0.0.0" ]
# CMD . venv/bin/activate && exec flask run --host 0.0.0.0