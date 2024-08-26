from openai import OpenAI; 
import openai; 
import json; 
import os;
# import datasets from './commit_data_row.json'; 

with open('./commit_datas.json') as json_file:
    json_data = json.load(json_file)
# print(json_data)


OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
ai = openai.Client(api_key=OPENAI_API_KEY)


# client = OpenAI()

data3 = json_data

data = [
    {
        "commit_message": "Add interactive charts to dashboard",
        "commit_date": "2024-07-15",
        "commit_repo": "data-visualization"
    },
    {
        "commit_message": "Implement random forest algorithm",
        "commit_date": "2024-07-16",
        "commit_repo": "machine-learning-model"
    },
    {
        "commit_message": "Update API documentation",
        "commit_date": "2024-07-17",
        "commit_repo": "backend-api"
    },
    {
        "commit_message": "Fix state management bug in user profile",
        "commit_date": "2024-07-18",
        "commit_repo": "frontend-react"
    },
    {
        "commit_message": "Optimize data preprocessing pipeline",
        "commit_date": "2024-07-19",
        "commit_repo": "machine-learning-model"
    }
]

data3 = [
    {
        "commit_message": "Initial setup of React Native project",
        "commit_date": "2024-07-10",
        "commit_repo": "mobile-fitness-app"
    },
    {
        "commit_message": "Implement basic user registration flow",
        "commit_date": "2024-07-12",
        "commit_repo": "mobile-fitness-app"
    },
    {
        "commit_message": "Add Redux for state management",
        "commit_date": "2024-07-14",
        "commit_repo": "mobile-fitness-app"
    },
    {
        "commit_message": "Create README with project setup instructions",
        "commit_date": "2024-07-15",
        "commit_repo": "mobile-fitness-app"
    },
    {
        "commit_message": "Integrate Firebase for backend services",
        "commit_date": "2024-07-17",
        "commit_repo": "mobile-fitness-app"
    },
    {
        "commit_message": "Implement workout tracking feature",
        "commit_date": "2024-07-19",
        "commit_repo": "mobile-fitness-app"
    },
    {
        "commit_message": "Add unit tests for Redux reducers",
        "commit_date": "2024-07-21",
        "commit_repo": "mobile-fitness-app"
    },
    {
        "commit_message": "Optimize app performance and reduce load times",
        "commit_date": "2024-07-23",
        "commit_repo": "mobile-fitness-app"
    }
]

data2 = [
    {
        "commit_message": "Implement user authentication using JWT",
        "commit_date": "2024-07-15",
        "commit_repo": "secure-login-system"
    },
    {
        "commit_message": "Add responsive design to landing page",
        "commit_date": "2024-07-16",
        "commit_repo": "company-website"
    },
    {
        "commit_message": "Optimize database queries for faster load times",
        "commit_date": "2024-07-17",
        "commit_repo": "e-commerce-platform"
    },
    {
        "commit_message": "Create CI/CD pipeline using GitHub Actions",
        "commit_date": "2024-07-18",
        "commit_repo": "devops-tools"
    },
    {
        "commit_message": "Fix memory leak in image processing module",
        "commit_date": "2024-07-19",
        "commit_repo": "photo-editing-app"
    },
    {
        "commit_message": "Add unit tests for user registration process",
        "commit_date": "2024-07-20",
        "commit_repo": "secure-login-system"
    },
    {
        "commit_message": "Implement dark mode toggle",
        "commit_date": "2024-07-21",
        "commit_repo": "company-website"
    },
    {
        "commit_message": "Refactor payment gateway integration",
        "commit_date": "2024-07-22",
        "commit_repo": "e-commerce-platform"
    },
    {
        "commit_message": "Document API endpoints using Swagger",
        "commit_date": "2024-07-23",
        "commit_repo": "e-commerce-platform"
    },
    {
        "commit_message": "Implement caching mechanism for frequently accessed data",
        "commit_date": "2024-07-24",
        "commit_repo": "photo-editing-app"
    }
]
#   응답은 친근하고 격려하는 톤으로 작성해줘. 적절한 이모지를 사용하여 메시지를 강조해주고, 커밋 메시지의 빈도, 다양성, 명확성을 고려해줘. 저장소 간의 활동 분포도 분석에 포함시켜줘.

