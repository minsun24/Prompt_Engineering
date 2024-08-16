from venv import logger
from openai import OpenAI
import os
import openai
import re
import json
import ast




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


test_messages : list[dict] = [
    {
        "role" : "user",
        "content" : {
            "title": "Implement user authentication feature",
            "body": "This PR implements a user authentication system using JWT tokens. Key changes include:\n- Added new `UserAuth` middleware\n- Created login and registration endpoints\n- Integrated bcrypt for password hashing\n- Updated user model to include authentication fields\n\nTODO: Need to add unit tests for the new endpoints."
        }
    },
    {
        "role" : "assistant",
        "content" : {
        "eval": "positive",
        "label": "performance",
        "description": "데이터베이스 쿼리 최적화에 대한 상세한 설명과 구체적인 성능 개선 결과를 제시한 우수한 PR입니다. 변경 사항과 그 효과가 명확히 기술되어 있습니다."
    },
    }
]
pr_input_data = [
  {
    "title": "Implement user authentication feature",
    "body": "This PR implements a user authentication system using JWT tokens. Key changes include:\n- Added new `UserAuth` middleware\n- Created login and registration endpoints\n- Integrated bcrypt for password hashing\n- Updated user model to include authentication fields\n\nTODO: Need to add unit tests for the new endpoints."
  },
  {
    "title": "Optimize database queries for better performance",
    "body": "After profiling our application, I've identified and optimized several slow database queries. Changes include:\n- Added indexes to frequently queried fields\n- Refactored ORM queries to reduce N+1 problems\n- Implemented caching for expensive computations\n\nPerformance improvements:\n- Homepage load time reduced by 40%\n- API response time for user list improved by 60%"
  },
  {
    "title": "Add dark mode to the UI",
    "body": "This PR introduces a dark mode option for our web application. Changes include:\n- Created a theme switcher component\n- Added dark mode color palette to our design system\n- Updated all existing components to support both light and dark modes\n- Implemented user preference persistence using local storage\n\nScreenshots of the new dark mode are attached for review."
  },
  {
    "title": "Refactor payment processing module",
    "body": "This PR refactors our payment processing module to improve maintainability and prepare for future payment method additions. Key changes:\n- Introduced a PaymentStrategy interface\n- Implemented separate classes for each payment method (Credit Card, PayPal, etc.)\n- Updated existing code to use the new payment strategies\n- Added unit tests for each new class\n\nNote: This change is backwards compatible and shouldn't affect existing functionality."
  },
  {
    "title": "Update dependencies and migrate to React 18",
    "body": "This PR updates our front-end dependencies, most notably upgrading to React 18. Changes include:\n- Updated package.json with new dependency versions\n- Migrated from ReactDOM.render to createRoot\n- Implemented useEffect cleanup functions where necessary\n- Updated our custom hooks to take advantage of React 18 features\n\nPlease test thoroughly as this is a major version update."
  },
  {
    "title": "Add data visualization dashboard",
    "body": "This PR adds a new data visualization dashboard to help users understand their analytics at a glance. Features include:\n- Interactive charts using D3.js\n- Real-time data updates using WebSockets\n- Customizable widgets that users can add/remove/rearrange\n- Responsive design for mobile and desktop views\n\nThe dashboard is accessible at `/analytics` for users with admin privileges."
  },
  {
    "title": "Implement CI/CD pipeline using GitHub Actions",
    "body": "This PR sets up a Continuous Integration and Continuous Deployment pipeline using GitHub Actions. The pipeline includes:\n- Automated testing on push and pull requests\n- Code linting and style checking\n- Building and pushing Docker images to our registry\n- Automated deployment to staging environment on merge to develop branch\n- Manual approval step for production deployment\n\nConfiguration files are in the `.github/workflows` directory."
  },
    {
    "title": "Fixed bug",
    "body": "I fixed the bug."
  },
  {
    "title": "Update stuff",
    "body": "Updated some files. Please review and merge."
  },
  {
    "title": "Add new feature",
    "body": "Added a new feature to improve user experience. It should work fine."
  },
  {
    "title": "Refactor code",
    "body": "Refactored some parts of the codebase to make it better. Changed a lot of files."
  },
  {
    "title": "Performance improvements",
    "body": "Made some changes to improve performance. It seems faster now."
  },
  {
    "title": "UI changes",
    "body": "Changed some UI elements. Looks better now I think."
  },
  {
    "title": "Database schema update",
    "body": "Updated the database schema. Added some new tables and columns."
  },

  # Additional positive examples
  {
    "title": "Implement robust error handling and logging system",
    "body": "This PR introduces a comprehensive error handling and logging system to improve our application's reliability and debuggability. Key changes include:\n\n- Implemented a centralized error handling middleware\n- Added detailed error logging with stack traces\n- Integrated with Sentry for real-time error tracking\n- Created custom error classes for different types of application errors\n- Added unit tests for error handling scenarios\n\nThis change will significantly improve our ability to identify and resolve issues quickly in production. Please review the error categories and logging levels to ensure they meet our needs."
  },
  {
    "title": "Implement accessibility improvements across the application",
    "body": "This PR focuses on improving the accessibility of our web application to ensure it's usable by people with various disabilities. Changes include:\n\n- Added proper ARIA labels to all interactive elements\n- Improved keyboard navigation throughout the app\n- Enhanced color contrast ratios to meet WCAG 2.1 AA standards\n- Implemented skip navigation links\n- Added alt text to all images and icons\n- Ensured all forms are screen reader friendly\n\nThese changes have been tested with various screen readers and keyboard-only navigation. Please review and test, particularly if you have experience with accessibility tools."
  }
]


