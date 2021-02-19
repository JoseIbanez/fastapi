FROM python:3.7-slim

ENV INSTALL_PATH /deployments/
ENV CONFIG_PATH /etc/cifastapi/

# Copy resources first
#ADD client /client
ADD *.py $INSTALL_PATH
ADD *.sh $INSTALL_PATH
ADD *.txt $INSTALL_PATH
ADD VERSION_FULL $CONFIG_PATH
ADD file.config $CONFIG_PATH
WORKDIR $INSTALL_PATH

# Setup deps
RUN python -m pip install --upgrade setuptools pip wheel
#RUN pip install -e /client
RUN python -m pip install -r $INSTALL_PATH/requirements.txt

EXPOSE 5000/tcp
CMD ./run.sh

