# base image
FROM python:3.9

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
COPY ./app/requirements.txt ./requirements.txt
RUN pip3 install cython
RUN pip3 install -r requirements.txt

# copying everything over
COPY . .