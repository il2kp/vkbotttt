import bs4 as bs4
import requests


class VkBot:

    def __init__(self, user_id):
        print("\nСоздан объект бота!")

        self._USER_ID = user_id
        self._USERNAME = self._get_user_name_from_vk_id(user_id)

        self._COMMANDS = ["ПРИВЕТ", "ХОЧУ", "ВРЕМЯ", "ПОКА"]

    def _get_user_name_from_vk_id(self, user_id):
        request = requests.get("https://vk.com/id"+str(user_id))
        bs = bs4.BeautifulSoup(request.text, "html.parser")

        user_name = self._clean_all_tag_from_str(bs.findAll("title")[0])

        return user_name.split()[0]

    def new_message(self, message):
        count = 0
        if (count == 0):
            if (message.upper() == self._COMMANDS[0]):
                return f"Привет-привет, {self._USERNAME}!"
        # Время
            elif message.upper() == self._COMMANDS[2]:
                return self._get_time()
        # Пока
            elif message.upper() == self._COMMANDS[3]:
                return f"Пока-пока, {self._USERNAME}!"
            elif (message.upper() == "хочу") or (message.upper() == "Хочу") or (message.upper() == "ХОЧУ"):
                return f"Привет-привет, {self._USERNAME}! Ваш промокод на скидку 10% KOVALEV2020.Хотите посетить пробный урок?"
            elif (message.upper() == "да") or (message.upper() == "ДА") or (message.upper() == "Да") or (message.upper() == "lf"):
                return f"Отлично, {self._USERNAME}! Уроки проходят по адресу 70 лет октября 16 (ост. 70 лет октября или 11 микрорайон).Пробный урок бесплатный, по времени займёт 30 минут. В какой день вам будет удобно?"
            elif (message.upper() != "0"):
                return f"Хорошо, {self._USERNAME}!"
        else:
          return "Вопрос сложный.Наш преподаватель скоро ответит вам..."

    def _get_time(self):
        request = requests.get("https://my-calend.ru/date-and-time-today")
        b = bs4.BeautifulSoup(request.text, "html.parser")
        return self._clean_all_tag_from_str(str(b.select(".page")[0].findAll("h2")[1])).split()[1]

    @staticmethod
    def _clean_all_tag_from_str(string_line):

        """
        Очистка строки stringLine от тэгов и их содержимых
        :param string_line: Очищаемая строка
        :return: очищенная строка
        """

        result = ""
        not_skip = True
        for i in list(string_line):
            if not_skip:
                if i == "<":
                    not_skip = False
                else:
                    result += i
            else:
                if i == ">":
                    not_skip = True

        return result
