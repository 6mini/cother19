<div align=center>

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2F6mini%2FData-Pipeline-Project&count_bg=%23AAAAAA&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=Hits&edge_flat=false)](https://github.com/6mini/Data-Pipeline-Project)

</div>

![Project3 001](https://user-images.githubusercontent.com/79494088/136796271-f4a3aff3-a3a3-4137-a4b0-857faa3628a7.jpeg)

<div align=center>

<img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=HTML5&logoColor=white"/></a>
<img src="https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=Jupyter&logoColor=white"/></a>
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=JavaScript&logoColor=white"/></a>
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/></a>
<img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=CSS3&logoColor=white"/></a>
<img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=PostgreSQL&logoColor=white"/></a>
<img src="https://img.shields.io/badge/Amazon AWS-232F3E?style=flat-square&logo=AmazonAWS&logoColor=white"/></a>
<img src="https://img.shields.io/badge/Heroku-430098?style=flat-square&logo=Heroku&logoColor=white"/></a>
<img src="https://img.shields.io/badge/Flask-000000?style=flat-square&logo=Flask&logoColor=white"/></a>

# Welcome to CO-THER 19 🙋🏻‍♂️

</div>

- '기상으로 예측하는 서울의 확진자 수'라는 주제의 데이터 파이프라인 구축 및 머신러닝 서빙 앱 배포 프로젝트: 코로나 확진자 수 예측 앱 'CO-THER 19'
- [웹 어플리케이션 바로가기](https://cother.herokuapp.com/)
- [블로그 포스팅 바로가기](https://6mini.github.io/project/2021/10/06/cother1/)

# 문제 정의
- 플라스크(Flask) 웹 구현을 목표로 시작하는 데이터 파이프라인 구축 프로젝트이다.
- 머신 러닝 모델을 서빙할 예정이고 머신 러닝 성능보다 무에서 파이프라인을 만들어 보는데 의의를 두려고 한다.
- 태블로를 활용한 분석 및 배포까지 해보고 싶다.
- 주제는 아무래도 코로나 때문에 굉장히 힘들어하고 있는 한 사람으로서, 기상 변인으로 서울시의 확진자 수를 예측하는 머신 러닝 모델을 만들어보려한다.

# 데이터 파이프라인

![윤민쓰 의뢰 001](https://user-images.githubusercontent.com/79494088/143800098-30dd0c0f-d9b1-4ae5-8480-50aa45499c23.png)

- [공공데이터: 일별 기상 데이터, 확진자 수 데이터 ⇨ AWS RDS PostgreSQL](https://6mini.github.io/project/2021/10/06/cother1/)
  - [AWS EC2 Crontab 이용 DB 저장 자동화](https://6mini.github.io/project/2021/10/10/cother5/)
- [BI: Tableau, Tableau Public(웹사이트 내 링크)](https://6mini.github.io/project/2021/10/09/cother4/)
- [웹 프레임워크로 플라스크(Flask)이용, 헤로쿠(Heroku)로 배포](https://6mini.github.io/project/2021/10/08/cother3/)

# 머신러닝 모델링
- [머신러닝 모델링 과정 포스팅 바로가기](https://6mini.github.io/project/2021/10/07/cother2/)

![Project3 005](https://user-images.githubusercontent.com/79494088/136805363-a15f4472-06a5-477e-974e-ae885104ab83.jpeg)

- 코로나 확진자수가 유의하게 존재하는 기간은 그렇게 오래 되지 않았기 때문에 지금으로부터 1년 전까지의 데이터만 사용했다.
- **59가지의 기상 데이터를 사용 시 R²: 0.9**
- 기상 입력값을 받아 확진자 예측을 해야하기 때문에, 59가지나 되는 기상을 사용할 수 없다.<br>
또한 기상예보에서 알려주는 데이터가 아닐 경우, 서비스의 유용력이 굉장히 떨어질거라 생각해서 기상예보로 확인할 수 있는 7가지의 기상 데이터만 사용했다.
- **7가지의 기상 데이터를 사용 시 R²: 0.5**
- 모두 사용했을때보다 성능이 굉장히 아쉬웠지만, 그래도 0.5라는 수치는 강력하진 않지만 중간정도의 효과 크기로 간주되기 때문에 이 모델로 웹서비스를 진행했다.

# 간략 회고
- [전체 회고 보러가기](https://6mini.github.io/project/2021/10/11/cother6/)
- 머신러닝을 접목해서 서비스를 한다는 것 자체가 개인적으로 사고를 높이는데 한단계 발전 할 수 있었던 프로젝트였다고 생각한다.
- 어떤 학습을 시켜야하는지 문제정의를 하는 것부터, 어떤 데이터를 어떻게 파이프라인으로 꾸려야하는지를 생각하는게 까다롭고 힘들다는 것을 느꼈다.
- 분석을 하면서도 느꼈고 도메인에 대해 탐색하면서도 느낀 점이지만 코로나가 기상과의 연관성이 크지 않아서 사실 서비스에대한 유용성을 스스로도 크게 느끼지 못한 것 같다.
- 사실 데이터도 굉장히 부족해서 앞서 R2 값이 0.9가 나왔지만 과적합의 위험도 크고, 7개의 변인으로만 사용한 모델은 설명력이 굉장히 부족하기 때문에 결과가 포부를 따라가지 못해 아쉬운 마음이 큰 프로젝트 였다.
- 시간의 한계 때문에 서울에 대해서만 모델링을 진행했는데, 전국적으로 또 전 세계적으로 오랜시간 연구하다보면 나름대로 유의미한 결과를 도출해낼 수도 있을거란 생각을 한다.

# 미리보기

![스크린샷 2021-10-10 17 01 47](https://user-images.githubusercontent.com/79494088/136687686-18ce64f4-830a-48d4-9b0e-363a268cb73b.png)

![스크린샷 2021-10-10 17 01 52](https://user-images.githubusercontent.com/79494088/136687688-44ec1016-8fe2-4e31-9360-8b19317a687f.png)

![스크린샷 2021-10-10 17 01 56](https://user-images.githubusercontent.com/79494088/136687689-805cfc62-c2b5-40f3-a003-788da1f9a72a.png)

![스크린샷 2021-10-10 17 02 00](https://user-images.githubusercontent.com/79494088/136687690-9bd3959c-c555-47c9-876a-00453c3c1d99.png)

![스크린샷 2021-10-10 17 02 39](https://user-images.githubusercontent.com/79494088/136687682-c965ca54-b4e1-4007-8765-ff405fd5b545.png)

![스크린샷 2021-10-10 17 02 04](https://user-images.githubusercontent.com/79494088/136687692-caf45609-fef4-4118-98b4-3d591860cb9f.png)

![스크린샷 2021-10-10 17 02 15](https://user-images.githubusercontent.com/79494088/136687693-29019123-c5b8-4682-8954-cca5caca2910.png)
