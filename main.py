from bs4 import BeautifulSoup
import csv
import json
from datetime import datetime

current_file = 'data/CK_activity.html'

def write_csv(file_path, data):
    with open(file_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(data)
    print('Written!')

def get_financial_data(file_path):
    with open(file_path, 'r', encoding='utf8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        divs = soup.find_all('div', class_='KplRow_innerRow__biA6g')
        title = "KplRow_title__2WuSO"
        date_and_balance = "KplRow_subtitle__1LBJx"
        value = "KplRow_value__1anFU"
        all_transactions = [
            ['Name', 'Amount', 'Date', 'Remaining Balance'],
        ]
        for div in divs:
            # Get string from <div>'s with institution name
            tran_name = div.find_all('div', class_=title)[0].string
            
            # Get string from <div>'s with transaction amount
            tran_amount = div.find_all('div', class_=value)[0].string
            
            # Get string from <div>'s with date and remaining balance
            tran_date_balance = div.find_all('div', class_=date_and_balance)[0].string

            # Separate date and balance
            tran_date, remaining_balance = tran_date_balance.split('•')

            # Append year to transaction date
            date_with_year = f'{tran_date} 2024'

            # Convert to a date object
            date_object = datetime.strptime(date_with_year, '%b %d %Y').date()

            # Format the date object
            formatted_date = date_object.strftime('%m/%d/%Y')

            # Create transaction data
            transaction_data = [
                tran_name,
                tran_amount,
                formatted_date,
                remaining_balance[1:]
            ]
            all_transactions.append(transaction_data)
        return all_transactions

def group_by_name(list):
    object = {}
    for transaction in list[1:]:
        name = transaction[0]
    
    
if __name__ == '__main__':
    output_path = 'output/first.csv'
    # data = get_financial_data(current_file)
    # write_csv(output_path, data)
    with open(output_path, 'r') as csv_file:
        csv = csv.reader(csv_file)
        data = []
        for each in csv:
            if each[0] == 'Name':
                continue
            category = input(f'{each[0]} - {each[1]}: ')
            tran_data = {
                'name': each[0],
                'amount': each[1],
                'date': each[2],
                'remaining': each[3],
                'category': category
            }
            data.append(tran_data)
        with open('output/data.json', 'w') as json_file:
            json_data = json.dumps(data)
            json_file.write(json_data)

    

'''
<div class="KplRow_titleContainer__12euA flex">
    <div class="KplRow_icon__27xJH flex items-center mr3 flex-shrink-0 KplRow_iconWithSubtitle__1gHrJ">
        <div>
            <img src="https://creditkarmacdn-a.akamaihd.net/res/content/bundles/savings/6.50.0/e51b03c86ce92e6420c3.svg" width="16" height="16" alt="" class="TransactionRow_icon__3NNHI mt1">
        </div>
    </div>
    <div class="KplRow_titleAndSubtitle__3S7_0 flex flex-column lh-copy tl">
        <div class="KplRow_title__2WuSO f4 semibold">
            <span>
                <span>Coca Cola Spokane</span>
            </span>
        </div>
        <div class="KplRow_subtitle__1LBJx flex items-center f5">
            <div class="TransactionRow_subtitle__2eWbZ flex flex-column flex-auto">
                <span class="TransactionRow_transactionDate__2XAOw f5 ck-black-60">Mar 13 • $1,343.08</span>
            </div>
        </div>
    </div>
</div>

<div class="KplRow_innerRow__biA6g flex justify-between pb-std items-start">
    <div class="KplRow_titleContainer__12euA flex">
        <div class="KplRow_icon__27xJH flex items-center mr3 flex-shrink-0 KplRow_iconWithSubtitle__1gHrJ">
            <div>
                <img src="https://creditkarmacdn-a.akamaihd.net/res/content/bundles/savings/6.50.0/e51b03c86ce92e6420c3.svg" width="16" height="16" alt="" class="TransactionRow_icon__3NNHI mt1">
            </div>
        </div>
        <div class="KplRow_titleAndSubtitle__3S7_0 flex flex-column lh-copy tl">
            <div class="KplRow_title__2WuSO f4 semibold">
                <span>
                    <span>R&amp;B Super Stop</span>
                </span>
            </div> 
            <div class="KplRow_subtitle__1LBJx flex items-center f5">
                <div class="TransactionRow_subtitle__2eWbZ flex flex-column flex-auto">
                    <span class="TransactionRow_transactionDate__2XAOw f5 ck-black-60">Mar 12 • $1,344.83</span>
                </div>
            </div>
        </div>
    </div>
    <div class="KplRow_value__1anFU f4 lh-copy semibold flex-shrink-0 ml2">
        <span data-di-mask="true" class="fs-mask TransactionRow_isNegative__35wva ck-black-90">
            <span>
                <span>-$33.15</span>
            </span>
        </span>
    </div>
</div>
'''
