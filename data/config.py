from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
IP = env.str("ip")
EMAIL = env.str("EMAIL")
PG_USER = env.str("PG_USER")
PG_PASSWORD = env.str("PG_PASSWORD")
PORT = env.str("PORT")
PATH_TO_DOCS_FROM_NCBI = env.str("PATH_TO_DOCS_FROM_NCBI")
