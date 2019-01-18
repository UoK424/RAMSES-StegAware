import requests
import json
import time, datetime

class PlatformMF:

    def __init__(self):
        try:

            self.client_id = None
            self.client_secret = None
            self.session_state = None
            self.token_type = None
            self.token_access = None
            self.token_expires_in = None
            self.token_refresh = None
            self.refresh_expires_in = None
            self.expiration_time = None
            self.isLogin = False
            self.platform_user_id = None

        except Exception, e:
            print 'Error in function __init__ of class PlatformMF: ', e
            pass

    def request_token(self, username, password):
        try:
            if self.client_id is not None and self.client_secret is not None:

                url = "https://ramses.treelogic.com/auth/realms/ramses/protocol/openid-connect/token"

                payload = "client_id={0}&"\
                          "client_secret={1}&" \
                          "username={2}&" \
                          "password={3}&" \
                          "grant_type=password".format(self.client_id,self.client_secret,username,password)
                headers = {
                    'Content-Type': "application/x-www-form-urlencoded"
                }

                try:
                    response = requests.request("POST", url, data=payload, headers=headers)
                except Exception,e:
                    response = None
                    print e
                    pass
                if response is not None:
                    if response.status_code == 200:#response_dict.has_key('token_type'):
                        response_dict = json.loads(response.text)
                        self.token_type = response_dict['token_type']
                        self.token_expires_in = time.time() + response_dict['expires_in']
                        self.token_access = response_dict['access_token']
                        self.token_refresh = response_dict['refresh_token']
                        self.refresh_expires_in = time.time() + response_dict['refresh_expires_in']
                        self.session_state = response_dict['session_state']
                        self.isLogin = True
                        #ToDo Change to get this parameter
                        self.platform_user_id = '6161f370-bdc1-4d15-bf3b-aba59d58d259'
                        return self.isLogin, None
                    else:
                        self.isLogin = False
                        return self.isLogin, response.reason
                else:
                    self.isLogin = False
                    return self.isLogin, "System not Connected to Internet"
            else:
                print 'No information about client and secret'
                self.isLogin = False
                return self.isLogin
        except Exception,e:
            print 'Error in function request_token PlatformMF class: ',e
            pass

    def refresh_token(self):
        try:
            if self.client_id is not None and self.client_secret is not None:

                url = "https://ramses.treelogic.com/auth/realms/ramses/protocol/openid-connect/token"

                payload = "client_id={0}" \
                          "&client_secret={1}" \
                          "&grant_type=refresh_token" \
                          "&refresh_token={2}".format(self.client_id,self.client_secret,self.token_refresh)
                headers = {
                    'Content-Type': "application/x-www-form-urlencoded"
                }

                response = requests.request("POST", url, data=payload, headers=headers)
                response_dict = json.loads(response.text)
                self.token_type = response_dict['token_type']
                self.token_expires_in = response_dict['expires_in']
                self.token_access = response_dict['access_token']
                self.token_refresh = response_dict['refresh_token']
                self.refresh_expires_in = response_dict['refresh_expires_in']
                self.session_state = response_dict['session_state']

            else:
                print 'No information about client and secret'
        except Exception,e:
            print 'Error in function refresh_token PlatformMF class: ',e
            pass

    def token_is_expired(self):
        try:
            if self.isLogin and self.token_access is not None:
                return self.token_expires_in < time.time()
        except Exception,e:
            print 'Error in function token_is_expired: ',e
            pass

    def refreh_token_is_expired(self):
        try:
            return self.refresh_expires_in < time.time()
        except Exception,e:
            print 'Error in function token_is_expired: ',e
            pass

