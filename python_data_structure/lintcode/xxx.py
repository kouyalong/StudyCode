# coding: utf-8

from __future__ import absolute_import

from functools import wraps
import time
from urllib.parse import urljoin

import requests
from requests.exceptions import HTTPError


landmark_key_enum = [
    "contour_left1",  # 0
    "contour_left2",  # 1，三庭五眼计算左侧位置
    "contour_left3",
    "contour_left4",  # 3，颧弓点位
    "contour_left5",
    "contour_left6",
    "contour_left7",
    "contour_left8",  # 7，下颌角宽度
    "contour_left9",
    "contour_left10",
    "contour_left11",
    "contour_left12",
    "contour_left13",   #12， 下巴宽度计算
    "contour_left14",
    "contour_left15",  # 14，下巴角度计算
    "contour_left16",
    "contour_chin",  # 16，下巴最下点
    "contour_right1",  # 17
    "contour_right2",  # 18，三庭五眼最右侧
    "contour_right3",
    "contour_right4",  # 20， 颧弓点位
    "contour_right5",
    "contour_right6",
    "contour_right7",
    "contour_right8",  # 24， 下颌角宽度
    "contour_right9",
    "contour_right10",
    "contour_right11",
    "contour_right12",
    "contour_right13",  #29， 下巴宽度计算
    "contour_right14",
    "contour_right15",  # 31，下巴角度计算
    "contour_right16",
    "left_eyebrow_left_corner",  # 33, 左眉毛最左点
    "left_eyebrow_upper_left_quarter",  # 34, 眉骨位置，用来测量中庭长度
    "left_eyebrow_upper_middle",
    "left_eyebrow_upper_right_quarter",  # 36, 眉毛高度
    "left_eyebrow_upper_right_corner",  # 37, 左眉毛右上角
    "left_eyebrow_lower_left_quarter",
    "left_eyebrow_lower_middle",
    "left_eyebrow_lower_right_quarter",  # 40 眉毛高度
    "left_eyebrow_lower_right_corner",  # 41, 左眉毛右下角
    "right_eyebrow_upper_left_corner",
    "right_eyebrow_upper_left_quarter",
    "right_eyebrow_upper_middle",
    "right_eyebrow_upper_right_quarter",
    "right_eyebrow_right_corner",  # 右眉毛右下角
    "right_eyebrow_lower_left_corner",
    "right_eyebrow_lower_left_quarter",
    "right_eyebrow_lower_middle",
    "right_eyebrow_lower_right_quarter",
    "nose_bridge1",
    "nose_bridge2",
    "nose_bridge3",
    "nose_tip",
    "nose_left_contour1",
    "nose_left_contour2",  # 56, 鼻翼
    "nose_left_contour3",
    "nose_left_contour4",
    "nose_left_contour5",  # 59, 鼻孔距离默认为1，用于计算比例尺
    "nose_middle_contour",  # 60， 鼻子正下方位置，中庭下庭区分点
    "nose_right_contour1",
    "nose_right_contour2",  # 62， 鼻翼
    "nose_right_contour3",
    "nose_right_contour4",
    "nose_right_contour5",  # 65 鼻孔距离默认为1，用于计算比例尺
    "left_eye_left_corner",  # 66，左眼角，三庭五眼及眼睛宽度计算
    "left_eye_upper_left_quarter",
    "left_eye_top",  # 68, 左眼最上方
    "left_eye_upper_right_quarter",  # 69, 内眼角计算
    "left_eye_right_corner",  # 70，三庭五眼、眼睛宽度计算
    "left_eye_lower_right_quarter",  # 71, 内眼角计算
    "left_eye_bottom",  # 72， 左眼最下方
    "left_eye_lower_left_quarter",  # 73
    "left_eye_pupil",  # 74，左眼瞳孔
    "left_eye_center",
    "right_eye_left_corner",  # 76，右眼左眼角
    "right_eye_upper_left_quarter",
    "right_eye_top",
    "right_eye_upper_right_quarter",
    "right_eye_right_corner",  # 80,右眼右眼角
    "right_eye_lower_right_quarter",
    "right_eye_bottom",
    "right_eye_lower_left_quarter",
    "right_eye_pupil",  # 84，右眼瞳孔
    "right_eye_center",
    "mouth_left_corner",  # 86, 嘴唇左方
    "mouth_upper_lip_left_contour1",
    "mouth_upper_lip_left_contour2",
    "mouth_upper_lip_left_contour3",
    "mouth_upper_lip_left_contour4",
    "mouth_right_corner",  # 91，嘴唇最右点
    "mouth_upper_lip_right_contour1",
    "mouth_upper_lip_right_contour2",
    "mouth_upper_lip_right_contour3",
    "mouth_upper_lip_right_contour4",
    "mouth_upper_lip_top",  # 96， 上嘴唇顶点
    "mouth_upper_lip_bottom",
    "mouth_lower_lip_right_contour1",
    "mouth_lower_lip_right_contour2",
    "mouth_lower_lip_right_contour3",
    "mouth_lower_lip_left_contour1",
    "mouth_lower_lip_left_contour2",
    "mouth_lower_lip_left_contour3",
    "mouth_lower_lip_top",
    "mouth_lower_lip_bottom"  # 105，下唇最低点
]


