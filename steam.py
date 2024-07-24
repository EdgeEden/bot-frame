import requests
import parsel
import csv


def get_steam(start):
    url = f'https://store.steampowered.com/contenthub/querypaginated/specials/TopSellers/render/?query=&start='\
          + str(start)+'&count=6&cc=CN&l=schinese&v=4&tag='
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)
    datasheet = []

    html_data = response.json()['results_html']
    # print(html_data)

    selector = parsel.Selector(html_data)
    lis = selector.css('a.tab_item')
    for li in lis:
        title = li.css('.tab_item_name::text').get()
        tag_list = li.css('.tab_item_top_tags .top_tag::text').getall()
        tag = ''.join(tag_list)
        price = li.css('.discount_original_price::text').get()
        price_1 = li.css('.tab_item_discount .discount_final_price::text').get()
        discount = li.css('.tab_item_discount .discount_pct::text').get()
        # print(title, tag, price, price_1, discount, href)

        dit = {
            '游戏': title,
            '标签': tag,
            '原价': price,
            '售价': price_1,
            '折扣': discount,
        }
        datasheet.append(dit)

    try:
        f = open('SteamDsc.csv', mode='r+', encoding='utf-8')
        f.truncate(0)
        f.close()
    except FileNotFoundError:
        pass

    with open('SteamDsc.csv', mode='a', encoding='utf-8', newline='') as f:
        for i in datasheet:
            csv_writer = csv.DictWriter(f, fieldnames=[
                '游戏',
                '标签',
                '原价',
                '售价',
                '折扣',
            ])
            csv_writer.writerow(i)
            if datasheet.index(i) == 5:
                break

