# API密钥配置说明

## 🎉 好消息：有免费额度！

大部分AI API都有免费额度，对于大创项目完全够用！

## 🆓 推荐的免费AI API

### 1. 智谱AI（GLM）- 最推荐 ⭐⭐⭐⭐⭐
- **免费额度**：有免费额度
- **获取地址**：https://open.bigmodel.cn/
- **模型**：glm-4（免费版）
- **优点**：免费额度充足，中文效果好，适合学生使用

### 2. 通义千问 - 推荐 ⭐⭐⭐⭐
- **免费额度**：有免费额度
- **获取地址**：https://dashscope.aliyun.com/
- **模型**：qwen-plus（免费版）
- **优点**：阿里云提供，稳定可靠

### 3. 豆包 - 可选 ⭐⭐⭐
- **免费额度**：新用户有免费额度
- **获取地址**：https://console.volcengine.com/
- **模型**：ep-20241210170525-mxj9h
- **优点**：字节跳动出品，中文理解能力强

## 📋 快速配置步骤

### 步骤1：选择AI提供商

在 `.env` 文件中设置 `AI_PROVIDER`：
```
AI_PROVIDER=zhipu  # 或 qwen、doubao
```

### 步骤2：获取API密钥

#### 智谱AI（推荐）
1. 访问：https://open.bigmodel.cn/
2. 注册/登录
3. 进入"API Key管理"
4. 创建API Key
5. 复制密钥

#### 通义千问
1. 访问：https://dashscope.aliyun.com/
2. 注册/登录
3. 进入"API-KEY管理"
4. 创建API Key
5. 复制密钥

#### 豆包
1. 访问：https://console.volcengine.com/
2. 搜索"豆包"
3. 开通服务
4. 进入"API密钥管理"
5. 创建API Key
6. 复制密钥

### 步骤3：配置密钥

#### 方式1：使用配置向导（最简单）
```bash
python3 configure_api.py
```

#### 方式2：直接修改.env文件
打开 `.env` 文件，将对应的API密钥填入：
```
# 智谱AI
ZHIPU_API_KEY=你的智谱AI密钥

# 通义千问
QWEN_API_KEY=你的通义千问密钥

# 豆包
DOUBAO_API_KEY=你的豆包密钥
```

### 步骤4：重启服务器
```bash
python3 app.py
```

## 🔧 配置示例

### 使用智谱AI（推荐）
```
AI_PROVIDER=zhipu
ZHIPU_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
ZHIPU_MODEL=glm-4
```

### 使用通义千问
```
AI_PROVIDER=qwen
QWEN_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
QWEN_MODEL=qwen-plus
```

### 使用豆包
```
AI_PROVIDER=doubao
DOUBAO_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
DOUBAO_API_URL=https://ark.cn-beijing.volces.com/api/v3/chat/completions
DOUBAO_MODEL=ep-20241210170525-mxj9h
```

## 💡 切换API提供商

只需修改 `.env` 文件中的 `AI_PROVIDER` 值，然后重启服务器即可：

```bash
# 切换到智谱AI
AI_PROVIDER=zhipu

# 切换到通义千问
AI_PROVIDER=qwen

# 切换到豆包
AI_PROVIDER=doubao
```

## 📊 费用说明

### 免费额度对比

| AI提供商 | 免费额度 | 有效期 | 推荐指数 |
|---------|---------|--------|---------|
| 智谱AI | 充足 | 长期 | ⭐⭐⭐⭐⭐ |
| 通义千问 | 充足 | 长期 | ⭐⭐⭐⭐ |
| 豆包 | 新用户 | 有限期 | ⭐⭐⭐ |

### 大创项目用量估算

- 每次测评：约1000-2000 tokens
- 100次测评：约10-20万 tokens
- 大部分免费额度都够用！

## ❓ 常见问题

### Q: 一定要用API吗？能不能用免费的网页版？
A: 网页版AI（如豆包网页版）需要手动操作，无法自动化集成到网站中。使用API可以实现自动化分析，用户体验更好。

### Q: 免费额度用完了怎么办？
A: 
1. 切换到其他有免费额度的API
2. 申请学生优惠
3. 联系项目指导老师获取资助

### Q: API密钥格式是什么样的？
A: 
- 智谱AI：通常是一串字符
- 通义千问：通常以 `sk-` 开头
- 豆包：通常以 `sk-` 开头

### Q: 配置后还是报错怎么办？
A: 检查：
1. API密钥是否正确复制
2. `AI_PROVIDER` 是否正确设置
3. 网络连接是否正常
4. 查看服务器日志获取详细错误信息

### Q: 可以同时配置多个API吗？
A: 可以！在 `.env` 文件中配置所有API密钥，然后通过 `AI_PROVIDER` 切换使用哪个。

## 🎯 推荐配置

**对于大创项目，推荐使用智谱AI**：
- ✅ 免费额度充足
- ✅ 中文效果好
- ✅ API稳定
- ✅ 适合学生使用

配置步骤：
1. 访问 https://open.bigmodel.cn/ 注册
2. 获取API密钥
3. 在 `.env` 文件中设置：
   ```
   AI_PROVIDER=zhipu
   ZHIPU_API_KEY=你的密钥
   ```
4. 重启服务器

## 📞 获取帮助

如果遇到问题：
1. 查看 `.env` 文件配置是否正确
2. 查看服务器日志
3. 检查网络连接
4. 联系项目指导老师
