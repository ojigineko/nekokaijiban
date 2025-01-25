import requests
import json
import random

# Supabase設定
SUPABASE_URL = 'https://mzxrofrhguxnxvkhzjqr.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im16eHJvZnJoZ3V4bnh2a2h6anFyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Mzc4MTA2NTEsImV4cCI6MjA1MzM4NjY1MX0.p87wyhVNPXnGSu3_xbnAL0y2Jyc5FHK2lEMcj0WZnxs'

# APIヘッダー
headers = {
    'apikey': SUPABASE_KEY,
    'Authorization': f'Bearer {SUPABASE_KEY}',
    'Content-Type': 'application/json',
    'Prefer': 'return=representation'
}

# かわいい猫の名前リスト
CAT_NAMES = [
    'モモ', 'ミケ', 'タマ', 'クロ', 'シロ', 'ハチ', 'ソラ', 'ルナ', 'レオ', 'マル',
    'チャチャ', 'ポテト', 'ゴマ', 'キナコ', 'ずんだ', 'もち', 'プリン', 'ミルク', 'コロ', 'チョコ',
    'ココア', 'ソックス', 'みかん', 'きなこ', 'わさび', 'のり', 'めんま', 'うどん', 'そば', 'まっちゃ'
]

def insert_cat_name():
    """ランダムな猫の名前を挿入"""
    # ランダムに名前を選択
    cat_name = random.choice(CAT_NAMES)
    message = f'かわいい猫の名前: {cat_name}'
    
    try:
        data = {'content': message}
        response = requests.post(
            f'{SUPABASE_URL}/rest/v1/messages',
            headers=headers,
            json=data
        )
        
        print('\n=== 猫の名前を追加 ===')
        print('ステータス:', response.status_code)
        if response.status_code in [200, 201]:
            print('追加された名前:', json.dumps(response.json(), indent=2, ensure_ascii=False))
        else:
            print('エラー:', response.text)
            
    except Exception as e:
        print(f'エラーが発生しました: {str(e)}')

def get_messages():
    """メッセージ一覧を取得"""
    try:
        response = requests.get(
            f'{SUPABASE_URL}/rest/v1/messages?select=*&order=created_at.desc',
            headers=headers
        )
        
        print('\n=== 保存されている猫の名前一覧 ===')
        print('ステータス:', response.status_code)
        if response.status_code == 200:
            messages = response.json()
            if messages:
                for msg in messages:
                    print(f"- {msg['content']} (ID: {msg['id']})")
            else:
                print("まだ名前が登録されていません")
        else:
            print('エラー:', response.text)
            
    except Exception as e:
        print(f'エラーが発生しました: {str(e)}')

if __name__ == '__main__':
    # 5匹分の名前を追加
    for _ in range(5):
        insert_cat_name()
    
    # 保存された名前を表示
    get_messages() 