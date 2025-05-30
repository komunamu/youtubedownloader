import yt_dlp
import os

def download_video(url, download_path):
    """주어진 URL의 YouTube 비디오를 지정된 경로에 다운로드하고, 메시지와 파일 경로를 반환합니다."""
    # 파일명에 포함될 수 없는 문자 제거 또는 변경 (간단한 예시)
    # 실제로는 더 견고한 방식이 필요할 수 있습니다.
    title_template = '%(title)s.%(ext)s'
    
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': os.path.join(download_path, title_template),
        'noplaylist': True,
        # 'progress_hooks': [lambda d: print(d['status'])], # 콘솔 출력용, UI에서는 다른 방식 필요
        'restrictfilenames': True, # 파일명 길이 및 특수문자 제한
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False) # 먼저 정보만 가져옴
            # 실제 저장될 파일명 생성 (ydl.prepare_filename 사용)
            # 이 방식은 yt-dlp가 내부적으로 파일명을 결정하는 방식을 따릅니다.
            # outtmpl에 %(title)s 등이 포함되어 있을 때 정확한 파일명을 얻기 위함입니다.
            filename = ydl.prepare_filename(info_dict)
            
            # 실제 다운로드 실행
            ydl.download([url])
            
            video_title = info_dict.get('title', '비디오')
            # filename은 전체 경로이므로, 여기서 download_path를 기준으로 할 필요는 없습니다.
            return (f"'{video_title}' 다운로드 완료!", filename)
    except Exception as e:
        return (f"다운로드 중 오류 발생: {str(e)}", None)

if __name__ == '__main__':
    # 테스트용 코드
    test_url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ' # 예시 URL
    test_download_dir = os.path.join(os.path.expanduser('~'), 'Downloads', 'youtubedownloader_test')
    if not os.path.exists(test_download_dir):
        os.makedirs(test_download_dir)
    message, filepath = download_video(test_url, test_download_dir)
    print(message)
    if filepath:
        print(f"저장된 위치: {filepath}")