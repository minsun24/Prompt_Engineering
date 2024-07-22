# from openai import OpenAI
from dotenv import load_dotenv
import openai
import os
import re
import json
import ast

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
ai = openai.Client(api_key=api_key)

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

my_data= [{"commit_message": "Update README.md", "commit_date": "2024-07-18", "commit_repo": "minsun24/minsun24"}, {"commit_message": "Update README.md", "commit_date": "2024-07-18", "commit_repo": "minsun24/minsun24"}, {"commit_message": "Update README.md", "commit_date": "2024-07-18", "commit_repo": "minsun24/minsun24"}, {"commit_message": "Update README.md", "commit_date": "2024-07-18", "commit_repo": "minsun24/minsun24"}, {"commit_message": "Update README.md", "commit_date": "2024-07-18", "commit_repo": "minsun24/minsun24"}, {"commit_message": "Update README.md", "commit_date": "2024-07-18", "commit_repo": "minsun24/minsun24"}, {"commit_message": "Initial commit", "commit_date": "2024-07-18", "commit_repo": "minsun24/minsun24"}, {"commit_message": "Update README.md", "commit_date": "2024-07-18", "commit_repo": "MannDyu/ARUM_frontend"}, {"commit_message": "init screen", "commit_date": "2024-07-18", "commit_repo": "MannDyu/ARUM_frontend"}, {"commit_message": "init project", "commit_date": "2024-07-17", "commit_repo": "MannDyu/ARUM_frontend"}, {"commit_message": "Initial commit", "commit_date": "2024-07-15", "commit_repo": "MannDyu/ARUM_backend"}, {"commit_message": "Initial commit", "commit_date": "2024-07-15", "commit_repo": "MannDyu/ARUM_frontend"}, {"commit_message": "Update README.md", "commit_date": "2024-06-05", "commit_repo": "minsun24/Chatting-Program"}, {"commit_message": "client 파일 주석 추가 & 리드미 수정", "commit_date": "2024-06-05", "commit_repo": "minsun24/Chatting-Program"}, {"commit_message": "Update README.md", "commit_date": "2024-06-05", "commit_repo": "minsun24/Chatting-Program"}, {"commit_message": "Update README.md", "commit_date": "2024-06-05", "commit_repo": "minsun24/Chatting-Program"}, {"commit_message": "Update README.md", "commit_date": "2024-06-05", "commit_repo": "minsun24/Chatting-Program"}, {"commit_message": "Add files via upload", "commit_date": "2024-06-05", "commit_repo": "minsun24/Chatting-Program"}, {"commit_message": "Initial commit", "commit_date": "2024-06-05", "commit_repo": "minsun24/Chatting-Program"}, {"commit_message": "Add files via upload", "commit_date": "2023-12-24", "commit_repo": "minsun24/dday_calender"}]


test_data = [
    {"commit_message": "Initial commit", "commit_date": "2024-07-15", "commit_repo": "MannDyu/ARUM_frontend"},
    {"commit_message": "init screen", "commit_date": "2024-07-18", "commit_repo": "MannDyu/ARUM_frontend"},
    {"commit_message": "Update README.md", "commit_date": "2024-07-18", "commit_repo": "MannDyu/ARUM_frontend"},
    {"commit_message": "Initial commit", "commit_date": "2024-06-05", "commit_repo": "minsun24/Chatting-Program"},
    {"commit_message": "client 파일 주석 추가 & 리드미 수정", "commit_date": "2024-06-05", "commit_repo": "minsun24/Chatting-Program"},
    {"commit_message": "Add files via upload", "commit_date": "2023-12-24", "commit_repo": "minsun24/dday_calender"}
]


def fix_json_string(s):
    # 키의 따옴표를 수정
    s = re.sub(r'(?<!\\\\)"(\\w+)":', r'"\\1":', s)
    # 값의 따옴표를 수정
    s = re.sub(r': "(.+?)"', lambda m: ': "' + m.group(1).replace('"', '\\\\"') + '"', s)
    return s



