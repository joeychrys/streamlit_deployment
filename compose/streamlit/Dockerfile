# base image
FROM python:3.9-slim

#basic build prep
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

# streamlit-specific commands
RUN mkdir -p /root/.streamlit
RUN bash -c 'echo -e "\
[general]\n\
email = \"\"\n\
" > /root/.streamlit/credentials.toml'
RUN bash -c 'echo -e "\
[server]\n\
enableCORS = false\n\
" > /root/.streamlit/config.toml'

# copy over and install packages
COPY ./src/requirements.txt ./requirements.txt
RUN pip3 install cython
RUN pip3 install -r requirements.txt

# copying everything over
COPY . .