## Change Logs
### [2024-01-06]
- API 버전 v1에서 v2로 변경
- 19세 방송 여부 확인 로직 추가
- API 요청에 네이버 쿠키 적용 가능

## 플러그인 사용 방법

다운로드 한 파일을 폴더에 집어넣고 폴더 경로를 `--plugin-dirs` 뒤에 넣어주시면 됩니다.

또는 `{{파이썬 설치 폴더}}\Lib\site-packages\streamlink\plugins\`에 chzzk.py를 넣으면 `--plugin-dirs` 옵션을 안 넣어도 됩니다.

비디오와 오디오 스트림이 따로여서 `--ffmpeg-copyts` 옵션을 넣어야 싱크가 맞습니다.

`--chzzk-cookies` 옵션을 통해 API에 네이버 쿠키를 적용할 수 있습니다. 

## 사용 예시
```bash
streamlink --ffmpeg-copyts --plugin-dirs ".\plugins" https://chzzk.naver.com/live/blahblah best --chzzk-cookies "NID_AUT=BLAH; NID_SES=BLAHBLAH;" -o output.mp4
```

## Todo List
- [x] API 호출시 쿠키 적용
- [ ] 네이버 로그인 추가 
