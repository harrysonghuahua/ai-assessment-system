# AI潜能测评与生涯导航系统

基于大模型的多维度潜能测评与动态生涯路径发展导航工具

## 项目简介

本项目是一个大学生创新创业项目，旨在通过AI技术为用户提供多维度潜能测评和个性化的生涯发展建议。系统集成了性格测评、能力测评、职业兴趣测评和学习风格测评四个维度，通过豆包大模型API生成个性化的分析报告和发展路径建议。

## 功能特点

- **多维度测评**：涵盖性格、能力、职业兴趣、学习风格四个维度
- **AI智能分析**：基于豆包大模型API生成个性化分析报告
- **动态生涯导航**：根据测评结果提供个性化的发展路径建议
- **用户友好界面**：简洁美观的前端界面，良好的用户体验
- **实时反馈**：即时的测评结果展示和建议

## 技术栈

### 前端
- HTML5
- CSS3
- JavaScript (原生)

### 后端
- Python 3.8+
- Flask Web框架
- 豆包API (火山引擎)

## 项目结构

```
ai-career-assessment/
├── app.py                      # Flask应用主文件
├── requirements.txt            # Python依赖包
├── templates/                  # HTML模板文件
│   ├── index.html             # 首页
│   ├── assessment.html        # 测评选择页面
│   ├── quiz.html              # 测评题目页面
│   └── result.html            # 测评结果页面
├── static/                    # 静态资源
│   ├── css/
│   │   └── style.css          # 样式文件
│   └── js/                    # JavaScript文件（预留）
└── data/                      # 数据文件
    ├── personality_questions.json    # 性格测评题目
    ├── ability_questions.json       # 能力测评题目
    ├── interest_questions.json      # 职业兴趣测评题目
    └── learning_questions.json      # 学习风格测评题目
```

## 安装和运行

### 1. 克隆项目

```bash
cd /Users/songhuawei/Desktop/code/ai-career-assessment
```

### 2. 创建虚拟环境（推荐）

```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# 或
venv\Scripts\activate  # Windows
```

### 3. 安装依赖

```bash
pip install -r requirements.txt
```

### 4. 配置环境变量

创建 `.env` 文件并配置豆包API密钥：

```bash
DOUBAO_API_KEY=your-api-key-here
DOUBAO_API_URL=https://ark.cn-beijing.volces.com/api/v3/chat/completions
```

### 5. 运行应用

```bash
python app.py
```

应用将在 `http://localhost:5000` 启动

## 使用说明

1. **首页**：访问应用首页，了解系统功能
2. **选择测评**：在测评选择页面选择要进行的测评类型
3. **完成测评**：按照提示完成测评题目
4. **查看结果**：查看AI生成的个性化分析报告和发展建议

## API配置说明

### 豆包API配置

本项目使用火山引擎的豆包大模型API进行智能分析。配置步骤：

1. 注册火山引擎账号：https://www.volcengine.com/
2. 创建应用并获取API密钥
3. 在 `.env` 文件中配置API密钥和端点

### API调用示例

```python
def call_doubao_api(prompt):
    api_key = os.getenv('DOUBAO_API_KEY')
    api_url = os.getenv('DOUBAO_API_URL')
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }
    
    payload = {
        'model': 'ep-20241210170525-mxj9h',
        'messages': [
            {
                'role': 'system',
                'content': '你是一个专业的心理咨询师和职业规划师...'
            },
            {
                'role': 'user',
                'content': prompt
            }
        ],
        'temperature': 0.7,
        'max_tokens': 2000
    }
    
    response = requests.post(api_url, headers=headers, json=payload)
    return response.json()
```

## 测评维度说明

### 1. 性格测评
- 基于MBTI和五大人格理论
- 分析用户的性格特点和行为风格
- 20道题目，预计完成时间5分钟

### 2. 能力测评
- 评估核心能力和技能水平
- 包括逻辑思维、创造力、沟通能力等
- 15道题目，预计完成时间5分钟

### 3. 职业兴趣测评
- 基于霍兰德职业兴趣理论
- 探索适合用户的职业方向
- 15道题目，预计完成时间4分钟

### 4. 学习风格测评
- 了解用户的学习偏好和认知风格
- 10道题目，预计完成时间3分钟

## 数据存储

测评结果保存在 `data/` 目录下的JSON文件中：
- `personality_results.json`
- `ability_results.json`
- `interest_results.json`
- `learning_results.json`

每个结果包含：
- 时间戳
- 用户答案
- AI生成的分析报告

## 扩展功能建议

1. **用户系统**：添加用户注册和登录功能
2. **历史记录**：保存用户的测评历史记录
3. **对比分析**：提供多次测评结果的对比分析
4. **导出功能**：支持导出PDF格式的测评报告
5. **数据可视化**：添加图表展示测评结果
6. **移动端适配**：优化移动端用户体验

## 注意事项

1. 请妥善保管API密钥，不要泄露
2. 在生产环境中，请修改 `app.py` 中的 `secret_key`
3. 建议使用HTTPS保护用户数据
4. 定期备份测评数据

## 贡献指南

欢迎贡献代码、提出建议或报告问题！

## 许可证

本项目为大创项目，仅供学习和研究使用。

## 联系方式

如有问题或建议，请联系项目团队。

---

**祝您使用愉快！**