import pandas as pd
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
import calendar

import python_enviar_sms.credentials


account_sid = python_enviar_sms.credentials.account_sid()
auth_token = python_enviar_sms.credentials.auth_token()
phone_nun = python_enviar_sms.credentials.phone_num()
client = Client(account_sid, auth_token)

print(account_sid)
print(auth_token)

month_list = []
for month_idx in range(1, 7):
    # monthList.append(calendar.month_name[month_idx])
    month_list.append(calendar.month_abbr[month_idx])

def find_doc (month_nickname):
    sales_table = pd.read_excel(f'/home/anmer.machado/IdeaProjects/python-programs/python_enviar_sms/arquivos/{month_nickname}.xlsx')
    return sales_table

for month in month_list:
    # print(month)
    monthlyData = find_doc(month)
    # print(monthlyData)

    if (monthlyData['Vendas'] >= 55000).any():
        vendedor = monthlyData.loc[monthlyData['Vendas'] >= 55000, 'Vendedor'].values[0]
        vendas = monthlyData.loc[monthlyData['Vendas'] >= 55000, 'Vendas'].values[0]
        print(f'No mês {month} , {vendedor} bateu as metas com R$: {vendas}')
        try:
            message = client.messages.create(
            to=phone_nun,
            from_="+12543454332",
            body=f'No mês {month} , {vendedor} bateu as metas com R$: {vendas}')
            print(message.sid)
        except TwilioRestException as err:
            print(err)
