import os
import sys
import ssl
import json
import time
import gzip
import base64
import random
import socket
import logging
import asyncio
import binascii
import threading
import warnings
import types as _stdtypes
import http.client
from io import BytesIO
from datetime import datetime
import requests
import urllib3
import aiohttp
import jwt as pyjwt
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from urllib3.exceptions import InsecureRequestWarning
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
from google.protobuf.timestamp_pb2 import Timestamp
from protobuf_decoder.protobuf_decoder import Parser
import telebot
from telebot import types
warnings.simplefilter('ignore', InsecureRequestWarning)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
log = logging.getLogger('xct')
_sym_db = _symbol_database.Default()

def _build_pb2(module_name, serialized_file):
    mod = _stdtypes.ModuleType(module_name)
    mod_globals = mod.__dict__
    descriptor = _descriptor_pool.Default().AddSerializedFile(serialized_file)
    mod_globals['DESCRIPTOR'] = descriptor
    _builder.BuildMessageAndEnumDescriptors(descriptor, mod_globals)
    _builder.BuildTopDescriptorsAndMessages(descriptor, module_name, mod_globals)
    sys.modules[module_name] = mod
    return mod
like_pb2 = _build_pb2('like_pb2', b'\n\nlike.proto"#\n\x04like\x12\x0b\n\x03uid\x18\x01 \x01(\x03\x12\x0e\n\x06region\x18\x02 \x01(\tb\x06proto3')
like_count_pb2 = _build_pb2('like_count_pb2', b'\n\x10like_count.proto"?\n\tBasicInfo\x12\x0b\n\x03UID\x18\x01 \x01(\x03\x12\x16\n\x0ePlayerNickname\x18\x03 \x01(\t\x12\r\n\x05Likes\x18\x15 \x01(\x03"\'\n\x04Info\x12\x1f\n\x0bAccountInfo\x18\x01 \x01(\x0b2\n.BasicInfob\x06proto3')
uid_generator_pb2 = _build_pb2('uid_generator_pb2', b'\n\x13uid_generator.proto"0\n\ruid_generator\x12\x0f\n\x07saturn_\x18\x01 \x01(\x03\x12\x0e\n\x06garena\x18\x02 \x01(\x03b\x06proto3')
my_pb2 = _build_pb2('my_pb2', b'\n\x08my.proto"\xae\t\n\x08GameData\x12\x11\n\ttimestamp\x18\x03 \x01(\t\x12\x11\n\tgame_name\x18\x04 \x01(\t\x12\x14\n\x0cgame_version\x18\x05 \x01(\x05\x12\x14\n\x0cversion_code\x18\x07 \x01(\t\x12\x0f\n\x07os_info\x18\x08 \x01(\t\x12\x13\n\x0bdevice_type\x18\t \x01(\t\x12\x18\n\x10network_provider\x18\n \x01(\t\x12\x17\n\x0fconnection_type\x18\x0b \x01(\t\x12\x14\n\x0cscreen_width\x18\x0c \x01(\x05\x12\x15\n\rscreen_height\x18\r \x01(\x05\x12\x0b\n\x03dpi\x18\x0e \x01(\t\x12\x10\n\x08cpu_info\x18\x0f \x01(\t\x12\x11\n\ttotal_ram\x18\x10 \x01(\x05\x12\x10\n\x08gpu_name\x18\x11 \x01(\t\x12\x13\n\x0bgpu_version\x18\x12 \x01(\t\x12\x0f\n\x07user_id\x18\x13 \x01(\t\x12\x12\n\nip_address\x18\x14 \x01(\t\x12\x10\n\x08language\x18\x15 \x01(\t\x12\x0f\n\x07open_id\x18\x16 \x01(\t\x12\x15\n\rplatform_type\x18\x17 \x01(\x05\x12\x1a\n\x12device_form_factor\x18\x18 \x01(\t\x12\x14\n\x0cdevice_model\x18\x19 \x01(\t\x12\x14\n\x0caccess_token\x18\x1d \x01(\t\x12\x18\n\x10unknown_field_30\x18\x1e \x01(\x05\x12"\n\x1asecondary_network_provider\x18) \x01(\t\x12!\n\x19secondary_connection_type\x18* \x01(\t\x12\x11\n\tunique_id\x189 \x01(\t\x12\x10\n\x08field_60\x18< \x01(\x05\x12\x10\n\x08field_61\x18= \x01(\x05\x12\x10\n\x08field_62\x18> \x01(\x05\x12\x10\n\x08field_63\x18? \x01(\x05\x12\x10\n\x08field_64\x18@ \x01(\x05\x12\x10\n\x08field_65\x18A \x01(\x05\x12\x10\n\x08field_66\x18B \x01(\x05\x12\x10\n\x08field_67\x18C \x01(\x05\x12\x10\n\x08field_70\x18F \x01(\x05\x12\x10\n\x08field_73\x18I \x01(\x05\x12\x14\n\x0clibrary_path\x18J \x01(\t\x12\x10\n\x08field_76\x18L \x01(\x05\x12\x10\n\x08apk_info\x18M \x01(\t\x12\x10\n\x08field_78\x18N \x01(\x05\x12\x10\n\x08field_79\x18O \x01(\x05\x12\x17\n\x0fos_architecture\x18Q \x01(\t\x12\x14\n\x0cbuild_number\x18S \x01(\t\x12\x10\n\x08field_85\x18U \x01(\x05\x12\x18\n\x10graphics_backend\x18V \x01(\t\x12\x19\n\x11max_texture_units\x18W \x01(\x05\x12\x15\n\rrendering_api\x18X \x01(\x05\x12\x18\n\x10encoded_field_89\x18Y \x01(\t\x12\x10\n\x08field_92\x18\\ \x01(\x05\x12\x13\n\x0bmarketplace\x18] \x01(\t\x12\x16\n\x0eencryption_key\x18^ \x01(\t\x12\x15\n\rtotal_storage\x18_ \x01(\x05\x12\x10\n\x08field_97\x18a \x01(\x05\x12\x10\n\x08field_98\x18b \x01(\x05\x12\x10\n\x08field_99\x18c \x01(\t\x12\x11\n\tfield_100\x18d \x01(\tb\x06proto3')
output_pb2 = _build_pb2('output_pb2', b'\n\x13jwt_generator.proto"\xd2\x02\n\nGarena_420\x12\x12\n\naccount_id\x18\x01 \x01(\x03\x12\x0e\n\x06region\x18\x02 \x01(\t\x12\r\n\x05place\x18\x03 \x01(\t\x12\x10\n\x08location\x18\x04 \x01(\t\x12\x0e\n\x06status\x18\x05 \x01(\t\x12\r\n\x05token\x18\x08 \x01(\t\x12\n\n\x02id\x18\t \x01(\x05\x12\x0b\n\x03api\x18\n \x01(\t\x12\x0e\n\x06number\x18\x0c \x01(\x05\x12\x1e\n\tGarena420\x18\x0f \x01(\x0b2\x0b.Garena_420\x12\x0c\n\x04area\x18\x10 \x01(\t\x12\x11\n\tmain_area\x18\x12 \x01(\t\x12\x0c\n\x04city\x18\x13 \x01(\t\x12\x0c\n\x04name\x18\x14 \x01(\t\x12\x11\n\ttimestamp\x18\x15 \x01(\x03\x12\x0e\n\x06binary\x18\x16 \x01(\x0c\x12\x13\n\x0bbinary_data\x18\x17 \x01(\x0c\x1a"\n\x12Decrypted_Payloads\x12\x0c\n\x04type\x18\x01 \x01(\x05b\x06proto3')

class _runtime_version:

    class Domain:
        PUBLIC = 0

    @staticmethod
    def ValidateProtobufRuntimeVersion(*args, **kwargs):
        return True
_runtime_version.ValidateProtobufRuntimeVersion()
_MY_MSG_DESC = _descriptor_pool.Default().AddSerializedFile(b'\n\x10my_message.proto\">\n\tMyMessage\x12\x0f\n\x07field21\x18\x15 \x01(\x03\x12\x0f\n\x07field22\x18\x16 \x01(\x0c\x12\x0f\n\x07field23\x18\x17 \x01(\x0cb\x06proto3')
_my_msg_globals = {'DESCRIPTOR': _MY_MSG_DESC}
_builder.BuildMessageAndEnumDescriptors(_MY_MSG_DESC, _my_msg_globals)
_builder.BuildTopDescriptorsAndMessages(_MY_MSG_DESC, 'my_message_pb2', _my_msg_globals)
MyMessage = _my_msg_globals['MyMessage']
PORT = int(os.environ.get('PORT', 3086))
STORAGE_PATH = '.'
ACCOUNTS_FILE = os.path.join(STORAGE_PATH, 'accounts.txt')
TOKEN_FILE = os.path.join(STORAGE_PATH, 'token_me.json')
AES_KEY = b'Yg&tc%DEuh6%Zc^8'
AES_IV = b'6oyZDr22E3ychjM%'
TOKEN_REFRESH_INTERVAL_HOURS = 0.1
MAX_WORKERS = 20
TOKEN_CHECK_INTERVAL_SECONDS = 360
MIN_TOKENS_REQUIRED = 209
MIN_TOKENS_THRESHOLD = 200
FIXED_PROFILE_INDEX = 0
scheduler_started = False
REMOTE_CONFIG_URL = 'https://redzedupdater.vercel.app/'
remote_config = None
remote_config_last_fetch = 0
REMOTE_CONFIG_TTL = 3600
TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN', '8987849883:AAHNPcadpexKmsxrrfTOUg-PLiUh2CFXO0E')
AUTOLIKE_DEFAULT_DAYS = 30
                    
OWNER_ID_1 = 7788474071                                     
OWNER_ID_2 = 7788474071                                      
OWNER_USERNAME_1 = '@T_HJP'
OWNER_USERNAME_2 = '@T_HJP'
OWNERS = [OWNER_ID_1, OWNER_ID_2]
DEV_ID = OWNER_ID_1                                                
SETTINGS_FILE = 'settings.json'
POINTS_FILE = 'points.json'                                  
COOLDOWN_FILE = 'cooldown.json'                                       
LIKE_LOG_FILE = 'like_log.json'                                      
AUTOLIKE_FILE = 'autolike.json'                                 
VIDEO_URLS = ['https://files.manuscdn.com/user_upload_by_module/session_file/310519663335892754/GfyAbOEojZXntNzY.mp4', 'https://files.manuscdn.com/user_upload_by_module/session_file/310519663164155365/xDgUpDjOaxevfcCn.mp4', 'https://files.manuscdn.com/user_upload_by_module/session_file/310519663335892754/soBMHvEgqEiTlvLo.mp4', 'https://files.manuscdn.com/user_upload_by_module/session_file/310519663335892754/RJASbgsIouLYfpVs.mp4', 'https://files.manuscdn.com/user_upload_by_module/session_file/310519663335892754/KFjcpUZTvYTTAoUk.mp4']
DEFAULT_SETTINGS = {
    'maintenance_mode': False,
    'use_external_like_api': False,
    'external_like_api_url': 'https://l9bi7e-likes-100.onrender.com/like?uid={uid}&server_name=ME',
    'external_like_api_key': '',
    'external_like_api_timeout': 120,
    'bot_description': '<tg-emoji emoji-id=\"6113652711951963203\">🔥</tg-emoji> RA7 x LIKE BOT <tg-emoji emoji-id=\"6115989917190330036\">🔥</tg-emoji>\n\n<tg-emoji emoji-id=\"6113765721131456191\">🎮</tg-emoji> بوت لايكات فري فاير مع Auto-Like يومي\n\n<tg-emoji emoji-id=\"6116444878781027101\">❤</tg-emoji> /like UID\n<tg-emoji emoji-id=\"6113761116926513509\">🤖</tg-emoji> Auto-Like مع مدة انتهاء\n\nDEV BY : @CB_2H',
    'like_command': '/like',
    'broadcast_message': '',
    'max_accounts': 15,
                               
    'points_required_local': 1,                                                
    'points_required_api': 1,                                         
    'require_points_local': False,                                   
    'require_points_api': True,                                    
                            
    'cooldown_hours': 7,                                              
    'cooldown_enabled': True,                                 
                             
    'autolike_enabled': True,
    'autolike_hour': 5,
    'autolike_minute': 0,
    'autolike_channel_id': '',                                  
    'autolike_channel_title': '',                                
    'private_enabled': True,
    'groups_enabled': True,
    'login_timeout': 15,
    'max_retries': 5,
    'help_message_template': '<blockquote><b><tg-emoji emoji-id=\"6113825592975560832\">🔥</tg-emoji> S1X x LIKE BOT <tg-emoji emoji-id=\"6116154779509985300\">🔥</tg-emoji></b></blockquote>\n\n<blockquote><b><tg-emoji emoji-id=\"6113987307084190650\">🎮</tg-emoji> الأوامر المتاحة:</b>\n\n<b><tg-emoji emoji-id=\"6114020073389692577\">❤</tg-emoji> إرسال لايكات:</b>\n<code>{like_cmd} [UID]</code>\nمثال: <code>{like_cmd} 123456789</code>\n\n<b><tg-emoji emoji-id=\"6116331543184020120\">💰</tg-emoji> رصيد النقاط:</b>\n<code>/points</code>\n\n<b><tg-emoji emoji-id=\"6113942089668497853\">🛒</tg-emoji> شراء النقاط:</b>\n<code>/buy</code>\n\n<b><tg-emoji emoji-id=\"6114087555915846958\">👑</tg-emoji> لوحة المالك:</b>\n<code>/owner</code>\n\n<b><tg-emoji emoji-id=\"6113875126833386131\">🤖</tg-emoji> Auto-Like:</b> من لوحة المالك تقدر تضيف UID مع مدة انتهاء\n\n<b>ℹ مساعدة:</b> <code>/start</code> أو <code>/help</code></blockquote>\n\n<b>DEV BY:</b> <b>' + OWNER_USERNAME_1 + '</b>',
    'like_response_template': '<blockquote><b><tg-emoji emoji-id=\"6113926348613357755\">🔥</tg-emoji> نتيجة اللايكات <tg-emoji emoji-id=\"6113646419824874154\">🔥</tg-emoji></b></blockquote>\n\n<blockquote><b><tg-emoji emoji-id=\"6114095922512139382\">🎮</tg-emoji> اسم اللاعب:</b> <b>{PlayerNickname}</b>\n<b>🆔 الايدي:</b> <code>{UID}</code>\n<b><tg-emoji emoji-id=\"6113823454081848116\">❤</tg-emoji> اللايكات قبل:</b> <b>{LikesbeforeCommand}</b>\n<b><tg-emoji emoji-id=\"6115905027161723867\">✨</tg-emoji> اللايكات بعد:</b> <b>{LikesafterCommand}</b>\n<b><tg-emoji emoji-id=\"6113807747386446494\">➕</tg-emoji> تم إضافة:</b> <b>{LikesGivenByAPI}</b>\n<b><tg-emoji emoji-id=\"6116375149986979339\">⚡</tg-emoji> الطلبات الناجحة:</b> <b>{tokens_used}</b>\n<b><tg-emoji emoji-id=\"6116434807082718394\">🎯</tg-emoji> الحالة:</b> <b>{status}</b>\n<b><tg-emoji emoji-id=\"6113798032170422849\">💰</tg-emoji> رصيدك المتبقي:</b> <b>{points_left}</b></blockquote>\n\n<b>DEV BY:</b> <b>' + OWNER_USERNAME_1 + '</b>'
}
_settings = {}
_settings_lock = threading.Lock()
LOGIN_SERVERS = ['loginbp.ggpolarbear.com'] * 30
GETPORTS_SERVERS = ['https://clientbp.ggpolarbear.com/GetLoginData', 'https://client.ind.freefiremobile.com/GetLoginData', 'https://client.us.freefiremobile.com/GetLoginData']
_active_count = 0
_active_lock = threading.Lock()
_max_active = 15
_clis = []
_clis_lock = threading.Lock()

def get_random_video():
    return random.choice(VIDEO_URLS)

def load_settings():
    global _settings, _max_active
    try:
        if os.path.exists(SETTINGS_FILE):
            with open(SETTINGS_FILE, 'r', encoding='utf-8') as f:
                loaded = json.load(f)
                _settings = {**DEFAULT_SETTINGS, **loaded}
                log.info(f'[SETTINGS] Loaded from file: {SETTINGS_FILE}')
        else:
            _settings = DEFAULT_SETTINGS.copy()
            save_settings()
            log.info(f'[SETTINGS] Created new file: {SETTINGS_FILE}')
                                  
        old_help_marker = 'الأوامر المتاحة'                     
        if old_help_marker in (_settings.get('help_message_template') or ''):
            _settings['help_message_template'] = DEFAULT_SETTINGS['help_message_template']
            log.info('[SETTINGS] Migrated help_message_template to English version')
        save_settings()
        _max_active = _settings.get('max_accounts', 15)
        log.info(f'[SETTINGS] Max accounts set to: {_max_active}')
    except Exception as e:
        log.error(f'[SETTINGS ERROR] {e}, using defaults')
        _settings = DEFAULT_SETTINGS.copy()
        _max_active = 15

def save_settings():
    try:
        with _settings_lock:
            with open(SETTINGS_FILE, 'w', encoding='utf-8') as f:
                json.dump(_settings, f, indent=2, ensure_ascii=False)
        log.info('[SETTINGS] Saved to file')
        return True
    except Exception as e:
        log.error(f'[SETTINGS SAVE ERROR] {e}')
        return False

def update_setting(key, value):
    global _settings, _max_active
    with _settings_lock:
        _settings[key] = value
        if key == 'max_accounts':
            _max_active = value
    save_settings()
    log.info(f'[SETTINGS] Updated {key} = {value}')