pr_output_data = pr_evaluation_data = [
    {
        "eval": "positive",
        "label": "feature",
        "description": "잘 작성된 PR입니다. 사용자 인증 기능 구현에 대한 명확한 설명과 주요 변경 사항이 잘 나열되어 있습니다. TODO 항목에서 단위 테스트 추가 필요성을 언급한 것도 좋습니다."
    },
    {
        "eval": "positive",
        "label": "performance",
        "description": "데이터베이스 쿼리 최적화에 대한 상세한 설명과 구체적인 성능 개선 결과를 제시한 우수한 PR입니다. 변경 사항과 그 효과가 명확히 기술되어 있습니다."
    },
    {
        "eval": "positive",
        "label": "enhancement",
        "description": "UI에 다크 모드를 추가하는 이 PR은 변경 사항을 명확히 설명하고 있습니다. 스크린샷을 첨부한 것도 리뷰어의 이해를 돕는 좋은 방법입니다."
    },
    {
        "eval": "positive",
        "label": "refactor",
        "description": "결제 처리 모듈 리팩토링에 대한 상세한 설명이 있는 우수한 PR입니다. 변경 사항의 목적과 주요 변경 내용이 잘 기술되어 있으며, 하위 호환성 유지에 대한 언급도 좋습니다."
    },
    {
        "eval": "positive",
        "label": "dependencies",
        "description": "React 18로의 마이그레이션에 대한 명확한 설명이 있는 좋은 PR입니다. 주요 변경 사항을 잘 나열했고, 철저한 테스트의 필요성을 언급한 것도 적절합니다."
    },
    {
        "eval": "positive",
        "label": "feature",
        "description": "데이터 시각화 대시보드 추가에 대한 상세한 설명이 있는 우수한 PR입니다. 주요 기능들이 잘 나열되어 있고, 접근 권한에 대한 정보도 포함되어 있습니다."
    },
    {
        "eval": "positive",
        "label": "ci-cd",
        "description": "CI/CD 파이프라인 구현에 대한 명확한 설명이 있는 훌륭한 PR입니다. 파이프라인의 각 단계가 상세히 설명되어 있어 리뷰어의 이해를 돕습니다."
    },
    {
        "eval": "negative",
        "label": "needs-more-info",
        "description": "PR의 제목과 설명이 너무 간단합니다. 어떤 버그를 수정했는지, 어떻게 수정했는지 등의 구체적인 정보가 필요합니다. 변경 사항의 영향과 테스트 방법도 설명해주세요."
    },
    {
        "eval": "negative",
        "label": "needs-more-info",
        "description": "PR의 설명이 매우 모호합니다. 어떤 파일들을 업데이트했는지, 왜 업데이트했는지, 어떤 변경사항이 있는지 구체적으로 설명해주세요. 리뷰어가 변경 사항을 이해하고 평가하기 어렵습니다."
    },
    {
        "eval": "negative",
        "label": "needs-more-info",
        "description": "새로운 기능에 대한 설명이 부족합니다. 이 기능이 무엇인지, 어떻게 구현했는지, 사용자 경험을 어떻게 개선하는지 상세히 설명해주세요. 또한 테스트 방법과 예상되는 영향도 기술해주세요."
    },
    {
        "eval": "negative",
        "label": "needs-more-info",
        "description": "코드 리팩토링의 목적과 구체적인 변경 사항을 설명해주세요. '더 좋게 만들었다'는 설명은 모호합니다. 어떤 파일들이 변경되었는지, 왜 변경되었는지, 어떤 개선이 이루어졌는지 구체적으로 기술해주세요."
    },
    {
        "eval": "negative",
        "label": "needs-more-info",
        "description": "성능 개선에 대한 구체적인 정보가 필요합니다. '더 빨라진 것 같다'는 주관적인 평가보다는, 어떤 부분이 얼마나 개선되었는지 정량적인 데이터를 제공해주세요. 또한 어떤 변경을 통해 성능이 개선되었는지 설명해주세요."
    },
    {
        "eval": "negative",
        "label": "needs-more-info",
        "description": "UI 변경사항에 대한 구체적인 설명이 필요합니다. 어떤 요소들이 변경되었는지, 왜 변경되었는지, 사용자 경험에 어떤 영향을 미칠지 설명해주세요. 가능하다면 변경 전후의 스크린샷을 첨부하는 것도 좋습니다."
    },
    {
        "eval": "negative",
        "label": "needs-more-info",
        "description": "데이터베이스 스키마 변경에 대한 더 자세한 정보가 필요합니다. 어떤 테이블과 컬럼이 추가되었는지, 왜 이러한 변경이 필요한지, 기존 데이터에 미치는 영향은 무엇인지 설명해주세요. 마이그레이션 계획도 포함되면 좋겠습니다."
    },
    {
        "eval": "positive",
        "label": "error-handling",
        "description": "에러 처리 및 로깅 시스템 구현에 대한 상세하고 체계적인 설명이 있는 훌륭한 PR입니다. 각 변경 사항의 목적과 영향이 명확히 기술되어 있으며, 실제 운영 환경에서의 이점도 잘 설명되어 있습니다."
    },
    {
        "eval": "positive",
        "label": "accessibility",
        "description": "웹 애플리케이션의 접근성 개선에 대한 포괄적이고 상세한 설명이 있는 우수한 PR입니다. 각 변경 사항이 어떻게 접근성을 향상시키는지 잘 설명되어 있으며, 다양한 도구로 테스트한 점도 높이 평가됩니다."
    }
]