data4= [{"commit_message": "Update README.md", "commit_date": "2024-07-18", "commit_repo": "minsun24/minsun24"}, {"commit_message": "Update README.md", "commit_date": "2024-07-18", "commit_repo": "minsun24/minsun24"}, {"commit_message": "Update README.md", "commit_date": "2024-07-18", "commit_repo": "minsun24/minsun24"}, {"commit_message": "Update README.md", "commit_date": "2024-07-18", "commit_repo": "minsun24/minsun24"}, {"commit_message": "Update README.md", "commit_date": "2024-07-18", "commit_repo": "minsun24/minsun24"}, {"commit_message": "Update README.md", "commit_date": "2024-07-18", "commit_repo": "minsun24/minsun24"}, {"commit_message": "Initial commit", "commit_date": "2024-07-18", "commit_repo": "minsun24/minsun24"}, {"commit_message": "Update README.md", "commit_date": "2024-07-18", "commit_repo": "MannDyu/ARUM_frontend"}, {"commit_message": "init screen", "commit_date": "2024-07-18", "commit_repo": "MannDyu/ARUM_frontend"}, {"commit_message": "init project", "commit_date": "2024-07-17", "commit_repo": "MannDyu/ARUM_frontend"}, {"commit_message": "Initial commit", "commit_date": "2024-07-15", "commit_repo": "MannDyu/ARUM_backend"}, {"commit_message": "Initial commit", "commit_date": "2024-07-15", "commit_repo": "MannDyu/ARUM_frontend"}, {"commit_message": "Update README.md", "commit_date": "2024-06-05", "commit_repo": "minsun24/Chatting-Program"}, {"commit_message": "client 파일 주석 추가 & 리드미 수정", "commit_date": "2024-06-05", "commit_repo": "minsun24/Chatting-Program"}, {"commit_message": "Update README.md", "commit_date": "2024-06-05", "commit_repo": "minsun24/Chatting-Program"}, {"commit_message": "Update README.md", "commit_date": "2024-06-05", "commit_repo": "minsun24/Chatting-Program"}, {"commit_message": "Update README.md", "commit_date": "2024-06-05", "commit_repo": "minsun24/Chatting-Program"}, {"commit_message": "Add files via upload", "commit_date": "2024-06-05", "commit_repo": "minsun24/Chatting-Program"}, {"commit_message": "Initial commit", "commit_date": "2024-06-05", "commit_repo": "minsun24/Chatting-Program"}, {"commit_message": "Add files via upload", "commit_date": "2023-12-24", "commit_repo": "minsun24/dday_calender"}]

