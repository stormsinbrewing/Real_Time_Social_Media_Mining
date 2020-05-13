FROM ubuntu
RUN apt-get upgrade
RUN apt-get update
RUN apt install -y git
RUN git clone "https://www.github.com/stormsinbrewing/Real_Time_Social_Media_Mining"
RUN chmod 777 Real_Time_Social_Media_Mining
