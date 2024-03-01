import telebot
from telebot import types
import base64

class BeautyBot:
    def __init__(self, token):
        self.bot = telebot.TeleBot(token)

    def main_menu_markup(self):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        dry_button = types.KeyboardButton("Сухой тип кожи")
        oily_button = types.KeyboardButton("Жирный тип кожи")
        normal_button = types.KeyboardButton("Нормальный тип кожи")
        combination_button = types.KeyboardButton("Комбинированный тип кожи")
        markup.row(dry_button, oily_button, normal_button, combination_button)
        return markup

    def back_to_main_menu_markup(self):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        home_button = types.KeyboardButton("Домой")
        back_button = types.KeyboardButton("Назад к выбору типа кожи")
        markup.row(home_button)
        markup.row(back_button)
        return markup

    def recommendation_markup(self):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        recommendations = [
            "Рекомендации для сухой кожи",
            "Рекомендации для жирной кожи",
            "Рекомендации для нормальной кожи",
            "Рекомендации для комбинированной кожи"
        ]
        markup.add(*[types.KeyboardButton(recommendation) for recommendation in recommendations])
        return markup

    def start(self):
        @self.bot.message_handler(commands=['start', 'help'])
        def send_welcome(message):
            welcome_message = ("Привет, красотка!\n"
                               "Я твой помощник, чтобы стать красивее и увереннее в себе. "
                               "Выбери свой тип кожи, чтобы я мог предложить тебе рекомендации и советы по уходу 💅")
            self.bot.reply_to(message, welcome_message, reply_markup=self.main_menu_markup())

        @self.bot.message_handler(commands=['cancel'])
        def cancel_operation(message):
            self.bot.send_message(message.chat.id, "Операция отменена. Выбери, что тебя интересует: ", reply_markup=self.main_menu_markup())


        @self.bot.message_handler(func=lambda message: True)
        def handle_skin_type(message):
            skin_type = message.text.lower()
            descriptions = {
                'сухой тип кожи': "Сухой тип кожи характеризуется недостаточным уровнем увлажнения. Кожа может быть шелушиться, напряженной и чувствительной. \n чтобы вернуться назад нажмите /cancel",
                'жирный тип кожи': "Жирный тип кожи характеризуется избыточным выделением кожного сала, что делает кожу блестящей и склонной к появлению угрей и черных точек.\n чтобы вернуться назад нажмите /cancel",
                'нормальный тип кожи': "Нормальный тип кожи имеет здоровый баланс себума и влаги. Кожа выглядит ухоженной, гладкой и упругой.\n чтобы вернуться назад нажмите /cancel",
                'комбинированный тип кожи': "Комбинированный тип кожи объединяет черты сухой и жирной кожи. Обычно лоб, нос и подбородок (T-зона) жирные, а щеки более сухие.\n чтобы вернуться назад нажмите /cancel"
            }

            if skin_type in descriptions:
                markup = self.back_to_main_menu_markup()
                self.bot.reply_to(message, f"Ты выбрала {skin_type}.\n\n{descriptions[skin_type]}\n\nТеперь выбери, что тебя интересует:", reply_markup=self.recommendation_markup())
            elif message.text == "Назад к выбору типа кожи":
                self.bot.send_message(message.chat.id, "Выбери свой тип кожи:", reply_markup=self.main_menu_markup())
            elif message.text.startswith("Рекомендации для"):
                recommendation_type = message.text.split(" ")[2].lower()
                recommendation_text = f"Здесь будут рекомендации для {recommendation_type} \n чтобы вернуться назад нажмите /cancel"
                if recommendation_type == "сухой":
                    with open("/Users/gazizatanirbergen/PycharmProjects/новый бот бьюти/.venv/lib/dry.jpg", "rb") as a:
                        self.bot.send_photo(message.chat.id, photo=a, caption=recommendation_text)
                elif recommendation_type == "жирной":
                    with open("/Users/gazizatanirbergen/PycharmProjects/новый бот бьюти/.venv/lib/oily.jpeg", "rb") as b:
                        self.bot.send_photo(message.chat.id, photo=b, caption=recommendation_text)
                elif recommendation_type == "нормальной":
                    with open("/Users/gazizatanirbergen/PycharmProjects/новый бот бьюти/.venv/lib/dry.jpg", "rb") as c:
                        self.bot.send_photo(message.chat.id, photo=c, caption=recommendation_text)
                elif recommendation_type == "комбинированной":
                    with open("/Users/gazizatanirbergen/PycharmProjects/новый бот бьюти/.venv/lib/dry.jpg", "rb") as d:
                        self.bot.send_photo(message.chat.id, photo=d, caption=recommendation_text)
            else:
                self.bot.reply_to(message, "Пожалуйста, выбери тип кожи из предложенных вариантов.")

        self.bot.infinity_polling()

if __name__ == "__main__":
    token = "7163957184:AAFiXVesSVqC9LIa6FhbiQBkY74rdHV7n3Y"
    beauty_bot = BeautyBot(token)
    beauty_bot.start()