# ---- Authorship Functions ---- #

    def get_authorship_list(self,user_id):
        try:
            url = "https://ramses.treelogic.com/ramses-1.0.0/api/ramses/mf/authorship?userId={0}".format(user_id)

            headers = {
                'Authorization': "Bearer {0}".format(self.token_access),
                'Content-Type': "application/json",
                'Cache-Control': "no-cache"
            }
            response = requests.request("GET", url, headers=headers)
            if response.status_code == 200:
                return True, json.loads(response.text)
            else:
                return False, (response.status_code, response.reason)
        except Exception,e:
            print 'Error in function get_authorship_list: ',e
            pass

    def get_specific_authorship_information(self,id_authorship_json):
        try:
            if not self.token_is_expired() or not self.refreh_token_is_expired():
                if self.token_is_expired():
                    self.refresh_token()
                url = "https://ramses.treelogic.com/ramses-1.0.0/api/ramses/mf/authorship/{0}".format(id_authorship_json)
                headers = {
                    'Authorization': "Bearer {0}".format(self.token_access),
                    'Content-Type': "application/json",
                    'Cache-Control': "no-cache"
                }
                response = requests.request("GET", url, headers=headers)
                if response.status_code == 200:
                    return response.text, response.status_code
                else:
                    return False, (response.status_code, response.reason)
            else:
                print 'Refresh token to upload'
        except Exception,e:
            print 'Error in function upload_authorship_information: ',e
            pass

    def upload_authorship_information(self, authorship_json):
        try:
            if not self.token_is_expired() or not self.refreh_token_is_expired():
                if self.token_is_expired():
                    self.refresh_token()
                url = "https://ramses.treelogic.com/ramses-1.0.0/api/ramses/mf/authorship"

                payload = "{0}".format(authorship_json)

                headers = {
                    'Authorization': "Bearer {0}".format(self.token_access),
                    'Content-Type': "application/json",
                    'Cache-Control': "no-cache"
                }
                response = requests.request("POST", url, data=payload,headers=headers)
                if response.status_code == 200:
                    return True, None#response.reason, response.status_code
                else:
                    return False, (response.status_code, response.reason) #response.reason, response.status_code
            else:
                print 'Refresh token to upload'
        except Exception,e:
            print 'Error in function upload_authorship_information: ',e
            pass

    def update_authorship_information(self, id_authorship_json, authorship_json):
        try:
            if not self.token_is_expired() or not self.refreh_token_is_expired():
                if self.token_is_expired():
                    self.refresh_token()
                url = "https://ramses.treelogic.com/ramses-1.0.0/api/ramses/mf/authorship/{0}".format(id_authorship_json)

                payload = "{0}".format(authorship_json)

                headers = {
                    'Authorization': "Bearer {0}".format(self.token_access),
                    'Content-Type': "application/json",
                    'Cache-Control': "no-cache"
                }
                response = requests.request("POST", url, data=payload,headers=headers)
                if response.status_code == 200:
                    return response.text, response.status_code
                else:
                    return False,(response.status_code, response.reason)
            else:
                print 'Refresh token to upload'
        except Exception,e:
            print 'Error in function upload_authorship_information: ',e
            pass

    def delete_authorship_information(self, id_authorship_json):
        try:
            if not self.token_is_expired() or not self.refreh_token_is_expired():
                if self.token_is_expired():
                    self.refresh_token()
                url = "https://ramses.treelogic.com/ramses-1.0.0/api/ramses/mf/authorship/{0}".format(id_authorship_json)

                headers = {
                    'Authorization': "Bearer {0}".format(self.token_access),
                    'Content-Type': "application/json",
                    'Cache-Control': "no-cache"
                }
                response = requests.request("DELETE", url, headers=headers)
                if response.status_code == 200:
                    return True, (response.text, response.status_code)
                else:
                    return False, (response.status_code, response.reason)
            else:
                print 'Refresh token to upload'
        except Exception,e:
            print 'Error in function upload_authorship_information: ',e
            pass

