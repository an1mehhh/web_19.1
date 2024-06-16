from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs


class MyServer(BaseHTTPRequestHandler):
    """
        Специальный класс, который отвечает за
        обработку входящих запросов от клиентов
    """

    @staticmethod
    def __get_html_content() -> str:
        """
        Считывание html страницы
        """
        with open("index.html", "r", encoding='utf-8') as file:
            html_content: str = file.read()
        return html_content

    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        query_components = parse_qs(urlparse(self.path).query)
        print(query_components)
        page_content = self.__get_html_content()
        self.send_response(200)  # Отправка кода ответа
        self.send_header("Content-type", "text/html")  # Отправка типа данных, который будет передаваться
        self.end_headers()  # Завершение формирования заголовков ответа
        self.wfile.write(bytes(page_content, "utf-8"))  # Тело ответа
