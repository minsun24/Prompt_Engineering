from openai import OpenAI
import os
import openai
import re
import json
import ast

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
ai = openai.Client(api_key=OPENAI_API_KEY)



issue_labels = {
          "labels": [
            {
              "name": "bug",
              "description": "Indicates an unexpected problem or unintended behavior"
            },
            {
              "name": "documentation",
              "description": "Indicates a need for improvements or additions to documentation"
            },
            {
              "name": "duplicate",
              "description": "Indicates similar issues, pull requests, or discussions"
            },
            {
              "name": "enhancement",
              "description": "Indicates new feature requests"
            },
            {
              "name": "good first issue",
              "description": "Indicates a good issue for first-time contributors"
            },
            {
              "name": "help wanted",
              "description": "Indicates that a maintainer wants help on an issue or pull request"
            },
            {
              "name": "invalid",
              "description": "Indicates that an issue, pull request, or discussion is no longer relevant"
            },
            {
              "name": "question",
              "description": "Indicates that an issue, pull request, or discussion needs more information"
            },
            {
              "name": "wontfix",
              "description": "Indicates that work won't continue on an issue, pull request, or discussion"
            }
          ]
        }

data1={
    'title': 'Issue opened: Enhancement: 사용자 프로필 페이지에 활동 그래프 추가',
    'event': 'issues',
    'date': '2024-08-15',
    'content': '사용자 프로필 페이지에 활동 그래프를 추가하여 사용자 참여도를 시각화하는 기능을 제안합니다.  구체적인 제안 내용: 1. 그래프 유형: 히트맵 캘린더 (GitHub의 컨트리뷰션 그래프와 유사) 2. 표시 데이터: 일일 로그인 횟수, 게시물 작성 수, 댓글 수 3. 기간 옵션: 최근 1개월, 3개월, 6개월, 1년 4. 인터랙션: 마우스 호버 시 해당 날짜의 상세 활동 내역 표시 5. 색상 구성: 활동 빈도에 따라 5단계 색상 구분 (예: #ebedf0, #9be9a8, #40c463, #30a14e, #216e39)  기대 효과: - 사용자의 지속적인 참여 유도 - 개인 활동 이력에 대한 직관적인 파악 가능 - gamification 요소 도입으로 사용자 충성도 향상  기술적 고려사항: - 프론트엔드: React와 D3.js를 활용한 그래프 구현 - 백엔드: 사용자 활동 로그 집계 API 개발 필요 - 성능: 대량의 데이터 처리를 위한 캐싱 전략 수립  구현 예상 시간: 2주 (백엔드 API 1주, 프론트엔드 구현 1주) 담당자 제안: 프론트엔드 개발자 1명, 백엔드 개발자 1명  추가 의견이나 제안사항 있으면 댓글로 남겨주세요.'
}
data2={
    'title': 'Issue opened: 웹사이트가 느려요',
    'event': 'issues',
    'date': '2024-08-16',
    'content': '요즘 웹사이트 속도가 너무 느린 것 같아요. 빨리 고쳐주세요.'
}
data3={
    'title': 'Issue opened: Bug: 모바일에서 이미지 업로드 실패',
    'event': 'issues',
    'date': '2024-08-17',
    'content': '모바일 환경에서 이미지 업로드 시 간헐적으로 실패하는 문제가 발생하고 있습니다.  재현 환경: 1. 기기: iPhone 12, Samsung Galaxy S21 2. OS: iOS 14.8, Android 12 3. 앱 버전: 2.5.0 4. 네트워크 환경: Wi-Fi 및 4G LTE 모두에서 발생  재현 단계: 1. 앱 실행 후 로그인 2. \'게시물 작성\' 버튼 클릭 3. \'이미지 추가\' 버튼 클릭 4. 갤러리에서 이미지 선택 5. \'업로드\' 버튼 클릭  기대 결과: 이미지가 성공적으로 업로드되고 미리보기 표시 실제 결과: 약 30% 확률로 "업로드 실패" 메시지 출력  오류 로그: ``` ERROR [2024-08-17 15:23:45] ImageUploadService: Failed to upload image java.io.IOException: Unexpected end of stream     at okhttp3.internal.http2.Http2Stream$FramingSource.read(Http2Stream.java:485)     at okio.RealBufferedSource.indexOf(RealBufferedSource.kt:449)     at okio.RealBufferedSource.readUtf8LineStrict(RealBufferedSource.kt:333)     at okhttp3.internal.http1.Http1ExchangeCodec.readHeaderLine(Http1ExchangeCodec.kt:212) ```  시도한 해결 방법: 1. Wi-Fi 및 모바일 데이터 전환 - 문제 지속 2. 앱 재설치 - 문제 지속 3. 다른 기기에서 시도 - 동일한 문제 발생  추가 정보: - 서버 로그 확인 결과, 클라이언트에서 연결이 갑자기 끊기는 현상 발견 - 백엔드 팀에 서버 측 타임아웃 설정 검토 요청  해결 방향 제안: 1. 네트워크 연결 안정성 체크 로직 추가 2. 업로드 실패 시 자동 재시도 메커니즘 구현 3. 프로그레스 바 추가로 사용자에게 업로드 진행 상황 표시  담당자: @frontend-team, @backend-team 우선순위: 높음 (사용자 경험에 직접적인 영향)'
}
data4={
    'title': 'Issue opened: 새로운 기능 추가해주세요',
    'event': 'issues',
    'date': '2024-08-18',
    'content': '다크 모드가 있으면 좋을 것 같아요. 눈이 덜 아플 것 같네요.'
}


