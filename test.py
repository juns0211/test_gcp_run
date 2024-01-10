from flask.blueprints import Blueprint
from flask.views import MethodView
from flasgger import swag_from
import requests
import datetime

class view(MethodView):
    @swag_from('test.yaml')
    def post(self):
        url = 'https://shopee.tw/api/v4/flash_sale/get_all_sessions'
        params = {
            'category_personalization_type': 1,
            'tracker_info_version': 1
        }
        headers = {
            'Sec-Ch-Ua':'"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
            'Sec-Ch-Ua-Mobile':'?0',
            'Sec-Ch-Ua-Platform':"Windows",
            'Sec-Fetch-Dest':'empty',
            'Sec-Fetch-Mode':'cors',
            'Sec-Fetch-Site':'same-origin',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        }
        resp = requests.get(url, params=params, headers=headers)
        if resp.status_code != 200:
            return {'success':False, 'message':f'取得活動時間與ID失敗, status_code={resp.status_code}', 'data':''}
        sessions = resp.json()['data']['sessions']
        start_time = []
        for s in sessions:
            start_time.append(datetime.datetime.fromtimestamp(s['start_time']))
        return {'success':True, 'message':'', 'data':start_time}

bp = Blueprint('test', __name__, url_prefix='/api/v1/test')
bp.add_url_rule('/test', view_func=view.as_view('test'))