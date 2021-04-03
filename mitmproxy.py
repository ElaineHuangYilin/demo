import json
#from mitmproxy import ctx

def response(flow):
    url = 'https://gbpda.weather.gov.hk/locspc/data/fnd_uc.xml'
    if flow.request.url.startswith(url):
        text = flow.response.text
        status = flow.response.status_code

        # ctx.log.info(str(status))
        with open('api_status_data.json', 'w') as file:
            file.write(str(status))

        data = json.loads(text)
        books = data.get('forecast_detail')
        results = []
        for book in books:
            data = {
                'forecast_date': book.get('forecast_date'),
                'max_rh': book.get('max_rh'),
                'min_rh': book.get('min_rh')
            }
            results.append(data)
            with open('forecast_detail_data.json', 'w') as file:
                file.write(json.dumps(results))
           