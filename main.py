from simp_bot import Bot
from bot import LongPollBot

if __name__ == '__main__':
    # long poll bot start with an automatic response to managed messages
    long_poll_bot = LongPollBot()
    long_poll_bot.run_long_poll()