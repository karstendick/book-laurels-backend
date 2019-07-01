FROM python:3.6

ENV APP /app

RUN mkdir $APP
WORKDIR $APP

EXPOSE 5000

# Copy the requirements file in order to install
# Python dependencies
COPY requirements.txt .
# Install Python dependencies
RUN pip install -r requirements.txt

# We copy the rest of the codebase into the image
COPY . .

CMD python app.py