# MEGVII_KEY = "-6zs61jR1M4GqzE9jIO3eiL1W1sojaeE"
# MEGVII_SECRET = "J82yKgSplMDppw9oPpHeTVTA4hYxp0iB"


MEGVII_BASE_URL = 'https://api-cn.faceplusplus.com/'
MEGVII_DETECT_URL_PATH = "facepp/v3/detect"
MEGVII_SKIN_ANALYZE_URL_PATH = '/facepp/v1/skinanalyze_advanced'

MEGVII_ARTTRIBUTES = "gender,age,smiling,headpose,facequality,blur,eyestatus,emotion," \
                     "ethnicity,beauty,mouthstatus,eyegaze,skinstatus"
MEGVII_LAND_MARK_ENUM = 2


# 缓存megvii 分析结果
def cache_megvii_result(func):
    @wraps(func)
    def cache_result(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except HTTPError:
            return None
        return result
    return cache_result


class MegviiAnalytics(object):

    url = MEGVII_BASE_URL
    detect_path = MEGVII_DETECT_URL_PATH
    skin_analyze_path = MEGVII_SKIN_ANALYZE_URL_PATH
    key = MEGVII_KEY
    secret = MEGVII_SECRET
    attributes = MEGVII_ARTTRIBUTES
    land_mark_enum = MEGVII_LAND_MARK_ENUM

    def __init__(self, img_url):
        self.img_url = img_url
        self.boundary = '----------%s' % hex(int(time.time() * 1000))
        self.http_body = None
        self.detect_result = None
        self.skin_analyze_result = None

    @property
    def headers(self):
        return {
            'content-type': 'multipart/form-data; boundary=%s' % self.boundary,
        }

    @property
    def base_data(self):
        return dict(
            api_key=self.key,
            api_secret=self.secret,
            image_url=self.img_url,
        )

    def format_request_body(self, request_info: dict):
        data = list()
        for k, v in request_info.items():
            data.append('--{}'.format(self.boundary))
            data.append('Content-Disposition: form-data; name="{}"\r\n'.format(k))
            data.append(str(v))

        data.append('--%s\r\n' % self.boundary)
        data.append('Content-Disposition: form-data; name="%s"; filename=" "' % ('image_file'))
        data.append('Content-Type: application/octet-stream\r\n')
        data.append(open("xxxa.jpeg", "rb").read())
        data.append('--%s--\r\n' % self.boundary)

        for i, d in enumerate(data):
            if isinstance(d, str):
                data[i] = d.encode('utf-8')


        self.http_body = b'\r\n'.join(data)

    @cache_megvii_result
    def detect(self):
        new_data = dict(
            return_landmark=self.land_mark_enum,
            return_attributes=self.attributes
        )
        new_data.update(self.base_data)

        self.format_request_body(new_data)
        detect_url = urljoin(self.url, self.detect_path)
        print(detect_url, self.http_body, self.headers)
        response = requests.request(
            "POST", detect_url, data=self.http_body, headers=self.headers
        )
        self.detect_result = response.json()
        return self.detect_result

    @cache_megvii_result
    def skinanalyze_advanced(self):
        new_data = self.base_data
        self.format_request_body(new_data)
        skin_analyze_url = urljoin(self.url, self.skin_analyze_path)
        response = requests.request(
            "POST", skin_analyze_url, data=self.http_body, headers=self.headers
        )
        self.skin_analyze_result = response.json()
        return self.skin_analyze_result

    @property
    def detect_landmark(self):
        detect_result = self.detect()
        if detect_result:
            landmarks = detect_result['faces'][0]['landmark']
            return [landmarks[key] for key in landmark_key_enum]
        return []

    @property
    def skin_analyze_landmark(self):
        skin_analyze_result = self.skinanalyze_advanced()
        if not skin_analyze_result:
            skin_analyze_result = DEFAULT_SKIN_ANALYZE_RESULT

        if skin_analyze_result.get("error_message"):
            return DEFAULT_SKIN_ANALYZE_RESULT.get("result")

        result = skin_analyze_result.get("result", {})
        if not result:
            result = DEFAULT_SKIN_ANALYZE_RESULT.get("result")
        return result


DEFAULT_SKIN_ANALYZE_RESULT = {
    "request_id": "1528687092,efbe87f7-6c0f-4754-b108-afe8f42abe17",
    "time_used": 666,
    "face_rectangle": {
        "top": 1,
        "left": 1,
        "width": 1,
        "height": 1
    },
    "result": {
        "skin_color": {
            "value": "2",
            "confidence": 0.89
        },
        "skin_age": {
            "value": "25"
        },
        "left_eyelids": {
            "value": "0",
            "confidence": 0.89
        },
        "right_eyelids": {
            "value": "0",
            "confidence": 0.89
        },
        "eye_pouch": {
            "value": "1",
            "confidence": 0.89
        },
        "dark_circle": {
            "value": "1",
            "confidence": 0.89
        },
        "forehead_wrinkle": {
            "value": "1",
            "confidence": 0.89
        },
        "crows_feet": {
            "value": "1",
            "confidence": 0.89
        },
        "eye_finelines": {
            "value": "1",
            "confidence": 0.89
        },
        "glabella_wrinkle": {
            "value": "1",
            "confidence": 0.89
        },
        "nasolabial_fold": {
            "value": "1",
            "confidence": 0.89
        },
        # 待定
        "skin_type": {
            "details": {
                "0": {
                    "value": 0,
                    "confidence": 0.89
                },
                "1": {
                    "value": 0,
                    "confidence": 0.89
                },
                "2": {
                    "value": 0,
                    "confidence": 0.01
                },
                "3": {
                    "value": 1,
                    "confidence": 0.01
                },
            },
            "skin_type": 3,
        },
        "pores_forehead": {
            "value": "1",
            "confidence": 1
        },
        "pores_left_cheek": {
            "value": "0",
            "confidence": 1
        },
        "pores_right_cheek": {
            "value": "0",
            "confidence": 1
        },
        "pores_jaw": {
            "value": "0",
            "confidence": 1
        },
        "blackhead": {
            "value": "1",
            "confidence": 1
        },
        "acne": {
            "rectangle": [
                {
                    "width": 3,
                    "top": 17,
                    "height": 1,
                    "left": 35
                },
                {
                    "width": 4,
                    "top": 20,
                    "height": 1,
                    "left": 35
                },
                {
                    "width": 5,
                    "top": 22,
                    "height": 1,
                    "left": 35
                }
            ]
        },
        "mole": {
            "rectangle": [
                {
                    "width": 3,
                    "top": 17,
                    "height": 1,
                    "left": 35
                },
                {
                    "width": 4,
                    "top": 20,
                    "height": 1,
                    "left": 35
                },
                {
                    "width": 5,
                    "top": 22,
                    "height": 1,
                    "left": 35
                }
            ]
        },
        "skin_spot": {
            "rectangle": [
                {
                    "width": 3,
                    "top": 17,
                    "height": 1,
                    "left": 35
                },
                {
                    "width": 4,
                    "top": 20,
                    "height": 1,
                    "left": 35
                },
                {
                    "width": 5,
                    "top": 22,
                    "height": 1,
                    "left": 35
                }
            ]
        }
    },
}


from urllib import parse


class MegviiAgent:
    def __init__(self, image_url, megvii_type="landmark"):
        self.image_url = image_url
        self.megvii_client = MegviiAnalytics(image_url)
        self.megvii_type = megvii_type

    def deal_request_data(self):
        new_data = dict()
        if self.megvii_type == "landmark":
            new_data = dict(
                return_landmark=self.megvii_client.land_mark_enum,
                return_attributes=self.megvii_client.attributes
            )
            new_data.update(self.megvii_client.base_data)
        self.megvii_client.format_request_body(new_data)

    def deal_request_url(self):
        if self.megvii_type == "landmark":
            url = parse.urljoin(self.megvii_client.url, self.megvii_client.detect_path)
        else:
            url = parse.urljoin(self.megvii_client.url, self.megvii_client.skin_analyze_path)
        return url

    def do_megvii_request(self):
        url = self.deal_request_url()
        self.megvii_client.base_data["return_rect_confidence"] = 1
        print(url)
        try:
            response = requests.request(
                "POST",
                url,
                data=self.megvii_client.base_data,
            )
            resp = response.json()
        except requests.HTTPError:
            if self.megvii_type == "skin_analyze":
                resp = DEFAULT_SKIN_ANALYZE_RESULT
            else:
                resp = {}
        print(len(resp["result"].get("acne", {}).get("rectangle", [])))
        print(resp)


from typing import List


class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        if len(s) < 2:
            return []

        result = []
        i = 0
        for j in range(1, len(s)):
            if s[i] != s[j]:
                if (j - i - 1) >= 2:
                    result.append([i, j-1])
                i = j
            if j == (len(s) - 1):
                if (j - i) >= 2:
                    result.append([i, j])
        print(result)
        return result


s = Solution()
s.largeGroupPositions("aaa")
