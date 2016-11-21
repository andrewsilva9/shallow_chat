import chatbot_brain

bot = chatbot_brain.Chatbot()
bot.user_feeling = 'happy'
print(bot.get_started())
while True:
	input_t = input("> ")
	response = bot.respond_to(input_t)
	print(response)