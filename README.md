# Gmail Transferwise Rate

Small script to retrieve exchange rates CHF -> EUR from the Transferwise newsletter in a GMail account.

Basic install :
 
 + create venv `python -m venv ./venv`
 + rename `configuration.py.dist` to `configuration.py`
 + edit values of `configuration.py`
   * query : Query as it would be run in the gmail search bar
   * userId : `me` otherwise look into documentation to connect as somebody else.
   * rateFile: Name of the csv file where the rate are going to be saved
 + Activate GMail api : [More details here](https://developers.google.com/gmail/api/quickstart/python)
   * Store credentials.json in project root.
 + Activate Kaggle api : [More details here](https://github.com/Kaggle/kaggle-api#api-credentials)
   * Download kaggle.json
   * Retrieve `username` and `key` attributes from json
   * Update the `venv/[bin/Scripts]/activate` bash script to add env vars :
     + `export KAGGLE_USERNAME=[json username]`
     + `export KAGGLE_KEY=[json key]`
   * Update/Create `dataset/dataset-metadata.json` [More details here]()

 + Launch console execute : 
 ```
 source venv/[bin/Scripts]/activate
 pip install -r requirements.txt
 python get_mails.py
 ```
 If this is the first time that you run the script on this computer, it will start a navigation so that you can go through the OAuth process and store your connection information in the `token.pickle` file.
 If all goes well, the script will retrieve corresponding mails from your gmail
 account, parse them and update/create the rate_file.csv
 
 Once done, it will connect to the kaggle API to upload the new file and create
 the new version of the dataset
