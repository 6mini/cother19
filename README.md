<div align=center>

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2F6mini%2FData-Pipeline-Project&count_bg=%23AAAAAA&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=Hits&edge_flat=false)](https://github.com/6mini/Data-Pipeline-Project)

</div>

![Project3 001](https://user-images.githubusercontent.com/79494088/136796271-f4a3aff3-a3a3-4137-a4b0-857faa3628a7.jpeg)

<div align=center>

<img src="https://img.shields.io/badge/HTML5
-E34F26?style=flat-square&logo=HTML5
&logoColor=white"/></a>
<img src="https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=Jupyter&logoColor=white"/></a>
<img src="https://img.shields.io/badge/JavaScript
-F7DF1E?style=flat-square&logo=JavaScript
&logoColor=white"/></a>
<img src="https://img.shields.io/badge/Python
-3776AB?style=flat-square&logo=Python
&logoColor=white"/></a>
<img src="https://img.shields.io/badge/CSS3
-1572B6?style=flat-square&logo=CSS3
&logoColor=white"/></a>
<img src="https://img.shields.io/badge/PostgreSQL
-4169E1?style=flat-square&logo=PostgreSQL
&logoColor=white"/></a>
<img src="https://img.shields.io/badge/Amazon AWS-232F3E?style=flat-square&logo=AmazonAWS&logoColor=white"/></a>
<img src="https://img.shields.io/badge/Heroku
-430098?style=flat-square&logo=Heroku
&logoColor=white"/></a>
<img src="https://img.shields.io/badge/Flask-000000?style=flat-square&logo=Flask&logoColor=white"/></a>

# Welcome to CO-THER 19 🙋🏻‍♂️

</div>

- [Data Pipeline 구축 Project] 기상으로 알아보는 코로나 확진자 수 예측 프로그램<br>
(feat. AWS PostgreSQL, LGBM, Flask, Tableau)
- [웹 사이트 바로가기](https://cother.herokuapp.com/)
- [블로그 포스팅 바로가기](https://6mini.github.io/project/2021/10/06/Cother/)

## History

### 10. 6. 0300i 
- start

### 10. 7. 0344i
- 날씨 API req 및 AWS PostgreSQL 저장
- 일별 확진자 수 csv 저장
- LGBM 이용 다중회귀 모델링

### 10. 8. 1617i
- Model Pickle 이용 import 및 export
- HTML template 적용
- 모델 활용 예측값 API 구현

### 10.10. 0619i
- HTML, CSS 수정
- Dashboard 개발 및 배포 후 웹사이트 적용
- GUI 최종 수정
- favicon.ico 추가

### 10.10. 1542i
- 모바일 친화 작업
- Heroku 이용 최종 배포 및 git 정리
- 404 page 추가

### 10.11. 2209i
- AWS EC2 Crontab 이용 DB 저장 자동화
- 404 title 수정
- README.md 설명 추가

## Indroduction

### Pipline

![Project3 004](https://user-images.githubusercontent.com/79494088/136806298-98343035-00ac-4a35-85d9-2167514655ed.jpeg)

- 공공데이터: 일별 기상 데이터, 확진자 수 데이터 ⇨ AWS RDS PostgreSQL
  - AWS EC2 Crontab 이용 DB 저장 자동화
- BI: Tableau, Tableau Public(웹사이트 내 링크)
- Web Framework: Python Flask

### Machine Learning

![Project3 005](https://user-images.githubusercontent.com/79494088/136805363-a15f4472-06a5-477e-974e-ae885104ab83.jpeg)

- 코로나 확진자수가 유의하게 존재하는 기간은 그렇게 오래 되지 않았기 때문에 지금으로부터 1년 전까지의 데이터만 사용
- **59가지의 기상 데이터를 사용 시 R²: 0.9**
- 기상 입력값을 받아 확진자 예측을 해야하기 때문에, 59가지나 되는 기상을 사용할 수 없다.<br>
또한 기상예보에서 알려주는 데이터가 아닐 경우, 서비스의 유용력이 굉장히 떨어질거라 생각해서 기상예보로 확인할 수 있는 7가지의 기상 데이터만 사용
- **7가지의 기상 데이터를 사용 시 R²: 0.5**
- 모두 사용했을때보다 성능이 굉장히 아쉬웠지만, 그래도 0.5라는 수치는 강력하진 않지만 중간정도의 효과 크기로 간주되기 때문에 이 모델로 웹서비스를 진행



## Preview

![스크린샷 2021-10-10 17 01 47](https://user-images.githubusercontent.com/79494088/136687686-18ce64f4-830a-48d4-9b0e-363a268cb73b.png)

![스크린샷 2021-10-10 17 01 52](https://user-images.githubusercontent.com/79494088/136687688-44ec1016-8fe2-4e31-9360-8b19317a687f.png)

![스크린샷 2021-10-10 17 01 56](https://user-images.githubusercontent.com/79494088/136687689-805cfc62-c2b5-40f3-a003-788da1f9a72a.png)

![스크린샷 2021-10-10 17 02 00](https://user-images.githubusercontent.com/79494088/136687690-9bd3959c-c555-47c9-876a-00453c3c1d99.png)

![스크린샷 2021-10-10 17 02 39](https://user-images.githubusercontent.com/79494088/136687682-c965ca54-b4e1-4007-8765-ff405fd5b545.png)

![스크린샷 2021-10-10 17 02 04](https://user-images.githubusercontent.com/79494088/136687692-caf45609-fef4-4118-98b4-3d591860cb9f.png)

![스크린샷 2021-10-10 17 02 15](https://user-images.githubusercontent.com/79494088/136687693-29019123-c5b8-4682-8954-cca5caca2910.png)
