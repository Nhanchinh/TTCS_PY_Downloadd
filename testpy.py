import requests
from bs4 import BeautifulSoup

# Giả sử bạn đang truy cập vào một URL có chứa thẻ <a> này
url1 = 'https://tbtvietnam.edu.vn/blog/tu-vung-hsk-2/'
response = requests.get(url1)

# Phân tích nội dung HTML
soup = BeautifulSoup(response.text, 'lxml')

# Tìm thẻ <a> chứa văn bản '...'
link = soup.find('a', string='tại đây')

# Lấy giá trị thuộc tính href
if link:
    print(link.get('href'))  # In ra giá trị của href
else:
    print("Không tìm thấy thẻ <a> có văn bản này")


url = link.get('href')
# Bước 1: Chuyển đổi URL Google Drive sang dạng tải trực tiếp
file_id = url.split('/d/')[1].split('/view')[0]  # Trích xuất file ID từ URL
download_url = f'https://drive.google.com/uc?export=download&id={file_id}'

print(f"URL tải trực tiếp: {download_url}")

# Bước 2: Gửi yêu cầu HTTP để tải file
response = requests.get(download_url)

# Bước 3: Kiểm tra trạng thái phản hồi và lưu file
if response.status_code == 200:
    # Lưu file PDF với tên mong muốn
    with open('hsk2.pdf', 'wb') as file:
        file.write(response.content)
    print("File đã được tải về thành công.")
else:
    print(f"Không thể tải file. Mã trạng thái: {response.status_code}")
