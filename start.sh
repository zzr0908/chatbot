export WECHATY_LOG="verbose"
export WECHATY_PUPPET="wechaty-puppet-padlocal"
export WECHATY_PUPPET_PADLOCAL_TOKEN="puppet_padlocal_79e4a23ce72c4f58b88465d1c1f80d32"
export WECHATY_PUPPET_SERVER_PORT="8080"
export WECHATY_TOKEN="b750b55b-e5d7-4528-910e-40c97b70fe94"
sed -i s/token=.*/token=$WECHATY_TOKEN/g .env

docker run -ti \
  --name wechaty_puppet_service_token_gateway \
  --rm \
  -e WECHATY_LOG \
  -e WECHATY_PUPPET \
  -e WECHATY_PUPPET_PADLOCAL_TOKEN \
  -e WECHATY_PUPPET_SERVER_PORT \
  -e WECHATY_TOKEN \
  -p "$WECHATY_PUPPET_SERVER_PORT:$WECHATY_PUPPET_SERVER_PORT" \
  wechaty/wechaty:0.65
