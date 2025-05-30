# YouTube Downloader

이 애플리케이션은 Python과 Flask를 사용하여 YouTube 비디오를 다운로드하는 간단한 웹 애플리케이션입니다.
사용자는 웹 UI를 통해 YouTube 비디오 URL을 입력하고, 해당 비디오를 자신의 컴퓨터에 다운로드할 수 있습니다.

## 주요 기능

- 웹 브라우저를 통한 YouTube 비디오 URL 입력
- 지정된 경로 (기본값: 사용자 홈 디렉토리의 'Downloads' 폴더)에 비디오 다운로드
- 간단한 다운로드 상태 및 오류 메시지 표시

## 요구 사항

- Python 3.x
- pip (Python 패키지 설치 프로그램)
- ffmpeg (비디오/오디오 포맷 변환 및 병합 도구)

## 설치 방법

1.  **저장소 복제 (Clone the repository):**
    ```bash
    git clone https://github.com/your-username/youtubedownloader.git # 실제 저장소 URL로 변경해주세요.
    cd youtubedownloader
    ```

2.  **가상 환경 생성 및 활성화 (권장):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # macOS/Linux
    # venv\Scripts\activate  # Windows
    ```

3.  **필요한 라이브러리 설치:**
    ```bash
    pip install -r requirements.txt
    ```
    `requirements.txt` 파일에는 다음 라이브러리가 포함되어 있습니다:
    - `Flask`: 웹 프레임워크
    - `yt-dlp`: YouTube 비디오 다운로드 라이브러리

4.  **ffmpeg 설치 (macOS의 경우 Homebrew 사용):**
    `yt-dlp`가 비디오와 오디오를 병합하기 위해 `ffmpeg`를 사용합니다. Homebrew를 사용하여 설치할 수 있습니다.
    ```bash
    brew install ffmpeg
    ```
    Homebrew가 설치되어 있지 않다면, [Homebrew 공식 웹사이트](https://brew.sh/index_ko)를 참고하여 설치하세요.

## 실행 방법

1.  **Flask 애플리케이션 실행:**
    ```bash
    python app.py
    ```

2.  **웹 브라우저에서 접속:**
    애플리케이션이 실행되면 터미널에 다음과 같은 메시지가 표시됩니다:
    ```
     * Running on http://127.0.0.1:5000/
    ```
    웹 브라우저를 열고 `http://127.0.0.1:5000/` 주소로 접속하면 YouTube 다운로더 웹 UI를 사용할 수 있습니다.

