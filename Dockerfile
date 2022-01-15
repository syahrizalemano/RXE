# Using Python Slim-Buster
FROM vckyouuu/geezprojects:buster
#━━━━━ RXE ━━━━━

RUN git clone -b RXE https://github.com/syahrizalemano/RXE /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/syahrizalemano/RXE/RXE/requirements.txt

EXPOSE 80 443

# Finalization
CMD ["python3", "-m", "userbot"]
