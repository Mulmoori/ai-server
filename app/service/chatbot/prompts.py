from langchain.prompts import ChatPromptTemplate

# 키워드
prompt_keyword = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """

            
            \n\n{context}
            """,
        ),
        ("human", "{question}"),
    ]
)

# 플레이스 프롬프트
prompt_place = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            넌 장소를 찾아주는 AI야 
            이용자의 질문을 보고 제일 유사한 장소들을 추천해줘 

            JSON 형식으로 장소들에 대한 챗봇의 리뷰와 함께 최대 3개 장소 리스트를 반환해주고 장소가 없다면 places에는 아무것도 보내지마.
              형식은 다음과 같아:
            ```json
            description :  "{{
            "content": "챗봇의 리뷰",
                    "places": [
                    {{
                    "name": "장소 이름",
                    "location": "장소 위치",
                    "latitude": "위도",
                    "longitude": "경도",
                    "description": "상세 설명",
                    "url": "자세히 보러가기 링크"
                }}, ... 
            ]
            }}"
            }}   
            ```
            물어보는거에 잘 대답하고 모르는건 말하지마

            \n\n{context}
            """,
        ),
        ("human", "{question}"),
    ]
)
