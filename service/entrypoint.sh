#!/bin/bash

python ${APP_HOME}/app.py \
  --web_app_port ${WEB_PORT} \
  --color_endpoint_name ${ENDPOINT_COLOR} \
  --dress_type_endpoint_name ${ENDPOINT_DRESS_TYPES} \
  --length_endpoint_name ${ENDPOINT_LENGTH} \
  --material_endpoint_name ${ENDPOINT_MATERIAL} \
  --aws_region ${AWS_REGION}