def generate_text(prompt) :
    response = ai.chat.completions.create(
    # model="gpt-3.5-turbo",
    # model="llama3-70b-8192",
    model="gpt-3.5-turbo", 
    messages=[
        {"role": "system", "content": 
         """너는 지금부터 github 활동 분석가야. 주어진 커밋 정보를 바탕으로 커밋 내용을 요약해주고, 추천사항을 제공, 격려의 말을 해줘야 해. 각 세션은 bullet poitn로 구성되어야 해. 
         응답은 친근하고 격려하는 톤으로 작성해줘. 적절한 이모지를 사용하여 메시지를 강조해주고, 커밋 메시지의 빈도, 다양성, 명확성을 고려해줘. 저장소 간의 활동 분포도 분석에 포함시켜줘.
         """},
        {"role": "user", "content": f"'''{data}''' 가 내 최근 활동인데, 나한테 격려할만한 말을 써줘! 줄바꿈 형식과 출력 형식을 잘 기억해서 같은 형식으로 출력해줘."},
        {'role': 'assistant', 
         'content': """
         ** 요약 \n 
         최근 <data-visualiztion> 저장소에서의 작업이 인상적입니다. 데이터 시각화 능력 향상에 집중하고 있군요  👍 
         \n machine-learning-model 저장소의 커밋 빈도가 높습니다. 꾸준한 학습과 개선이 보입니다. 
         \n 'backend-api' 저장소에 단위 테스트를 추가해보세요. 코드의 안정성을 높일 수 있습니다. 
         \n'frontend-react' 프로젝트에서 상태 관리 라이브러리 사용을 고려해보세요. 복잡성 관리에 도움이 될 것입니다. 
         \n오픈 소스 프로젝트에 기여해보는 것은 어떨까요? 새로운 기술을 배우고 커뮤니티와 소통할 좋은 기회가 될 것입니다.
         \n다양한 저장소에 걸쳐 문서화 작업을 꾸준히 하고 있어 좋습니다. 
         \n\n 
         ** 추천사항 
         \n'backend-api' 저장소에 단위 테스트를 추가해보세요. 코드의 안정성을 높일 수 있습니다.  
         \n 'frontend-react' 프로젝트에서 상태 관리 라이브러리 사용을 고려해보세요. 복잡성 관리에 도움이 될 것입니다.
         \n 오픈 소스 프로젝트에 기여해보는 것은 어떨까요? 새로운 기술을 배우고 커뮤니티와 소통할 좋은 기회가 될 것입니다.
         """ }, 
        {"role": "user", "content": f"'''{data}''' 가 내 최근 활동인데, 나한테 격려할만한 말을 써줘!"},
    
        {'role': 'assistant', 
        'content': """
        ** 요약 
        \n모바일 피트니스 앱 개발에 집중하고 있군요. React Native를 사용한 프로젝트 설정부터 주요 기능 구현까지 체계적으로 진행하고 있어 인상적입니다 👍
        \n상태 관리를 위해 Redux를 도입하고, Firebase를 백엔드로 사용하는 등 현대적인 개발 스택을 잘 활용하고 있습니다. 기술 선택이 훌륭해요.
        \n프로젝트 문서화(README 작성)와 테스트 작성에도 신경 쓰고 있어 좋습니다. 이는 프로젝트의 유지보수성과 안정성을 높이는 중요한 실천이에요.
        \n\n 
        ** 추천사항 
        \n사용자 경험(UX)에 더 집중해보는 건 어떨까요? 예를 들어, 사용자 피드백을 수집하고 UI/UX를 개선하는 작업을 추가해보세요. 앱의 성공에 큰 영향을 미칠 수 있습니다.
        \n지속적 통합/배포(CI/CD) 파이프라인을 구축해보세요. 이를 통해 개발 프로세스를 자동화하고 더 빠르게 반복할 수 있을 거예요. GitHub Actions나 Fastlane 같은 도구를 고려해보세요.
        \n성능 최적화 작업을 꾸준히 진행하고 있지만, 더 나아가 프로파일링 도구를 사용해 구체적인 병목점을 찾아내고 개선해보는 것은 어떨까요? React Native의 성능 모니터링 도구들을 활용해보세요.
        """},
        # {"role": "assistant", "content": "'''# Summary\n너의 최근 활동을 보니 열심히 일하고 있네요!\nREADME.md 를 잘 수정하는건 레파지토리 활성화에 도움이 됩니다.\n계속해서 열심히 활동해주세요!'''"},
        {"role": "user", "content": f"'''{prompt}''' 가 내 최근 활동인데, 나한테 격려할만한 말을 써줘! 분석 결과를 요약과 추천사항으로 나누어 제공해주고, 줄바꿈 형식과 출력 형식을 잘 지켜줘. 친구처럼 반말로 해줘."},
        
    ], max_tokens=1023
    )



     #print(response.model_dump_json())
    # print(response.choices[0].message.content)
    # lines = response.choices[0].message.content.splitlines()

    #print(lines)
    # return lines
    return response.choices[0].message.content


if __name__ == "__main__":
    # res = generate_text(data2)
    res = generate_text(data4)
    print(res)  