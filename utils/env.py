from environs import Env

env = Env()
env.read_env()


BOT_TOKEN = env('BOT_TOKEN')
ADMIN = env('ADMIN')

SOURCE_GROUP_ID = env('SOURCE_GROUP_ID')
TARGET_GROUP_ID = env('TARGET_GROUP_ID')