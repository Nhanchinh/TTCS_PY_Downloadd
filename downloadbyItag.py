import requests
from bs4 import BeautifulSoup

# URL của trang web chứa liên kết tải xuống
url = 'https://example.com'  # Thay bằng URL thực tế
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

# Tìm thẻ <i> có class "fa fa-download"
icon = soup.find('i', class_='fa fa-download')

# Kiểm tra nếu thẻ <i> có tồn tại
if icon:
    # Tìm thẻ cha <a> hoặc thẻ có chứa liên kết (vd: <a> hoặc <button>)
    parent = icon.find_parent(['a', 'button'])
    
    if parent and parent.has_attr('href'):
        # Lấy liên kết từ thuộc tính href
        download_url = parent['href']
        print(f"Liên kết tải xuống: {download_url}")
        
        # Tải xuống file từ liên kết
        response = requests.get(download_url)
        if response.status_code == 200:
            with open('downloaded_file', 'wb') as file:
                file.write(response.content)
            print("File đã được tải về thành công.")
        else:
            print(f"Không thể tải file. Mã trạng thái: {response.status_code}")
    else:
        print("Không tìm thấy thẻ cha chứa liên kết.")
else:
    print("Không tìm thấy thẻ <i> có class 'fa fa-download'.")
