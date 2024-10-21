import spotipy
from spotipy.oauth2 import SpotifyOAuth
import win32gui
import win32process
import psutil
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import ctypes
from pywinauto import Application
import ctypes
from time import sleep
import re

# 定义 VK_MEDIA_PLAY_PAUSE
VK_MEDIA_PLAY_PAUSE = 0xB3

# 设置 ChromeDriver 的路径
CHROME_DRIVER_PATH = r".\chromedriver.exe"


# 设置 Chrome 无头模式
chrome_options = Options()
chrome_options.add_argument("--headless")  # 无头模式
chrome_options.add_argument("--window-size=1920x1080")  # 设置窗口大小，确保页面完全加载
# 初始化浏览器
service = Service(CHROME_DRIVER_PATH)
# 初始化浏览器，自动管理 ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 打开 Spotify 网页版
driver.get('https://accounts.spotify.com/zh-CN/login?continue=https%3A%2F%2Fopen.spotify.com%2F')

# 等待页面加载
sleep(10)


def separate_chinese_english(song_name_text):
    # 正则表达式，匹配中文字符和英文字符
    chinese = re.findall(r'[\u4e00-\u9fff]+', song_name_text)
    english = re.findall(r'[a-zA-Z\s]+', song_name_text)
    
    # 将结果合并为字符串
    chinese_text = ''.join(chinese)
    english_text = ''.join(english)
    
    return chinese_text, english_text

def get_song_name(song_name_text):
    chinese_text, english_text = separate_chinese_english(song_name_text)
    
    # 优先使用英文部分，如果英文部分为空，则使用中文部分
    if english_text.strip():
        return english_text.strip()  # 返回英文歌曲名称
    else:
        return chinese_text.strip()  # 返回中文歌曲名称

# 登录 Spotify
def login_spotify(username, password):
    while True:
        try:
            # 输入用户名和密码
            username_input = driver.find_element(By.ID, "login-username")
            password_input = driver.find_element(By.ID, "login-password")
            username_input.send_keys(username)
            password_input.send_keys(password)
            password_input.send_keys(Keys.RETURN)
            sleep(15)
            break
        except Exception as e:
            print(f"登录 Spotify 失败: {e}, 正在重试...")
            sleep(1)

# 搜索并播放歌曲
def search_and_play_song(song_name):
    while True:
        try:
            search_box = driver.find_element(By.XPATH, "//input[@data-testid='search-input']")
            search_box.clear()
            search_box.send_keys(song_name)
            search_box.send_keys(Keys.RETURN)
            sleep(7)

            first_result = driver.find_element(By.XPATH, "//a[@href and contains(@href, '/track/')]")
            first_result.click()
            sleep(5)

            sleep(3)
            play_button_area = driver.find_element(By.XPATH, "//div[@class='ix_8kg3iUb9VS5SmTnBY']/button[@data-testid='play-button' and @aria-label='播放']")
            driver.execute_script("arguments[0].click();", play_button_area)
            sleep(3.5)
            ctypes.windll.user32.keybd_event(VK_MEDIA_PLAY_PAUSE, 0, 0, 0)  # 按下键
            ctypes.windll.user32.keybd_event(VK_MEDIA_PLAY_PAUSE, 0, 2, 0)  # 松开键
            #sleep(3)  # 等待播放按钮加载
            #sync_music_playback()
            break
        except Exception as e:
            print(f"搜索并播放歌曲失败: {e}, 正在重试...")
            sleep(1)




# 定义 VK_MEDIA_PLAY_PAUSE (用于控制 QQ 音乐或 Spotify)
VK_MEDIA_PLAY_PAUSE = 0xB3


# 连接到 QQ 音乐的进程并获取窗口标题
def find_qqmusic_window():
    qq_windows = []
    win32gui.EnumWindows(enum_windows_callback, qq_windows)
    if qq_windows:
        hwnd, window_title = qq_windows[0]
        return hwnd, window_title
    else:
        print("未找到 QQ 音乐窗口")
        return None, None