def get_settings():
    with _settings_lock:
        return _settings.copy()

def fetch_remote_config():
    global remote_config, remote_config_last_fetch
    try:
        r = requests.get(REMOTE_CONFIG_URL, timeout=10)
        if r.status_code == 200:
            remote_config = r.json()
            remote_config_last_fetch = time.time()
            log.info(f"Remote config loaded: version {remote_config.get('current_version')}")
            return True
    except Exception as e:
        log.error(f'Failed to fetch remote config: {e}')
    return False

def get_client_url():
    global remote_config
    if not remote_config or time.time() - remote_config_last_fetch > REMOTE_CONFIG_TTL:
        fetch_remote_config()
    if remote_config and 'client_url' in remote_config:
        return remote_config['client_url'].get('etc', 'https://clientbp.ggpolarbear.com/')
    return 'https://clientbp.ggpolarbear.com/'

def get_server_url():
    global remote_config
    if not remote_config or time.time() - remote_config_last_fetch > REMOTE_CONFIG_TTL:
        fetch_remote_config()
    if remote_config and 'server_url' in remote_config:
        return remote_config['server_url'].rstrip('/')
    return 'https://loginbp.ggpolarbear.com'

def get_release_version():
    global remote_config
    if not remote_config or time.time() - remote_config_last_fetch > REMOTE_CONFIG_TTL:
        fetch_remote_config()
    if remote_config and 'latest_release_version' in remote_config:
        return remote_config['latest_release_version']
    return 'OB54'

def decode_jwt_payload(token):
    try:
        parts = token.split('.')
        if len(parts) != 3:
            return None
        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:
            payload += '=' * padding
        decoded = base64.urlsafe_b64decode(payload)
        return json.loads(decoded)
    except Exception:
        return None

def is_token_expired(token):
    try:
        payload = decode_jwt_payload(token)
        if not payload:
            return True
        exp = payload.get('exp')
        if not exp:
            iat = payload.get('iat')
            ttl = payload.get('ttl', 7200)
            if iat:
                exp = iat + ttl
            else:
                return True
        current_time = int(time.time())
        return current_time >= exp
    except Exception:
        return True

def get_token_remaining_time(token):
    try:
        payload = decode_jwt_payload(token)
        if not payload:
            return 0
        exp = payload.get('exp')
        if not exp:
            iat = payload.get('iat')
            ttl = payload.get('ttl', 7200)
            if iat:
                exp = iat + ttl
            else:
                return 0
        remaining = exp - int(time.time())
        return max(0, remaining)
    except Exception:
        return 0

def get_oauth_token(password, uid):
    log.info(f'[LOCAL JWT] Requesting Garena OAuth token for UID {uid}...')
    url = 'https://ffmconnect.live.gop.garenanow.com/oauth/guest/token/grant'
    headers = {'Host': '100067.connect.garena.com', 'User-Agent': 'GarenaMSDK/4.0.19P4(G011A ;Android 9;en;US;)', 'Content-Type': 'application/x-www-form-urlencoded', 'Accept-Encoding': 'gzip, deflate, br', 'Connection': 'close'}
    data = {'uid': uid, 'password': password, 'response_type': 'token', 'client_type': '2', 'client_secret': '2ee44819e9b4598845141067b281621874d0d5d7af9d8f7e00c1e54715b7d1e3', 'client_id': '100067'}
    try:
        r = requests.post(url, headers=headers, data=data, timeout=30, verify=False)
        if r.status_code != 200:
            log.error(f'[LOCAL JWT] Garena returned HTTP {r.status_code} for UID {uid}')
            return None
        try:
            j = r.json()
        except Exception as e:
            log.error(f'[LOCAL JWT] Failed to parse Garena JSON for UID {uid}: {e}')
            return None
        token = j.get('access_token') or j.get('token') or j.get('session_key') or j.get('jwt') or (j.get('data') or {}).get('token')
        if not token:
            log.warning(f'[LOCAL JWT] No access_token in Garena response for UID {uid}: {j}')
            return None
        j['access_token'] = token
        log.info(f'[LOCAL JWT] Garena OAuth success for UID {uid}')
        return {'access_token': j.get('access_token'), 'open_id': j.get('open_id', ''), 'uid': j.get('uid', uid), 'raw': j, 'source': 'garena_local'}
    except Exception as e:
        log.error(f'[LOCAL JWT] Garena OAuth request failed for UID {uid}: {e}')
        return None

def encrypt_aes(key, iv, plaintext):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_message = pad(plaintext, AES.block_size)
    return cipher.encrypt(padded_message)

def parse_major_login_response(response_content):
    response_dict = {}
    try:
        lines = response_content.split('\n')
        for line in lines:
            if ':' in line:
                key, value = line.split(':', 1)
                response_dict[key.strip()] = value.strip().strip('"')
    except Exception:
        pass
    return response_dict

def generate_jwt_token(uid, password):
    token_data = get_oauth_token(password, uid)
    if not token_data or not token_data.get('access_token'):
        log.error(f'No access token for UID {uid} from any source')
        return None
    access_token = token_data['access_token']
    open_id = token_data.get('open_id', '')
    release_version = get_release_version()
    server_url = get_server_url()
    token_source = token_data.get('source', 'unknown')
    game_data = my_pb2.GameData()
    game_data.timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    game_data.game_name = 'free fire'
    game_data.game_version = 1
    game_data.version_code = '1.108.3'
    game_data.os_info = 'Android OS 9 / API-28 (PI/rel.cjw.20220518.114133)'
    game_data.device_type = 'Handheld'
    game_data.network_provider = 'Verizon Wireless'
    game_data.connection_type = 'WIFI'
    game_data.screen_width = 1280
    game_data.screen_height = 960
    game_data.dpi = '240'
    game_data.cpu_info = 'ARMv7 VFPv3 NEON VMH | 2400 | 4'
    game_data.total_ram = 5951
    game_data.gpu_name = 'Adreno (TM) 640'
    game_data.gpu_version = 'OpenGL ES 3.0'
    game_data.user_id = f'Google|{uid}-{int(time.time())}'
    game_data.ip_address = '172.190.111.97'
    game_data.language = 'en'
    game_data.open_id = open_id
    game_data.access_token = access_token
    game_data.platform_type = 4
    game_data.device_form_factor = 'Handheld'
    game_data.device_model = 'Asus ASUS_I005DA'
    game_data.field_60 = 32968
    game_data.field_61 = 29815
    game_data.field_62 = 2479
    game_data.field_63 = 914
    game_data.field_64 = 31213
    game_data.field_65 = 32968
    game_data.field_66 = 31213
    game_data.field_67 = 32968
    game_data.field_70 = 4
    game_data.field_73 = 2
    game_data.library_path = '/data/app/com.dts.freefireth-QPvBnTUhYWE-7DMZSOGdmA==/lib/arm'
    game_data.field_76 = 1
    game_data.apk_info = '5b892aaabd688e571f688053118a162b|/data/app/com.dts.freefireth-QPvBnTUhYWE-7DMZSOGdmA==/base.apk'
    game_data.field_78 = 6
    game_data.field_79 = 1
    game_data.os_architecture = '32'
    game_data.build_number = '2019117877'
    game_data.field_85 = 1
    game_data.graphics_backend = 'OpenGLES2'
    game_data.max_texture_units = 16383
    game_data.rendering_api = 4
    game_data.encoded_field_89 = '\x17T\x11\x17\x02\x08\x0eUMQ\x08EZ\x03@ZK;Z\x02\x0eV\ri[QVi\x03\ro\t\x07e'
    game_data.field_92 = 9204
    game_data.marketplace = '3rd_party'
    game_data.encryption_key = 'KqsHT2B4It60T/65PGR5PXwFxQkVjGNi+IMCK3CFBCBfrNpSUA1dZnjaT3HcYchlIFFL1ZJOg0cnulKCPGD3C3h1eFQ='
    game_data.total_storage = 111107
    game_data.field_97 = 1
    game_data.field_98 = 1
    game_data.field_99 = '4'
    game_data.field_100 = '4'
    serialized = game_data.SerializeToString()
    encrypted = encrypt_aes(AES_KEY, AES_IV, serialized)
    major_login_url = f'{server_url}/MajorLogin'
    headers = {'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 9; ASUS_Z01QD Build/PI)', 'Connection': 'Keep-Alive', 'Accept-Encoding': 'gzip', 'Content-Type': 'application/octet-stream', 'Expect': '100-continue', 'X-GA': 'v1 1', 'X-Unity-Version': '2018.4.11f1', 'ReleaseVersion': release_version}
    try:
        log.info(f'MajorLogin for UID {uid} to {major_login_url}')
        response = requests.post(major_login_url, data=encrypted, headers=headers, verify=False, timeout=30)
        if response.status_code == 200:
            parsed = output_pb2.Garena_420()
            parsed.ParseFromString(response.content)
            result = parse_major_login_response(str(parsed))
            jwt_token = result.get('token')
            if jwt_token:
                log.info(f'JWT generated for UID {uid} via {token_source}')
                return {'uid': str(uid), 'token': jwt_token, 'region': 'ME', 'status': 'live', 'generated_at': int(time.time()), 'server_url': server_url, 'release_version': release_version, 'token_source': token_source}
            else:
                log.error(f'No JWT in MajorLogin response for UID {uid}')
        else:
            log.error(f'MajorLogin returned status {response.status_code} for UID {uid}')
        return None
    except Exception as e:
        log.error(f'MajorLogin failed for {uid}: {e}')
        return None

