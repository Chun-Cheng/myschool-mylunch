import requests
import json
import pymongo



def request_account_get(token, cols):
    """
    向帳號管理端請求使用者資料
    input:
      token
      cols:list
    output:
      res_data
      False
    """
    data = json.dumps({'token':str(token), 'cols':cols})
    res = requests.post('https://myschool-account.herokuapp.com/api/account_data_request', data=data)
    res_data = json.loads(res.text)
    status_code = res.status_code
    if status_code == 200:
        return res_data
    else:
        return False

    
def request_token_check(token):
    """
    向帳號管理端確認用戶登入權杖是否有效
    input:
      token
    output:
      res_data['result']
      status_code
    """
    data = {'token':token}
    res = requests.post('https://myschool-account.herokuapp.com/api/token_check_request', data=data)
    res_data = json.loads(res.text)
    status_code = res.status_code
    if status_code == 200:
        return res_data['result']
    else:
        return status_code