# 回调函数获取 QQ 音乐的窗口
def enum_windows_callback(hwnd, extra):
    title = win32gui.GetWindowText(hwnd)
    if "QQ音乐" in title:
        extra.append((hwnd, title))



# 使用 set 来去重存储歌曲信息，避免重复输出
song_windows = set()

# 遍历系统中的所有窗口，打印每个窗口的标题
def print_all_windows():
    def enum_windows_callback(hwnd, extra):
        print(f"窗口句柄: {hwnd}, 标题: {win32gui.GetWindowText(hwnd)}")
    win32gui.EnumWindows(enum_windows_callback, None)

# 遍历系统中的所有进程，查找 QQ 音乐的进程
def find_qqmusic_process():
    while True:
        try:
            for proc in psutil.process_iter(['pid', 'name', 'username']):
                process_name = proc.info['name']
                if process_name and "QQMusic" in process_name:
                    print(f"找到 QQ 音乐进程: {proc.info}")
                    return proc.info
            return None
        except Exception as e:
            print(f"查找 QQ 音乐进程失败: {e}, 正在重试...")
            sleep(5)


# 获取所有属于指定进程ID的窗口句柄
def enum_windows_by_pid(pid):
    def enum_windows_callback(hwnd, windows):
        try:
            _, found_pid = win32process.GetWindowThreadProcessId(hwnd)  # 使用 win32process 获取进程ID
            if found_pid == pid:
                windows.append(hwnd)
        except Exception as e:
            print(f"Error: {e}")

    windows = []
    win32gui.EnumWindows(enum_windows_callback, windows)
    return windows

# 你可以使用找到的窗口句柄提取歌曲信息
def get_song_info_from_windows(windows):
    for hwnd in windows:
        window_text = win32gui.GetWindowText(hwnd)
        if window_text and " - " in window_text:  # 假设歌曲名称和艺术家之间使用 " - " 作为分隔符
            if window_text not in song_windows:  # 去重，防止重复输出
                song_windows.clear()
                song_windows.add(window_text)
                print(f"当前播放的歌曲: {window_text}")
                ctypes.windll.user32.keybd_event(VK_MEDIA_PLAY_PAUSE, 0, 0, 0)  # 按下键
                ctypes.windll.user32.keybd_event(VK_MEDIA_PLAY_PAUSE, 0, 2, 0)  # 松开键
                song_name=window_text
                song_name = window_text.split('-')[0].strip()
                # 示例文本
                song_name_text = song_name

                song_name = get_song_name(song_name_text)

                print("选择的歌曲名称:", song_name)
                #track_id = search_song_on_spotify(song_name)
                #if track_id:
                #    play_song_on_spotify(track_id)
                search_and_play_song(song_name)


# 定时获取 QQ 音乐的播放状态
def monitor_music_playing(pid, interval=1):
    while True:
        windows = enum_windows_by_pid(pid)
        if windows:
            get_song_info_from_windows(windows)
        else:
            print("未找到属于该进程的窗口")

        # 每隔 `interval` 秒检查一次
        time.sleep(interval)


# 运行程序
print("遍历系统中的所有窗口:")
print_all_windows()
# 主程序
username = ''  # 替换为你的 Spotify 用户名
password = ''  # 替换为你的 Spotify 密码
#song_name = 'Fragile - Laufey'

login_spotify(username, password)



# 查找 QQ 音乐进程
process_info = find_qqmusic_process()
if process_info:
    print(f"QQ 音乐进程详情: {process_info}")

    # 提取 PID
    pid = process_info['pid']

    # 实时监控 QQ 音乐播放状态，每 1 秒获取一次
    monitor_music_playing(pid, interval=1)
else:
    print("未找到 QQ 音乐进程")


# 浏览器保持打开状态
input("按 Enter 键退出程序...")
driver.quit()
