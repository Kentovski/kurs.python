import io
import re
from urllib.parse import urlencode
import logging
from concurrent import futures
import lxml.html as html


def get_urls(url):
    logging.info("Opening initial url - %s" % url)
    parsed = html.parse(url)
    last_link = parsed.xpath("//a[contains(@class, 'last')]")
    try:
        last_link_number = int(last_link[0].attrib['href'].split('=')[1])
    except Exception:
        logging.error("Can't load main page %s" % url)
        exit(1)
    urls = [(initial_url + '?' + urlencode({'p': page}))  for page in range(0, last_link_number+1)]
    if urls:
        logging.info("Got list of category pages. Total  - %d items" % len(urls))
    else:
        logging.error("Error while fetching the list of urls" % url)
    return urls


def get_page_items(url):
    logging.info("Open page with url - %s" % url)
    page_content = html.parse(url)
    items = page_content.xpath("//div[contains(@class, 'gd')]/div[contains(@class, 'gd-box')]")
    if not items:
        logging.error("Items of page %s could'n be fetched" % url)
    return items


def get_item(item, out):
    if (item.cssselect("div.gd-price-sum>div:first-child")[0].text is None):
        price = item.cssselect("div.gd-price-sum>div:first-child>b")[0].text
    else:
        price = item.cssselect("div.gd-price-sum>div:first-child")[0].text
    price = re.sub("[^0-9]", "", price)
    title = item.cssselect("b>a[data-eventlabel]")[0].text.rstrip()
    logging.info("Got item with title: %s and price %s" % (title, price))
    print(title, price, sep=';', file=out)


def main():
    initial_url = 'http://hotline.ua/computer/noutbuki-netbuki/'
    logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(message)s')
    output = io.StringIO()

    urls = get_urls(initial_url)

    with futures.ThreadPoolExecutor(max_workers=3) as executor:
        queue = []
        for url in urls:
            future = executor.submit(get_page_items, url)
            queue.append(future)

        for future in futures.as_completed(queue):
            res = future.result()
            for item in res:
                get_item(item, output)

    # print(output.getvalue())

if __name__ == '__main__':
    main()
