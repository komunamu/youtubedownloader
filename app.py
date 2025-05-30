from flask import Flask, render_template, request, redirect, url_for
import downloader
import os

app = Flask(__name__)

# 다운로드 받을 기본 경로 설정 (예: 사용자 홈의 Downloads 폴더)
DOWNLOAD_DIR = os.path.join(os.path.expanduser('~'), 'Downloads')
if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)

@app.route('/', methods=['GET', 'POST'])
def index():
    message = None
    error = None
    filepath = None
    if request.method == 'POST':
        video_url = request.form['url']
        if video_url:
            try:
                # downloader.py 모듈의 함수를 호출하여 다운로드 실행
                download_message, downloaded_file_path = downloader.download_video(video_url, DOWNLOAD_DIR)
                if downloaded_file_path: # 성공
                    message = download_message
                    filepath = downloaded_file_path
                else: # 실패
                    error = download_message
            except Exception as e:
                error = str(e)
    return render_template('index.html', message=message, error=error, filepath=filepath, download_dir=DOWNLOAD_DIR)

if __name__ == '__main__':
    app.run(debug=True)