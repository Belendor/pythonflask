FROM python
EXPOSE 5000
WORKDIR /app
RUN python -m venv venv
RUN pip install --upgrade pip \
    pip install flask 
COPY . /app/    
# CMD [ "flask" , "run" , "--host" , "0.0.0.0" ]
CMD . venv/bin/activate && exec flask run --host 0.0.0.0