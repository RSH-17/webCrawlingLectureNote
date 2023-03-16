from PIL import Image
import os


class ConvertToPdf:
    def __init__(self, file_path, pdf_path):
        self.file_path = file_path
        self.pdf_path = pdf_path

    def convert_folder_image(self):
        file_list = os.listdir(self.file_path)

        img_list = []

        img_path = self.file_path + file_list[0]
        im_buf = Image.open(img_path)
        cvt_rgb_0 = im_buf.convert('RGB')

        for i in file_list:
            img_path = self.file_path + i
            im_buf = Image.open(img_path)
            cvt_rgb = im_buf.convert('RGB')
            img_list.append(cvt_rgb)

        del img_list[0]
        cvt_rgb_0.save(self.pdf_path + 'convert.pdf', save_all=True, append_images=img_list)


if __name__ == "__main__":
    con = ConvertToPdf("./image/", "./")
    con.convert_folder_image()