# ---- Manipulation Functions ---- #
    def get_manipulation_list(self,user_id):
        try:
            url = "https://ramses.treelogic.com/ramses-1.0.0/api/ramses/mf/manipulation?userId={0}".format(user_id)

            headers = {
                'Authorization': "Bearer {0}".format(self.token_access),
                'Content-Type': "application/json",
                'Cache-Control': "no-cache"
            }
            response = requests.request("GET", url, headers=headers)
            if response.status_code == 200:
                return True, json.loads(response.text)
            else:
                return False, (response.status_code, response.reason)
        except Exception,e:
            print 'Error in function get_manipulation_list: ',e
            pass

    def get_specific_manipulation_information(self,id_manipulation_json):
        try:
            if not self.token_is_expired() or not self.refreh_token_is_expired():
                if self.token_is_expired():
                    self.refresh_token()
                url = "https://ramses.treelogic.com/ramses-1.0.0/api/ramses/mf/manipulation/{0}".format(id_manipulation_json)
                headers = {
                    'Authorization': "Bearer {0}".format(self.token_access),
                    'Content-Type': "application/json",
                    'Cache-Control': "no-cache"
                }
                response = requests.request("GET", url, headers=headers)
                if response.status_code == 200:
                    return response.text, response.status_code
                else:
                    return False, (response.status_code, response.reason)
            else:
                print 'Refresh token to upload'
        except Exception,e:
            print 'Error in function get_specific_manipulation_information: ',e
            pass

    def upload_manipulation_information(self, manipulation_json):
        try:
            if not self.token_is_expired() or not self.refreh_token_is_expired():
                if self.token_is_expired():
                    self.refresh_token()
                url = "https://ramses.treelogic.com/ramses-1.0.0/api/ramses/mf/manipulation"

                payload = "{0}".format(manipulation_json)

                headers = {
                    'Authorization': "Bearer {0}".format(self.token_access),
                    'Content-Type': "application/json",
                    'Cache-Control': "no-cache"
                }
                response = requests.request("POST", url, data=payload,headers=headers)
                if response.status_code == 200:
                    return response.reason, response.status_code
                else:
                    return False, (response.status_code, response.reason)
            else:
                print 'Refresh token to upload'
        except Exception,e:
            print 'Error in function upload_manipulation_information: ',e
            pass

    def update_manipulation_information(self, id_manipulation_json, manipulation_json):
        try:
            if not self.token_is_expired() or not self.refreh_token_is_expired():
                if self.token_is_expired():
                    self.refresh_token()
                url = "https://ramses.treelogic.com/ramses-1.0.0/api/ramses/mf/manipulation/{0}".format(id_manipulation_json)

                payload = "{0}".format(manipulation_json)

                headers = {
                    'Authorization': "Bearer {0}".format(self.token_access),
                    'Content-Type': "application/json",
                    'Cache-Control': "no-cache"
                }
                response = requests.request("POST", url, data=payload,headers=headers)
                if response.status_code == 200:
                    return response.text, response.status_code
                else:
                    return False, (response.status_code, response.reason)
            else:
                print 'Refresh token to upload'
        except Exception,e:
            print 'Error in function update_manipulation_information: ',e
            pass

    def delete_manipulation_information(self, id_manipulation_json):
        try:
            if not self.token_is_expired() or not self.refreh_token_is_expired():
                if self.token_is_expired():
                    self.refresh_token()
                url = "https://ramses.treelogic.com/ramses-1.0.0/api/ramses/mf/manipulation/{0}".format(id_manipulation_json)

                headers = {
                    'Authorization': "Bearer {0}".format(self.token_access),
                    'Content-Type': "application/json",
                    'Cache-Control': "no-cache"
                }
                response = requests.request("DELETE", url, headers=headers)
                if response.status_code == 200:
                    return True, (response.text, response.status_code)
                else:
                    return False, (response.status_code, response.reason)
            else:
                print 'Refresh token to upload'
        except Exception,e:
            print 'Error in function delete_manipulation_information: ',e
            pass