def generate_text(prompt) :
    response = ai.chat.completions.create(
    # model="gpt-3.5-turbo",
    # model="llama3-70b-8192",
    model="gpt-3.5-turbo", 
    
    messages=[
        {"role": "system", "content": 
         """
         You are now a GitHub activity analyst. Your task is to analyze the given commit information and provide:

            1. Summary of commit content
            2. Recommendations for improvement
            3. Words of encouragement

            Guidelines:
            - Use a friendly and encouraging tone
            - Structure each section with bullet points
            - Use appropriate emojis frequently to emphasize messages 😊
            - Consider commit message frequency, diversity, and clarity
            - Include analysis of activity distribution across repositories
            - When mentioning repository names, enclose them in angle brackets, e.g., <repo-name>

            Response format:
            - Provide the analysis in JSON format with keys: "summary" and "recommendation"
            - Ensure all keys and string values in the JSON are enclosed in double quotes
            - Do not include a comma after the last item in each array

            Additional notes:
            - Pay attention to the commit message frequency, diversity, and clarity
            - Provide specific, actionable recommendations
            - Be encouraging and highlight positive aspects of the user's activity

            Please respond in English and use emojis liberally throughout your response.

         """},
         
        {
        "role": "user",
        "content": f"""Analyze the following recent GitHub activities:

        '''
        {data}
        '''

        Please provide:
        1. An encouraging summary of my activities
        2. Helpful recommendations based on my commit history

        Guidelines:
        - Use a friendly and supportive tone
        - Respond entirely in English
        - Use emojis generously to add emphasis and positivity
        - Maintain the specified JSON format for your response
        - Ensure proper line breaks and formatting in your output

        I'm looking forward to your insightful analysis and motivating feedback!"""
        }, 
        {
            'role': 'assistant',
            'content': """
            {
                "summary": [
                    "Your recent work in the <data-visualization> repository is impressive! 🎉 You're clearly focused on enhancing your data visualization skills. Keep it up! 👍",
                    "The commit frequency in the <machine-learning-model> repository is notable. 📊 Your consistent learning and improvement are evident. Great job! 🌟",
                    "It's great to see you working across various repositories. 🔀 This diversity shows your versatility as a developer!",
                    "Your commitment to documentation across different repositories is commendable. 📚 This practice greatly enhances project maintainability. Well done! ✨",
                    "The balance between frontend and backend work demonstrates your full-stack capabilities. 💻 You're building a well-rounded skill set!"
                ],
                "recommendation": [
                    "Consider adding unit tests to your <backend-api> repository. 🧪 This can significantly improve code stability and make future changes easier.",
                    "For the <frontend-react> project, explore using a state management library. 🔄 It could help manage complexity as your project grows.",
                    "Why not contribute to an open source project? 🌐 It's a great opportunity to learn new technologies and connect with the developer community!",
                    "Keep up with the latest trends in data visualization. 📈 Maybe try incorporating interactive elements in your next <data-visualization> project!",
                    "For your <machine-learning-model> work, consider documenting your model's performance metrics. 📊 It's crucial for tracking improvements over time."
                ]
            }
            """
        },

        
        {
            "role": "user",
            "content": f"""Analyze the following recent GitHub activities:

            '''
            {data3}
            '''

            Please provide an encouraging summary and helpful recommendations based on my commit history. 
            Remember to respond in English and use plenty of emojis!
            """
        },

        {
            'role': 'assistant',
            'content': """
            {
                "summary": [
                    "Wow! You're fully immersed in developing a mobile fitness app using React Native! 📱💪 Your systematic approach from project setup to core feature implementation is truly impressive! 🌟",
                    "Great job incorporating modern development stacks! 🚀 Using Redux for state management and Firebase as a backend shows you're making excellent technology choices. 👨‍💻",
                    "It's fantastic to see you paying attention to project documentation (README) and writing tests. 📚✅ This is crucial for maintaining and stabilizing your project. Keep it up! 🎉",
                    "Your commitment to optimizing app performance and reducing load times is commendable. ⚡ This focus on user experience will make your app stand out! 🏆",
                    "Adding unit tests for Redux reducers shows your dedication to code quality. 🧪 This practice will pay off in the long run! 💯"
                ],
                "recommendation": [
                    "Consider diving deeper into user experience (UX) design. 🎨 Collecting user feedback and improving UI/UX can significantly impact your app's success. Why not add some user testing to your workflow? 👥",
                    "Think about setting up a CI/CD pipeline to automate your development process. 🔄 Tools like GitHub Actions or Fastlane can help you iterate faster and more efficiently. 🚀",
                    "While you're doing great with performance optimization, consider using profiling tools to identify and improve specific bottlenecks. 📊 React Native has some great performance monitoring tools you could leverage! 🛠️",
                    "As your app grows, you might want to explore more advanced state management techniques. 🧠 Look into Redux Saga or Redux Thunk for handling complex asynchronous actions. 🔀",
                    "Don't forget to celebrate your progress! 🎊 Each feature you implement is a step forward. How about treating yourself after each major milestone? You deserve it! 🍕"
                ]
            }
            """
        },
        {
            "role": "user",
            "content": f"""Analyze these recent GitHub activities and provide encouraging feedback:

            '''
            {test_data}
            '''

            Please respond in English with a summary and recommendations. Don't forget to use plenty of emojis!"""
        },

        {
            "role": "assistant",
            "content": """
            {
                "summary": [
                    "Wow! You're juggling multiple projects and making great progress! 🎉 Your work on <MannDyu/ARUM_frontend> shows you're diving deep into initial setup and screen configuration. You're really nailing those crucial early stages! 🚀",
                    "I see you're enhancing the <minsun24/Chatting-Program> by adding comments and updating the README.md. That's a fantastic way to improve code comprehension! 📚👀",
                    "Your attention to project documentation (especially README files) is commendable. 📝 This practice significantly boosts project maintainability and stability. Keep it up! 🌟",
                    "It's impressive how you're actively implementing new ideas across various projects. Your initiative in setting up multiple repositories shows your diverse interests and skills! 🌈💻",
                    "The commit on <minsun24/dday_calender> from late 2023 shows you're maintaining and revisiting older projects too. That's great long-term thinking! 🗓️👍"
                ],
                "recommendation": [
                    "For projects in their early stages, like <MannDyu/ARUM_frontend>, consider clearly defining and documenting your goals and key features. This roadmap will be invaluable as you progress! 🎯📊",
                    "To elevate your code quality, think about implementing continuous refactoring and writing more test code. This will make your projects much easier to maintain in the long run. 🧹🧪",
                    "Why not explore collaboration opportunities? Strengthening teamwork on projects like <MannDyu/ARUM_frontend> and contributing to open-source could really boost your technical growth. 🤝🌐",
                    "For your chat program, consider adding some automated tests to ensure reliability as you continue to develop. It's a great way to catch bugs early! 🐛🔍",
                    "Don't forget to celebrate your progress! Each commit, whether it's an initial setup or a README update, is a step forward. You're doing great! 🎊🏆"
                ]
            }
            """
        },
                        
                
        
        # {"role": "user", "content": f"'''{prompt}''' 가 
        #  내 최근 활동인데, 나한테 격려할만한 말을 써줘! 분석 결과를 요약과 추천사항으로 나누어 제공해주고, 모든 답변을 영어로 대답해줘. "},
        {
            "role": "user",
            "content": f"""Analyze my recent GitHub activities:

            '''
            {prompt}
            '''

            Please provide:
            1. An encouraging summary of my activities
            2. Helpful recommendations based on my commit history

            Guidelines:
            - Use a friendly and supportive tone
            - Respond entirely in English
            - Use emojis generously to add emphasis and positivity
            - Structure your response in JSON format with "summary" and "recommendation" keys
            - Enclose repository names in angle brackets, e.g., <repo-name>
            - Consider commit message frequency, diversity, and clarity in your analysis
            - Include insights on activity distribution across repositories

            I'm looking forward to your motivating feedback and insightful analysis!"""
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
    my_data= [{"commit_message": "Update README.md", "commit_date": "2024-07-18", "commit_repo": "minsun24/minsun24"}, {"commit_message": "Update README.md", "commit_date": "2024-07-18", "commit_repo": "minsun24/minsun24"}, {"commit_message": "Update README.md", "commit_date": "2024-07-18", "commit_repo": "minsun24/minsun24"}, {"commit_message": "Update README.md", "commit_date": "2024-07-18", "commit_repo": "minsun24/minsun24"}, {"commit_message": "Update README.md", "commit_date": "2024-07-18", "commit_repo": "minsun24/minsun24"}, {"commit_message": "Update README.md", "commit_date": "2024-07-18", "commit_repo": "minsun24/minsun24"}, {"commit_message": "Initial commit", "commit_date": "2024-07-18", "commit_repo": "minsun24/minsun24"}, {"commit_message": "Update README.md", "commit_date": "2024-07-18", "commit_repo": "MannDyu/ARUM_frontend"}, {"commit_message": "init screen", "commit_date": "2024-07-18", "commit_repo": "MannDyu/ARUM_frontend"}, {"commit_message": "init project", "commit_date": "2024-07-17", "commit_repo": "MannDyu/ARUM_frontend"}, {"commit_message": "Initial commit", "commit_date": "2024-07-15", "commit_repo": "MannDyu/ARUM_backend"}, {"commit_message": "Initial commit", "commit_date": "2024-07-15", "commit_repo": "MannDyu/ARUM_frontend"}, {"commit_message": "Update README.md", "commit_date": "2024-06-05", "commit_repo": "minsun24/Chatting-Program"}, {"commit_message": "client 파일 주석 추가 & 리드미 수정", "commit_date": "2024-06-05", "commit_repo": "minsun24/Chatting-Program"}, {"commit_message": "Update README.md", "commit_date": "2024-06-05", "commit_repo": "minsun24/Chatting-Program"}, {"commit_message": "Update README.md", "commit_date": "2024-06-05", "commit_repo": "minsun24/Chatting-Program"}, {"commit_message": "Update README.md", "commit_date": "2024-06-05", "commit_repo": "minsun24/Chatting-Program"}, {"commit_message": "Add files via upload", "commit_date": "2024-06-05", "commit_repo": "minsun24/Chatting-Program"}, {"commit_message": "Initial commit", "commit_date": "2024-06-05", "commit_repo": "minsun24/Chatting-Program"}, {"commit_message": "Add files via upload", "commit_date": "2023-12-24", "commit_repo": "minsun24/dday_calender"}]

    res = generate_text(my_data)
    print(res)