def fix_json_string(s):
    # 키의 따옴표를 수정
    s = re.sub(r'(?<!\\\\)"(\\w+)":', r'"\\1":', s)
    # 값의 따옴표를 수정
    s = re.sub(r': "(.+?)"', lambda m: ': "' + m.group(1).replace('"', '\\\\"') + '"', s)
    return s


def issue_evaluator(prompt):
    response = ai.chat.completions.create(
        model = "gpt-3.5-turbo", 
        messages = [
            {
            "role": "system",
            "content": 
            """
            당신은 GitHub에 생성되는 이슈를 평가하는 분석가입니다. 다음 가이드라인에 따라 이슈를 평가하세요:

            1. 평가 기준:
            - Positive: 내용이 구체적이고 잘 정리된 이슈
            - Negative: 내용이 빈약하거나 모호한 이슈

            2. Positive 평가 시:
            - 이슈의 카테고리를 아래 제공된 라벨을 참고하여 분류하세요.

            3. Negative 평가 시:
            - 내용의 문제점을 지적하고 구체화해야 할 부분을 제안하세요.

            4. 평가 결과는 다음 형식으로 제공하세요:
            {
                "eval": "positive" 또는 "negative",
                "recommend": "분류 또는 구체화 추천 내용",
                "message": "칭찬 내용 또는 지적 내용"
            }

            이슈 라벨 및 설명: {issue_labels}
            

            각 이슈를 신중히 평가하고, 위의 지침에 따라 상세한 피드백을 제공하세요.
            모든 피드백은 영어로 해주세요.
            """
        },
        {
            "role" : "user",
            "content" : f"최근 이슈 내용을 평가해줘. 각 이슈를 신중히 평가하고, 영어로 상세한 피드백을 해줘." 
            '''{data1}'''

        },
        {
            "role" : "assistant",
            "content" : 
            """
            {
            "eval": "positive",
            "recommend": "enhancement",
            "message": "이 이슈는 매우 상세하고 잘 구조화되어 있습니다. 다음과 같은 점에서 높은 평가를 받을 수 있습니다: 1. 명확한 기능 설명: 활동 그래프의 구체적인 특성과 구현 방법을 상세히 제시했습니다. 2. 기대 효과 명시: 제안된 기능이 가져올 이점을 명확히 설명했습니다. 3. 기술적 고려사항 포함: 구현에 필요한 기술 스택과 성능 최적화 방안을 제시했습니다. 4. 구현 계획 제시: 예상 소요 시간과 필요한 인력을 명시했습니다. 5. 추가 의견 요청: 다른 팀원들의 참여를 유도하여 협업을 장려하고 있습니다.  이러한 상세한 정보는 개발 팀이 해당 기능의 구현 가능성을 평가하고 작업 계획을 수립하는 데 매우 유용할 것입니다."
            }
            """
        },
        {
            "role" : "user",
            "content" : f"최근 이슈 내용을 평가해줘. 각 이슈를 신중히 평가하고, 영어로 상세한 피드백을 해줘." 
            '''{data1}'''

        },
        {
            "role" : "assistant",
            "content" : 
            """
            {
            "eval": "negative",
            "recommend": "이 이슈의 내용을 더 구체화할 필요가 있습니다. 다음과 같은 정보를 추가로 제공해 주시면 문제 해결에 큰 도움이 될 것입니다: 1. 어떤 페이지에서 특히 느린지 (예: 메인 페이지, 로그인 페이지 등) 2. 언제부터 이런 현상이 발생했는지 3. 사용 중인 브라우저와 기기 정보 4. 네트워크 환경 (예: Wi-Fi, 유선 인터넷 등) 5. 구체적인 '느림'의 정도 (예: 페이지 로딩에 걸리는 시간) 6. 다른 웹사이트와 비교했을 때의 상대적인 속도",
            "message": "이 이슈는 중요한 문제를 제기하고 있지만, 내용이 매우 간략하여 개발팀이 문제를 파악하고 해결하는 데 어려움이 있을 수 있습니다. 성능 문제는 다양한 요인에 의해 발생할 수 있으므로, 더 자세한 정보가 필요합니다. 추가 정보를 제공해 주시면, 개발팀이 문제의 원인을 더 빠르고 정확하게 파악하여 효과적인 해결책을 마련할 수 있을 것입니다."
            }
            """
        },
        {
            "role" : "user",
            "content" : f"최근 이슈 내용을 평가해줘. 각 이슈를 신중히 평가하고, 영어로 상세한 피드백을 해줘." 
            '''{data3}'''

        },
        {
            "role" : "assistant",
            "content" : 
            """
            {
            "eval": "positive",
            "recommend": "bug",
            "message": "이 이슈 보고는 매우 상세하고 체계적으로 작성되어 있어 높은 평가를 받을 수 있습니다. 다음과 같은 점에서 뛰어납니다:  1. 명확한 문제 설명: 모바일 환경에서의 이미지 업로드 실패 문제를 명확히 기술했습니다. 2. 재현 환경 상세 기술: 기기, OS, 앱 버전, 네트워크 환경 등 문제 재현에 필요한 모든 정보를 제공했습니다. 3. 재현 단계 명시: 문제 발생까지의 단계를 순서대로 상세히 기술했습니다. 4. 기대 결과와 실제 결과 비교: 예상되는 정상 동작과 실제 발생하는 문제를 명확히 대비해 설명했습니다. 5. 오류 로그 제공: 구체적인 오류 메시지와 스택 트레이스를 포함하여 디버깅에 도움을 줍니다. 6. 시도한 해결 방법 기술: 이미 시도해 본 해결 방법들을 나열하여 중복 작업을 방지합니다. 7. 추가 정보 제공: 서버 로그 확인 결과 등 문제 해결에 도움이 될 수 있는 추가 정보를 제공했습니다. 8. 해결 방향 제안: 가능한 해결 방법을 제시하여 개발 팀에 도움을 줍니다. 9. 담당자 지정 및 우선순위 설정: 관련 팀을 태그하고 우선순위를 명시하여 효율적인 작업 분배를 돕습니다.  이러한 상세하고 체계적인 버그 리포트는 개발 팀이 문제를 신속하게 이해하고 효과적으로 해결하는 데 큰 도움이 될 것입니다."
            }
            """
        }

    ], max_tokens=1023
    )



    json_string = response.choices[0].message.content
    json_string = json_string.strip()
    json_string = re.sub(r'^```json\\s*|\\s*```$', '', json_string, flags=re.MULTILINE)
    json_string = fix_json_string(json_string)

    try:
        python_dict = json.loads(json_string)
    except json.JSONDecodeError:
        try:
            python_dict = ast.literal_eval(json_string)
        except:
            print(f"Parsing failed. Problematic string: {json_string}")
            return {"error": "JSON decoding failed", "raw_string": json_string}

    return python_dict




if __name__ == "__main__":
    
    res = issue_evaluator(data4)
    print(res)
