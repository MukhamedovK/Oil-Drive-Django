from datetime import datetime

from django.core.serializers import serialize
import json
import gspread
import requests


# scope = ["https://spreadsheets.google.com/feeds",
#          'https://www.googleapis.com/auth/spreadsheets',
#          "https://www.googleapis.com/auth/drive.file",
#          "https://www.googleapis.com/auth/drive"]
# gc = gspread.service_account(filename='main_page/creds.json',
#                              scopes=scope)
#
# wks = gc.open("Oildrive_заявки").get_worksheet(0)


def add_product_to_seen(request, exact_product):
    data = serialize('json', exact_product)
    data = json.loads(data)
    # print(data)
    pk = data[0]['pk']
    data = data[0]['fields']
    data.update({'id': pk})
    # print(exact_product[0].volume_photos.all()[0].volume_photo)
    try:
        data.update({'volume_photos': str([i for i in exact_product[0].volume_photos.all() if i.first][0].volume_photo)})
        data.update({'price': str([i for i in exact_product[0].volume_photos.all() if i.first][0].volume_price)})
    except:
        data.update(
            {'volume_photos': str(exact_product[0].volume_photos.all()[0].volume_photo)})
        data.update({'price': str(exact_product[0].volume_photos.all()[0].volume_price)})

    # print(data)
    if 'have_seen' in request.session:
        if data not in request.session['have_seen']:
            have_seen = request.session['have_seen']
            have_seen.append(data)
            request.session['have_seen'] = have_seen
    else:
        request.session['have_seen'] = [data]
    # request.session['have_seen'] = []
    # print(request.session['have_seen'])
    return request.session['have_seen']


# Отправить заявку в гугл таблицу
def send_google_sheets(pk, full_name, phone_number, email, request_text, added_date,):
    added_date = datetime.strftime(added_date, '%d-%m-%Y %H:%M:%S')
    wks.append_row([pk, full_name, phone_number, email, request_text, added_date])


def get_access_token(client_id, client_secret, redirect_uri, code):
    url = 'https://cspacesales.amocrm.ru/oauth2/access_token'
    data = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': redirect_uri
    }
    response = requests.post(url, json=data)
    if response.status_code == 200:
        return response.json()['access_token']
    else:
        return None


access_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjgwMjE5ODE0MWFhMDcxNWRiYjA2YzljZTlhYTczMTIzNDRjZTlkZmE5ZTNkOWJiYWFiZTY0YzliZjRmMjdmMTcwMjVkMGVhZTU0OTU0NzUwIn0.eyJhdWQiOiIyMDU1MmZlMS1mODE5LTQ0ZGMtYmI4Yy00YzE3MzFlYjUwNzYiLCJqdGkiOiI4MDIxOTgxNDFhYTA3MTVkYmIwNmM5Y2U5YWE3MzEyMzQ0Y2U5ZGZhOWUzZDliYmFhYmU2NGM5YmY0ZjI3ZjE3MDI1ZDBlYWU1NDk1NDc1MCIsImlhdCI6MTcxNDc0NTc0NSwibmJmIjoxNzE0NzQ1NzQ1LCJleHAiOjE3MzgzNjgwMDAsInN1YiI6IjEwMjg2NzIyIiwiZ3JhbnRfdHlwZSI6IiIsImFjY291bnRfaWQiOjI5OTA0Mjk1LCJiYXNlX2RvbWFpbiI6ImFtb2NybS5ydSIsInZlcnNpb24iOjIsInNjb3BlcyI6WyJjcm0iLCJmaWxlcyIsImZpbGVzX2RlbGV0ZSIsIm5vdGlmaWNhdGlvbnMiLCJwdXNoX25vdGlmaWNhdGlvbnMiXSwiaGFzaF91dWlkIjoiZGVkZjhhNmItNTMxMi00NjM2LWJjZmItMTIwNjk2YWNjM2ExIn0.ZmdJWpwv1K8ehzNM_OCjoWHcIBb8anGOfLZQLz5xg0c8nkEK_ehousUoXw9N1Pj4o9lwILglsgMzX4lyuKP0p3BoQJV6y8YbuchUiPMVG7KyxTCVXZlz2fPfIQEGd_k18OzahVbs-ru8V7pT_sonE8k2qWl7TYDWlU34mwjy8G7OWRJOwhQAsNeK-58l8dlPRL_s-Es07UnKgTucO6RP0Vqg8BFwTiEgA_R2XzIs0dk_5VDKgbsG_OdZRt6ksujQ36YX47Da9wKwqsWo_dgSewz7wKOIMi98p7ACb7h_Juh59qA_g-fvQVGC_T_m9ST02McQQSsgGB4sMzUOnFOBUw'


def get_leads():
    url = 'https://vlt.amocrm.ru/api/v4/leads'
    headers = {'Authorization': f'Bearer {access_token}',
               'Content-Type': 'application/json'}
    data = {
        'client_id': '20552fe1-f819-44dc-bb8c-4c1731eb5076',
        'client_secret': 'EXUMfvaHi1WZoTdtGEih22lGplJoMkvgqp4UQRNDJTkBgIBwVXA5Im2rrLx48qtQ',
        'grant_type': 'authorization_code',
        'code': access_token,
        'redirect_uri': 'https://test.oildrive.uz'
    }

    response = requests.get(url, headers=headers)

    print(response.text)


def create_lid(client_name, comment=None, come_from=None, phone_number=None, email=None):
    url = 'https://vlt.amocrm.ru/api/v4/leads/complex'
    headers = {'Authorization': f'Bearer {access_token}',
               'Content-Type': 'application/json'}
    if phone_number and email:
        custom_contacts = [
            {
                "field_code": "PHONE",
                "values": [
                    {
                        "enum_code": "WORK",
                        "value": phone_number
                    }
                ]
            },
            {
                "field_code": "EMAIL",
                "values": [
                    {
                        "enum_code": "WORK",
                        "value": email
                    }
                ]
            },
        ]

    elif email:
        custom_contacts = [
            {
                "field_code": "EMAIL",
                "values": [
                    {
                        "enum_code": "WORK",
                        "value": email
                    }
                ]
            },
        ]

    else:
        custom_contacts = [
            {
                "field_code": "PHONE",
                "values": [
                    {
                        "enum_code": "WORK",
                        "value": phone_number
                    }
                ]
            },
        ]
    data = [
        {
            "name": "Сделка c сайта",
            "created_by": 0,
            "_embedded": {
                "contacts": [
                    {
                        "first_name": client_name,
                        # "phone_number": phone_number,
                        "custom_fields_values": custom_contacts
                    }
                ]
            },
            # "custom_fields_values": [
            #     {
            #         "field_id": 311703,
            #         "values": [
            #             {
            #                 "value": filial
            #             }
            #         ]
            #     },
            #     {
            #         "field_id": 311145,
            #         "values": [
            #             {
            #                 "value": person_count
            #             }
            #         ]
            #     },
            #     {
            #         "field_id": 311141,
            #         "values": [
            #             {
            #                 "value": bron_type
            #             }
            #         ]
            #     },
            #     {
            #         "field_id": 311705,
            #         "values": [
            #             {
            #                 "value": date
            #             }
            #         ]
            #     }
            # ],
        }]

    response = requests.post(url, json=data, headers=headers)

    return str(response.status_code)


# get_leads()
create_lid('Javlon', phone_number='+998900007777', email='some@mail.ru')

