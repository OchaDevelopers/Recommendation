# -*- coding: utf-8 -*- 

import os
import openpyxl
import configparser
from tqdm import tqdm
from pprint import pprint

import NaverPy.Search


result_path = './result'
max_item_count = 5
keywords = list()
word_sample = {
    'summer': {
        'top': ['티', '셔츠', '후드', '맨투맨'],
        'outer': ['후드집업', '블루종']
    },
    'fall': {   # 봄도 같이.
        'top': ['티', '셔츠', '후드', '맨투맨'],
        'outer': ['점퍼', '자켓', '후드집업', '블루종', '가디건']
    },
    'winter': {
        'top': ['티', '셔츠', '후드', '맨투맨', '니트'],
        'outer': ['점퍼', '자켓', '후드집업', '가디건', '패딩', '코트']
    }
}


# keyword
def gen_keyword(info):
    '''
    info : dict() -> ['sex', 'temp', 'weather', 'part', 'color', 'material', 'word']
    '''

    # gender
    if info['sex'] in ['남자', '남', '남성']:
        sex = '남자'
    elif info['sex'] in ['여자', '여', '여성']:
        sex = '여자'
    else:
        sex = info['sex']

    # additional keyword
    if info['word'] in ['상관없음', '상관 없음', '없음']:
        word = ''
    else:
        word = info['word']

    # weather
    if int(info['temp'].replace('도', '')) < 5:
        weather = 'winter'
    elif int(info['temp'].replace('도', '')) < 20:
        weather = 'fall'
    else:
        weather = 'summer'

    # body part
    if info['part'] == '상의':
        part = word_sample[weather]['top']
    elif info['part'] == '하의':
        if '남' in info['sex']:
            part = ['바지']
        else:
            part = ['바지', '치마']
    elif info['part'] in ['겉옷', '아우터']:
        part = word_sample[weather]['outer']
    else:
        part = [info['part']]

    common_keyword = '{} {} '.format(sex, info['color'])

    return [common_keyword + '{} {} {}'.format(info['material'], it, word).strip() for it in part]



if __name__ == '__main__':
    if not os.path.exists(result_path):
        os.mkdir(result_path)

    # CONFIG
    config = configparser.ConfigParser()
    config.read('./program_setting.txt')
    api_id = config['NAVER_API']['NAVER_X_CLIENT_ID']
    api_secret = config['NAVER_API']['NAVER_X_CLIENT_SECRET']
    result_path = config['RESULT']['RESULT_PATH']
    max_item_count = int(config['RESULT']['MAX_ITEM_COUNT'])
    if max_item_count > 100:
        max_item_count = 100

    # 네이버 API
    naver = NaverPy.Search(api_id, api_secret)
    
    # KEYWORD
    with open('./keywords.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    for line in lines:
        temp_dict = {
            'sex': '', 'temp': '', 'weather': '', 'part': '', 'color': '', 'material': '', 'word': ''
        }
        splits = [it.strip() for it in line.split(',')]
        for idx, key in enumerate(temp_dict):
            temp_dict[key] = splits[idx]
        keywords.append(temp_dict)

    # result file make
    with open(result_path + '/result.txt', 'w') as f:
        f.write('')

    # get search list
    query_lists = [gen_keyword(keyword) for keyword in keywords]
    for query_list in tqdm(query_lists, ncols=90, desc='진행률'):
        error_cnt = 0
        for query in query_list:
            urls = list()
            try:
                data = naver.shop(query, display=max_item_count)
            except:
                try:
                    data = naver.shop(query, display=max_item_count)
                except:
                    print('[ERROR] 검색어 "{}" 수집 에러.'.format(query))
                    continue
                error_cnt += 1
            for it in data['items']:
                #urls.append(it['link'])
                urls.append(it['image'])
            # print
            with open(result_path + '/result.txt', 'a') as f:
                f.write('\n'.join(urls))
    
