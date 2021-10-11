from datetime import datetime, timedelta
import requests
import psycopg2
import logging
import sys
import json

key = ''
yesterday = (datetime.today() - timedelta(1)).strftime("%Y%m%d")
startDate = yesterday
endDate = yesterday
location = '108' # 서울


host = "covid.cjwptwa04yyi.ap-northeast-2.rds.amazonaws.com"
port = 5432
username = "sixmini"
database = "postgres"
password = ""


def main():
    try:
        conn = psycopg2.connect(
            host=host,
            database=database,
            user=username,
            password=password)
        cursor = conn.cursor()
    except:
        logging.error("could not connect to rds")
        sys.exit()

    API_URL = 'http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList?serviceKey={}&pageNo=1&numOfRows=999&dataType=JSON&dataCd=ASOS&dateCd=DAY&startDt={}&endDt={}&stnIds={}'.format(key, startDate, endDate, location)
    
    r = requests.get(API_URL)
    raw = json.loads(r.text)

    weather_raw = raw['response']['body']['items']['item']
    for i in range(len(weather_raw)):
        weather = {}
        try:
            weather.update(
                {
                    'date': weather_raw[i]['tm'],
                    'avgTa': weather_raw[i]['avgTa'],
                    'minTa': weather_raw[i]['minTa'],
                    'minTaHrmt': weather_raw[i]['minTaHrmt'],
                    'maxTa': weather_raw[i]['maxTa'],
                    'maxTaHrmt': weather_raw[i]['maxTaHrmt'],
                    'mi10MaxRn': weather_raw[i]['mi10MaxRn'],
                    'mi10MaxRnHrmt': weather_raw[i]['mi10MaxRnHrmt'],
                    'hr1MaxRn': weather_raw[i]['hr1MaxRn'],
                    'hr1MaxRnHrmt': weather_raw[i]['hr1MaxRnHrmt'],
                    'sumRnDur': weather_raw[i]['sumRnDur'],
                    'sumRn': weather_raw[i]['sumRn'],
                    'maxInsWs': weather_raw[i]['maxInsWs'],
                    'maxInsWsWd': weather_raw[i]['maxInsWsWd'],
                    'maxInsWsHrmt': weather_raw[i]['maxInsWsHrmt'],
                    'maxWs': weather_raw[i]['maxWs'],
                    'maxWsWd': weather_raw[i]['maxWsWd'],
                    'maxWsHrmt': weather_raw[i]['maxWsHrmt'],
                    'avgWs': weather_raw[i]['avgWs'],
                    'hr24SumRws': weather_raw[i]['hr24SumRws'],
                    'maxWd': weather_raw[i]['maxWd'],
                    'avgTd': weather_raw[i]['avgTd'],
                    'minRhm': weather_raw[i]['minRhm'],
                    'minRhmHrmt': weather_raw[i]['minRhmHrmt'],
                    'avgRhm': weather_raw[i]['avgRhm'],
                    'avgPv': weather_raw[i]['avgPv'],
                    'avgPa': weather_raw[i]['avgPa'],
                    'maxPs': weather_raw[i]['maxPs'],
                    'maxPsHrmt': weather_raw[i]['maxPsHrmt'],
                    'minPs': weather_raw[i]['minPs'],
                    'minPsHrmt': weather_raw[i]['minPsHrmt'],
                    'avgPs': weather_raw[i]['avgPs'],
                    'ssDur': weather_raw[i]['ssDur'],
                    'sumSsHr': weather_raw[i]['sumSsHr'],
                    'hr1MaxIcsrHrmt': weather_raw[i]['hr1MaxIcsrHrmt'],
                    'hr1MaxIcsr': weather_raw[i]['hr1MaxIcsr'],
                    'sumGsr': weather_raw[i]['sumGsr'],
                    'ddMefs': weather_raw[i]['ddMefs'],
                    'ddMefsHrmt': weather_raw[i]['ddMefsHrmt'],
                    'ddMes': weather_raw[i]['ddMes'],
                    'ddMesHrmt': weather_raw[i]['ddMesHrmt'],
                    'sumDpthFhsc': weather_raw[i]['sumDpthFhsc'],
                    'avgTca': weather_raw[i]['avgTca'],
                    'avgLmac': weather_raw[i]['avgLmac'],
                    'avgTs': weather_raw[i]['avgTs'],
                    'minTg': weather_raw[i]['minTg'],
                    'avgCm5Te': weather_raw[i]['avgCm5Te'],
                    'avgCm10Te': weather_raw[i]['avgCm10Te'],
                    'avgCm20Te': weather_raw[i]['avgCm20Te'],
                    'avgCm30Te': weather_raw[i]['avgCm30Te'],
                    'avgM05Te': weather_raw[i]['avgM05Te'],
                    'avgM10Te': weather_raw[i]['avgM10Te'],
                    'avgM15Te': weather_raw[i]['avgM15Te'],
                    'avgM30Te': weather_raw[i]['avgM30Te'],
                    'avgM50Te': weather_raw[i]['avgM50Te'],
                    'sumLrgEv': weather_raw[i]['sumLrgEv'],
                    'sumSmlEv': weather_raw[i]['sumSmlEv'],
                    'n99Rn': weather_raw[i]['n99Rn'],
                    'iscs': weather_raw[i]['iscs'],
                    'sumFogDur': weather_raw[i]['sumFogDur']
                }
            )
            for i in weather:
                if weather[i] == '':
                    weather[i] = '0'
            insert_row(cursor, weather, 'weather')
        except:
            print('some error!')
            continue
        
    conn.commit()
    

def insert_row(cursor, data, table):
    placeholders = ', '.join(['%s'] * len(data))
    columns = ', '.join(data.keys())
    key_placeholders = ', '.join(['{0}=%s'.format(k) for k in data.keys()])
    sql = "INSERT INTO %s ( %s ) VALUES ( %s ) ON CONFLICT ( %s ) DO UPDATE SET  %s" % (table, columns, placeholders, list(data.keys())[0] ,key_placeholders)
    cursor.execute(sql, list(data.values())*2)


if __name__=='__main__':
    main()