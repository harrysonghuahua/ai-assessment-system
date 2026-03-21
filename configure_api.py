#!/usr/bin/env python3
"""
API密钥配置向导
帮助用户快速配置豆包API密钥
"""

import os

def configure_api():
    print("=" * 60)
    print("🔑 豆包API密钥配置向导")
    print("=" * 60)
    print()
    
    print("这个向导将帮助你配置豆包API密钥。")
    print("如果你还没有API密钥，请先访问以下网址获取：")
    print("https://console.volcengine.com/")
    print()
    
    # 获取API密钥
    api_key = input("请输入你的豆包API密钥（以sk-开头）: ").strip()
    
    if not api_key:
        print("❌ 未输入API密钥，配置取消。")
        return False
    
    if not api_key.startswith('sk-'):
        print("⚠️  警告：API密钥通常以'sk-'开头，请确认是否正确。")
        confirm = input("是否继续？(y/n): ").strip().lower()
        if confirm != 'y':
            print("❌ 配置取消。")
            return False
    
    # 获取API URL（使用默认值）
    print()
    api_url = input("请输入API URL（直接回车使用默认值）: ").strip()
    if not api_url:
        api_url = "https://ark.cn-beijing.volces.com/api/v3/chat/completions"
    
    # 获取模型名称（使用默认值）
    model = input("请输入模型名称（直接回车使用默认值）: ").strip()
    if not model:
        model = "ep-20241210170525-mxj9h"
    
    # 写入.env文件
    env_content = f"""# API配置文件
DOUBAO_API_KEY={api_key}
DOUBAO_API_URL={api_url}
DOUBAO_MODEL={model}
"""
    
    env_file = os.path.join(os.path.dirname(__file__), '.env')
    
    try:
        with open(env_file, 'w', encoding='utf-8') as f:
            f.write(env_content)
        
        print()
        print("=" * 60)
        print("✅ 配置成功！")
        print("=" * 60)
        print()
        print(f"API密钥: {api_key[:10]}...{api_key[-4:]}")
        print(f"API URL: {api_url}")
        print(f"模型: {model}")
        print()
        print("配置已保存到 .env 文件")
        print()
        print("下一步：")
        print("1. 重启服务器：python3 app.py")
        print("2. 访问网站测试AI分析功能")
        print()
        
        return True
        
    except Exception as e:
        print()
        print(f"❌ 保存配置失败：{e}")
        return False

if __name__ == '__main__':
    configure_api()
