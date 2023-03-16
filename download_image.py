import os.path
import urllib.request


class DownloadImage:
    def __init__(self, url, max_, file_path):
        self.url_lst = url.split("<>")
        self.max = max_
        self.file_path = file_path

    def download_image_url(self):
        try:
            print(self.delete_all_files())
            count = 1

            for _ in range(self.max):
                url = self.url_lst[0] + str(count) + self.url_lst[1]
                print(url)

                if count < 10:
                    urllib.request.urlretrieve(url, self.file_path + "0" + str(count) + ".jpg")
                else:
                    urllib.request.urlretrieve(url, self.file_path + str(count) + ".jpg")
                count += 1
        except:
            return "Error"

    def download_url_image(self):
        pass

    def find_dir(self):
        if not os.path.exists(self.file_path):
            os.mkdir(self.file_path)
            return "Complete Mkdir"

        return "Already Exist"

    def delete_all_files(self):
        self.find_dir()

        for file in os.scandir(self.file_path):
            os.remove(file.path)

        return "Complete Delete"


if __name__ == "__main__":
    down = DownloadImage("https://doc.coursemos.co.kr/kmu/225659/610a9aa6d5f9d7c1a2020e912d7f235a8444d8d5/610a9aa6d5f9d7c1a2020e912d7f235a8444d8d5.files/<>.png", 45, "./image/")
    down.download_image_url()


