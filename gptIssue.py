import os
import openai
import re
import json


OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
ai = openai.Client(api_key=OPENAI_API_KEY)
 
# GitHub 이슈 라벨 정의
issue_labels = {
    "labels": [
        {"name": "bug", "description": "Indicates an unexpected problem or unintended behavior"},
        {"name": "documentation", "description": "Indicates a need for improvements or additions to documentation"},
        {"name": "duplicate", "description": "Indicates similar issues, pull requests, or discussions"},
        {"name": "enhancement", "description": "Indicates new feature requests"},
        {"name": "good first issue", "description": "Indicates a good issue for first-time contributors"},
        {"name": "help wanted", "description": "Indicates that a maintainer wants help on an issue or pull request"},
        {"name": "invalid", "description": "Indicates that an issue, pull request, or discussion is no longer relevant"},
        {"name": "question", "description": "Indicates that an issue, pull request, or discussion needs more information"},
        {"name": "wontfix", "description": "Indicates that work won't continue on an issue, pull request, or discussion"}
    ]
}

# 샘플 이슈 데이터
sample_issues = [
    {
        'title': 'Issue opened: Enhancement: 사용자 프로필 페이지에 활동 그래프 추가',
        'event': 'issues',
        'date': '2024-08-15',
        'content': '사용자 프로필 페이지에 활동 그래프를 추가하여 사용자 참여도를 시각화하는 기능을 제안합니다.\n\n...'
    },
    {
        'title': 'Issue opened: 웹사이트가 느려요',
        'event': 'issues',
        'date': '2024-08-16',
        'content': '요즘 웹사이트 속도가 너무 느린 것 같아요. 빨리 고쳐주세요.'
    },
    {
        'title': 'Issue opened: Bug: 모바일에서 이미지 업로드 실패',
        'event': 'issues',
        'date': '2024-08-17',
        'content': '모바일 환경에서 이미지 업로드 시 간헐적으로 실패하는 문제가 발생하고 있습니다.\n\n...'
    },
    {
        'title': 'Issue opened: 새로운 기능 추가해주세요',
        'event': 'issues',
        'date': '2024-08-18',
        'content': '다크 모드가 있으면 좋을 것 같아요. 눈이 덜 아플 것 같네요.'
    }
]

def fix_json_string(s):
    s = re.sub(r'(?<!\\)"(\w+)":', r'"\1":', s)
    s = re.sub(r': "(.+?)"', lambda m: ': "' + m.group(1).replace('"', '\\"') + '"', s)
    return s



def issue_evaluator(issue):
    system_content = """
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
    """

    response = ai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_content},
            {"role": "user", "content": f"최근 이슈 내용을 평가해줘. 각 이슈를 신중히 평가하고, 상세한 피드백을 제공해줘.: {issue}"}
        ],
        max_tokens=1023
    )

    return response.choices[0].message.content

# 메인 실행 부분
if __name__ == "__main__":
    for issue in sample_issues:
        evaluation = issue_evaluator(issue)
        print(f"Issue: {issue['title']}")
        print(f"Evaluation: {evaluation}\n")