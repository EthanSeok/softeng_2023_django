## 수업 내용 복습하기

### windows에서 파이썬 가상환경 만들기

1. 윈도우 검색창에 cmd를 관리자 권한으로 실행

`cd`: change directory의 약자로 CLI 상에서 폴더를 이동할 때 사용합니다. 


2. cmd를 실행하고 다음 코드 입력

```python
cd 장고프로젝트 파일 경로
```

3. 파이썬 venv 이름의 가상환경 생성

```python
python -m venv venv
```

4. 가상환경 실행하기

```python
venv\Scripts\activate.bat
```

(venv)가 뜨면 성공

5. 장고 패키지 설치

```python
pip install django
```