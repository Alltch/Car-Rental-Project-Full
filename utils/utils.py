from datetime import datetime
import configparser

import telebot
from telebot import types

from utils.utils import get_token, get_contacts, get_contact_by_id, update_contact, delete_contact, save_to_excel
from keyboards.buttons import menu_button

CONFIG = configparser.ConfigParser()
CONFIG.read('config.ini')
TOKEN = CONFIG['Telebot']['TOKEN']


bot = telebot.TeleBot(TOKEN, parse_mode="HTML")


@bot.message_handler(commands=['start'])
def handle_start_command(message: types.Message):
    """Приветственное сообщение при старте бота."""
    bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}!", reply_markup=menu_button())


@bot.message_handler(func=lambda message: message.text.lower() == 'получить все заявки')
def handle_get_all_applications(message: types.Message):
    """Получение всех заявок и отправка их в виде Excel-файла."""
    contacts = get_contacts()
    if not contacts:
        bot.send_message(message.chat.id, "Заявки не найдены.")
        return

    bot.send_document(message.chat.id, open(save_to_excel(contacts), 'rb'))


@bot.message_handler(func=lambda message: message.text.lower() == 'получить заявку по id')
def handle_get_application_by_id_prompt(message: types.Message):
    """Запрос ID заявки для дальнейшего поиска."""
    bot.send_message(message.chat.id, "Введите ID заявки:")
    bot.register_next_step_handler(message, handle_get_application_by_id)


def handle_get_application_by_id(message: types.Message):
    """Обработка ID заявки и отображение информации."""
    contact_id = message.text.strip()
    contact = get_contact_by_id(contact_id)

    if isinstance(contact, dict):
        application_info = (
            f"\nID заявки: {contact.get('id')}"
            f"\nПолное имя: {contact.get('full_name')}"
            f"\nНомер телефона: {contact.get('phone_number')}"
            f"\nДата начала аренды: {contact.get('date_start')}"
            f"\nДата окончания аренды: {contact.get('date_end')}"
            f"\nГород: {contact.get('city').capitalize()}"
            f"\nАвтомобиль: {contact['auto']['brand']} {contact['auto']['model']}\n"
            f"\n<b>Прочитано: {'Да' if contact.get('is_read') else 'Нет'}</b>"
        )

    else:
        application_info = contact

    bot.send_message(message.chat.id, application_info)


def handle_update_application_status(message: types.Message):
    """Обновление статуса заявки (прочитано/непрочитано)."""
    try:
        contact_id = int(message.text)
    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, введите правильный ID заявки (число).")
        bot.register_next_step_handler(message, handle_update_application_status)
        return

    contact = get_contact_by_id(contact_id)
    if not contact:
        bot.send_message(message.chat.id, "Заявка с таким ID не найдена. Попробуйте снова.")
        return

    contact['is_read'] = True
    updated_contact = update_contact(contact_id, contact)

    updated_info = (
        f"\nID заявки: {updated_contact.get('id')}"
        f"\nПолное имя: {updated_contact.get('full_name')}"
        f"\nНомер телефона: {updated_contact.get('phone_number')}"
        f"\nДата начала аренды: {updated_contact.get('date_start')}"
        f"\nДата окончания аренды: {updated_contact.get('date_end')}"
        f"\nГород: {updated_contact.get('city').capitalize()}"
        f"\nАвтомобиль: {contact['auto']['brand']} {contact['auto']['model']}\n"
        f"\n<b>Прочитано: {'Да' if updated_contact.get('is_read') else 'Нет'}</b>"
    )

    bot.send_message(message.chat.id, f'Статус заявки обновлен. Обновленная информация:\n{updated_info}')


@bot.message_handler(func=lambda message: message.text.lower() == 'обновить статус заявки')
def handle_update_application_status_prompt(message: types.Message):
    """Запрос ID заявки для обновления статуса."""
    bot.send_message(message.chat.id, "Пожалуйста, введите ID заявки:")
    bot.register_next_step_handler(message, handle_update_application_status)


bot.polling(none_stop=True)