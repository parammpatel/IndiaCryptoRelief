# currently only implements normal transactions
# etherscan has seperate API call for ERC-20 token transactions

import requests
import csv


def getDonations(donateToAddress, apiKey):
    url = "https://api.etherscan.io/api?module=account&action=txlist&" + \
          "address="+donateToAddress+"&startblock=0&endblock=99999999&sort=asc&" + \
          "apikey="+apiKey
    returnedResults = requests.get(url).json()['result']
    return returnedResults


if __name__ == '__main__':
    donateToAddress = "0x68a99f89e475a078645f4bac491360afe255dff1"
    apiKey = "[api_key]"
    # apiKey from Etherscan
    # limited to 5 calls per second

    results = getDonations(donateToAddress, apiKey)

    with open('data/top_donations.csv', mode='w', newline='') as write_file:
        donations_writer = csv.writer(write_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        donations_writer.writerow(['name', 'count'])
        for row in results:
            if row['to'] != donateToAddress or row['txreceipt_status'] == 0:
                continue
            else:
                # add if statements here to filter transaction amount
                donations_writer.writerow([row['from'], float(row['value'])/(10**18)])
