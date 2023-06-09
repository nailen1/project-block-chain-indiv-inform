# 🧱 Blockchain Project: MY DATA

## ✏️ 프로젝트명
- 개인정보의 소유 주체인 개인이 자신의 개인정보를 주체적으로 전수 관리 감독할 수 있는 블록체인 시스템 구현

## ✏️ 프로젝트 개요
- 빅데이터를 활용한 데이터 산업의 발달로 현재까지 개인정보의 무분별한 수집과 활용에 대한 우려가 커지고 있다. 이에 대한 대책으로 개인정보보호법을 포함한 데이터 3법 등이 개정 시행되어 왔지만, 이는 여전히 개인의 정보보호에 대한 투명성을 보장하기에는 부족했고, 오히려 데이터를 자원으로 삼아 영리행위를 지속하는 수많은 기업들은 더 많은 개인정보 관리 및 처리 권한을 요구하고 있는 실정이다.
- 본 프로젝트는 현재의 실정법과 제도, 데이터 활용 주체가 해결하지 못하는, 혹은 해결할 의지가 부족한 개인정보
보호의 문제를 블록체인을 도입 활용하여 기술적으로 해결하고자 한다. 
- 블록체인 활용 방안은 다음과 같다:

  - 개인정보의 고유한 소유 주체인 개인은 자신의 개인정보를 탈중앙화된 블록체인 상에서 직접 관리할 수 있으며,

  - 외부 업체나 기관은 해당 개인의 개인정보를 활용하고자 할 때 개인정보 활용 관련 상세 기록을 블록으로 추가하는
과정을 거쳐야만 정보를 활용할 수 있다. 

  - 또한, 이 과정에서 개인정보 활용에 대한 대가 지불이 이루어진다. 이는 블록체인 상에서 atomic swap 과정을 거쳐 투명하게 결제되므로, 개인정보의 부정적인 무단 활용이 억제될 수 있다.

## 🗒 파일 목록과 설명 (ver051600)

### `smart-contract-personal.sol`
  개인의 블록체인 내부에 담긴 스마트컨트랙트 예시. 개인정보 활용 승인, 개인정보를 조회 등의 기능 메소드가 있음

### `toy-example-fee-payment.py`
  개인정보 조회, 활용에 따른 수수료 지불 기능 함수 시뮬레이터. 트랜잭션 상의 수수료 지불 주체와 잔고 수치를 조회 후 수수료 수취

### `toy-example-permission-and-payment.py`
  개인정보 조회에 따른 결과 출력 함수 시뮬레이터. 개인정보 활용 및 조회 승인과 수수료 지불 상태 출력

### `toy-example-price-setting.py`
  개인정보 조회 활용 수수료 수치 반영 함수 시뮬레이터. 개인정보 소유자 혹은 활용자가 수수료를 조절하는 기능을 구현하고자 함  

### `toy-example-output-form.py`
  개인정보 활용의 결과 생성된 블록체인 상의 정보를 출력하는 함수. 사용자 Daniel의 개인정보를 Naver와 Shinhan card가 조회한 경우 예시

### `web-demo`
  사용자가 블록체인을 손쉽게 관리할 수 있도록 한 web GUI 구현 예시

## 🗒 블록체인 출력 결과 예시 (ver051600)

- 개인정보의 소유 주체가 확인 가능한 블록체인 상의 기록
 ```
 Transaction ID: 0xabc123
Timestamp: 2023-05-12 10:30:15
Block Number: 1234
Previous Hash: 0x789def
Hash: 0x123abc

Transaction Details:
Data: Naver requested access to Daniel's personal information.
Date: 2023-05-12
Time: 10:30:00
Transaction Fee: 0.1 ETH
Payment Address: 0x456def

####### encryption ########
Personal Information:
Name: Daniel
Birthdate: 1990-01-01
Gender: Male
Address: Seoul, South Korea
Phone Number: 010-1234-5678
Email: daniel@email.com
############################

 ```
- 개인정보 사용 내역 로그 조회
```
Blockchain status:
{"Index": 0, "Timestamp": 1684087378.633405, "Data": "Genesis Block", "Previous Hash": "0", "Hash": "70555ec7f81a89cde22f919fd194d1c1050f65b8e2f34e8fea390ed087e19d96"}
{"Index": 1, "Timestamp": 1684087378.6354618, "Data": {"Name": "Daniel", "Service": "Naver"}, "Previous Hash": "a84d25bff8f4f42c817328813b2511c11775a10e8f99d342f28da79a33986c96", "Hash": "35216b9b88a0fb76d5e2fab2e7d65fc6729ca41feea685f08f58e72273f5b878"}
{"Index": 2, "Timestamp": 1684087378.6362822, "Data": {"Name": "Daniel", "Service": "Shinhan Card"}, "Previous Hash": "35216b9b88a0fb76d5e2fab2e7d65fc6729ca41feea685f08f58e72273f5b878", "Hash": "36831c02809107583203821cc510e1228f6ca65991ae076353b1ee86e2eca69d"}
Daniel's Blockchain status:
{"Index": 0, "Timestamp": 1684087378.6346948, "Data": "Genesis Block", "Previous Hash": "0", "Hash": "a84d25bff8f4f42c817328813b2511c11775a10e8f99d342f28da79a33986c96"}
{"Index": 1, "Timestamp": 1684087378.6354618, "Data": {"Name": "Daniel", "Service": "Naver"}, "Previous Hash": "a84d25bff8f4f42c817328813b2511c11775a10e8f99d342f28da79a33986c96", "Hash": "35216b9b88a0fb76d5e2fab2e7d65fc6729ca41feea685f08f58e72273f5b878"}
{"Index": 2, "Timestamp": 1684087378.6362822, "Data": {"Name": "Daniel", "Service": "Shinhan Card"}, "Previous Hash": "35216b9b88a0fb76d5e2fab2e7d65fc6729ca41feea685f08f58e72273f5b878", "Hash": "36831c02809107583203821cc510e1228f6ca65991ae076353b1ee86e2eca69d"}

```
