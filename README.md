# Bài tập Lập trình Web 
## Sinh viên
Hoàng Đình Điệp

## Yêu cầu
- Cài đặt môi trường Linux (WSL Ubuntu) và Docker Compose
- Triển khai 5 dịch vụ: Nginx, Node-RED, MariaDB, phpMyAdmin, Cloudflared
- Cấu hình Nginx phục vụ 2 domain riêng biệt: lab1 và lab2
- Xây dựng API trên Node-RED, cấu hình proxy qua Nginx
- Viết JavaScript gọi API và hiển thị dữ liệu trên trang HTML
- Public ra internet bằng Cloudflare Tunnel với domain thật

## thực hiện (7 commit)

### 1. `docs: khoi tao repo, xac nhan da cai WSL Ubuntu`
Khởi tạo repo, xác nhận đã cài WSL Ubuntu.

### 2. `chore: da cai dat Docker + Docker Compose`
Cài đặt Docker và Docker Compose trên WSL Ubuntu.
<img width="1483" height="762" alt="Screenshot 2026-09-28 000616" src="https://github.com/user-attachments/assets/9c59cc0d-bbaf-4d81-90ca-30156a668296" />

### 3. `feat: tao cau truc thu muc va docker-compose.yml cho 5 dich vu`
Tạo cấu trúc thư mục và file `docker-compose.yml` khai báo 5 dịch vụ: nginx, nodered, mariadb, phpmyadmin, cloudflared.
<img width="1483" height="762" alt="Screenshot 2026-09-28 001038" src="https://github.com/user-attachments/assets/f14894ab-8325-4ab1-b53e-30ad40df65c3" />

### 4. `feat: cau hinh nginx 2 domain lab1 va lab2, them anh minh chung`
Cấu hình Nginx phục vụ 2 domain riêng biệt qua Cloudflare Tunnel.
<img width="1920" height="1020" alt="Screenshot 2026-09-28 005940" src="https://github.com/user-attachments/assets/2d160910-a724-4dfc-9eea-affb6997222b" />
<img width="1920" height="1020" alt="Screenshot 2026-09-28 005945" src="https://github.com/user-attachments/assets/c2d7a102-21a4-4c28-9d8c-11b1e7da19e4" />

### 5. `feat: tao API /api/tacke tren Node-RED, them anh minh chung`
Tạo API `/api/tacke` trên Node-RED (http in → function → http response).
<img width="1920" height="1020" alt="Screenshot 2026-09-28 005932" src="https://github.com/user-attachments/assets/8af7157c-4a25-45d9-86d6-e5bfca4b258a" />

### 6. `feat: them proxy /api/ tren nginx lab1 toi nodered`
Cấu hình Nginx proxy `/api/` từ domain thật tới Node-RED.
<img width="1920" height="1020" alt="Screenshot 2026-09-28 013026" src="https://github.com/user-attachments/assets/905216db-5d36-48e7-a023-f6483b15cddd" />

### 7. `feat: hoan thanh JS goi API va hien thi du lieu, them anh minh chung`
Viết JavaScript trong trang HTML gọi API và hiển thị bảng dữ liệu.
<img width="1920" height="1020" alt="Screenshot 2026-09-28 005940" src="https://github.com/user-attachments/assets/c1597c8c-6113-45d2-a8f7-55ddae9f64c0" />

# Môn an toàn và bảo mật thông tin
### 1 quy trình mã hoá/giải mã cài đặt AES trên ngôn ngữ lập trình python
<img width="1920" height="1020" alt="Screenshot 2026-09-28 030606" src="https://github.com/user-attachments/assets/5d242f41-d8c8-4815-940c-49acae76c348" />
<img width="1920" height="1020" alt="Screenshot 2026-09-28 030623" src="https://github.com/user-attachments/assets/b8e601c9-5920-4ebe-841e-c528a771511f" />

### 2 phần còn lại em làm trong file an toàn và bảo mật thông tin
