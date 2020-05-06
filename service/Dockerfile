FROM python:3

ENV APP_HOME="/usr/src/app" \
    WEB_PORT="8080" \
    ENDPOINT_LENGTH="visual-attributes-length-endpoint-2020-04-15-08-03-19" \
    ENDPOINT_DRESS_TYPES="visual-attributes-dress-types-endpoint-2020-04-15-08-11-51" \
    ENDPOINT_COLOR="visual-attributes-color-endpoint-2020-04-15-08-21-23" \
    ENDPOINT_MATERIAL="visual-attributes-material-endpoint-2020-04-15-08-29-55"

WORKDIR ${APP_HOME}

COPY requirements.txt ${APP_HOME}

RUN pip install --upgrade pip \
 && pip install --no-cache-dir -r ${APP_HOME}/requirements.txt

COPY .. ${APP_HOME}
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
CMD ["/entrypoint.sh"]

