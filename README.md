# python_enviar_sms
Envio de sms utilizando Python

# importando recursos
pandas, twilio, calendar para utilizar o projeto

# Orientações Twilio abaixo
Crie sua conta e siga as instruções: 

  # Download the helper library from https://www.twilio.com/docs/python/install
  import os
  from twilio.rest import Client


  # Find your Account SID and Auth Token at twilio.com/console
  # and set the environment variables. See http://twil.io/secure
  account_sid = os.environ['TWILIO_ACCOUNT_SID']
  auth_token = os.environ['TWILIO_AUTH_TOKEN']
  client = Client(account_sid, auth_token)

  message = client.messages.create(
                                body='Hi there',
                                from_='+15017122661',
                                to='+15558675310'
                            )

  print(message.sid)
