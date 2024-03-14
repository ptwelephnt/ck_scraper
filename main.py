from bs4 import BeautifulSoup

with open('money_data.html', 'r', encoding='utf8') as file:
    soup = BeautifulSoup(file, 'html.parser')
    divs = soup.find_all('div', class_='KplRow_innerRow__biA6g')
    title = "KplRow_title__2WuSO"
    date_and_balance = "KplRow_subtitle__1LBJx"
    value = "KplRow_value__1anFU"
    for div in divs:
        tran_name = div.find_all('div', class_=title)[0].string
        tran_date = div.find_all('div', class_=date_and_balance)[0].string
        tran_value = div.find_all('div', class_=value)[0].string
        print(f'{tran_name}: {tran_value} - {tran_date}')
        # spans = div.find_all('span')
        # for span in spans:
        #     nested_span = span.find_all('span')
        #     print(nested_span)

        
    

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
