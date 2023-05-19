# -- coding: utf-8 --
from lxml import html
import os

etree = html.etree

import requests
import urllib.parse


def get_filename_from_url(url):
    parsed_url = urllib.parse.urlparse(url)
    file_path = urllib.parse.unquote(os.path.basename(parsed_url.path))
    return file_path


def download_image(url, save_path):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        content_length = response.headers.get('content-length')

        with open(save_path, 'wb') as file:
            file.write(response.content)

        print(f"Downloaded {url} successfully. Status code: {response.status_code}, Content length: {content_length}")
    else:
        print(f"Failed to download {url}. Status code: {response.status_code}")


def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)


def read_files_in_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            with open(file_path, 'r') as file:
                if not file_path.endswith(".txt"):
                    continue
                # print(file_path)
                content = file.read()
                s = etree.HTML(content)
                img_elements = s.xpath('//img')

                # 遍历img标签，判断是否存在src属性
                for img in img_elements:
                    if 'src' in img.attrib:
                        src_value = img.attrib['src']
                        # print(src_value)
                        filename = get_filename_from_url(src_value)
                        save_directory = './data/notes/photos'
                        create_directory(save_directory)
                        save_path = os.path.join(save_directory, filename)
                        # print(save_path)
                        if not os.path.exists(save_path):
                            download_image(src_value, save_path)


# 调用函数来读取目录下的文件
directory_path = './data/notes'
read_files_in_directory(directory_path)