if __name__ == '__main__':
    platform = PlatformMF()

    c = {
        "md5-hash": "5df9f63916ebf8528697b629022993e8",
        "whas": "d879f8f89b1bbf",
        "privacy": "agency",
        "ramses_user_comments": "This photograph was found in https://cybercrime.onion",
        "brand": "Apple",
        "sha256-hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
        "fileName": "IMG_2593.JPG",
        "date": "2018-02-14T08:53:00+0000",
        "hit_percetage": 95.2,
        "metadata_information": {
            "image": {
                "yResolution": 72,
                "orientation": "Horizontal (normal)",
                "make": "Apple",
                "dateTime": "2012-12-26T11:36:00+0000",
                "exifOffset": 204,
                "yCbCrPositioning": "Centered",
                "xResolution": 72,
                "date": 1356521760000,
                "model": "iPhone 4S",
                "software": "5.1 .1"
            },
            "exif": {
                "exposureProgram": "Program Normal",
                "focalLengthIn35mmFilm": 35,
                "colorSpace": "sRGB",
                "sharpness": "Normal",
                "apertureValue": "4845/1918",
                "brightnessValue": "8227/1011",
                "whiteBalance": "Auto",
                "sensingMethod": "One-chip color area",
                "fNumber": "12/5",
                "focalLength": "107/25",
                "flash": "Off",
                "componentsConfiguration": "YCbCr",
                "sceneCaptureType": "Standard",
                "exposureTime": "1/746",
                "photographicSensitivity": 64,
                "shutterSpeedValue": "7863/824",
                "pixelXDimension": 3264,
                "dateTimeDigitized": "2012-12-26T11:36:00+0000",
                "dateTimeOriginal": "2012-12-26T11:36:00+0000",
                "pixelYDimension": 2448,
                "exposureMode": "Auto Exposure",
                "flashpixVersion": 100,
                "subjectArea": [1631, 1223, 881, 881],
                "meteringMode": "Pattern",
                "exifVersion": 221
            },
            "gps": {
                "gpsTimeStamp": "[0/0, 0/0, 0/0]",
                "gpsImgDirectionRef": "T",
                "gpsImgDirection": "25449/74",
                "gpsLongitude": "[3, 1423/100, 0]",
                "gpsLatitudeRef": "N",
                "gpsAltitude": "4421/962",
                "gpsLatitude": "[51, 259/20, 0]",
                "gpsLongitudeRef": "E",
                "gpsAltitudeRef": 0
            }
        },
        "owner": {
            "username": "testing",
            "lastName": "testLastName",
            "agency": "Other",
            "userId": "0f9c51ee-3c3c-4bed-92d6-90548b63a8c1",
            "name": "testName"
        },
        "model": "iPhone 4 S",
        "id": "2"
    }
    x = {"privacy": "Private", "ramses_user_comments": "ssdfgsdfg", "fileName": "20160312_225412.jpg", "metadata_information": {"image": {"YResolution": "72", "ResolutionUnit": "Pixels/Inch", "ImageLength": "1836", "Orientation": "Rotated 90 CW", "Make": "SAMSUNG", "GPSInfo": "914", "ExifOffset": "238", "YCbCrPositioning": "Centered", "XResolution": "72", "ImageWidth": "3264", "Model": "GT-I9192", "DateTime": "2016-03-12T22:54:12+0000", "Software": "I9192UBUCNG2"}, "exif": {"LightSource": "Unknown", "ColorSpace": "sRGB", "ExposureMode": "Auto Exposure", "Flash": "Fired", "FlashpixVersion": "0100", "SceneCaptureType": "Standard", "MeteringMode": "CenterWeightedAverage", "ExifVersion": "0220", "InteroperabilityOffset": "884", "ImageUniqueID": "S08Q0LEGC01", "ExposureBiasValue": "0", "Saturation": "Normal", "MakerNote": "(7L, 0L, 1L, 0L, 7L, 0L, 4L, 0L, 0L, 0L, 48L, 49L, 48L, 48L, 2L, 0L, 4L, 0L, 1L, 0L, 0L, 0L, 0L, 32L, 1L, 0L, 12L, 0L, 4L, 0L, 1L, 0L, 0L, 0L, 0L, 0L, 0L, 0L, 16L, 0L, 5L, 0L, 1L, 0L, 0L, 0L, 90L, 0L, 0L, 0L, 64L, 0L, 4L, 0L, 1L, 0L, 0L, 0L, 0L, 0L, 0L, 0L, 80L, 0L, 4L, 0L, 1L, 0L, 0L, 0L, 1L, 0L, 0L, 0L, 0L, 1L, 3L, 0L, 1L, 0L, 0L, 0L, 0L, 0L, 0L, 0L, 0L, 0L, 0L, 0L, 0L, 0L, 0L, 0L, 0L, 0L, 0L, 0L)", "ExposureProgram": "Aperture Priority", "ShutterSpeedValue": "1/15", "PixelXDimension": "3264", "PixelYDimension": "1836", "ApertureValue": "69/25", "UserComment": "(65L, 83L, 67L, 73L, 73L, 0L, 0L, 0L, 85L, 115L, 101L, 114L, 32L, 99L, 111L, 109L, 109L, 101L, 110L, 116L, 115L, 0L)", "SceneType": "Directly Photographed", "BrightnessValue": "80", "WhiteBalance": "Auto", "SensingMethod": "One-chip color area", "FNumber": "13/5", "FocalLength": "37/10", "ComponentsConfiguration": "YCbCr", "ExposureTime": "1/15", "MaxApertureValue": "69/25", "PhotographicSensitivity": "800", "Sharpness": "Normal", "DigitalZoomRatio": "1"}, "gps": {"GPSVersionID": "(2L, 2L, 0L, 0L)"}}, "owner": {"username": "", "lastName": "Prototype", "agency": "Prototype", "userId": "None", "name": "Prototype"}, "id": 4}
    a = {"owner":
             {"username": "",
              "lastName": "Prototype",
              "agency": "Prototype",
              "userId": "None",
              "name": "Prototype"
              },
         "ramses_user_comments": "asdfasdf",
         "metadata_information": {
             "image": {
                 "YResolution": 72,
                 "ResolutionUnit": "Pixels/Inch",
                 "Orientation": "Horizontal (normal)",
                 "Make": "                               ",
                 "ImageDescription": "                               ",
                 "GPSInfo": 720,
                 "ExifOffset": 370,
                 "YCbCrPositioning": "Co-sited",
                 "XResolution": 72,
                 "Model": "                               ",
                 "DateTime": "2013-11-15T13:02:56+0000",
                 "Software": "MediaTek Camera Application;;;;"
             },
             "exif": {
                 "ExposureTime": "2357/500000",
                 "LightSource": "Other",
                 "FNumber": 2,
                 "Flash": "No",
                 "PhotographicSensitivity": 111,
                 "ExposureProgram": "Unidentified",
                 "FocalLength": "177/50",
                 "ExposureMode": "Auto Exposure",
                 "ColorSpace": "sRGB",
                 "FlashpixVersion": 0100,
                 "ComponentsConfiguration": "YCbCr",
                 "SceneCaptureType": "Standard",
                 "PixelYDimension": 3072,
                 "MeteringMode": "CenterWeightedAverage",
                 "ExifVersion": 0220,
                 "PixelXDimension": 4096,
                 "DigitalZoomRatio": 1,
                 "InteroperabilityOffset": 1119,
                 "WhiteBalance": "Auto",
                 "ExposureBiasValue": 0
             }
         },
         "id": 1,
         "fileName": "2013-11-15_13.02.56.jpg",
    }
    platform.client_secret = 'e32d1260-4724-4148-aefd-d9df677ecd78'
    platform.client_id = 'desktopapps-cli'
    platform.request_token('darren.smith','steganography')
    result, lst = platform.get_authorship_list('6161f370-bdc1-4d15-bf3b-aba59d58d259')
    result, lst = platform.get_authorship_list('')
    # result, lst = platform.get_manipulation_list('6161f370-bdc1-4d15-bf3b-aba59d58d259')
    for ele in range(0,20):
        y = ele
        result, details = platform.delete_authorship_information(y)
        #result, details = platform.delete_authorship_information(y)
        if result:
            print result, details
        else:
            print result, details

    #a = lst[0]
    b = json.dumps(a)
    #d = json.dumps(c)
    #z = json.dumps(x)
    #id = "4e95b0e3-6028-4690-8b31-518c07db9823"
# --- Authorship testing -- #
    result, details = platform.upload_authorship_information(b)
    print result,details
    result, listauth = platform.get_authorship_list('6161f370-bdc1-4d15-bf3b-aba59d58d259')

    if result:
        print result
    else:
        print details[0],details[1]

    # print platform.get_specific_authorship_information(id)
    # print platform.update_authorship_information(id, d)
    # print platform.delete_authorship_information(id)
# --- Manipulation testing --- #
    # print platform.get_manipulation_list()
    # print platform.get_specific_manipulation_information(5)
    # print platform.update_manipulation_information(2,d)
    # print platform.upload_manipulation_information(z)