def load_accounts():
    accounts = []
    if not os.path.exists(ACCOUNTS_FILE):
        log.error(f'Accounts file not found: {ACCOUNTS_FILE}')
        return accounts
    with open(ACCOUNTS_FILE, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if ':' in line:
                uid, pwd = line.split(':', 1)
                accounts.append({'uid': uid.strip(), 'password': pwd.strip()})
    log.info(f'Loaded {len(accounts)} accounts')
    return accounts

def load_tokens():
    if not os.path.exists(TOKEN_FILE):
        log.warning(f'Token file not found: {TOKEN_FILE}')
        return (None, 0, 0)
    try:
        with open(TOKEN_FILE, 'r') as f:
            tokens = json.load(f)
        if not isinstance(tokens, list):
            return (None, 0, 0)
        valid_tokens = []
        expired_count = 0
        for token_entry in tokens:
            token = token_entry.get('token', '')
            if not token:
                continue
            if is_token_expired(token):
                expired_count += 1
                token_entry['expires_in'] = 0
                valid_tokens.append(token_entry)
            else:
                remaining = get_token_remaining_time(token)
                token_entry['expires_in'] = remaining
                valid_tokens.append(token_entry)
        log.info(f'Tokens: {len(valid_tokens)} valid (including expired for retry), {expired_count} expired, {len(tokens)} total')
        return (valid_tokens, expired_count, len(tokens))
    except Exception as e:
        log.error(f'Failed to load tokens: {e}')
        return (None, 0, 0)

def save_tokens(tokens):
    try:
        os.makedirs(os.path.dirname(TOKEN_FILE) if os.path.dirname(TOKEN_FILE) else '.', exist_ok=True)
        with open(TOKEN_FILE, 'w') as f:
            json.dump(tokens, f, indent=2)
        log.info(f'Saved {len(tokens)} tokens to {TOKEN_FILE}')
        return True
    except Exception as e:
        log.error(f'Failed to save tokens: {e}')
        return False

def refresh_expired_tokens():
    log.info('Refreshing expired tokens...')
    accounts = load_accounts()
    if not accounts:
        log.error('No accounts found')
        return False
    current_tokens = []
    if os.path.exists(TOKEN_FILE):
        try:
            with open(TOKEN_FILE, 'r') as f:
                current_tokens = json.load(f)
        except Exception:
            current_tokens = []
    uid_to_account = {acc['uid']: acc for acc in accounts}
    tokens_to_refresh = []
    for token_entry in current_tokens:
        uid = token_entry.get('uid')
        token = token_entry.get('token', '')
        if not token or is_token_expired(token):
            if uid in uid_to_account:
                tokens_to_refresh.append(uid_to_account[uid])
    existing_uids = {t.get('uid') for t in current_tokens if not is_token_expired(t.get('token', ''))}
    valid_count = len(existing_uids)
    if valid_count < MIN_TOKENS_THRESHOLD:
        needed = MIN_TOKENS_REQUIRED - valid_count
        log.info(f'Token count {valid_count} below threshold {MIN_TOKENS_THRESHOLD}, generating {needed} more to reach {MIN_TOKENS_REQUIRED}')
        added = 0
        for acc in accounts:
            if acc['uid'] in existing_uids:
                continue
            if any(a['uid'] == acc['uid'] for a in tokens_to_refresh):
                continue
            tokens_to_refresh.append(acc)
            added += 1
            if valid_count + added >= MIN_TOKENS_REQUIRED:
                break
    else:
        for acc in accounts:
            if acc['uid'] not in existing_uids and not any(a['uid'] == acc['uid'] for a in tokens_to_refresh):
                tokens_to_refresh.append(acc)
    if not tokens_to_refresh:
        log.info('No tokens need refresh')
        return True
    log.info(f'Refreshing {len(tokens_to_refresh)} tokens...')
    results = []
    results_lock = threading.Lock()
    threads = []

    def worker(acc):
        try:
            result = generate_jwt_token(acc['uid'], acc['password'])
            if result:
                with results_lock:
                    results.append(result)
        except Exception as e:
            log.error(f'worker error for {acc.get("uid")}: {e}')
        time.sleep(0.2)
    for acc in tokens_to_refresh:
        t = threading.Thread(target=worker, args=(acc,))
        threads.append(t)
    for i in range(0, len(threads), MAX_WORKERS):
        batch = threads[i:i + MAX_WORKERS]
        for t in batch:
            t.start()
        for t in batch:
            t.join()
    if results:
        valid_existing = [t for t in current_tokens if not is_token_expired(t.get('token', ''))]
        uid_map = {t['uid']: t for t in valid_existing}
        for new_token in results:
            uid_map[new_token['uid']] = new_token
        merged = list(uid_map.values())
        log.info(f'After refresh: {len(merged)} total tokens available')
        return save_tokens(merged)
    return False

def refresh_all_tokens():
    log.info('Starting full token refresh...')
    accounts = load_accounts()
    if not accounts:
        log.error('No accounts to refresh')
        return
    current_tokens = []
    if os.path.exists(TOKEN_FILE):
        try:
            with open(TOKEN_FILE, 'r') as f:
                current_tokens = json.load(f)
        except Exception:
            current_tokens = []
    valid_existing_count = sum(1 for t in current_tokens if not is_token_expired(t.get('token', '')))
    log.info(f'Currently valid tokens: {valid_existing_count}')
    if valid_existing_count >= MIN_TOKENS_REQUIRED:
        log.info('Sufficient valid tokens, refreshing only expired ones')
        return refresh_expired_tokens()
    needed = max(MIN_TOKENS_REQUIRED - valid_existing_count, len(accounts))
    log.info(f'Need to generate up to {needed} tokens')
    valid_uids = {t.get('uid') for t in current_tokens if not is_token_expired(t.get('token', ''))}
    to_process = [acc for acc in accounts if acc['uid'] not in valid_uids]
    to_process = to_process[:max(needed, MIN_TOKENS_REQUIRED)]
    results = []
    results_lock = threading.Lock()
    threads = []

    def worker(acc):
        try:
            result = generate_jwt_token(acc['uid'], acc['password'])
            if result:
                with results_lock:
                    results.append(result)
        except Exception as e:
            log.error(f'worker error for {acc.get("uid")}: {e}')
        time.sleep(0.2)
    for acc in to_process:
        t = threading.Thread(target=worker, args=(acc,))
        threads.append(t)
    for i in range(0, len(threads), MAX_WORKERS):
        batch = threads[i:i + MAX_WORKERS]
        for t in batch:
            t.start()
        for t in batch:
            t.join()
    if results:
        existing = []
        if os.path.exists(TOKEN_FILE):
            try:
                with open(TOKEN_FILE, 'r') as f:
                    existing = json.load(f)
            except Exception:
                existing = []
        uid_map = {item['uid']: item for item in existing}
        for new_item in results:
            uid_map[new_item['uid']] = new_item
        merged = list(uid_map.values())
        save_tokens(merged)
        log.info(f'Saved {len(merged)} tokens to {TOKEN_FILE}')
    else:
        log.error('No tokens generated!')

def scheduled_refresh():
    while True:
        log.info('Starting a new token refresh cycle...')
        try:
            current_tokens = []
            if os.path.exists(TOKEN_FILE):
                try:
                    with open(TOKEN_FILE, 'r') as f:
                        current_tokens = json.load(f)
                except Exception:
                    current_tokens = []
            valid_count = sum(1 for t in current_tokens if not is_token_expired(t.get('token', '')))
            log.info(f'[SCHEDULER] Valid tokens count: {valid_count}')
            if valid_count < MIN_TOKENS_THRESHOLD:
                log.info(f'[SCHEDULER] Valid tokens {valid_count} below {MIN_TOKENS_THRESHOLD}, generating more to reach {MIN_TOKENS_REQUIRED}')
                refresh_all_tokens()
            else:
                refresh_expired_tokens()
        except Exception as e:
            log.error(f'scheduled_refresh cycle error: {e}')
        log.info(f'Cycle completed. Next check in {TOKEN_CHECK_INTERVAL_SECONDS} seconds ({TOKEN_CHECK_INTERVAL_SECONDS // 60} minutes)...')
        time.sleep(TOKEN_CHECK_INTERVAL_SECONDS)

def start_scheduler():
    global scheduler_started
    if not scheduler_started:
        t = threading.Thread(target=scheduled_refresh, daemon=True)
        t.start()
        scheduler_started = True
        log.info('Token scheduler started')

def encrypt_for_like(plaintext):
    try:
        cipher = AES.new(AES_KEY, AES.MODE_CBC, AES_IV)
        padded = pad(plaintext, AES.block_size)
        encrypted = cipher.encrypt(padded)
        return binascii.hexlify(encrypted).decode('utf-8')
    except Exception:
        return None

def create_like_protobuf(uid, region):
    try:
        msg = like_pb2.like()
        msg.uid = int(uid)
        msg.region = region
        return msg.SerializeToString()
    except Exception:
        return None

def create_uid_protobuf(uid):
    try:
        msg = uid_generator_pb2.uid_generator()
        msg.saturn_ = int(uid)
        msg.garena = 1
        return msg.SerializeToString()
    except Exception:
        return None

def decode_player_info(binary_data):
    if not binary_data or len(binary_data) < 5:
        return None
    try:
        info = like_count_pb2.Info()
        info.ParseFromString(binary_data)
        if info.AccountInfo.UID != 0:
            return info
    except Exception:
        pass
    try:
        basic = like_count_pb2.BasicInfo()
        basic.ParseFromString(binary_data)
        if basic.UID != 0:
            info = like_count_pb2.Info()
            info.AccountInfo.UID = basic.UID
            info.AccountInfo.PlayerNickname = basic.PlayerNickname
            info.AccountInfo.Likes = basic.Likes
            return info
    except Exception:
        pass
    return None

def get_player_info_pb(encrypted_uid, token):
    try:
        client_url = get_client_url()
        url = f'{client_url}GetPlayerPersonalShow'
        edata = bytes.fromhex(encrypted_uid)
        headers = {'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 9; ASUS_Z01QD Build/PI)', 'Connection': 'Keep-Alive', 'Accept-Encoding': 'gzip', 'Authorization': f'Bearer {token}', 'Content-Type': 'application/x-www-form-urlencoded', 'Expect': '100-continue', 'X-Unity-Version': '2018.4.11f1', 'X-GA': 'v1 1', 'ReleaseVersion': get_release_version()}
        response = requests.post(url, data=edata, headers=headers, verify=False, timeout=15)
        if response.status_code == 401:
            return (None, 'EXPIRED')
        if response.status_code != 200:
            return (None, f'HTTP_{response.status_code}')
        result = decode_player_info(response.content)
        return (result, 'OK')
    except Exception:
        return (None, 'ERROR')

async def send_like_request(encrypted_uid, token):
    try:
        client_url = get_client_url()
        url = f'{client_url}LikeProfile'
        edata = bytes.fromhex(encrypted_uid)
        headers = {'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 9; ASUS_Z01QD Build/PI)', 'Connection': 'Keep-Alive', 'Accept-Encoding': 'gzip', 'Authorization': f'Bearer {token}', 'Content-Type': 'application/x-www-form-urlencoded', 'Expect': '100-continue', 'X-Unity-Version': '2018.4.11f1', 'X-GA': 'v1 1', 'ReleaseVersion': get_release_version()}
        async with aiohttp.ClientSession() as session:
            async with session.post(url, data=edata, headers=headers, timeout=10) as resp:
                return resp.status
    except Exception:
        return None

async def send_multiple_likes(uid, tokens):
    try:
        proto_data = create_like_protobuf(uid, 'ME')
        if not proto_data:
            return None
        encrypted = encrypt_for_like(proto_data)
        if not encrypted:
            return None
        tasks = []
        num_to_send = len(tokens)
        log.info(f'Sending likes from ALL {num_to_send} tokens to UID {uid}')
        for i in range(num_to_send):
            token = tokens[i]['token']
            tasks.append(send_like_request(encrypted, token))
        results = await asyncio.gather(*tasks, return_exceptions=True)
        success = sum(1 for r in results if isinstance(r, int) and r == 200)
        log.info(f'Like requests sent: {num_to_send}, successful HTTP 200: {success}')
        return results
    except Exception as e:
        log.error(f'send_multiple_likes error: {e}')
        return None

def get_profile_check_token(valid_tokens):
    if not valid_tokens:
        return None
    for t in valid_tokens:
        tok = t.get('token', '')
        if tok and not is_token_expired(tok):
            return tok
    return valid_tokens[0].get('token') if valid_tokens else None

def do_like(uid):
    try:
        valid_tokens, expired_count, total_count = load_tokens()
        if not valid_tokens or len(valid_tokens) < MIN_TOKENS_THRESHOLD:
            log.warning(f'Tokens count {len(valid_tokens) if valid_tokens else 0} below threshold, refreshing...')
            refresh_expired_tokens()
            valid_tokens, _, _ = load_tokens()
            if not valid_tokens or len(valid_tokens) == 0:
                return {'error': 'No valid tokens available', 'message': 'Token refresh failed', 'expired_count': expired_count, 'total_count': total_count}
        non_expired = [t for t in valid_tokens if not is_token_expired(t.get('token', ''))]
        if not non_expired:
            return {'error': 'All tokens expired'}
        check_token = non_expired[FIXED_PROFILE_INDEX % len(non_expired)]['token']
        log.info(f'Using fixed profile-check token (index {FIXED_PROFILE_INDEX}) for UID {uid}')
        uid_proto = create_uid_protobuf(uid)
        if not uid_proto:
            return {'error': 'UID protobuf failed'}
        encrypted_uid = encrypt_for_like(uid_proto)
        if not encrypted_uid:
            return {'error': 'Encryption failed'}
        before_info, status = get_player_info_pb(encrypted_uid, check_token)
        if status == 'EXPIRED':
            log.warning('Profile-check token expired, refreshing...')
            refresh_expired_tokens()
            valid_tokens, _, _ = load_tokens()
            if not valid_tokens:
                return {'error': 'Token expired and refresh failed'}
            non_expired = [t for t in valid_tokens if not is_token_expired(t.get('token', ''))]
            if not non_expired:
                return {'error': 'All tokens expired after refresh'}
            check_token = non_expired[FIXED_PROFILE_INDEX % len(non_expired)]['token']
            before_info, status = get_player_info_pb(encrypted_uid, check_token)
        if before_info is None:
            return {'error': 'Failed to retrieve player info', 'token_status': status, 'valid_tokens_available': len(valid_tokens)}
        before_likes = int(before_info.AccountInfo.Likes)
        player_name = str(before_info.AccountInfo.PlayerNickname)
        player_uid = int(before_info.AccountInfo.UID)
        log.info(f'Before: {player_name} has {before_likes} likes')
        target_tokens = non_expired
        log.info(f'Sending likes from ALL {len(target_tokens)} valid tokens')
        asyncio.run(send_multiple_likes(uid, target_tokens))
        time.sleep(8)
        after_info, _ = get_player_info_pb(encrypted_uid, check_token)
        if after_info is None:
            return {'error': 'Failed to get final player info'}
        after_likes = int(after_info.AccountInfo.Likes)
        likes_given = after_likes - before_likes
        log.info(f'After: {player_name} has {after_likes} likes (added: {likes_given})')
        return {'LikesAdded': likes_given, 'LikesGivenByAPI': likes_given, 'LikesafterCommand': after_likes, 'LikesbeforeCommand': before_likes, 'PlayerNickname': player_name, 'UID': player_uid, 'message': f'تمت إضافة {likes_given} إعجاب بنجاح' if likes_given > 0 else 'فشل في إضافة الإعجابات', 'status': 1 if likes_given > 0 else 2, 'tokens_used': len(target_tokens)}
    except Exception as e:
        log.error(f'do_like error: {e}')
        return {'error': str(e)}

def do_like_external_api(uid):
\
\
\
\
\
\
\
\
\
       
    try:
        settings = get_settings()
        api_template = settings.get('external_like_api_url', '') or ''
        if not api_template:
            return {'error': 'External API not configured'}
        timeout_s = int(settings.get('external_like_api_timeout', 120) or 120)
        api_key = (settings.get('external_like_api_key', '') or '').strip()
                                                                          
        if '{uid}' in api_template:
            full_url = api_template.replace('{uid}', str(uid))
        else:
            sep = '&' if '?' in api_template else '?'
            full_url = f'{api_template}{sep}uid={uid}'
                                                                        
        headers = {
            'Accept': 'application/json',
            'User-Agent': 'XcT-LikeBot/1.0'
        }
        if api_key:
                                                          
            if '{key}' in full_url:
                full_url = full_url.replace('{key}', api_key)
            elif '{api_key}' in full_url:
                full_url = full_url.replace('{api_key}', api_key)
            elif '{apikey}' in full_url:
                full_url = full_url.replace('{apikey}', api_key)
            elif '{token}' in full_url:
                full_url = full_url.replace('{token}', api_key)
            else:
                                                                             
                lower_url = full_url.lower()
                if ('key=' not in lower_url and 'api_key=' not in lower_url
                        and 'apikey=' not in lower_url and 'token=' not in lower_url):
                    sep2 = '&' if '?' in full_url else '?'
                                                                                           
                    full_url = f'{full_url}{sep2}key={api_key}'
                                                                         
            headers['X-API-Key'] = api_key
            headers['apikey'] = api_key
            headers['Authorization'] = f'Bearer {api_key}'
                                                             
        try:
            log.info(f'Calling external like API (masked): {_mask_api_url(api_template)} for UID {uid} (key_used={bool(api_key)})')
        except Exception:
            pass
        try:
            resp = requests.get(full_url, headers=headers, timeout=timeout_s, verify=False)
        except requests.exceptions.Timeout:
            return {'error': 'External API timeout'}
        except requests.exceptions.RequestException:
                                                                                                
            return {'error': 'External API connection failed'}
        if resp.status_code != 200:
                                                                   
            try:
                err_body = resp.json()
                if isinstance(err_body, dict):
                    err_msg = err_body.get('error') or err_body.get('message') or err_body.get('detail') or ''
                    if err_msg:
                        return {'error': f'API HTTP {resp.status_code}: {str(err_msg)[:120]}'}
            except Exception:
                pass
            return {'error': f'External API HTTP {resp.status_code}'}
        try:
            data = resp.json()
        except Exception:
            return {'error': 'External API returned non-JSON'}
        if not isinstance(data, dict):
            return {'error': 'External API bad response'}
                                                                     
        def _g(*keys, default=None):
            for k in keys:
                if k in data and data[k] not in (None, ''):
                    return data[k]
            return default

        likes_before_v = _g('LikesbeforeCommand', 'LikesBefore', 'likes_before', 'BeforeLikes', default=0)
        likes_after_v = _g('LikesafterCommand', 'LikesAfter', 'likes_after', 'AfterLikes', default=0)
        likes_given_v = _g('LikesGivenByAPI', 'LikesGiven', 'likes_given', 'GivenLikes', default=None)
                                                                     
        if likes_given_v is None:
            try:
                likes_given_v = max(0, int(likes_after_v) - int(likes_before_v))
            except Exception:
                likes_given_v = 0

        token_pool = data.get('token_pool_info') if isinstance(data.get('token_pool_info'), dict) else {}
        tokens_available = token_pool.get('total_tokens_available', _g('TotalTokensUsed', default=0))

        normalized = {
            'PlayerNickname': _g('PlayerNickname', 'PlayerName', 'nickname', 'username', default='Unknown'),
            'UID': _g('UID', 'uid', 'PlayerUID', default=uid),
            'LikesbeforeCommand': likes_before_v,
            'LikesafterCommand': likes_after_v,
            'LikesGivenByAPI': likes_given_v,
            'tokens_used': _g('tokens_used', 'TokensUsed', 'SuccessfulRequests', 'successful_requests', default=0),
            'TotalTokensUsed': _g('TotalTokensUsed', 'tokens_used', default=0),
            'tokens_available': tokens_available,
            'status': _g('status', 'Status', default=1),
            'message': _g('message', default=''),
            'source': 'external_api',
            'raw': data,                                    
        }
        return normalized
    except Exception as e:
                                                     
        msg_txt = str(e)
                                             
        try:
            import re as _re_s
            msg_txt = _re_s.sub(r'https?://\S+', '[hidden-url]', msg_txt)
        except Exception:
            msg_txt = '[error]'
        return {'error': f'External API error: {msg_txt[:120]}'}

def init_like_engine():
    fetch_remote_config()
    if not os.path.exists(STORAGE_PATH):
        os.makedirs(STORAGE_PATH, exist_ok=True)
    if not os.path.exists(ACCOUNTS_FILE):
        with open(ACCOUNTS_FILE, 'w') as f:
            f.write('')
        log.info(f'Created empty {ACCOUNTS_FILE}')
    start_scheduler()

def ua():
    versions = ['4.0.18P6', '4.0.19P7', '4.0.20P1', '4.1.0P3', '4.1.5P2', '4.2.1P8', '4.2.3P1', '5.0.1B2', '5.0.2P4', '5.1.0P1', '5.2.0B1', '5.2.5P3', '5.3.0B1', '5.3.2P2', '5.4.0P1', '5.4.3B2', '5.5.0P1', '5.5.2P3']
    models = ['SM-A125F', 'SM-A225F', 'SM-A325M', 'SM-A515F', 'SM-A725F', 'SM-M215F', 'SM-M325FV', 'Redmi 9A', 'Redmi 9C', 'POCO M3', 'POCO M4 Pro', 'RMX2185', 'RMX3085', 'moto g(9) play', 'CPH2239', 'V2027', 'OnePlus Nord', 'ASUS_Z01QD']
    android_versions = ['9', '10', '11', '12', '13', '14']
    languages = ['en-US', 'es-MX', 'pt-BR', 'id-ID', 'ru-RU', 'hi-IN']
    countries = ['USA', 'MEX', 'BRA', 'IDN', 'RUS', 'IND']
    return f'GarenaMSDK/{random.choice(versions)}({random.choice(models)};Android {random.choice(android_versions)};{random.choice(languages)};{random.choice(countries)};)'

def encAEs(hexStr):
    cipher = AES.new(AES_KEY, AES.MODE_CBC, AES_IV)
    return cipher.encrypt(pad(bytes.fromhex(hexStr), AES.block_size)).hex()

def decAEs(hexStr):
    cipher = AES.new(AES_KEY, AES.MODE_CBC, AES_IV)
    return unpad(cipher.decrypt(bytes.fromhex(hexStr)), AES.block_size).hex()

def encPacket(hexStr, k, iv):
    return AES.new(k, AES.MODE_CBC, iv).encrypt(pad(bytes.fromhex(hexStr), 16)).hex()

def decPacket(hexStr, k, iv):
    return unpad(AES.new(k, AES.MODE_CBC, iv).decrypt(bytes.fromhex(hexStr)), 16).hex()

def encUid(h, tp):
    e, h = ([], int(h))
    while h:
        e.append(h & 127 | (128 if h > 127 else 0))
        h >>= 7
    return bytes(e).hex() if tp == 'Uid' else None

def encVarint(n):
    if n < 0:
        return b''
    h = []
    while True:
        b = n & 127
        n >>= 7
        if n:
            b |= 128
        h.append(b)
        if not n:
            break
    return bytes(h)

def decUid(h):
    n = s = 0
    for b in bytes.fromhex(h):
        n |= (b & 127) << s
        if not b & 128:
            break
        s += 7
    return n

def createVarint(field, value):
    return encVarint(field << 3 | 0) + encVarint(value)

def createLength(field, value):
    hdr = encVarint(field << 3 | 2)
    enc = value.encode() if isinstance(value, str) else value
    return hdr + encVarint(len(enc)) + enc

def createProto(fields):
    pkt = bytearray()
    for f, v in fields.items():
        if isinstance(v, dict):
            nested = createProto(v)
            pkt.extend(createLength(f, nested))
        elif isinstance(v, int):
            pkt.extend(createVarint(f, v))
        elif isinstance(v, (str, bytes)):
            pkt.extend(createLength(f, v))
    return pkt

def decodeHex(h):
    r = hex(h)[2:]
    return '0' + r if len(r) == 1 else r

def fixParsed(parsed):
    d = {}
    for r in parsed:
        fd = {'wire_type': r.wire_type}
        if r.wire_type in ('varint', 'string', 'bytes'):
            fd['data'] = r.data
        elif r.wire_type == 'length_delimited':
            fd['data'] = fixParsed(r.data.results)
        d[r.field] = fd
    return d

def decodePacket(hexInput):
    try:
        parsed = Parser().parse(hexInput)
        return json.dumps(fixParsed(parsed))
    except Exception:
        return None

def xBunner():
    av = ['902000016', '902000031', '902000011', '902000065', '902000204', '902000192', '902000191', '902000179', '902000133', '902045001', '902038023', '902048004', '902039014', '902000063', '902000306', '902047009']
    return int(random.choice(av))

def genPkt(pkt, n, k, iv):
    enc = encPacket(pkt, k, iv)
    l = decodeHex(len(enc) // 2)
    if len(l) == 2:
        hdr = n + '000000'
    elif len(l) == 3:
        hdr = n + '00000'
    elif len(l) == 4:
        hdr = n + '0000'
    elif len(l) == 5:
        hdr = n + '000'
    else:
        hdr = n + '000000'
    return bytes.fromhex(hdr + l + enc)

def openRoom(k, iv):
    f = {1: 2, 2: {1: 1, 2: 15, 3: 5, 4: 'xAyOuB', 5: '1', 6: 12, 7: 1, 8: 1, 9: 1, 11: 1, 12: 2, 14: 36981056, 15: {1: 'IDC3', 2: 126, 3: 'ME'}, 16: '\x01\x03\x04\x07\t\n\x0b\x12\x0f\x0e\x16\x19\x1a \x1d', 18: 2368584, 27: 1, 34: '\x00\x01', 40: 'en', 48: 1, 49: {1: 21}, 50: {1: 36981056, 2: 2368584, 5: 2}}}
    return genPkt(str(createProto(f).hex()), '0E15', k, iv)

def spmRoom(k, iv, uid):
    f = {1: 22, 2: {1: int(uid)}}
    return genPkt(str(createProto(f).hex()), '0E15', k, iv)

def gAccess(u, p):
    r = requests.post('https://100067.connect.garena.com/oauth/guest/token/grant', headers={'Host': '100067.connect.garena.com', 'User-Agent': ua(), 'Content-Type': 'application/x-www-form-urlencoded', 'Accept-Encoding': 'gzip, deflate, br', 'Connection': 'close'}, data={'uid': str(u), 'password': str(p), 'response_type': 'token', 'client_type': '2', 'client_secret': '2ee44819e9b4598845141067b281621874d0d5d7af9d8f7e00c1e54715b7d1e3', 'client_id': '100067'}, verify=False)
    if r.status_code == 200:
        return (r.json()['access_token'], r.json()['open_id'])
    return (None, None)

def majorLogin(pyl, server=None):
    if server is None:
        server = random.choice(LOGIN_SERVERS)
    ctx = ssl._create_unverified_context()
    timeout = get_settings().get('login_timeout', 30)
    for attempt in range(3):
        try:
            conn = http.client.HTTPSConnection(server, context=ctx, timeout=timeout)
            conn.request('POST', '/MajorLogin', body=pyl, headers={'X-Unity-Version': '2022.3.47f1', 'ReleaseVersion': 'OB54', 'Content-Type': 'application/x-www-form-urlencoded', 'X-GA': 'v1 1', 'Content-Length': str(len(pyl)), 'User-Agent': 'UnityPlayer/2022.3.47f1 (UnityWebRequest/1.0, libcurl/8.5.0-DEV)', 'Host': server, 'Connection': 'Keep-Alive', 'Accept-Encoding': 'deflate, gzip'})
            resp = conn.getresponse()
            raw = resp.read()
            if resp.getheader('Content-Encoding') == 'gzip':
                raw = gzip.GzipFile(fileobj=BytesIO(raw)).read()
            conn.close()
            if resp.status in [200, 201]:
                return (raw, server)
            log.info(f'[-] majorLogin status {resp.status} from {server}')
            return (None, server)
        except Exception as e:
            log.info(f'[-] majorLogin attempt {attempt + 1}/3 failed ({server}): {e}')
            if attempt < 2:
                time.sleep(2)
                server = random.choice(LOGIN_SERVERS)
    return (None, server)

def getPorts(tok, pyl):
    for server_url in GETPORTS_SERVERS:
        for attempt in range(3):
            try:
                host = server_url.split('/')[2]
                r = requests.post(server_url, headers={'Expect': '100-continue', 'Authorization': f'Bearer {tok}', 'X-Unity-Version': '2022.3.47f1', 'X-GA': 'v1 1', 'ReleaseVersion': 'OB54', 'Content-Type': 'application/x-www-form-urlencoded', 'User-Agent': 'UnityPlayer/2022.3.47f1 (UnityWebRequest/1.0, libcurl/8.5.0-DEV)', 'Host': host, 'Connection': 'close', 'Accept-Encoding': 'deflate, gzip'}, data=pyl, verify=False, timeout=30)
                d = json.loads(decodePacket(r.content.hex()))
                a1, a2 = (d['32']['data'], d['14']['data'])
                log.info(f'[+] getPorts successful via {host}')
                return (a1[:len(a1) - 6], a1[len(a1) - 5:], a2[:len(a2) - 6], a2[len(a2) - 5:])
            except Exception as e:
                log.info(f'[-] getPorts attempt {attempt + 1}/3 failed ({host}): {e}')
                if attempt < 2:
                    time.sleep(2)
    raise Exception('All getPorts servers failed')

def getKiv(raw):
    m = MyMessage()
    m.ParseFromString(raw)
    ts = Timestamp()
    ts.FromNanoseconds(m.field21)
    return (ts.seconds * 1000000000 + ts.nanos, m.field22, m.field23)

def buildAuth(jwtTok, k, iv, ts):
    dec = pyjwt.decode(jwtTok, options={'verify_signature': False})
    enc = hex(dec['account_id'])[2:]
    tsH = decodeHex(ts)
    jH = jwtTok.encode().hex()
    hLen = hex(len(encPacket(jH, k, iv)) // 2)[2:]
    padMap = {9: '0000000', 8: '00000000', 10: '000000', 7: '000000000'}
    pad_ = padMap.get(len(enc), '00000000')
    return f'0115{pad_}{enc}{tsH}00000{hLen}' + encPacket(jH, k, iv)

def login(u, p):
    at, oid = gAccess(u, p)
    if not at:
        return None
    dT = bytes.fromhex('1a13323032362d30342d30382031313a35363a3438220966726565206669726528013a07312e3132332e314232416e64726f6964204f532039202f204150492d3238202850492f72656c2e636a772e32303232303531382e313134313333294a0848616e6468656c64520c4d544e2f537061636574656c5a045749464960800a68d00572033234307a2d7838362d3634205353453320535345342e3120535345342e32204156582041565832207c2032343030207c20348001e61e8a010f416472656e6f2028544d292036343092010d4f70656e474c20455320332e329a012b476f6f676c657c36323566373136662d393161372d343935622d396631362d303866653964336336353333a2010e3137362e32382e3133392e313835aa01026172b201203433303632343537393364653836646134323561353263616164663231656564ba010134c2010848616e6468656c64ca010d4f6e65506c7573204135303130ea014063363961653230386661643732373338623637346232383437623530613361316466613235643161313966616537343566633736616334613065343134633934f00101ca020c4d544e2f537061636574656cd2020457494649ca03203161633462383065636630343738613434323033626638666163363132306635e003b5ee02e8039a8002f003af13f80384078004a78f028804b5ee029004a78f029804b5ee02b00404c80401d2043d2f646174612f6170702f636f6d2e6474732e667265656669726574682d66705843537068495636644b43376a4c2d574f7952413d3d2f6c69622f61726de00401ea045f65363261623933353464386662356662303831646233333861636233333439317c2f646174612f6170702f636f6d2e6474732e667265656669726574682d66705843537068495636644b43376a4c2d574f7952413d3d2f626173652e61706bf00406f804018a050233329a050a32303139313139303236a80503b205094f70656e474c455332b805ff01c00504e005be7eea05093372645f7061727479f205704b717348543857393347646347335a6f7a454e6646775648746d377171316552554e6149444e67526f626f7a4942744c4f695943633459367a767670634943787a514632734f453463627974774c7334785a62526e70524d706d5752514b6d654f35766373386e51594268777148374bf805e7e4068806019006019a060134a2060134b2062213521146500e590349510e460900115843395f005b510f685b560a6107576d0f0366')
    dT = dT.replace(b'2025-11-26 01:51:28', str(datetime.now())[:-7].encode())
    dT = dT.replace(b'c69ae208fad72738b674b2847b50a3a1dfa25d1a19fae745fc76ac4a0e414c94', at.encode())
    dT = dT.replace(b'4306245793de86da425a52caadf21eed', oid.encode())
    pyl = bytes.fromhex(encAEs(dT.hex()))
    max_retries = get_settings().get('max_retries', 5)
    for attempt in range(max_retries):
        raw, used_server = majorLogin(pyl)
        if raw:
            try:
                d = json.loads(decodePacket(raw.hex()))
                jwtTok = d['8']['data']
                ts, k, iv = getKiv(raw)
                ip, port, ip2, port2 = getPorts(jwtTok, pyl)
                auth = buildAuth(jwtTok, k, iv, ts)
                log.info(f'[+] Login successful via {used_server} (attempt {attempt + 1})')
                return (auth, k, iv, ip, port, ip2, port2)
            except Exception as e:
                log.info(f'[-] Failed to parse login response from {used_server}: {e}')
        else:
            log.info(f'[-] Login failed via {used_server} (attempt {attempt + 1})')
    return None

_points_lock = threading.Lock()
_cooldown_lock = threading.Lock()
_likelog_lock = threading.Lock()
_autolike_lock = threading.Lock()

def _load_json_file(path, default):
    try:
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
    except Exception as e:
        log.error(f'[JSON LOAD ERROR] {path}: {e}')
    return default

def _save_json_file(path, data):
    try:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        log.error(f'[JSON SAVE ERROR] {path}: {e}')
        return False

def get_user_points(user_id):
    with _points_lock:
        data = _load_json_file(POINTS_FILE, {})
        return int(data.get(str(user_id), 0))

def set_user_points(user_id, amount):
    with _points_lock:
        data = _load_json_file(POINTS_FILE, {})
        data[str(user_id)] = max(0, int(amount))
        _save_json_file(POINTS_FILE, data)
        return data[str(user_id)]

def add_user_points(user_id, amount):
    with _points_lock:
        data = _load_json_file(POINTS_FILE, {})
        cur = int(data.get(str(user_id), 0))
        cur = max(0, cur + int(amount))
        data[str(user_id)] = cur
        _save_json_file(POINTS_FILE, data)
        return cur

def deduct_user_points(user_id, amount):
                                                                          
    with _points_lock:
        data = _load_json_file(POINTS_FILE, {})
        cur = int(data.get(str(user_id), 0))
        if cur < int(amount):
            return (False, cur)
        cur -= int(amount)
        data[str(user_id)] = cur
        _save_json_file(POINTS_FILE, data)
        return (True, cur)

def list_all_points():
    with _points_lock:
        return _load_json_file(POINTS_FILE, {})

def is_owner(user_id):
    return int(user_id) in OWNERS

def get_cooldown_remaining(target_uid):
\
                     
    s = get_settings()
    if not s.get('cooldown_enabled', True):
        return 0
    hours = float(s.get('cooldown_hours', 7) or 0)
    if hours <= 0:
        return 0
    with _cooldown_lock:
        data = _load_json_file(COOLDOWN_FILE, {})
        last_ts = float(data.get(str(target_uid), 0) or 0)
    if last_ts <= 0:
        return 0
    elapsed = time.time() - last_ts
    remaining = (hours * 3600) - elapsed
    return max(0, int(remaining))

def mark_cooldown(target_uid):
    with _cooldown_lock:
        data = _load_json_file(COOLDOWN_FILE, {})
        data[str(target_uid)] = time.time()
        _save_json_file(COOLDOWN_FILE, data)

def format_remaining(seconds):
    seconds = int(seconds)
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    if h > 0:
        return f'{h}h {m}m'
    if m > 0:
        return f'{m}m {s}s'
    return f'{s}s'

def log_like_usage(user_id, username, target_uid, likes_given, mode):
                                                                           
    with _likelog_lock:
        data = _load_json_file(LIKE_LOG_FILE, [])
        if not isinstance(data, list):
            data = []
        entry = {
            'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'user_id': int(user_id),
            'username': str(username or ''),
            'target_uid': str(target_uid),
            'likes_given': int(likes_given or 0),
            'mode': mode,                                  
        }
        data.append(entry)
                                    
        if len(data) > 500:
            data = data[-500:]
        _save_json_file(LIKE_LOG_FILE, data)

def get_like_log(limit=20):
    with _likelog_lock:
        data = _load_json_file(LIKE_LOG_FILE, [])
        if not isinstance(data, list):
            return []
        return list(reversed(data))[:limit]

def format_autolike_duration(days):
    try:
        days = int(days or 0)
    except Exception:
        days = 0
    if days <= 0:
        return 'دائم'
    if days == 1:
        return 'يوم واحد'
    if days == 2:
        return 'يومان'
    if days <= 10:
        return f'{days} أيام'
    return f'{days} يوم'


def format_datetime_local(ts):
    try:
        ts = int(ts or 0)
        if ts <= 0:
            return '—'
        return datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M')
    except Exception:
        return '—'


def format_remaining_detailed(seconds):
    try:
        seconds = int(seconds or 0)
    except Exception:
        seconds = 0
    if seconds <= 0:
        return 'منتهية'
    days = seconds // 86400
    hours = (seconds % 86400) // 3600
    minutes = (seconds % 3600) // 60
    if days > 0:
        return f'{days} يوم {hours} ساعة'
    if hours > 0:
        return f'{hours} ساعة {minutes} دقيقة'
    return format_remaining(seconds)


def _normalize_autolike_entries(raw_data):
    result = []
    if not isinstance(raw_data, list):
        return result
    now_ts = int(time.time())
    for item in raw_data:
        if isinstance(item, str):
            result.append({
                'uid': str(item),
                'added_at': now_ts,
                'duration_days': AUTOLIKE_DEFAULT_DAYS,
                'expires_at': now_ts + (AUTOLIKE_DEFAULT_DAYS * 86400)
            })
        elif isinstance(item, dict):
            uid = str(item.get('uid', '')).strip()
            if not uid:
                continue
            added_at = int(item.get('added_at') or now_ts)
            duration_days = int(item.get('duration_days') or AUTOLIKE_DEFAULT_DAYS)
            expires_at = int(item.get('expires_at') or 0)
            if duration_days <= 0:
                expires_at = 0
            elif expires_at <= 0:
                expires_at = added_at + (duration_days * 86400)
            result.append({
                'uid': uid,
                'added_at': added_at,
                'duration_days': duration_days,
                'expires_at': expires_at
            })
    return result


def get_autolike_list():
    with _autolike_lock:
        data = _load_json_file(AUTOLIKE_FILE, [])
        entries = _normalize_autolike_entries(data)
        if data != entries:
            _save_json_file(AUTOLIKE_FILE, entries)
        return entries


def get_autolike_active_list():
    now_ts = int(time.time())
    entries = get_autolike_list()
    active = []
    changed = False
    for entry in entries:
        expires_at = int(entry.get('expires_at') or 0)
        if expires_at > 0 and expires_at <= now_ts:
            changed = True
            continue
        active.append(entry)
    if changed:
        with _autolike_lock:
            _save_json_file(AUTOLIKE_FILE, active)
    return active


def add_autolike_uid(uid, duration_days=AUTOLIKE_DEFAULT_DAYS):
    with _autolike_lock:
        data = _load_json_file(AUTOLIKE_FILE, [])
        entries = _normalize_autolike_entries(data)
        uid = str(uid).strip()
        if any(str(x.get('uid')) == uid for x in entries):
            return False, None
        now_ts = int(time.time())
        duration_days = int(duration_days or 0)
        expires_at = 0 if duration_days <= 0 else now_ts + (duration_days * 86400)
        entry = {
            'uid': uid,
            'added_at': now_ts,
            'duration_days': duration_days,
            'expires_at': expires_at
        }
        entries.append(entry)
        _save_json_file(AUTOLIKE_FILE, entries)
        return True, entry


def remove_autolike_uid(uid):
    with _autolike_lock:
        data = _load_json_file(AUTOLIKE_FILE, [])
        entries = _normalize_autolike_entries(data)
        uid = str(uid).strip()
        new_entries = [x for x in entries if str(x.get('uid')) != uid]
        if len(new_entries) != len(entries):
            _save_json_file(AUTOLIKE_FILE, new_entries)
            return True
        return False

_autolike_thread_started = False
_autolike_last_run_date = None

def _autolike_worker():
    global _autolike_last_run_date
    log.info('[AUTOLIKE] Scheduler started')
    while True:
        try:
            s = get_settings()
            entries = get_autolike_active_list()
            if s.get('autolike_enabled', True):
                now = datetime.now()
                target_h = int(s.get('autolike_hour', 5))
                target_m = int(s.get('autolike_minute', 0))
                today_key = now.strftime('%Y-%m-%d')
                if (now.hour == target_h and now.minute == target_m
                        and _autolike_last_run_date != today_key):
                    _autolike_last_run_date = today_key
                    log.info(f'[AUTOLIKE] Triggering for {len(entries)} UIDs at {now}')
                    for entry in entries:
                        uid = str(entry.get('uid'))
                        try:
                            use_api = bool(s.get('use_external_like_api', False))
                            data = do_like_external_api(uid) if use_api else do_like(uid)
                            if not isinstance(data, dict):
                                data = {}
                            given = int(data.get('LikesGivenByAPI') or 0)
                            player_name = str(data.get('PlayerNickname') or data.get('PlayerName') or 'Unknown')
                            likes_before = int(data.get('LikesbeforeCommand') or data.get('LikesBefore') or 0)
                            likes_after = int(data.get('LikesafterCommand') or data.get('LikesAfter') or 0)
                            status_text = '<tg-emoji emoji-id=\"6115955617581503451\">✅</tg-emoji> تم الإرسال' if given > 0 else '<tg-emoji emoji-id=\"6113779946063139126\">⚠</tg-emoji> لم يتم إضافة لايكات'
                            added_at = int(entry.get('added_at') or 0)
                            duration_days = int(entry.get('duration_days') or 0)
                            expires_at = int(entry.get('expires_at') or 0)
                            remaining_text = 'دائم' if expires_at <= 0 else format_remaining_detailed(max(0, expires_at - int(time.time())))
                            expires_text = 'بدون انتهاء' if expires_at <= 0 else format_datetime_local(expires_at)
                            duration_text = format_autolike_duration(duration_days)
                            log_like_usage(0, 'AUTOLIKE', uid, given, 'autolike')
                            if given > 0:
                                mark_cooldown(uid)
                            message_text = (
                                '<tg-emoji emoji-id=\"6113928466032235268\">🔥</tg-emoji> <b>AUTO LIKE RESULT</b> <tg-emoji emoji-id=\"6116118139143984337\">🔥</tg-emoji>\n\n'
                                f'<tg-emoji emoji-id=\"6113699548570325974\">🎮</tg-emoji> <b>اسم اللاعب:</b> <b>{player_name}</b>\n'
                                f'🆔 <b>الايدي:</b> <code>{uid}</code>\n'
                                f'<tg-emoji emoji-id=\"6113684937091584843\">❤</tg-emoji> <b>اللايكات قبل:</b> <b>{likes_before}</b>\n'
                                f'<tg-emoji emoji-id=\"6115940881548711252\">✨</tg-emoji> <b>اللايكات بعد:</b> <b>{likes_after}</b>\n'
                                f'<tg-emoji emoji-id=\"6113948471989900276\">➕</tg-emoji> <b>تمت الإضافة:</b> <b>{given}</b>\n'
                                f'<tg-emoji emoji-id=\"6114112148898583350\">📌</tg-emoji> <b>الحالة:</b> <b>{status_text}</b>\n\n'
                                f'<tg-emoji emoji-id=\"6113994453909772072\">📅</tg-emoji> <b>تاريخ الإضافة للأوتو لايك:</b> <b>{format_datetime_local(added_at)}</b>\n'
                                f'<tg-emoji emoji-id=\"6116084191722476904\">⏳</tg-emoji> <b>المدة المحددة:</b> <b>{duration_text}</b>\n'
                                f'<tg-emoji emoji-id=\"6115915850479309711\">⌛</tg-emoji> <b>المدة المتبقية:</b> <b>{remaining_text}</b>\n'
                                f'<tg-emoji emoji-id=\"6113776583103747337\">🗓</tg-emoji> <b>ينتهي في:</b> <b>{expires_text}</b>'
                            )
                            for oid in OWNERS:
                                try:
                                    bot.send_message(oid, message_text, parse_mode='HTML')
                                except Exception:
                                    pass
                                                                                                          
                            try:
                                ch_id = (s.get('autolike_channel_id') or '').strip()
                                if ch_id:
                                    target = int(ch_id) if (ch_id.lstrip('-').isdigit()) else ch_id
                                    bot.send_message(target, message_text,
                                                     parse_mode='HTML',
                                                     reply_markup=_autolike_buy_keyboard(),
                                                     disable_web_page_preview=True)
                            except Exception as _ch_err:
                                log.error(f'[AUTOLIKE] channel send error: {_ch_err}')
                            time.sleep(2)
                        except Exception as e:
                            log.error(f'[AUTOLIKE] uid={uid} error: {e}')
        except Exception as e:
            log.error(f'[AUTOLIKE] loop error: {e}')
        time.sleep(30)

def start_autolike_scheduler():
    global _autolike_thread_started
    if _autolike_thread_started:
        return
    _autolike_thread_started = True
    t = threading.Thread(target=_autolike_worker, daemon=True)
    t.start()

bot = telebot.TeleBot(TELEGRAM_TOKEN, parse_mode='HTML')

def _mask_api_url(url):
\
                                                                        
    try:
        if not url:
            return '(not set)'
        import re as _re
        m = _re.match(r'^(https?://)([^/?#]+)(.*)$', url)
        if not m:
            return '****'
        scheme, host, _rest = m.group(1), m.group(2), m.group(3)
        if len(host) <= 6:
            host_masked = host[:1] + '***'
        else:
            host_masked = host[:3] + '****' + host[-3:]
        return f'{scheme}{host_masked}/****'
    except Exception:
        return '****'

def owner_panel_keyboard():
                                                     
    kb = types.InlineKeyboardMarkup(row_width=2)
    settings = get_settings()
                
    maintenance_text = '<tg-emoji emoji-id=\"6114154501571090045\">🔴</tg-emoji> إيقاف البوت' if not settings['maintenance_mode'] else '<tg-emoji emoji-id=\"6116332651285582453\">🟢</tg-emoji> تشغيل البوت'
    kb.add(types.InlineKeyboardButton(maintenance_text, callback_data='toggle_maintenance'))
                        
    like_src_text = '<tg-emoji emoji-id=\"6113840006885807270\">🌐</tg-emoji> وضع: API' if settings.get('use_external_like_api', False) else '<tg-emoji emoji-id=\"6116219388703020383\">🏠</tg-emoji> وضع: Local'
    kb.add(types.InlineKeyboardButton(like_src_text, callback_data='toggle_like_source'))
                                                
    req_api = settings.get('require_points_api', True)
    req_local = settings.get('require_points_local', False)
    kb.add(types.InlineKeyboardButton(
        f"{'<tg-emoji emoji-id=\"6113691641535534529\">✅</tg-emoji>' if req_api else '<tg-emoji emoji-id=\"6114022469981443174\">❌</tg-emoji>'} نقاط لـ API",
        callback_data='toggle_points_api'))
    kb.add(types.InlineKeyboardButton(
        f"{'<tg-emoji emoji-id=\"6114185695918559996\">✅</tg-emoji>' if req_local else '<tg-emoji emoji-id=\"6113700313074504581\">❌</tg-emoji>'} نقاط لـ Local",
        callback_data='toggle_points_local'))
                       
    kb.add(types.InlineKeyboardButton('<tg-emoji emoji-id=\"6114017431984805017\">💰</tg-emoji> إرسال نقاط لمستخدم', callback_data='send_points'))
    kb.add(types.InlineKeyboardButton('<tg-emoji emoji-id=\"6114192984478062175\">📋</tg-emoji> رصيد المستخدمين', callback_data='list_points'))
    kb.add(types.InlineKeyboardButton('<tg-emoji emoji-id=\"6114153406354429603\">⚙</tg-emoji> تعديل سعر النقاط', callback_data='edit_point_cost'))
              
    cd_enabled = settings.get('cooldown_enabled', True)
    cd_hours = settings.get('cooldown_hours', 7)
    cooldown_status = 'تشغيل' if cd_enabled else 'إيقاف'
    cooldown_button_text = (
        '<tg-emoji emoji-id="6113795047168152280">⏱</tg-emoji> '
        f'Cooldown: {cooldown_status} ({cd_hours}h)'
    )
    kb.add(types.InlineKeyboardButton(
        cooldown_button_text,
        callback_data='cooldown_menu'))
               
    al_enabled = settings.get('autolike_enabled', True)
    al_h = settings.get('autolike_hour', 5)
    al_m = settings.get('autolike_minute', 0)
    kb.add(types.InlineKeyboardButton(
        f"<tg-emoji emoji-id=\"6115911993598677568\">🤖</tg-emoji> Auto-Like: {'ON' if al_enabled else 'OFF'} ({al_h:02d}:{al_m:02d})",
        callback_data='autolike_menu'))
                                       
    ch_title = settings.get('autolike_channel_title') or settings.get('autolike_channel_id') or ''
    ch_btn_text = f"<tg-emoji emoji-id=\"6116310437714727918\">📡</tg-emoji> قناة الأوتو لايك: {ch_title}" if ch_title else '<tg-emoji emoji-id=\"6113815980838753459\">📡</tg-emoji> إضافة قناة الأوتو لايك'
    kb.add(types.InlineKeyboardButton(ch_btn_text, callback_data='autolike_channel'))
              
    kb.add(types.InlineKeyboardButton('<tg-emoji emoji-id=\"6113848540985824266\">📜</tg-emoji> سجل اللايكات', callback_data='like_log'))
                
    kb.add(types.InlineKeyboardButton('<tg-emoji emoji-id=\"6113689438217310821\">🔑</tg-emoji> رابط API', callback_data='set_like_api_url'))
    kb.add(types.InlineKeyboardButton('<tg-emoji emoji-id=\"6116286978603356999\">🗝</tg-emoji> مفتاح API', callback_data='set_like_api_key'))
          
    kb.add(types.InlineKeyboardButton('<tg-emoji emoji-id=\"6115953590356939544\">✏</tg-emoji> وصف البوت', callback_data='edit_desc'))
    kb.add(types.InlineKeyboardButton('<tg-emoji emoji-id=\"6116239218567025507\">📝</tg-emoji> رسالة المساعدة', callback_data='edit_help'))
    kb.add(types.InlineKeyboardButton('<tg-emoji emoji-id=\"6114119875544749556\">❤</tg-emoji> قالب رد اللايك', callback_data='edit_like_template'))
    kb.add(types.InlineKeyboardButton('<tg-emoji emoji-id=\"6113652711951963203\">❤</tg-emoji> تغيير أمر اللايك', callback_data='change_like'))
    kb.add(types.InlineKeyboardButton('<tg-emoji emoji-id=\"6115989917190330036\">📢</tg-emoji> إذاعة', callback_data='broadcast'))
    kb.add(types.InlineKeyboardButton('<tg-emoji emoji-id=\"6113765721131456191\">📊</tg-emoji> حالة البوت', callback_data='bot_status'))
    priv_en = settings.get('private_enabled', True)
    grp_en = settings.get('groups_enabled', True)
    kb.add(types.InlineKeyboardButton(
        ('<tg-emoji emoji-id=\"6116444878781027101\">🟢</tg-emoji> الخاص: مُفعّل' if priv_en else '<tg-emoji emoji-id=\"6113761116926513509\">🔴</tg-emoji> الخاص: موقوف'),
        callback_data='toggle_private'))
    kb.add(types.InlineKeyboardButton(
        ('<tg-emoji emoji-id=\"6113825592975560832\">🟢</tg-emoji> المجموعات: مُفعّل' if grp_en else '<tg-emoji emoji-id=\"6116154779509985300\">🔴</tg-emoji> المجموعات: موقوف'),
        callback_data='toggle_groups'))
    kb.add(types.InlineKeyboardButton('<tg-emoji emoji-id=\"6113987307084190650\">❌</tg-emoji> إغلاق', callback_data='close_panel'))
    return kb

def cooldown_keyboard():
    kb = types.InlineKeyboardMarkup(row_width=2)
    s = get_settings()
    enabled = s.get('cooldown_enabled', True)
    kb.add(types.InlineKeyboardButton(
        f"{'<tg-emoji emoji-id=\"6114020073389692577\">🔴</tg-emoji> تعطيل Cooldown' if enabled else '<tg-emoji emoji-id=\"6116331543184020120\">🟢</tg-emoji> تفعيل Cooldown'}",
        callback_data='toggle_cooldown'))
    kb.add(types.InlineKeyboardButton('<tg-emoji emoji-id=\"6113942089668497853\">🕐</tg-emoji> تغيير الوقت (ساعات)', callback_data='set_cooldown_hours'))
    kb.add(types.InlineKeyboardButton('<tg-emoji emoji-id=\"6114087555915846958\">♾</tg-emoji> بدون وقت (تعطيل)', callback_data='cooldown_disable'))
    kb.add(types.InlineKeyboardButton('<tg-emoji emoji-id=\"6113875126833386131\">🔙</tg-emoji> رجوع', callback_data='back_to_panel'))
    return kb

def autolike_channel_keyboard():
                                                
    kb = types.InlineKeyboardMarkup(row_width=2)
    s = get_settings()
    ch = s.get('autolike_channel_id') or ''
    if ch:
        kb.add(types.InlineKeyboardButton('<tg-emoji emoji-id=\"6113926348613357755\">♻</tg-emoji> تغيير القناة', callback_data='set_autolike_channel'))
        kb.add(types.InlineKeyboardButton('<tg-emoji emoji-id=\"6113646419824874154\">🗑</tg-emoji> إزالة القناة', callback_data='remove_autolike_channel'))
        kb.add(types.InlineKeyboardButton('<tg-emoji emoji-id=\"6114095922512139382\">🧪</tg-emoji> اختبار الإرسال', callback_data='test_autolike_channel'))
    else:
        kb.add(types.InlineKeyboardButton('<tg-emoji emoji-id=\"6113823454081848116\">➕</tg-emoji> تعيين القناة', callback_data='set_autolike_channel'))
    kb.add(types.InlineKeyboardButton('<tg-emoji emoji-id=\"6115905027161723867\">🔙</tg-emoji> رجوع', callback_data='back_to_panel'))
    return kb

def _autolike_buy_keyboard():
                                                                  
    kb = types.InlineKeyboardMarkup()
    owner_user = (OWNER_USERNAME_1 or '').lstrip('@') or 'xCTx_AyOuB'
    kb.add(types.InlineKeyboardButton('<tg-emoji emoji-id=\"6113807747386446494\">🛒</tg-emoji> شراء - تواصل مع المالك',
                                      url=f'https://t.me/{owner_user}'))
    return kb

def autolike_keyboard():
    kb = types.InlineKeyboardMarkup(row_width=2)
    s = get_settings()
    enabled = s.get('autolike_enabled', True)
    kb.add(types.InlineKeyboardButton(
        f"{'<tg-emoji emoji-id=\"6116375149986979339\">🔴</tg-emoji> إيقاف Auto-Like' if enabled else '<tg-emoji emoji-id=\"6116434807082718394\">🟢</tg-emoji> تشغيل Auto-Like'}",
        callback_data='toggle_autolike'))
    kb.add(types.InlineKeyboardButton('<tg-emoji emoji-id=\"6113798032170422849\">🕔</tg-emoji> تغيير الوقت', callback_data='set_autolike_time'))
    kb.add(types.InlineKeyboardButton('<tg-emoji emoji-id=\"6115955617581503451\">➕</tg-emoji> إضافة UID + مدة', callback_data='autolike_add'))
    kb.add(types.InlineKeyboardButton('<tg-emoji emoji-id=\"6113779946063139126\">➖</tg-emoji> حذف UID', callback_data='autolike_remove'))
    kb.add(types.InlineKeyboardButton('<tg-emoji emoji-id=\"6113928466032235268\">📋</tg-emoji> عرض القائمة', callback_data='autolike_list'))
    kb.add(types.InlineKeyboardButton('<tg-emoji emoji-id=\"6116118139143984337\">🔙</tg-emoji> رجوع', callback_data='back_to_panel'))
    return kb

def _owner_panel_text():
    s = get_settings()
    status = '<tg-emoji emoji-id=\"6113699548570325974\">🔴</tg-emoji> موقوف' if s['maintenance_mode'] else '<tg-emoji emoji-id=\"6113684937091584843\">🟢</tg-emoji> يعمل'
    like_mode = '<tg-emoji emoji-id=\"6115940881548711252\">🌐</tg-emoji> API' if s.get('use_external_like_api', False) else '<tg-emoji emoji-id=\"6113948471989900276\">🏠</tg-emoji> Local'
    req_api = '<tg-emoji emoji-id=\"6114112148898583350\">✅</tg-emoji>' if s.get('require_points_api', True) else '<tg-emoji emoji-id=\"6113994453909772072\">❌</tg-emoji>'
    req_local = '<tg-emoji emoji-id=\"6116084191722476904\">✅</tg-emoji>' if s.get('require_points_local', False) else '<tg-emoji emoji-id=\"6115915850479309711\">❌</tg-emoji>'
    cd = f"{s.get('cooldown_hours', 7)}h ({'ON' if s.get('cooldown_enabled', True) else 'OFF'})"
    al = f"{s.get('autolike_hour', 5):02d}:{s.get('autolike_minute', 0):02d} ({'ON' if s.get('autolike_enabled', True) else 'OFF'}) / مدة افتراضية {AUTOLIKE_DEFAULT_DAYS} يوم"
    return (
        '<b><tg-emoji emoji-id=\"6113776583103747337\">🎛</tg-emoji> لوحة المالك</b>\n\n'
        f'<b>الحالة:</b> {status}\n'
        f'<b>وضع اللايك:</b> {like_mode}\n'
        f'<b>أمر اللايك:</b> <code>{s.get("like_command", "/like")}</code>\n\n'
        f'<b><tg-emoji emoji-id=\"6114154501571090045\">💰</tg-emoji> نقاط API:</b> {req_api}  (سعر: {s.get("points_required_api", 1)})\n'
        f'<b><tg-emoji emoji-id=\"6116332651285582453\">💰</tg-emoji> نقاط Local:</b> {req_local}  (سعر: {s.get("points_required_local", 1)})\n'
        f'<b><tg-emoji emoji-id=\"6113840006885807270\">⏱</tg-emoji> Cooldown:</b> {cd}\n'
        f'<b><tg-emoji emoji-id=\"6116219388703020383\">🤖</tg-emoji> Auto-Like:</b> {al}\n'
        f'<b><tg-emoji emoji-id=\"6113691641535534529\">📩</tg-emoji> الخاص:</b> {"<tg-emoji emoji-id=\"6114022469981443174\">🟢</tg-emoji> مُفعّل" if s.get("private_enabled", True) else "<tg-emoji emoji-id=\"6114185695918559996\">🔴</tg-emoji> موقوف"}\n'
        f'<b><tg-emoji emoji-id=\"6113700313074504581\">👥</tg-emoji> المجموعات:</b> {"<tg-emoji emoji-id=\"6114017431984805017\">🟢</tg-emoji> مُفعّل" if s.get("groups_enabled", True) else "<tg-emoji emoji-id=\"6114192984478062175\">🔴</tg-emoji> موقوف"}\n\n'
        '<b>المالكون:</b>\n'
        f'• {OWNER_USERNAME_1} (<code>{OWNER_ID_1}</code>)\n'
        f'• {OWNER_USERNAME_2} (<code>{OWNER_ID_2}</code>)'
    )

@bot.message_handler(commands=['owner'])
def owner_panel(msg):
    if not is_owner(msg.from_user.id):
        return bot.reply_to(msg, '<tg-emoji emoji-id=\"6114153406354429603\">⛔</tg-emoji> هذه اللوحة للمالك فقط.')
    bot.send_message(msg.chat.id, _owner_panel_text(),
                     reply_markup=owner_panel_keyboard(), parse_mode='HTML')

@bot.callback_query_handler(func=lambda call: is_owner(call.from_user.id))
def owner_callbacks(call):
    s = get_settings()
    data = call.data

    if data == 'toggle_maintenance':
        update_setting('maintenance_mode', not s['maintenance_mode'])
        bot.answer_callback_query(call.id, 'تم التبديل')
        return _refresh_panel(call)

    if data == 'toggle_private':
        update_setting('private_enabled', not s.get('private_enabled', True))
        bot.answer_callback_query(call.id, 'تم تبديل وضع الخاص')
        return _refresh_panel(call)

    if data == 'toggle_groups':
        update_setting('groups_enabled', not s.get('groups_enabled', True))
        bot.answer_callback_query(call.id, 'تم تبديل وضع المجموعات')
        return _refresh_panel(call)

    if data == 'toggle_like_source':
        update_setting('use_external_like_api', not s.get('use_external_like_api', False))
        bot.answer_callback_query(call.id, 'تم تبديل مصدر اللايك')
        return _refresh_panel(call)

    if data == 'toggle_points_api':
        update_setting('require_points_api', not s.get('require_points_api', True))
        bot.answer_callback_query(call.id, 'تم التبديل (API)')
        return _refresh_panel(call)

    if data == 'toggle_points_local':
        update_setting('require_points_local', not s.get('require_points_local', False))
        bot.answer_callback_query(call.id, 'تم التبديل (Local)')
        return _refresh_panel(call)

    if data == 'send_points':
        m = bot.send_message(call.message.chat.id,
            '<tg-emoji emoji-id=\"6113795047168152280\">💰</tg-emoji> أرسل: <code>USER_ID العدد</code>\n'
            'مثال: <code>123456789 50</code>\n'
            'أو سالب للخصم: <code>123456789 -10</code>',
            parse_mode='HTML')
        bot.register_next_step_handler(m, _process_send_points)
        return

    if data == 'list_points':
        all_pts = list_all_points()
        if not all_pts:
            text = '<tg-emoji emoji-id=\"6115911993598677568\">📋</tg-emoji> لا يوجد مستخدمون لديهم نقاط حالياً.'
        else:
            lines = ['<b><tg-emoji emoji-id=\"6116310437714727918\">📋</tg-emoji> رصيد المستخدمين:</b>', '']
            sorted_items = sorted(all_pts.items(), key=lambda x: -int(x[1]))
            for uid, pts in sorted_items[:50]:
                lines.append(f'• <code>{uid}</code> → <b>{pts}</b> نقطة')
            text = '\n'.join(lines)
        kb = types.InlineKeyboardMarkup()
        kb.add(types.InlineKeyboardButton('<tg-emoji emoji-id=\"6113815980838753459\">🔙</tg-emoji> رجوع', callback_data='back_to_panel'))
        return bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                     reply_markup=kb, parse_mode='HTML')

    if data == 'edit_point_cost':
        m = bot.send_message(call.message.chat.id,
            f'<tg-emoji emoji-id=\"6113848540985824266\">⚙</tg-emoji> أرسل: <code>api العدد</code> أو <code>local العدد</code>\n'
            f'مثال: <code>api 1</code>\n'
            f'الحالي: API={s.get("points_required_api", 1)}, Local={s.get("points_required_local", 1)}',
            parse_mode='HTML')
        bot.register_next_step_handler(m, _process_edit_point_cost)
        return

    if data == 'cooldown_menu':
        return bot.edit_message_text(
            f'<b><tg-emoji emoji-id=\"6113689438217310821\">⏱</tg-emoji> إعدادات Cooldown</b>\n\n'
            f'الحالة: {"تشغيل" if s.get("cooldown_enabled", True) else "إيقاف"}\n'
            f'الوقت الحالي: <b>{s.get("cooldown_hours", 7)}</b> ساعة\n\n'
            f'كل UID مستهدف يحصل على لايك مرة واحدة في هذه المدة.',
            call.message.chat.id, call.message.message_id,
            reply_markup=cooldown_keyboard(), parse_mode='HTML')

    if data == 'toggle_cooldown':
        update_setting('cooldown_enabled', not s.get('cooldown_enabled', True))
        bot.answer_callback_query(call.id, 'تم التبديل')
        return bot.edit_message_text(
            f'<b><tg-emoji emoji-id=\"6116286978603356999\">⏱</tg-emoji> إعدادات Cooldown</b>\n\n'
            f'الحالة: {"تشغيل" if get_settings().get("cooldown_enabled", True) else "إيقاف"}\n'
            f'الوقت الحالي: <b>{get_settings().get("cooldown_hours", 7)}</b> ساعة',
            call.message.chat.id, call.message.message_id,
            reply_markup=cooldown_keyboard(), parse_mode='HTML')

    if data == 'set_cooldown_hours':
        m = bot.send_message(call.message.chat.id,
            f'<tg-emoji emoji-id=\"6115953590356939544\">🕐</tg-emoji> أرسل عدد الساعات (مثال: <code>7</code>) أو <code>0</code> لإلغاء الكولداون.\n'
            f'الحالي: <b>{s.get("cooldown_hours", 7)}</b>',
            parse_mode='HTML')
        bot.register_next_step_handler(m, _process_set_cooldown)
        return

    if data == 'cooldown_disable':
        update_setting('cooldown_enabled', False)
        bot.answer_callback_query(call.id, 'تم تعطيل Cooldown (بدون وقت)')
        return bot.edit_message_text(
            '<tg-emoji emoji-id=\"6116239218567025507\">✅</tg-emoji> تم تعطيل Cooldown — يمكن إرسال اللايكات بدون انتظار.',
            call.message.chat.id, call.message.message_id,
            reply_markup=cooldown_keyboard(), parse_mode='HTML')

    if data == 'autolike_menu':
        lst = get_autolike_active_list()
        return bot.edit_message_text(
            f'<b><tg-emoji emoji-id=\"6114119875544749556\">🤖</tg-emoji> Auto-Like</b>\n\n'
            f'الحالة: {"ON" if s.get("autolike_enabled", True) else "OFF"}\n'
            f'الوقت اليومي: <b>{s.get("autolike_hour", 5):02d}:{s.get("autolike_minute", 0):02d}</b>\n'
            f'عدد الـ UIDs النشطة: <b>{len(lst)}</b>\n\n'
            f'كل UID يمكن إضافته مع مدة محددة، وكل يوم في الوقت المحدد يتم إرسال اللايكات تلقائياً إلى أن تنتهي مدته.',
            call.message.chat.id, call.message.message_id,
            reply_markup=autolike_keyboard(), parse_mode='HTML')

    if data == 'toggle_autolike':
        update_setting('autolike_enabled', not s.get('autolike_enabled', True))
        bot.answer_callback_query(call.id, 'تم التبديل')
        return bot.edit_message_text(
            f'<b><tg-emoji emoji-id=\"6113652711951963203\">🤖</tg-emoji> Auto-Like</b>\n\n'
            f'الحالة: {"ON" if get_settings().get("autolike_enabled", True) else "OFF"}\n'
            f'الوقت: <b>{get_settings().get("autolike_hour", 5):02d}:{get_settings().get("autolike_minute", 0):02d}</b>',
            call.message.chat.id, call.message.message_id,
            reply_markup=autolike_keyboard(), parse_mode='HTML')

    if data == 'set_autolike_time':
        m = bot.send_message(call.message.chat.id,
            f'<tg-emoji emoji-id=\"6115989917190330036\">🕔</tg-emoji> أرسل الوقت بصيغة <code>HH:MM</code> (مثال: <code>05:00</code>)\n'
            f'الحالي: <b>{s.get("autolike_hour", 5):02d}:{s.get("autolike_minute", 0):02d}</b>',
            parse_mode='HTML')
        bot.register_next_step_handler(m, _process_set_autolike_time)
        return

    if data == 'autolike_add':
        m = bot.send_message(call.message.chat.id,
            '<tg-emoji emoji-id=\"6113765721131456191\">➕</tg-emoji> أرسل UID لإضافته إلى Auto-Like.\n\nبعدها سيطلب منك مدة التفعيل بالأيام.\nمثال UID: <code>123456789</code>', parse_mode='HTML')
        bot.register_next_step_handler(m, _process_autolike_add)
        return

    if data == 'autolike_remove':
        m = bot.send_message(call.message.chat.id,
            '<tg-emoji emoji-id=\"6116444878781027101\">➖</tg-emoji> أرسل UID لحذفه من Auto-Like:')
        bot.register_next_step_handler(m, _process_autolike_remove)
        return

    if data == 'autolike_list':
        lst = get_autolike_active_list()
        if not lst:
            text = '<tg-emoji emoji-id=\"6113761116926513509\">📋</tg-emoji> القائمة فارغة.'
        else:
            lines = ['<b><tg-emoji emoji-id=\"6113825592975560832\">📋</tg-emoji> قائمة Auto-Like:</b>', '']
            for item in lst:
                uid = item.get('uid', '—')
                added_at = int(item.get('added_at') or 0)
                duration_days = int(item.get('duration_days') or 0)
                expires_at = int(item.get('expires_at') or 0)
                remaining_text = 'دائم' if expires_at <= 0 else format_remaining_detailed(max(0, expires_at - int(time.time())))
                expires_text = 'بدون انتهاء' if expires_at <= 0 else format_datetime_local(expires_at)
                lines.append(
                    f'<tg-emoji emoji-id=\"6116154779509985300\">🎮</tg-emoji> <code>{uid}</code>\n'
                    f'• <tg-emoji emoji-id=\"6113987307084190650\">📅</tg-emoji> أضيف في: <b>{format_datetime_local(added_at)}</b>\n'
                    f'• <tg-emoji emoji-id=\"6114020073389692577\">⏳</tg-emoji> المدة: <b>{format_autolike_duration(duration_days)}</b>\n'
                    f'• <tg-emoji emoji-id=\"6116331543184020120\">⌛</tg-emoji> المتبقي: <b>{remaining_text}</b>\n'
                    f'• <tg-emoji emoji-id=\"6113942089668497853\">🗓</tg-emoji> ينتهي في: <b>{expires_text}</b>\n'
                )
            text = '\n'.join(lines)
        kb = types.InlineKeyboardMarkup()
        kb.add(types.InlineKeyboardButton('<tg-emoji emoji-id=\"6114087555915846958\">🔙</tg-emoji> رجوع', callback_data='autolike_menu'))
        return bot.edit_message_text(text[:4000], call.message.chat.id, call.message.message_id,
                                     reply_markup=kb, parse_mode='HTML')

    if data == 'like_log':
        entries = get_like_log(30)
        if not entries:
            text = '<tg-emoji emoji-id=\"6113875126833386131\">📜</tg-emoji> السجل فارغ.'
        else:
            lines = ['<b><tg-emoji emoji-id=\"6113926348613357755\">📜</tg-emoji> آخر استخدامات اللايك:</b>', '']
            for e in entries:
                mark = '<tg-emoji emoji-id=\"6113646419824874154\">🤖</tg-emoji>' if e.get('mode') == 'autolike' else ('<tg-emoji emoji-id=\"6114095922512139382\">🌐</tg-emoji>' if e.get('mode') == 'api' else '<tg-emoji emoji-id=\"6113823454081848116\">🏠</tg-emoji>')
                user_part = (f"@{e['username']}" if e.get('username') and e['username'] not in ('AUTOLIKE','') else f"id:{e.get('user_id')}")
                lines.append(
                    f"{mark} <code>{e.get('time','')}</code>\n"
                    f"   <tg-emoji emoji-id=\"6115905027161723867\">👤</tg-emoji> {user_part}  →  🆔 <code>{e.get('target_uid','')}</code>  (+{e.get('likes_given',0)})"
                )
            text = '\n'.join(lines)
        kb = types.InlineKeyboardMarkup()
        kb.add(types.InlineKeyboardButton('<tg-emoji emoji-id=\"6113807747386446494\">🔙</tg-emoji> رجوع', callback_data='back_to_panel'))
        return bot.edit_message_text(text[:4000], call.message.chat.id, call.message.message_id,
                                     reply_markup=kb, parse_mode='HTML')

    if data == 'set_like_api_url':
        current_url = s.get('external_like_api_url', '') or ''
        masked = _mask_api_url(current_url)
        timeout_val = s.get('external_like_api_timeout', 120)
        m = bot.send_message(call.message.chat.id,
            '<tg-emoji emoji-id=\"6116375149986979339\">🔑</tg-emoji> <b>إعدادات رابط API</b>\n\n'
            f'<b>الحالي (مخفي):</b> <code>{masked}</code>\n'
            f'<b>Timeout:</b> <code>{timeout_val}s</code>\n\n'
            'أرسل الرابط الجديد. استخدم <code>{uid}</code> كـ placeholder.\n'
            'أرسل <code>cancel</code> للإلغاء، <code>show</code> لإظهار الحالي 30 ثانية،\n'
            '<code>timeout 180</code> لتغيير المهلة.',
            parse_mode='HTML')
        bot.register_next_step_handler(m, process_set_like_api_url)
        return

    if data == 'set_like_api_key':
        current_key = s.get('external_like_api_key', '') or ''
        masked_key = _mask_api_key(current_key)
        m = bot.send_message(call.message.chat.id,
            '<tg-emoji emoji-id=\"6116434807082718394\">🗝</tg-emoji> <b>إعدادات مفتاح API</b>\n\n'
            f'<b>الحالي (مخفي):</b> <code>{masked_key}</code>\n\n'
            'أرسل المفتاح الجديد. <code>cancel</code> للإلغاء، <code>show</code> لإظهاره، <code>clear</code> لمسحه.',
            parse_mode='HTML')
        bot.register_next_step_handler(m, process_set_like_api_key)
        return

    if data == 'edit_desc':
        m = bot.send_message(call.message.chat.id, '<tg-emoji emoji-id=\"6113798032170422849\">✏</tg-emoji> أرسل الوصف الجديد:')
        bot.register_next_step_handler(m, process_new_description)
        return

    if data == 'edit_help':
        m = bot.send_message(call.message.chat.id, '<tg-emoji emoji-id=\"6115955617581503451\">📝</tg-emoji> أرسل قالب رسالة المساعدة الجديد:')
        bot.register_next_step_handler(m, process_edit_help)
        return

    if data == 'edit_like_template':
        m = bot.send_message(call.message.chat.id,
            '<tg-emoji emoji-id=\"6113779946063139126\">❤</tg-emoji> أرسل قالب رد اللايك الجديد.\n'
            'متغيرات: {PlayerNickname}, {UID}, {LikesbeforeCommand}, {LikesafterCommand}, '
            '{LikesGivenByAPI}, {tokens_used}, {status}, {points_left}, {added_at}, {expires_at}, {remaining_time}, {duration_days}')
        bot.register_next_step_handler(m, process_edit_like_template)
        return

    if data == 'change_like':
        m = bot.send_message(call.message.chat.id,
            f"<tg-emoji emoji-id=\"6113928466032235268\">❤</tg-emoji> أرسل الأمر الجديد للايك (مثال: <code>/like</code>).\n"
            f"الحالي: <code>{s.get('like_command', '/like')}</code>", parse_mode='HTML')
        bot.register_next_step_handler(m, process_change_like)
        return

    if data == 'broadcast':
        m = bot.send_message(call.message.chat.id, '<tg-emoji emoji-id=\"6116118139143984337\">📢</tg-emoji> أرسل الرسالة للإذاعة:')
        bot.register_next_step_handler(m, process_broadcast)
        return

    if data == 'bot_status':
        text = (
            '<b><tg-emoji emoji-id=\"6113699548570325974\">📊</tg-emoji> حالة البوت</b>\n\n'
            f'الحالة: {"<tg-emoji emoji-id=\"6113684937091584843\">🔴</tg-emoji> موقوف" if s["maintenance_mode"] else "<tg-emoji emoji-id=\"6115940881548711252\">🟢</tg-emoji> يعمل"}\n'
            f'وضع اللايك: {"API" if s.get("use_external_like_api") else "Local"}\n'
            f'Cooldown: {"ON" if s.get("cooldown_enabled", True) else "OFF"} ({s.get("cooldown_hours", 7)}h)\n'
            f'Auto-Like: {"ON" if s.get("autolike_enabled", True) else "OFF"} '
            f'({s.get("autolike_hour", 5):02d}:{s.get("autolike_minute", 0):02d})\n'
            f'عدد UIDs النشطة في Auto-Like: {len(get_autolike_active_list())}'
        )
        kb = types.InlineKeyboardMarkup()
        kb.add(types.InlineKeyboardButton('<tg-emoji emoji-id=\"6113948471989900276\">🔙</tg-emoji> رجوع', callback_data='back_to_panel'))
        return bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                     reply_markup=kb, parse_mode='HTML')

                                              
    if data == 'autolike_channel':
        cur_id = s.get('autolike_channel_id') or ''
        cur_title = s.get('autolike_channel_title') or ''
        if cur_id:
            cur_text = (f'<b><tg-emoji emoji-id=\"6114112148898583350\">📡</tg-emoji> القناة الحالية:</b>\n'
                        f'• الاسم: <b>{cur_title or "—"}</b>\n'
                        f'• المعرف: <code>{cur_id}</code>\n\n'
                        f'سيتم إرسال كل رسائل الأوتو لايك إلى هذه القناة\n'
                        f'مع زر <b><tg-emoji emoji-id=\"6113994453909772072\">🛒</tg-emoji> شراء - تواصل مع المالك</b> أسفل الرسالة.')
        else:
            cur_text = ('<b><tg-emoji emoji-id=\"6116084191722476904\">📡</tg-emoji> لم يتم تعيين قناة بعد.</b>\n\n'
                        'اضغط <b><tg-emoji emoji-id=\"6115915850479309711\">➕</tg-emoji> تعيين القناة</b> ثم أرسل:\n'
                        '• معرف القناة الرقمي مثل <code>-1001234567890</code>\n'
                        '• أو يوزر القناة مثل <code>@MyChannel</code>\n\n'
                        '<tg-emoji emoji-id=\"6113776583103747337\">⚠</tg-emoji> يجب أن يكون البوت <b>مشرفاً</b> في القناة لإرسال الرسائل.')
        return bot.edit_message_text(cur_text, call.message.chat.id, call.message.message_id,
                                     reply_markup=autolike_channel_keyboard(), parse_mode='HTML')

    if data == 'set_autolike_channel':
        m = bot.send_message(call.message.chat.id,
            '<tg-emoji emoji-id=\"6114154501571090045\">📡</tg-emoji> أرسل الآن:\n'
            '• معرف القناة الرقمي مثل <code>-1001234567890</code>\n'
            '• أو يوزر القناة مثل <code>@MyChannel</code>\n\n'
            '<tg-emoji emoji-id=\"6116332651285582453\">⚠</tg-emoji> تأكد أن البوت <b>مشرف</b> في القناة.',
            parse_mode='HTML')
        bot.register_next_step_handler(m, _process_set_autolike_channel)
        return

    if data == 'remove_autolike_channel':
        update_setting('autolike_channel_id', '')
        update_setting('autolike_channel_title', '')
        bot.answer_callback_query(call.id, '<tg-emoji emoji-id=\"6113840006885807270\">🗑</tg-emoji> تم إزالة القناة')
        return bot.edit_message_text(
            '<b><tg-emoji emoji-id=\"6116219388703020383\">✅</tg-emoji> تم إزالة قناة الأوتو لايك.</b>\n\nلن يتم إرسال رسائل الأوتو لايك لأي قناة الآن.',
            call.message.chat.id, call.message.message_id,
            reply_markup=autolike_channel_keyboard(), parse_mode='HTML')

    if data == 'test_autolike_channel':
        ch_id = (s.get('autolike_channel_id') or '').strip()
        if not ch_id:
            return bot.answer_callback_query(call.id, '<tg-emoji emoji-id=\"6113691641535534529\">⚠</tg-emoji> لا توجد قناة معينة', show_alert=True)
        try:
            target = int(ch_id) if (ch_id.lstrip('-').isdigit()) else ch_id
            bot.send_message(target,
                '<tg-emoji emoji-id=\"6114022469981443174\">🧪</tg-emoji> <b>اختبار قناة الأوتو لايك</b>\n\nهذه رسالة تجريبية. سيتم نشر رسائل الأوتو لايك هنا تلقائياً.',
                parse_mode='HTML', reply_markup=_autolike_buy_keyboard(),
                disable_web_page_preview=True)
            bot.answer_callback_query(call.id, '<tg-emoji emoji-id=\"6114185695918559996\">✅</tg-emoji> تم الإرسال للقناة')
        except Exception as e:
            bot.answer_callback_query(call.id, f'<tg-emoji emoji-id=\"6113700313074504581\">❌</tg-emoji> فشل: {str(e)[:120]}', show_alert=True)
        return

    if data == 'back_to_panel':
        return _refresh_panel(call)

    if data == 'close_panel':
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception:
            pass
        return bot.answer_callback_query(call.id, 'تم الإغلاق')

def _refresh_panel(call):
    try:
        bot.edit_message_text(_owner_panel_text(), call.message.chat.id, call.message.message_id,
                              reply_markup=owner_panel_keyboard(), parse_mode='HTML')
    except Exception:
        pass

def _process_send_points(msg):
    if not is_owner(msg.from_user.id):
        return
    try:
        parts = (msg.text or '').strip().split()
        if len(parts) != 2:
            return bot.reply_to(msg, '<tg-emoji emoji-id=\"6114017431984805017\">❌</tg-emoji> الصيغة: <code>USER_ID العدد</code>')
        target = int(parts[0])
        amount = int(parts[1])
        new_bal = add_user_points(target, amount)
        bot.reply_to(msg,
            f'<tg-emoji emoji-id=\"6114192984478062175\">✅</tg-emoji> تم.\n'
            f'<b>المستخدم:</b> <code>{target}</code>\n'
            f'<b>التعديل:</b> {"+" if amount >= 0 else ""}{amount}\n'
            f'<b>الرصيد الحالي:</b> <b>{new_bal}</b> نقطة',
            parse_mode='HTML')
                     
        try:
            if amount > 0:
                bot.send_message(target,
                    f'<tg-emoji emoji-id=\"6114153406354429603\">🎉</tg-emoji> تم شحن رصيدك بـ <b>{amount}</b> نقطة!\n'
                    f'<b>رصيدك الحالي:</b> <b>{new_bal}</b> نقطة',
                    parse_mode='HTML')
            elif amount < 0:
                bot.send_message(target,
                    f'<tg-emoji emoji-id=\"6113795047168152280\">⚠</tg-emoji> تم خصم <b>{abs(amount)}</b> نقطة من رصيدك.\n'
                    f'<b>رصيدك الحالي:</b> <b>{new_bal}</b> نقطة',
                    parse_mode='HTML')
        except Exception:
            pass
    except ValueError:
        bot.reply_to(msg, '<tg-emoji emoji-id=\"6115911993598677568\">❌</tg-emoji> صيغة غير صحيحة. مثال: <code>123456789 50</code>', parse_mode='HTML')
    except Exception as e:
        bot.reply_to(msg, f'<tg-emoji emoji-id=\"6116310437714727918\">❌</tg-emoji> خطأ: {str(e)[:120]}')

def _process_edit_point_cost(msg):
    if not is_owner(msg.from_user.id):
        return
    try:
        parts = (msg.text or '').strip().lower().split()
        if len(parts) != 2:
            return bot.reply_to(msg, '<tg-emoji emoji-id=\"6113815980838753459\">❌</tg-emoji> الصيغة: <code>api 1</code> أو <code>local 1</code>', parse_mode='HTML')
        mode, n = parts[0], int(parts[1])
        if n < 0:
            return bot.reply_to(msg, '<tg-emoji emoji-id=\"6113848540985824266\">❌</tg-emoji> يجب أن يكون رقماً موجباً.')
        if mode == 'api':
            update_setting('points_required_api', n)
            bot.reply_to(msg, f'<tg-emoji emoji-id=\"6113689438217310821\">✅</tg-emoji> سعر API = <b>{n}</b> نقطة لكل لايك.', parse_mode='HTML')
        elif mode == 'local':
            update_setting('points_required_local', n)
            bot.reply_to(msg, f'<tg-emoji emoji-id=\"6116286978603356999\">✅</tg-emoji> سعر Local = <b>{n}</b> نقطة لكل لايك.', parse_mode='HTML')
        else:
            bot.reply_to(msg, '<tg-emoji emoji-id=\"6115953590356939544\">❌</tg-emoji> النوع يجب أن يكون api أو local.')
    except Exception as e:
        bot.reply_to(msg, f'<tg-emoji emoji-id=\"6116239218567025507\">❌</tg-emoji> خطأ: {str(e)[:120]}')

def _process_set_cooldown(msg):
    if not is_owner(msg.from_user.id):
        return
    try:
        v = float((msg.text or '').strip())
        if v <= 0:
            update_setting('cooldown_enabled', False)
            update_setting('cooldown_hours', 0)
            return bot.reply_to(msg, '<tg-emoji emoji-id=\"6114119875544749556\">✅</tg-emoji> تم تعطيل Cooldown (بدون وقت).')
        update_setting('cooldown_hours', v)
        update_setting('cooldown_enabled', True)
        bot.reply_to(msg, f'<tg-emoji emoji-id=\"6113652711951963203\">✅</tg-emoji> Cooldown = <b>{v}</b> ساعة.', parse_mode='HTML')
    except Exception:
        bot.reply_to(msg, '<tg-emoji emoji-id=\"6115989917190330036\">❌</tg-emoji> رقم غير صالح.')

def _process_set_autolike_channel(msg):
                                                                       
    if not is_owner(msg.from_user.id):
        return
    raw = (msg.text or '').strip()
    if not raw:
        return bot.reply_to(msg, '<tg-emoji emoji-id=\"6113765721131456191\">❌</tg-emoji> لم يتم إرسال أي شيء.')
                                                  
    ch_input = raw
    if ch_input.startswith('https://t.me/'):
        ch_input = '@' + ch_input.replace('https://t.me/', '').split('/')[0]
    if not ch_input.startswith('@') and not ch_input.lstrip('-').isdigit():
        return bot.reply_to(msg,
            '<tg-emoji emoji-id=\"6116444878781027101\">❌</tg-emoji> صيغة غير صحيحة.\n'
            'استخدم <code>-1001234567890</code> أو <code>@MyChannel</code>',
            parse_mode='HTML')
                                                                  
    try:
        target = int(ch_input) if ch_input.lstrip('-').isdigit() else ch_input
        chat_info = bot.get_chat(target)
        title = getattr(chat_info, 'title', None) or getattr(chat_info, 'username', None) or str(target)
                                  
        bot.send_message(target,
            '<tg-emoji emoji-id=\"6113761116926513509\">✅</tg-emoji> <b>تم تعيين هذه القناة لاستقبال رسائل الأوتو لايك.</b>\n\n'
            'سيتم نشر كل رسائل الأوتو لايك هنا تلقائياً.',
            parse_mode='HTML', reply_markup=_autolike_buy_keyboard(),
            disable_web_page_preview=True)
        update_setting('autolike_channel_id', str(target))
        update_setting('autolike_channel_title', str(title))
        bot.reply_to(msg,
            f'<tg-emoji emoji-id=\"6113825592975560832\">✅</tg-emoji> <b>تم ربط القناة بنجاح!</b>\n\n'
            f'<tg-emoji emoji-id=\"6116154779509985300\">📡</tg-emoji> الاسم: <b>{title}</b>\n'
            f'🆔 المعرف: <code>{target}</code>\n\n'
            f'كل رسالة أوتو لايك ستصل لك ستُرسل أيضاً للقناة\n'
            f'مع زر <b><tg-emoji emoji-id=\"6113987307084190650\">🛒</tg-emoji> شراء - تواصل مع المالك</b>.',
            parse_mode='HTML')
    except Exception as e:
        bot.reply_to(msg,
            f'<tg-emoji emoji-id=\"6114020073389692577\">❌</tg-emoji> <b>فشل ربط القناة:</b>\n<code>{str(e)[:200]}</code>\n\n'
            f'تأكد من:\n'
            f'• أن البوت <b>مشرف</b> في القناة\n'
            f'• أن المعرف/اليوزر صحيح\n'
            f'• إذا كانت القناة خاصة، استخدم المعرف الرقمي',
            parse_mode='HTML')

def _process_set_autolike_time(msg):
    if not is_owner(msg.from_user.id):
        return
    try:
        text = (msg.text or '').strip()
        if ':' not in text:
            return bot.reply_to(msg, '<tg-emoji emoji-id=\"6116331543184020120\">❌</tg-emoji> الصيغة: <code>HH:MM</code>', parse_mode='HTML')
        h, m = text.split(':', 1)
        h, m = int(h), int(m)
        if not (0 <= h <= 23) or not (0 <= m <= 59):
            return bot.reply_to(msg, '<tg-emoji emoji-id=\"6113942089668497853\">❌</tg-emoji> ساعات 0-23، دقائق 0-59.')
        update_setting('autolike_hour', h)
        update_setting('autolike_minute', m)
        bot.reply_to(msg, f'<tg-emoji emoji-id=\"6114087555915846958\">✅</tg-emoji> وقت Auto-Like = <b>{h:02d}:{m:02d}</b>', parse_mode='HTML')
    except Exception:
        bot.reply_to(msg, '<tg-emoji emoji-id=\"6113875126833386131\">❌</tg-emoji> صيغة غير صحيحة.')

_pending_autolike_uid = {}


def _process_autolike_add(msg):
    if not is_owner(msg.from_user.id):
        return
    uid = (msg.text or '').strip()
    if not uid.isdigit():
        return bot.reply_to(msg, '<tg-emoji emoji-id=\"6113926348613357755\">❌</tg-emoji> UID يجب أن يكون رقماً.')
    _pending_autolike_uid[msg.chat.id] = uid
    m = bot.reply_to(
        msg,
        '<tg-emoji emoji-id=\"6113646419824874154\">📅</tg-emoji> الآن أرسل مدة التفعيل لهذا الـ UID بالأيام.\n\n'
        f'• UID: <code>{uid}</code>\n'
        f'• مثال: <code>30</code>\n'
        f'• أرسل <code>0</code> إذا أردته دائم بدون انتهاء',
        parse_mode='HTML'
    )
    bot.register_next_step_handler(m, _process_autolike_duration)


def _process_autolike_duration(msg):
    if not is_owner(msg.from_user.id):
        return
    uid = _pending_autolike_uid.pop(msg.chat.id, None)
    if not uid:
        return bot.reply_to(msg, '<tg-emoji emoji-id=\"6114095922512139382\">❌</tg-emoji> انتهت العملية. أعد إضافة الـ UID من جديد.')
    text = (msg.text or '').strip()
    if not text.isdigit():
        return bot.reply_to(msg, '<tg-emoji emoji-id=\"6113823454081848116\">❌</tg-emoji> المدة يجب أن تكون رقماً صحيحاً بالأيام.')
    duration_days = max(0, int(text))
    added, entry = add_autolike_uid(uid, duration_days)
    if not added:
        return bot.reply_to(msg, '<tg-emoji emoji-id=\"6115905027161723867\">⚠</tg-emoji> هذا الـ UID موجود بالفعل.')
    expires_at = int((entry or {}).get('expires_at') or 0)
    added_text = format_datetime_local((entry or {}).get('added_at'))
    expires_text = 'بدون انتهاء' if expires_at <= 0 else format_datetime_local(expires_at)
    bot.reply_to(
        msg,
        '<tg-emoji emoji-id=\"6113807747386446494\">✅</tg-emoji> <b>تمت إضافة الـ UID إلى Auto-Like بنجاح</b>\n\n'
        f'🆔 <b>الايدي:</b> <code>{uid}</code>\n'
        f'<tg-emoji emoji-id=\"6116375149986979339\">📅</tg-emoji> <b>تاريخ الإضافة:</b> <b>{added_text}</b>\n'
        f'<tg-emoji emoji-id=\"6116434807082718394\">⏳</tg-emoji> <b>المدة:</b> <b>{format_autolike_duration(duration_days)}</b>\n'
        f'<tg-emoji emoji-id=\"6113798032170422849\">🗓</tg-emoji> <b>ينتهي في:</b> <b>{expires_text}</b>\n\n'
        f'<tg-emoji emoji-id=\"6115955617581503451\">🤖</tg-emoji> سيتم إرسال اللايكات يومياً في الوقت المحدد طالما أن المدة لم تنتهِ.',
        parse_mode='HTML'
    )


def _process_autolike_remove(msg):
    if not is_owner(msg.from_user.id):
        return
    uid = (msg.text or '').strip()
    if remove_autolike_uid(uid):
        bot.reply_to(msg, f'<tg-emoji emoji-id=\"6113779946063139126\">✅</tg-emoji> تم حذف <code>{uid}</code> من Auto-Like.', parse_mode='HTML')
    else:
        bot.reply_to(msg, '<tg-emoji emoji-id=\"6113928466032235268\">⚠</tg-emoji> غير موجود في القائمة.')

def _mask_api_key(key):
    try:
        if not key:
            return '(not set)'
        k = str(key)
        if len(k) <= 4:
            return '****'
        if len(k) <= 10:
            return k[:2] + '****' + k[-2:]
        return k[:3] + '****' + k[-3:]
    except Exception:
        return '****'

def process_set_like_api_key(msg):
    if not is_owner(msg.from_user.id):
        return
    try:
        text = (msg.text or '').strip()
        if not text or text.lower() == 'cancel':
            try: bot.delete_message(msg.chat.id, msg.message_id)
            except Exception: pass
            return bot.send_message(msg.chat.id, '<tg-emoji emoji-id=\"6116118139143984337\">❎</tg-emoji> تم الإلغاء.')
        if text.lower() == 'show':
            current_key = get_settings().get('external_like_api_key', '') or '(not set)'
            try: bot.delete_message(msg.chat.id, msg.message_id)
            except Exception: pass
            warn = bot.send_message(msg.chat.id,
                f'<tg-emoji emoji-id=\"6113699548570325974\">🔐</tg-emoji> <b>المفتاح (سيُحذف بعد 30 ثانية):</b>\n<code>{current_key}</code>',
                parse_mode='HTML')
            def _del_key():
                try: time.sleep(30); bot.delete_message(warn.chat.id, warn.message_id)
                except Exception: pass
            threading.Thread(target=_del_key, daemon=True).start()
            return
        if text.lower() == 'clear':
            update_setting('external_like_api_key', '')
            try: bot.delete_message(msg.chat.id, msg.message_id)
            except Exception: pass
            return bot.send_message(msg.chat.id, '<tg-emoji emoji-id=\"6113684937091584843\">🧹</tg-emoji> تم مسح المفتاح.')
        update_setting('external_like_api_key', text)
        try: bot.delete_message(msg.chat.id, msg.message_id)
        except Exception: pass
        bot.send_message(msg.chat.id, f'<tg-emoji emoji-id=\"6115940881548711252\">✅</tg-emoji> تم تحديث المفتاح: <code>{_mask_api_key(text)}</code>', parse_mode='HTML')
    except Exception as e:
        bot.reply_to(msg, f'<tg-emoji emoji-id=\"6113948471989900276\">❌</tg-emoji> خطأ: {str(e)[:120]}')

def process_set_like_api_url(msg):
    if not is_owner(msg.from_user.id):
        return
    try:
        text = (msg.text or '').strip()
        if not text or text.lower() == 'cancel':
            try: bot.delete_message(msg.chat.id, msg.message_id)
            except Exception: pass
            return bot.send_message(msg.chat.id, '<tg-emoji emoji-id=\"6114112148898583350\">❎</tg-emoji> تم الإلغاء.')
        if text.lower() == 'show':
            current_url = get_settings().get('external_like_api_url', '') or '(not set)'
            try: bot.delete_message(msg.chat.id, msg.message_id)
            except Exception: pass
            warn = bot.send_message(msg.chat.id,
                f'<tg-emoji emoji-id=\"6113994453909772072\">🔐</tg-emoji> <b>الرابط (سيُحذف بعد 30 ثانية):</b>\n<code>{current_url}</code>',
                parse_mode='HTML')
            def _del():
                try: time.sleep(30); bot.delete_message(warn.chat.id, warn.message_id)
                except Exception: pass
            threading.Thread(target=_del, daemon=True).start()
            return
        if text.lower().startswith('timeout'):
            parts = text.split()
            if len(parts) >= 2 and parts[1].isdigit():
                v = max(5, min(600, int(parts[1])))
                update_setting('external_like_api_timeout', v)
                try: bot.delete_message(msg.chat.id, msg.message_id)
                except Exception: pass
                return bot.send_message(msg.chat.id, f'<tg-emoji emoji-id=\"6116084191722476904\">✅</tg-emoji> Timeout = <b>{v}s</b>', parse_mode='HTML')
            return bot.reply_to(msg, '<tg-emoji emoji-id=\"6115915850479309711\">❌</tg-emoji> مثال: <code>timeout 120</code>', parse_mode='HTML')
        if not (text.startswith('http://') or text.startswith('https://')):
            return bot.reply_to(msg, '<tg-emoji emoji-id=\"6113776583103747337\">❌</tg-emoji> يجب أن يبدأ بـ http(s)://')
        update_setting('external_like_api_url', text)
        try: bot.delete_message(msg.chat.id, msg.message_id)
        except Exception: pass
        bot.send_message(msg.chat.id, f'<tg-emoji emoji-id=\"6114154501571090045\">✅</tg-emoji> تم تحديث الرابط.\n<code>{_mask_api_url(text)}</code>', parse_mode='HTML')
    except Exception as e:
        bot.reply_to(msg, f'<tg-emoji emoji-id=\"6116332651285582453\">❌</tg-emoji> خطأ: {str(e)[:120]}')

def process_new_description(msg):
    if not is_owner(msg.from_user.id): return
    update_setting('bot_description', msg.text)
    bot.reply_to(msg, '<tg-emoji emoji-id=\"6113840006885807270\">✅</tg-emoji> تم تحديث الوصف.')

def process_edit_help(msg):
    if not is_owner(msg.from_user.id): return
    update_setting('help_message_template', msg.text)
    bot.reply_to(msg, '<tg-emoji emoji-id=\"6116219388703020383\">✅</tg-emoji> تم تحديث رسالة المساعدة.')

def process_edit_like_template(msg):
    if not is_owner(msg.from_user.id): return
    update_setting('like_response_template', msg.text)
    bot.reply_to(msg, '<tg-emoji emoji-id=\"6113691641535534529\">✅</tg-emoji> تم تحديث قالب رد اللايك.')

def process_broadcast(msg):
    if not is_owner(msg.from_user.id): return
    text = msg.text or ''
    sent = 0
    failed = 0
                                                                            
    all_users = list_all_points()
    for uid in all_users.keys():
        try:
            bot.send_message(int(uid), text, parse_mode='HTML')
            sent += 1
        except Exception:
            failed += 1
    bot.reply_to(msg, f'<tg-emoji emoji-id=\"6114022469981443174\">📢</tg-emoji> تم الإرسال إلى <b>{sent}</b> مستخدم (فشل {failed}).', parse_mode='HTML')

def process_change_like(msg):
    if not is_owner(msg.from_user.id): return
    new_cmd = (msg.text or '').strip()
    if not new_cmd:
        return bot.reply_to(msg, '<tg-emoji emoji-id=\"6114185695918559996\">❌</tg-emoji> أمر غير صالح.')
    update_setting('like_command', new_cmd)
    bot.reply_to(msg, f'<tg-emoji emoji-id=\"6113700313074504581\">✅</tg-emoji> أمر اللايك: <code>{new_cmd}</code>', parse_mode='HTML')

def _sanitize_error_text(text):
    try:
        import re as _re_s
        return _re_s.sub(r'https?://\S+', '[hidden]', str(text))
    except Exception:
        return '[error]'

def _send_insufficient_balance_message(msg, points_needed, points_have):
    text = (
        '<blockquote><b><tg-emoji emoji-id=\"6114017431984805017\">⛔</tg-emoji> رصيدك غير كافٍ!</b></blockquote>\n\n'
        '<blockquote>'
        f'<b>المطلوب:</b> <b>{points_needed}</b> نقطة\n'
        f'<b>رصيدك الحالي:</b> <b>{points_have}</b> نقطة\n\n'
        '<tg-emoji emoji-id=\"6114192984478062175\">🛒</tg-emoji> <b>لشراء النقاط، تواصل مع أحد المالكين:</b>\n'
        f'• <b>{OWNER_USERNAME_1}</b>\n'
        f'• <b>{OWNER_USERNAME_2}</b>'
        '</blockquote>\n\n'
        '<b>استخدم الأمر</b> <code>/buy</code> <b>لعرض معلومات الشراء.</b>'
    )
    try:
        bot.reply_to(msg, text, parse_mode='HTML')
    except Exception:
        bot.send_message(msg.chat.id, text, parse_mode='HTML')

def _handle_like_logic(msg):
                                                          
    try:
        parts = (msg.text or '').strip().split()
        if len(parts) < 2:
            return bot.reply_to(msg,
                f"<tg-emoji emoji-id=\"6114153406354429603\">❌</tg-emoji> الاستخدام: <code>{get_settings().get('like_command', '/like')} UID</code>",
                parse_mode='HTML')
        uid = parts[1]
        if not uid.isdigit():
            return bot.reply_to(msg, '<tg-emoji emoji-id=\"6113795047168152280\">❌</tg-emoji> UID يجب أن يكون رقماً.', parse_mode='HTML')

        settings_now = get_settings()
                                           
        if settings_now.get('maintenance_mode') and not is_owner(msg.from_user.id):
            return bot.reply_to(msg, '<tg-emoji emoji-id=\"6115911993598677568\">⛔</tg-emoji> البوت متوقف حالياً.')

        chat_type = getattr(msg.chat, 'type', 'private')
        if not is_owner(msg.from_user.id):
            if chat_type == 'private' and not settings_now.get('private_enabled', True):
                return bot.reply_to(msg, '<tg-emoji emoji-id=\"6116310437714727918\">⛔</tg-emoji> البوت موقوف في المحادثات الخاصة حالياً.\nتواصل مع المالك.')
            if chat_type in ('group', 'supergroup') and not settings_now.get('groups_enabled', True):
                return bot.reply_to(msg, '<tg-emoji emoji-id=\"6113815980838753459\">⛔</tg-emoji> البوت موقوف في المجموعات حالياً.\nتواصل مع المالك.')

        if not is_owner(msg.from_user.id):
            remaining = get_cooldown_remaining(uid)
            if remaining > 0:
                return bot.reply_to(msg,
                    f'<tg-emoji emoji-id=\"6113848540985824266\">⏱</tg-emoji> هذا الـ UID تم إعجابه مؤخراً.\n'
                    f'<b>المتبقي:</b> <code>{format_remaining(remaining)}</code>\n'
                    f'كل UID يمكن إضافة لايكات له مرة واحدة كل '
                    f'<b>{settings_now.get("cooldown_hours", 7)}</b> ساعة.',
                    parse_mode='HTML')

        use_api = bool(settings_now.get('use_external_like_api', False))
                                       
        if use_api:
            require_points = bool(settings_now.get('require_points_api', True))
            cost = int(settings_now.get('points_required_api', 1))
        else:
            require_points = bool(settings_now.get('require_points_local', False))
            cost = int(settings_now.get('points_required_local', 1))

        if require_points and not is_owner(msg.from_user.id):
            have = get_user_points(msg.from_user.id)
            if have < cost:
                return _send_insufficient_balance_message(msg, cost, have)

        processing_msg = None
        if use_api:
            try:
                processing_msg = bot.reply_to(msg,
                    '<tg-emoji emoji-id=\"6113689438217310821\">⏳</tg-emoji> <b>جاري إرسال الإعجابات عبر API...</b>\n<i>قد يستغرق دقيقة أو أكثر.</i>',
                    parse_mode='HTML')
            except Exception:
                processing_msg = None
            data = do_like_external_api(uid)
        else:
            data = do_like(uid)

        if processing_msg is not None:
            try: bot.delete_message(processing_msg.chat.id, processing_msg.message_id)
            except Exception: pass

        if not isinstance(data, dict) or 'error' in data:
            err = _sanitize_error_text((data or {}).get('error', 'Unknown error'))
            return bot.reply_to(msg, f'<tg-emoji emoji-id=\"6116286978603356999\">❌</tg-emoji> خطأ: {err}', parse_mode='HTML')

        def _pick(*keys, default='N/A'):
            for k in keys:
                if k in data and data[k] not in (None, ''):
                    return data[k]
            return default

        player_nickname = _pick('PlayerNickname','PlayerName','nickname','Nickname','username', default='Unknown')
        player_uid = _pick('UID','uid','PlayerUID', default=uid)
        likes_before = _pick('LikesbeforeCommand','LikesBefore','likes_before','BeforeLikes', default=0)
        likes_after = _pick('LikesafterCommand','LikesAfter','likes_after','AfterLikes', default=0)
        likes_given = _pick('LikesGivenByAPI','LikesGiven','likes_given','GivenLikes', default=0)
        tokens_used = _pick('tokens_used','TokensUsed','SuccessfulRequests','successful_requests', default=0)
        status_val = _pick('status','Status', default='N/A')
        try:
            if (likes_given in (0,'0',None) or likes_given == 'N/A') and likes_before != 'N/A' and likes_after != 'N/A':
                diff = int(likes_after) - int(likes_before)
                if diff > 0: likes_given = diff
        except Exception:
            pass

        points_left = get_user_points(msg.from_user.id)
        try:
            given_int = int(likes_given or 0)
        except Exception:
            given_int = 0

        if require_points and not is_owner(msg.from_user.id) and given_int > 0:
            ok, points_left = deduct_user_points(msg.from_user.id, cost)
            if not ok:
                                                                        
                return _send_insufficient_balance_message(msg, cost, points_left)

        if given_int > 0:
            mark_cooldown(uid)
            log_like_usage(msg.from_user.id, msg.from_user.username, uid, given_int,
                           'api' if use_api else 'local')
                                                
            try:
                user_part = (f"@{msg.from_user.username}" if msg.from_user.username
                             else f"id:{msg.from_user.id}")
                for oid in OWNERS:
                    try:
                        bot.send_message(oid,
                            f'<tg-emoji emoji-id=\"6115953590356939544\">❤</tg-emoji> <b>لايك جديد</b>\n'
                            f'<tg-emoji emoji-id=\"6116239218567025507\">👤</tg-emoji> المستخدم: {user_part} (<code>{msg.from_user.id}</code>)\n'
                            f'🆔 UID: <code>{uid}</code>\n'
                            f'<tg-emoji emoji-id=\"6114119875544749556\">➕</tg-emoji> إضافة: <code>{given_int}</code>\n'
                            f'<tg-emoji emoji-id=\"6113652711951963203\">⚙</tg-emoji> الوضع: {"API" if use_api else "Local"}',
                            parse_mode='HTML')
                    except Exception:
                        pass
            except Exception:
                pass

        template = settings_now.get('like_response_template', DEFAULT_SETTINGS['like_response_template'])
        fmt = {
            'PlayerNickname': player_nickname, 'UID': player_uid,
            'LikesbeforeCommand': likes_before, 'LikesafterCommand': likes_after,
            'LikesGivenByAPI': likes_given, 'tokens_used': tokens_used, 'status': status_val,
            'PlayerName': player_nickname, 'LikesBefore': likes_before, 'LikesAfter': likes_after,
            'LikesGiven': likes_given, 'likes_before': likes_before, 'likes_after': likes_after,
            'likes_given': likes_given, 'TokensUsed': tokens_used, 'SuccessfulRequests': tokens_used,
            'Status': status_val, 'uid': player_uid, 'nickname': player_nickname,
            'points_left': points_left,
            'added_at': '', 'expires_at': '', 'remaining_time': '', 'duration_days': '',
        }

        class _SafeDict(dict):
            def __missing__(self, key):
                return '{' + key + '}'

        text = template.format_map(_SafeDict(fmt))
        bot.reply_to(msg, text, parse_mode='HTML')
    except Exception as e:
        bot.reply_to(msg, f'<tg-emoji emoji-id=\"6115989917190330036\">❌</tg-emoji> خطأ: {str(e)[:200]}')

@bot.message_handler(commands=['like'])
def like_command(msg):
    _handle_like_logic(msg)

@bot.message_handler(commands=['points', 'balance', 'rasid'])
def points_command(msg):
    pts = get_user_points(msg.from_user.id)
    s = get_settings()
    text = (
        '<blockquote><b><tg-emoji emoji-id=\"6113765721131456191\">💰</tg-emoji> رصيد النقاط</b></blockquote>\n\n'
        '<blockquote>'
        f'<b>اسم المستخدم:</b> <b>@{msg.from_user.username or "—"}</b>\n'
        f'<b>معرفك:</b> <code>{msg.from_user.id}</code>\n'
        f'<b>رصيدك:</b> <b>{pts}</b> نقطة\n\n'
        f'<tg-emoji emoji-id=\"6116444878781027101\">💵</tg-emoji> <b>سعر اللايك:</b>\n'
        f'• <b>Local:</b> <b>{s.get("points_required_local", 1)}</b> نقطة\n'
        f'• <b>API:</b> <b>{s.get("points_required_api", 1)}</b> نقطة'
        '</blockquote>\n\n'
        '<tg-emoji emoji-id=\"6113761116926513509\">🛒</tg-emoji> <b>لشراء النقاط:</b> <code>/buy</code>'
    )
    bot.reply_to(msg, text, parse_mode='HTML')

@bot.message_handler(commands=['buy', 'shop', 'shira'])
def buy_command(msg):
    text = (
        '<blockquote><b><tg-emoji emoji-id=\"6113825592975560832\">🛒</tg-emoji> شراء النقاط</b></blockquote>\n\n'
        '<blockquote>'
        '<b>يمكنك شراء النقاط من أحد المالكين فقط:</b>\n\n'
        f'<tg-emoji emoji-id=\"6116154779509985300\">👑</tg-emoji> <b>المالك الأول:</b> <b>{OWNER_USERNAME_1}</b>\n'
        f'<tg-emoji emoji-id=\"6113987307084190650\">👑</tg-emoji> <b>المالك الثاني:</b> <b>{OWNER_USERNAME_2}</b>\n\n'
        '<tg-emoji emoji-id=\"6114020073389692577\">📩</tg-emoji> <b>تواصل معهم مباشرة لشراء النقاط.</b>\n'
        '<b>بعد الدفع، سيقوم المالك بإرسال النقاط إلى رصيدك تلقائياً.</b>'
        '</blockquote>\n\n'
        f'<b>معرفك:</b> <code>{msg.from_user.id}</code>\n'
        '<i>(أرسل هذا المعرف للمالك)</i>'
    )
    bot.reply_to(msg, text, parse_mode='HTML')

@bot.message_handler(commands=['start', 'help'])
def help_command(msg):
    settings = get_settings()
    help_template = settings.get('help_message_template', DEFAULT_SETTINGS['help_message_template'])
    try:
        help_text = help_template.format(like_cmd=settings.get('like_command', '/like'))
    except (KeyError, ValueError, IndexError):
        help_text = help_template
    try:
        bot.reply_to(msg, help_text, parse_mode='HTML')
    except Exception:
        try:
            bot.send_message(msg.chat.id, help_text, parse_mode='HTML',
                             reply_to_message_id=msg.message_id)
        except Exception as e:
            log.error(f'help_command send failed: {e}')

@bot.message_handler(func=lambda m: m.text and m.text and not m.text.startswith('/'))
def handle_dynamic_like(msg):
                                                                                
    settings = get_settings()
    like_cmd = settings.get('like_command', '/like')
    if like_cmd == '/like':
        return                                                              
    text = msg.text.strip()
    first = text.split()[0] if text.split() else ''
    if first == like_cmd or text.startswith(like_cmd + ' '):
        _handle_like_logic(msg)

def main_run():
    init_like_engine()
    load_settings()
    start_autolike_scheduler()
    log.info('Starting LIKE bot...')
    log.info(f'Settings file: {SETTINGS_FILE}')
    log.info(f'Owners: {OWNERS}')
    log.info('Owner panel: /owner')
    s = get_settings()
    log.info(f"Like command: {s.get('like_command', '/like')}")
    log.info(f"AutoLike: {s.get('autolike_enabled')} @ {s.get('autolike_hour'):02d}:{s.get('autolike_minute'):02d}")
    while True:
        try:
            bot.polling(none_stop=True, timeout=30, interval=0.5)
        except Exception as e:
            log.info(f'bot error: {e}')
            time.sleep(2)

if os.environ.get('XCT_DRY_RUN') == '1':
    log.info('DRY RUN: module imports & top-level code executed successfully. Exiting.')
    sys.exit(0)

if __name__ == '__main__':
    main_run()
