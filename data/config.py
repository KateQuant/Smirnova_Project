from environs import Env

env = Env()
env.read_env()

EMAIL = env.str("EMAIL")