def fix_json_string(s):
    # 줄 바꿈 제거
    s = s.replace('\\n', ' ').replace('\\r', '')

    # 키의 따옴표를 수정
    s = re.sub(r'(?<!\\\\)"(\\w+)":', r'"\\1":', s)

    # 값의 따옴표를 수정
    s = re.sub(r': "(.+?)"', lambda m: ': "' + m.group(1).replace('"', '\\\\"') + '"', s)

    # 마지막 쉼표 제거 (JSON에서 유효하지 않음)
    s = re.sub(r',\\s*}', '}', s)

    return s


OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
ai = openai.Client(api_key=OPENAI_API_KEY)



def pr_evaluator(prompt):
    response = ai.chat.completions.create(
        model = "gpt-3.5-turbo", 
        messages = [
            {
                "role": "system",
                "content": 
                f"""
                당신은 GitHub에 생성되는 Pull Request를 평가하는 전문 분석가입니다. 다음 가이드라인에 따라 Pull Request를 철저히 평가하세요:

                1. 평가 기준:
                - Positive: 잘 구조화되고, 명확하며, 프로젝트 기여도가 높은 Pull Request
                - Negative: 불명확하거나, 미완성이거나, 프로젝트 가이드라인을 따르지 않은 Pull Request

                2. 주요 평가 항목:
                a) PR 크기와 범위: 적절한 크기인지, 단일 목적에 집중하는지 평가
                b) 설명의 질: PR 설명이 변경 이유, 주요 변경사항, 테스트 방법 등을 포함하는지 확인
                c) 코드 품질: 코드 스타일 가이드 준수, 불필요한 코드 제거, 복잡한 로직에 대한 설명 여부
                d) 테스트: 새로운 기능이나 버그 수정에 대한 테스트 추가 여부
                e) 보안 고려사항: 민감한 정보 노출 여부, 보안 관련 변경사항 주의 필요성
                f) 성능 영향: 변경사항이 성능에 미치는 영향 고려
                g) 종속성 관리: 새로운 종속성 추가나 업데이트의 타당성
                h) 배포 고려사항: 배포 프로세스에 미치는 영향 고려

                3. Positive 평가 시:
                - PR의 강점을 구체적으로 언급하고 칭찬하세요.
                - 개선 가능한 작은 부분이 있다면 건설적인 제안을 해주세요.

                4. Negative 평가 시:
                - 구체적인 문제점을 지적하고, 명확한 개선 방향을 제시하세요.
                - 가능하다면 개선을 위한 리소스나 예시를 제공하세요.

                5. 평가 결과는 다음 JSON 형식으로 제공하세요:
                {{
                    "eval": "positive" 또는 "negative",
                    "label" : issue에 해당하는 label 을 추천해줘.
                    "description": "상세한 평가 메시지, 칭찬 내용 또는 지적 내용, 구체화 추천 내용"
                }}

                반드시 유효한 JSON 형식으로 응답해야 합니다. 줄바꿈이나 특수문자는 이스케이프 처리하세요.
                이슈 라벨 및 설명: {issue_labels}

                각 Pull Request를 철저히 평가하고, 위의 지침에 따라 상세하고 건설적인 피드백을 제공하세요. 당신의 평가는 코드 품질 향상과 개발 프로세스 개선에 중요한 역할을 합니다.
                """
            },
        {
            "role" : "user",
            "content" : f"최근 Pull Request 내용을 평가해줘. 각 PR을 신중히 평가하고, 상세한 피드백을 제공해줘. {pr_input_data[0]}" 

        },
        {
            "role" : "assistant",
            "content" : 
            f"""
            {pr_output_data[0]}
            """
        },
        {
            "role" : "user",
            "content" : f"최근 Pull Request 내용을 평가해줘. 각 PR을 신중히 평가하고, 상세한 피드백을 제공해줘. {pr_input_data[3]}" 

        },
        {
            "role" : "assistant",
            "content" : 
            f"""
            {pr_output_data[3]}
            """
        },
        {
            "role" : "user",
            "content" : f"최근 Pull Request 내용을 평가해줘. 각 PR을 신중히 평가하고, 상세한 피드백을 제공해줘. {pr_input_data[5]}" 

        },
        {
            "role" : "assistant",
            "content" : 
            f"""
            {pr_output_data[5]}
            """
        },
        {
            "role" : "user",
            "content" : f"최근 Pull Request 내용을 평가해줘. 각 PR을 신중히 평가하고, 상세한 피드백을 제공해줘. {pr_input_data[9]}" 

        },
        {
            "role" : "assistant",
            "content" : 
            f"""
            {pr_output_data[9]}
            """
        },
        #-----------------------------------------------------------------
        {
            "role" : "user",
            "content" : f"다음 이슈 내용을 평가해주세요: {prompt}"

        },

    ], max_tokens=1023
    )
 

    json_string = response.choices[0].message.content
    logger.debug(f"Raw response from API: {json_string}")

    # Remove any leading/trailing whitespace and newlines
    json_string = json_string.strip()

    # Remove any potential markdown code block syntax
    json_string = re.sub(r'^```json\\s*|\\s*```$', '', json_string, flags=re.MULTILINE)

    # Fix potential issues with JSON string
    json_string = fix_json_string(json_string)
    logger.debug(f"Processed JSON string: {json_string}")
    

    try:
        # First, try to parse with json.loads
        python_dict = json.loads(json_string)
        print('평가 결과 타입은', type(python_dict))
    except json.JSONDecodeError as e:
        try:
            # If json.loads fails, try ast.literal_eval
            python_dict = ast.literal_eval(json_string)
        except Exception as ast_error:
            # If both methods fail, return an error dictionary with more detailed information
            return {
                "error": "JSON decoding failed",
                "json_error": str(e),
                "ast_error": str(ast_error),
                "raw_string": json_string
            }
        

    return python_dict






# if __name__ == "__main__":
    
#     res = pr_evaluator(pr_output_data[10])
#     print(res)
