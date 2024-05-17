import scrapy


class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/perm/category/svet"]

    def parse(self, response):
        # Получаем все элементы на странице, соответствующие CSS-селектору 'div.lsooF'
        divans = response.css('div.lsooF')

        # Проходим по каждому найденному элементу
        for divan in divans:
            # Извлекаем название дивана
            name = divan.css('span[itemprop="name"]::text').get()
            # Извлекаем цену дивана из атрибута content внутри meta[itemprop="price"]
            price = divan.css('meta[itemprop="price"]::attr(content)').get()
            # Извлекаем URL для дивана из атрибута href внутри a
            url = divan.css('a::attr(href)').get()

            # Преобразуем относительный URL в абсолютный
            absolute_url = response.urljoin(url)

            # Возвращаем полученные данные как словарь
            yield {
                'name': name,
                'price': price,
                'url': absolute_url
            }

