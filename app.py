import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), './classes'))
from company_info import Info
from gmail import Gmail
from template_builder import Builder
info = Info()
mail = Gmail()
template = Builder()

stockURL = 'https://api.iextrading.com/1.0/stock/'
symbols = ['AAPL', 'GOOGL', 'AMZN'] # Insert your stock symbols here
summary = []
articles = []
companyName = []
exchange = []

try:
    # Get latest articles
    for i in symbols:
        summary.append(info.get_summary(i, stockURL))
        articles.append(info.get_articles(i, stockURL))
        companyName.append((info.get_company_name(i, stockURL)))
        exchange.append(info.get_exchange(i, stockURL))

    # Build jinja2 template
    body = template.build_template(symbols, summary, articles, companyName, exchange)

    # Send email
    mail.send_email(body)

    print('Email sent!')
except Exception as e:
    # Print thrown error
    print(str(e))
