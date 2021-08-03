# Keyword Analysis using Twitter API [Twitter API를 이용한 키워드 분석]

This is not my original work, I have expanded its usage (Copyright below). [원작자 및 Copyright에 대한 언급은 아래 있습니다.]

### Notebooks Order [노트북 순서]

0. Twitter API Registeration [Twitter API 등록하기]
1. Collect Data using Twitter API [Twitter API를 이용해 데이터 수집]
2. Extract Keywords [키워드 추출하기]
3. Analyze Keyword using Association Rule [연관 분석을 이용해 키워드 분석하기]
4. Visualize Keyword Network [키워드 네트워크 시각화하기]

### Twitter API Registeration [Twitter API 등록하기]

https://developer.twitter.com/en/apply-for-access

Register a developer account and create an app. [개발자 계정으로 등록하고 새로운 개발자 앱을 등록하세요.]

### Collect Data using Twitter API [Twitter API를 이용해 데이터 수집]

From the app's keys and tokens section, you will get access to your API keys. [만든 앱의 keys and tokens 구역에서 API key들을 확인하세요.]

Make a json file named 'api_config.json' at the top of your repository with your API keys ['api_config.json' 파일을 만들고 아래와 같이 코드를 작성하세요]:

```json
{
  "CONSUMER_KEY": "{YOUR_CONSUMER_KEY}",
  "CONSUMER_SECRET": "{YOUR_SECRET_CONSUMER_KEY}",
  "ACCESS_TOKEN_KEY": "{YOUR_ACCESS_TOKEN_}",
  "ACCESS_TOKEN_SECRET": "{YOUR_SECRET_ACCESS_TOKEN}"
}
```

We collect only the text data among all metadata crawled related to the given keyword. [크롤링된 모든 데이터 중 오직 키워드와 관련된 텍스트 데이터만을 수집합니다.]

Each 'api.search(keyword)' function call provides about a page length of tweet data. [각 'api.search(keyword)' 함수는 약 한 페이지 분량의 트윗 데이터를 불러옵니다.]

### Extract Keywords [키워드 추출하기]

We first discard any letter combination that is not an actual character of a certain language using 'text_cleaning()' function. [먼저 'text_cleaning()' 함수로 사용중인 언어의 글자가 아닌 데이터는 모두 삭제합니다.]

Then, we collect proper nouns using 'get_nouns()' function. [그리고 나서, 'get_nouns()' 함수로 명사들을 수집합니다.]

### Analyze Keyword using Association Rule [연관 분석을 이용해 키워드 분석하기]

Using apyori library, we collect the nouns' support, confidence, and lift indices for their association with our keyword. [apyori 라이브러리를 이용해서 각 명사의 지지도, 신뢰도, 향상도를 계산해 키워드 연관 분석에 사용할 수 있도록 합니다.]

As a result, we create new dataframes representing the network formed between the keywords and the frequencies of the nouns appeared. [결과적으로, 각 명사와 키워드의 네트워크를 보여주는 데이터프레임과 각 명사의 빈도수를 나타내는 프레임워크를 생성합니다.]

### Visualize Keyword Network [키워드 네트워크 시각화하기]

Using the network and the frequency dataframes, we visualize the associated keywords network. [명사 네트워크와 빈도수 데이터프레임을 사용해서 형성된 연관 키워드 네트워크를 가시화합니다.]

Copyright (c) 2019 [윤기태]

https://github.com/yoonkt200/python-data-analysis

```

```
