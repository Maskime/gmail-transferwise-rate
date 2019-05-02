from __future__ import print_function

import csv
import os.path
import pickle
import re
from collections import namedtuple
from datetime import datetime, timedelta
from typing import List

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from configuration import configuration
import pandas as pd

# If modifying these scopes, delete the file token.pickle.
from kaggle import api

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

rate_csv_columns = ['message_id', 'date', 'rate']
RateRow = namedtuple('RateRow', rate_csv_columns)
root_dir = os.path.dirname(os.path.realpath(__file__))
dataset_dir = os.path.join(root_dir, 'dataset')
rate_file = os.path.join(dataset_dir, configuration.rateFile)
metadata_file = os.path.join(dataset_dir, 'dataset-metadata.json')


def load_rates() -> pd.DataFrame :
    rate_df = pd.DataFrame(columns=rate_csv_columns)
    if path.exists(rate_file):
        rate_df = pd.read_csv(rate_file)
    return rate_df


def update_rates(to_append: List[RateRow]):
    with open(rate_file, 'a+') as chf_rate_file:
        writer = csv.DictWriter(chf_rate_file, rate_csv_columns)
        dict_row = [row._asdict() for row in to_append]
        writer.writerows(dict_row)

def initializeEnv():



def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """

    initializeEnv()

    service = build('gmail', 'v1', credentials=get_credentials())

    # Call the Gmail API
    results = service.users().messages().list(q=configuration.query, userId=configuration.userId).execute()
    rate_df = load_rates()
    messages = results.get('messages')
    # to_request = [message_res for message_res in messages if message_res['id'] not in rates]
    # print('I will request for', len(to_request), 'messages')
    # to_append: List[RateRow] = []
    # one_delta = timedelta(days=1)
    # for msg_resource in to_request:
    #     message = service.users().messages().get(userId='me', id=msg_resource['id'], format='minimal').execute()
    #     searchObj = re.search('1 CHF = ([0-9.]+) EUR', message['snippet'])
    #     if searchObj.group():
    #         rate_date = datetime.fromtimestamp(float(int(message['internalDate']) / 1000)).date()
    #         row = RateRow(message_id=msg_resource['id'], date=rate_date, rate=searchObj.group(1))
    #         to_append.append(row)
    #         if rate_date.weekday() == 4:
    #             for weekend in [rate_date + one_delta, rate_date + (one_delta * 2)]:
    #                 row_dict = row._asdict()
    #                 row_dict['date'] = weekend
    #                 to_append.append(RateRow(**row_dict))
    # if len(to_append) == 0:
    #     exit(0)
    # update_rates(to_append)

    # api.dataset_create_version(folder=os.path.dirname(rate_file),
    #                            version_notes='Script ran on {}'.format(datetime.now().strftime('%Y-%m-%d')))


def get_credentials():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return creds


if __name__ == '__main__':
    main()
