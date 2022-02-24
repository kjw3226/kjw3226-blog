---
title: Python Virtual Environments(파이썬 가상환경)
tag: Python Virtual Environments(파이썬 가상환경)
date: 2021-11-30
categories:	Python

---

![Python Virtual Environments](https://user-images.githubusercontent.com/93234783/143976775-024bc606-cc28-4fc4-acf5-23fc3c72a3b5.png)

### 가상환경(Virtual Environments)이란 

___
'자신이 원하는 Python 환경을 구축하기 위해 필요한 모듈만 담아 놓는 바구니' 라고 생각하면 된다.

즉, 위 사진 상단의 Python Virtual Envs 처럼 각 가상환경 (virtualenv1, 2, 3…) 은 독립적으로 관리된다.

각 모듈은 다른 모듈에 대한 의존성(dependency)이 다르기 때문에 마구잡이로 설치하다보면 

이유 모를 충돌이 날 수도 있다. 

따라서 각 프로젝트 별로 별개의 가상환경을 만들어놓고 사용하는 것이 정신 건강에 좋다.

다시 정리하면 가상환경을 사용하는 이유는, 같은 모듈을 사용한다고 하더라도 다른 버전을 필요로 한다거나,

Python 프로그램을 실행하기 위한 최소한의 환경을 마련하고자 할 때나, 

GitHub 등의 저장소나 네트워크와 연계하고자 할 때 등으로 매우 다양하다.

Python 에서 가상환경을 만드는 방법은 크게 2가지로 virtualenv 와 conda(anaconda3)를 사용한다.