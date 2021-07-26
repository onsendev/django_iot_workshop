import os
import json
import pprint
import requests

class NatureRemoApi:
    
    REMO_ACTIONS = {
        'light_on_off': 'xxxxx',
    }
    
    def fetch_sensor_values(self):
        """現在のセンサーの値をNature Cloud APIから取得する。
        
        Returns:
            Nature Cloud APIのレスポンスの['newest_events']のタプル。室温, 湿度, 照度の順番
        """
        pass

    def invoke_remo_action(self, action_name):
        """Nature Cloud APIを叩き、Nature Remoから赤外線信号を発出する。
        
        Returns: 成功した場合はTrue
        """
        pass


    def __get_access_token(self):
        return ''

    def __build_header(self):
        return {'Authorization': 'Bearer ' + self.__get_access_token()}
       
