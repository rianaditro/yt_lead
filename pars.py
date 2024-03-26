from bs4 import BeautifulSoup


class Parser:
    def __init__(self,html):
        self.soup = BeautifulSoup(html,"html.parser")
    
    def get_channels(self):
        def change_to_float(text):
            if "\xa0rb subscriber" in text:
                text = text.replace("\xa0rb subscriber", "").replace(",", ".")
                return float(text)*1000
            else:
                text = text.replace(" subscriber", "")
                return float(text)

        result = []
        # item_list = self.soup.find_all("div", {"id": "metadata"})
        channels = self.soup.find_all("yt-formatted-string", {"id": "subscribers"})
        subscribers = self.soup.find_all("span", {"id": "video-count"})

        for i in range(len(channels)):
            channel = channels[i].text
            subscriber = subscribers[i].text
            value = {"channels": channel, "subscribers": change_to_float(subscriber)}
            result.append(value)
        

        # for item in item_list:
        #     channels = item.find("yt-formatted-string", {"id": "subscribers"}).text
        #     subscribers = item.find("span", {"id": "video-count"}).text
        #     item_result = {"channels": channels, "subscribers": change_to_float(subscribers)}
        #     print(item_result)
        #     result.append(item_result)

        return result


if __name__ == "__main__":
    with open('rs.html', 'r') as file:
        html = file.read()

    parser = Parser(html)
    ls = parser.get_channels()
    print(ls)