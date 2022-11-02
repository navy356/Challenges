FROM selenium/standalone-chrome-debug
USER root
RUN apt update
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb
RUN wget -qP /tmp/ "https://chromedriver.storage.googleapis.com/$(curl -s "https://chromedriver.storage.googleapis.com/LATEST_RELEASE")/chromedriver_linux64.zip"
RUN unzip -o /tmp/chromedriver_linux64.zip -d /usr/bin