import requests
import base64
import uuid
from datetime import datetime
from urllib.parse import quote_plus

from app.config import settings

auth_string = f"{settings.UDS_ID}:{settings.UDS_KEY}"
auth_string = base64.b64encode(auth_string.encode('utf-8')).decode("utf-8")

url = 'https://api.uds.app/partner/v2/customers/find'


params = {
    'code': '809511',
    'number': quote_plus('+79775173283'),  # TODO: почему не работает поиск по телефону?
    'uid': 'f6fcab63-2a41-4d71-bed2-63be9772a2b2'
}

headers = {
    'Accept': 'application/json',
    'Accept-Charset': 'utf-8',
    'Authorization': f'Basic {auth_string}',
    'X-Origin-Request-Id': str(uuid.uuid4()),
    'X-Timestamp': datetime.now().isoformat(),
}

response = requests.get(url, headers=headers, params=params)

print(response.text)
