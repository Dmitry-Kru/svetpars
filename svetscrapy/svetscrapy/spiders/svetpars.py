import scrapy

class SvetparsSpider(scrapy.Spider):
    name = "svetpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        # Создаём переменную, в которую будет сохраняться информация
        svet = response.css('div._Ud0k')
        # Настраиваем работу с каждым отдельным светильником в списке
        for item in svet:
            yield {
                # Создаём словарик названий, используем поиск по диву, а внутри дива — по тегу span
                'name': item.css('div.lsooF span::text').get(),
                # Создаём словарик цен, используем поиск по диву, а внутри дива — по тегу span
                'price': item.css('div.pY3d2 span::text').get(),
                # Создаём словарик ссылок, используем поиск по тегу "a", а внутри тега — по атрибуту
                # Атрибуты — это настройки тегов
                'url': item.css('a').attrib['href']
            }
