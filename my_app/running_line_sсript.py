import cv2
import numpy as np


def create_running_line_video(text, textcolor, backgroundcolor):
    hex = textcolor.lstrip('#')
    color = tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
    # Настраиваем шрифт
    font = cv2.FONT_HERSHEY_COMPLEX
    font_scale = 1.7
    font_color = color
    font_thickness = 2

    titel = text[:50] + hex

    # Задаем цвет фона
    hex = backgroundcolor.lstrip('#')
    color = tuple(int(hex[i:i + 2], 16) for i in (0, 2, 4))

    titel += hex

    # Определяем скорость прокрутки текста за 3 секунды
    text_length = cv2.getTextSize(text, font, font_scale, font_thickness)[0][0]
    scroll_text = (text_length + 100) / (3 * 30)

    # Создаем объект записи видео
    width, height = 100, 100
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    output = cv2.VideoWriter(f'my_app/media/{titel}.mp4', fourcc, 30, (width, height))

    # Координата x начала текста
    text_x = width

    while text_x > -text_length:
        # Создаем фон
        frame = np.zeros((height, width, 3), dtype=np.uint8)
        frame[:,:] = color
        # Вкладываем тескт
        cv2.putText(frame, text, (int(text_x), 65), font, font_scale, font_color, font_thickness)
        # Записываем кадр
        output.write(frame)
        # Прокручиваем тескт
        text_x -= scroll_text

    output.release()
    return titel




