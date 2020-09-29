rabbitmqctl add_user $MAIN_USER $MAIN_USER_PASSWORD
rabbitmqctl add_vhost $MAIN_VHOST
rabbitmqctl set_permissions -p $MAIN_VHOST guest ".*" ".*" ".*"

# make websockets available
rabbitmq-plugins enable rabbitmq_web_stomp
