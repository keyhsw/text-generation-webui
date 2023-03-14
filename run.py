import os
os.system('python download-model.py PygmalionAI/pygmalion-350m --branch main')
# os.system('python download-model.py waifu-workshop/pygmalion-6b --branch original-sharded')
os.system('python server.py --cpu --cai-chat --model pygmalion-350m')