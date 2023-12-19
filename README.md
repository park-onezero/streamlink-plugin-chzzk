# 플러그인 사용 방법

다운로드 한 파일을 폴더에 집어넣고 폴더 경로를 **--plugin-dirs** 뒤에 넣어주시면 됩니다.

또는 {{파이썬 설치 폴더}}/Lib/site-packages/streamlink/plugins에 chzzk.py를 넣으면 **--plugin-dirs** 옵션을 안 넣어도 됩니다.

비디오와 오디오 스트림이 따로여서 **--ffmpeg-copyts** 옵션을 넣어야 싱크가 맞습니다.

## 사용 예시
```bash
streamlink --plugin-dirs .\plugins https://chzzk.naver.com/live/blahblah best -o output.mp4 --ffmpeg-copyts
```

