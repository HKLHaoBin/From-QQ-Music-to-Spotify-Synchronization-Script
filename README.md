# From QQ Music to Spotify Synchronization Script

## 简介 Introduction

这个脚本可以将 **QQ 音乐** 的播放与 **Spotify** 同步，从而通过 **Lyricify 4** 显示歌词。由于 Lyricify 4 不支持 QQ 音乐，这个脚本通过在您在 QQ 音乐上播放歌曲时自动在 Spotify 上播放相同的歌曲来弥补这一差距。

This script synchronizes the playback of **QQ Music** with **Spotify**, enabling the display of lyrics via **Lyricify 4**. Since Lyricify 4 does not support QQ Music, this script bridges that gap by automating the playback of the same song on Spotify when you play a song on QQ Music.

## 特性 Features

- **同步播放**：监控 QQ 音乐的播放并在 Spotify 上自动播放相同的歌曲。
- **歌词显示**：与 Lyricify 4 一起使用，显示同步的歌词。
- **自动控制**：在同步过程中自动暂停和恢复 QQ 音乐，确保歌词与音乐同步。

- **Playback Synchronization**: Monitors QQ Music playback and automatically plays the same song on Spotify.
- **Lyrics Display**: Works with Lyricify 4 to display synchronized lyrics.
- **Automated Control**: Automatically pauses and resumes QQ Music during synchronization to ensure lyrics are in sync.

## 安装 Installation

1. **克隆此仓库 Clone the repository**：

   ```bash
   git clone https://github.com/yourusername/From_QQmusic_to_Spotify.git
   ```

2. **安装所需的 Python 包 Install required Python packages**：

   ```bash
   pip install -r requirements.txt
   ```

3. **下载并安装 ChromeDriver Download and install ChromeDriver**：

   - 从 [这里](https://googlechromelabs.github.io/chrome-for-testing/) 下载与您的 Chrome 浏览器版本匹配的 ChromeDriver。
   - 将 `chromedriver.exe` 放在已知目录中，并在脚本中相应更新 `CHROME_DRIVER_PATH`。
    ```python
    # 设置 ChromeDriver 的路径
    CHROME_DRIVER_PATH = r".\chromedriver.exe"
    ```

4. **填写您的 Spotify 用户名和密码 Fill in your Spotify username and password in the script**：

   ```python
   # 主程序 Main program
   username = ''  # 替换为你的 Spotify 用户名 Replace with your Spotify username
   password = ''  # 替换为你的 Spotify 密码 Replace with your Spotify password
   ```

## 使用方法 Usage

1. **在 QQ 音乐上开始播放一首歌曲 Start playing a song on QQ Music**。

2. **打开 Lyricify 4 Open Lyricify 4**。

3. **运行脚本 Run the script**：

   ```bash
   python From_QQmusic_to_Spotify_v2.py
   ```

4. **等待脚本初始化（约一首歌的时间） Wait for the script to initialize (takes about the time of one song)**。

5. **脚本运行后，在 QQ 音乐上播放下一首歌曲 After the script is running, play the next song on QQ Music**。

6. **脚本将同步在 Spotify 上播放，Lyricify 4 将显示歌词 The script will synchronize playback on Spotify, and Lyricify 4 will display the lyrics**。

## 已知问题 Known Issues

1. **网页加载时间不同 Variable Web Page Loading Times**：

   - 每个电脑的性能不同，网页加载时间也会有所不同。建议用户根据自己电脑的性能调整脚本中的 `sleep` 时间。宁可长不可短。

     ```python
     # 在函数 search_and_play_song 中
     sleep(3.5)  # 根据需要调整此值，不能为负数
     ```

   -  Different computers have varying performances, and web page loading times may differ. It's recommended to adjust the `sleep` time in the script based on your computer's performance. It's better to have a longer wait time than too short.

     ```python
     # In the function search_and_play_song
     sleep(3.5)  # Adjust this value as needed, cannot be negative
     ```

2. **程序可能会死循环 Program May Enter a Dead Loop**：

   - 如果程序进入死循环，重启程序即可。
   -  If the program seems to be stuck in a loop, simply restart it.

3. **启动时间较长 Startup Time**：

   - 程序启动需要一首歌的时间。启动程序时最好播放一首歌，这首歌会作为启动资源。程序启动完成后，播放下一首歌，程序就能正常运行。
   -  The program takes about the time of one song to start up. It's best to play a song when starting the program; this song will be used as a startup resource. After the program starts, play the next song to get the program running properly.

4. **音乐暂停现象 Music Pausing**：

   - 为了对准歌词，程序会主动暂停 QQ 音乐，直到 Spotify 开始播放后 QQ 音乐才会恢复。这是正常现象。
   -  To synchronize the lyrics, the program will temporarily pause QQ Music until Spotify starts playing, after which QQ Music will resume. This is normal behavior.

5. **填写 Spotify 账号和密码 Fill in Spotify Credentials**：

   - 记得在脚本中填写您的 Spotify 用户名和密码：

     ```python
     # 主程序
     username = ''  # 替换为你的 Spotify 用户名
     password = ''  # 替换为你的 Spotify 密码
     ```

   -  Remember to fill in your Spotify username and password in the script:

     ```python
     # Main program
     username = ''  # Replace with your Spotify username
     password = ''  # Replace with your Spotify password
     ```

6. **同步延迟 Synchronization Delay**：

   - 如果您发现同步有较大的时间差，可以调整脚本中的 `sleep` 时间：

     ```python
     # 在函数 search_and_play_song 中
     sleep(3.5)  # 增大此值以增加播放前的延迟
     ```

   -  If you notice a significant time difference in synchronization, adjust the `sleep` time in the script:

     ```python
     # In the function search_and_play_song
     sleep(3.5)  # Increase this value to increase the delay before playback
     ```

## 完整流程 Full Process

1. **QQ 音乐播放歌曲 QQ Music plays a song**。
2. **打开 Lyricify 4 Open Lyricify 4**。
3. **开启程序 `From_QQmusic_to_Spotify_v2.py` Start the script `From_QQmusic_to_Spotify_v2.py`**。
4. **等待 Lyricify 4 发生变化 Wait for Lyricify 4 to update**。
5. **QQ 音乐播放下一首歌 QQ Music plays the next song**。
6. **程序为了对准歌词，会主动把 QQ 音乐的音乐暂时暂停，直到 Spotify 音乐启动后 QQ 音乐才会启动 The script pauses QQ Music until Spotify starts playing, then QQ Music resumes**。
7. **Lyricify 4 滚动歌词 Lyricify 4 displays the scrolling lyrics**。

## 注意事项 Notes

- **初次使用时记得填写账号和密码 Remember to fill in your username and password during first use**。
- **如果同步延迟较大，调整 `sleep` 值 If synchronization delay is significant, adjust the `sleep` value**。

## 鸣谢 Acknowledgements

特别感谢 **Lyricify 4**，由于这个软件不支持 QQ 音乐，所以这就是我写这个脚本的理由。

Special thanks to **Lyricify 4**. Since this software doesn't support QQ Music, it inspired me to write this script.

## 许可证 License

MIT License
