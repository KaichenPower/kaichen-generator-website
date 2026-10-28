---
title: "Máy phát điện diesel dự phòng cho bệnh viện: hướng dẫn chọn công suất"
date: "2026-10-28"
excerpt: "Cách chọn công suất máy phát điện diesel dự phòng bệnh viện: bảng phụ tải, tính kVA, khởi động động cơ, dự trữ nhiên liệu, dự phòng và kiểm tra bằng băng tải giả."
image: "/images/blog/hospital-generator-sizing.jpg"
---

![Máy phát điện diesel cách âm dự phòng bệnh viện tại nhà máy Yangzhou của chúng tôi](/images/blog/hospital-generator-sizing.jpg)

# Máy phát điện diesel dự phòng cho bệnh viện: hướng dẫn chọn công suất

Mất điện trong bệnh viện không phải là bất tiện. Trong vài giây, phòng mổ mất đèn, máy thở ở hồi sức chuyển sang pin chỉ trụ được vài phút chứ không phải vài giờ, tủ bảo quản máu bắt đầu vượt 6 °C, thang máy dừng giữa hai tầng với bệnh nhân bên trong, và hệ thống gọi điều dưỡng tắt ngấm.

Vì vậy **máy phát điện diesel dự phòng cho bệnh viện** được chỉ định khác với máy cho nhà xưởng hay công trường. Nó không phải “tổ máy lớn nhất vừa ngân sách”, mà là một cỗ máy an toàn tính mạng, với công suất, hành vi khởi động, dự trữ nhiên liệu, độ ồn và hồ sơ kiểm tra phải bảo vệ được trước thanh tra cấp chứng nhận.

Hướng dẫn này đi theo trình tự tính toán thực tế chúng tôi dùng cho dự án bệnh viện: lập bảng phụ tải, chuyển sang kVA với các hiệu chỉnh cần thiết, kiểm tra khởi động động cơ, rồi chốt nhiên liệu, dự phòng, tiếng ồn và phạm vi kiểm tra. Số liệu lấy từ bảng dữ liệu dòng KC của chúng tôi, gồm hai tổ máy thực tế thuộc cấp bệnh viện.

## 1. Máy phát thực sự cấp điện cho gì trong bệnh viện

Hệ thống điện bệnh viện thường chia thành nguồn bình thường và một hoặc vài thanh cái thiết yếu. Chỉ thanh cái thiết yếu đấu vào máy phát. Xác định đúng ranh giới này là một nửa công việc.

| Nhóm phụ tải | Nội dung điển hình | Ý nghĩa với việc chọn công suất |
|---|---|---|
| An toàn tính mạng | Chiếu sáng phòng mổ và hồi sức, báo cháy, hút khói, chiếu sáng thoát nạn, báo động khí y tế | Chuyển nguồn trong khoảng 10 giây, không bao giờ được cắt |
| Tối quan trọng | Thiết bị hồi sức và sơ sinh, lọc máu, làm lạnh ngân hàng máu, chuỗi lạnh dược, tủ ấm xét nghiệm, CNTT và gọi điều dưỡng | Ổn định điện áp quan trọng hơn công suất thô |
| Thiết bị | Thang máy, bơm nước, bơm chữa cháy, điều hòa, tiệt trùng, một phần bếp và giặt là | Khởi động động cơ quyết định, không phải công suất chạy |
| Tùy chọn | Ổ cắm buồng bệnh, điều hòa tiêu chuẩn, một phần bếp | Thường không đấu vào hoặc bị cắt khi quá tải |

Từ đó ra hai nguyên tắc. Một: đừng đưa toàn bệnh viện lên máy phát nếu ngân sách và bồn nhiên liệu không chịu nổi — phần lớn dự án giữ 40–60 % phụ tải đấu nối trên thanh cái thiết yếu. Hai: coi phụ tải động cơ là bài toán khởi động, không phải công suất chạy; động cơ thang máy 15 kW có thể kéo 5–7 lần dòng định mức trong một hai giây.

Khung pháp lý khác theo quốc gia — NFPA 99 và NFPA 110 ở Mỹ, HTM 06-01 ở Anh, IEC 60364-7-710 cho khu vực y tế ở châu Âu và nhiều thị trường xuất khẩu. Khác chi tiết nhưng đồng thuận ở cốt lõi: thanh cái thiết yếu xác định, thời gian chuyển nguồn xác định, thời lượng nhiên liệu xác định và kiểm tra định kỳ có ghi chép. Xác nhận bản địa phương trước khi chốt kVA.

## 2. Bảng phụ tải trước, kVA sau

Mọi tranh luận về công suất máy phát bệnh viện thực chất là tranh luận về bảng phụ tải. Lập trên bảng tính, từng mạch.

Mỗi hạng mục ghi bốn dữ liệu: kW trên nhãn, hệ số công suất, hệ số nhu cầu (bao nhiêu chạy cùng lúc) và phương pháp khởi động (trực tiếp, sao-tam giác, khởi động mềm, biến tần).

Ví dụ bệnh viện đa khoa 200 giường có chiller, bếp và giặt là trên thanh cái thiết yếu. Đây là số liệu quy hoạch, không thay thế sơ đồ một sợi của dự án:

| Phụ tải | kW đấu nối | Hệ số nhu cầu | kW khi chạy |
|---|---|---|---|
| Phòng mổ, hồi sức, chiếu sáng khẩn cấp, hệ thống cháy | 120 | 1,0 | 120 |
| Thiết bị hồi sức, ngân hàng máu, dược, CNTT | 90 | 1,0 | 90 |
| Thang máy (4 × 15 kW) | 60 | 0,6 | 36 |
| Chiller (một máy trên thanh cái thiết yếu) | 90 | 1,0 | 90 |
| Bơm, xử lý nước, bơm chữa cháy | 55 | 1,0 | 55 |
| Bếp và giặt là, một phần | 60 | 1,0 | 60 |
| **Tổng khi chạy** | | | **451** |

Hệ số đa dạng 0,9 cho khoảng **406 kW**. Cộng dự phòng phát triển — bệnh viện thêm chẩn đoán hình ảnh, thêm giường, thêm điều hòa — nên 20 % là mức hợp lý: **487 kW**. Tổ máy tiêu chuẩn gần nhất là **500 kW / 625 kVA**.

Sau đó xem lại trường hợp khởi động. Nếu chiller khởi động trực tiếp với dòng gấp sáu lần trong khi phòng mổ đã có tải, tổ máy phải hấp thụ bậc này mà điện áp không tụt đến mức ngắt thiết bị y tế. Nếu không đạt, câu trả lời không phải mặc định là máy lớn hơn: mà là khởi động mềm hoặc biến tần cho chiller, thường rẻ hơn 200 kW máy phát thêm.

## 3. Công thức và bốn hiệu chỉnh

Quy đổi cơ bản đơn giản:

**kVA = kW ÷ hệ số công suất**

Với hệ số 0,8 trễ tiêu chuẩn của tổ máy 50 Hz của chúng tôi, 400 kW phụ tải chạy cần 500 kVA máy phát trước hiệu chỉnh. Sau đó áp dụng bốn hiệu chỉnh.

**Dự phòng phát triển.** 15–25 % cho bệnh viện mới, vì không ai thiết kế theo số giường hôm nay.

**Khởi động động cơ và tải bậc.** Độ tụt áp tức thời phải nằm trong mức thiết bị y tế chịu được. Bảng dữ liệu dòng KC của chúng tôi quy định: sai lệch áp tức thời ≤ 15 %, điều chỉnh áp xác lập ≤ 0,5 %, sai lệch tần số tức thời ≤ 0,5 % và thời gian hồi phục áp và tần số ≤ 3 giây. Đó chính là điều màn hình theo dõi ở hồi sức cảm nhận khi chuyển nguồn.

**Giảm định mức theo hiện trường.** Tổ máy định mức 40 °C mất công suất ở 45 °C và mất nhiều hơn ở độ cao. Nếu phòng máy nóng vì két giải nhiệt thổi vào góc, hoặc giảm định mức hoặc sửa đường gió.

**Chế độ làm việc.** Định mức dự phòng (số giờ hạn chế, không quá tải) so với định mức chính (liên tục, quá tải 10 % trong một giờ). Bệnh viện chạy máy tám giờ khi sửa lưới là chế độ dự phòng; bệnh viện mất điện hằng ngày là chế độ chính và phải chỉ định như vậy.

## 4. Hai mốc tham chiếu thực

Hướng dẫn trừu tượng dễ viết khó áp dụng. Đây là hai tổ máy chúng tôi chế tạo cho công trình bệnh viện, số liệu lấy trực tiếp từ bảng kỹ thuật KC.

| Thông số | KC-YC200 | KC-YC1600 |
|---|---|---|
| Công suất định mức / dự phòng | 200 kW / 220 kW | 1.600 kW / 1.760 kW |
| Điện áp / dòng điện | 380/220 V, 360 A | 380/220 V, 2.880 A |
| Tần số, hệ số công suất | 50 Hz, 0,8 trễ | 50 Hz, 0,8 trễ |
| Động cơ | Yuchai YC6MK350L-D20, 235 / 258,5 kW | Yuchai YC16VTD2700-D30, 1.805 / 1.985 kW |
| Số xy-lanh / dung tích | Thẳng hàng 6, 10,34 L, 123 × 145 mm | V16, 52,26 L, 152 × 180 mm |
| Tăng áp / bộ điều tốc | Turbo làm mát trung gian, điện tử | Turbo làm mát trung gian, điện tử |
| Tiêu hao nhiên liệu | 200 g/kWh | 200 g/kWh |
| Máy phát | KCI-200, không chổi than, AVR, IP23, cấp H, đồng | KCI-1600, không chổi than, AVR, IP23, cấp H, đồng |
| Kích thước (D × R × C) | 3.000 × 1.100 × 1.750 mm | 5.500 × 2.200 × 2.700 mm |
| Khối lượng | 2.800 kg | 15.800 kg (tham khảo) |
| Độ ồn (LP7M) | 102 dB(A) | 102 dB(A) |

**Khi nào phù hợp cấp 200 kW.** Phòng khám, trung tâm phẫu thuật trong ngày, bệnh viện nhỏ và nhà chẩn đoán hình ảnh có thanh cái thiết yếu chỉ gồm chiếu sáng phòng mổ, thiết bị hồi sức, hệ thống cháy, CNTT và vài thang máy, chiller ở nguồn bình thường. Với 2.800 kg và dài 3 m, máy vào được phòng máy tầng hầm bằng xe nâng tay, rất quan trọng khi cải tạo với cửa rộng 1,2 m.

**Khi nào phù hợp cấp 1.600 kW.** Bệnh viện khu vực và bệnh viện giảng dạy có thanh cái thiết yếu thực sự gồm chiller trung tâm, bếp, giặt là, chẩn đoán hình ảnh và 10–20 thang máy. Với 15.800 kg và 5,5 m cần phòng máy thật, bệ sàn hoặc khu đặt ngang mặt đất, phương án cẩu và thường hai tổ song song chứ không phải một.

Giữa hai cỡ có các bậc trung gian; điểm chính là bảng dữ liệu phải đủ để kỹ sư thiết kế đưa số liệu trực tiếp vào mô hình điện.

## 5. Dự trữ nhiên liệu: câu hỏi 72 giờ

Nhiên liệu là chỗ quy định bệnh viện hay trượt kiểm tra nhất, vì tiêu hao ghi theo kWh và người ta quên quy đổi.

Với 200 g/kWh và diesel khoảng 0,84 kg/L:

**Lít mỗi giờ = kW định mức × 0,2 ÷ 0,84**

| Phụ tải (KC-YC200) | Nhiên liệu mỗi giờ | Trong 24 giờ | Trong 72 giờ |
|---|---|---|---|
| 100 % (200 kW) | 47,6 L/h | 1.143 L | 3.429 L |
| 50 % trung bình (100 kW) | 23,8 L/h | 571 L | 1.714 L |
| 25 % trung bình (50 kW) | 11,9 L/h | 286 L | 857 L |

Vậy tổ 200 kW với mức trung bình thực tế nửa tải cần khoảng **1.700 L cho 72 giờ**. Chỉ định bồn chính 2.000 L sẽ còn dư và cả thể tích không dùng được. Với tổ 1.600 kW ở nửa tải là khoảng **4.570 L mỗi 24 giờ**, nên bệnh viện lớn dùng bồn chôn hoặc bồn có bể chứa tràn kèm hợp đồng lọc nhiên liệu, chứ không dùng bồn trên bệ máy.

Ba chi tiết thanh tra xem: **bồn ngày** cho 8 giờ chạy (để sự cố bồn chính không dừng máy ngay), **bể chứa tràn 110 %** thể tích và **báo mức cao/thấp** đấu về hệ thống quản lý tòa nhà. Trên đường nhiên liệu, van chặn chống cháy ở đầu ra bồn, và tuyệt đối không đi qua thang bộ.

## 6. Dự phòng, song song và chuyển nguồn

Một máy phát là một điểm hỏng duy nhất. Bệnh viện hiếm khi chấp nhận ở công trình mới.

| Sơ đồ | Ý nghĩa | Ứng dụng điển hình |
|---|---|---|
| N | Một tổ đủ cho phụ tải thiết yếu | Phòng khám, bệnh viện nhỏ |
| N+1 | Thêm một tổ có thể gánh tải khi bất kỳ tổ nào hỏng | Bệnh viện đa khoa, 3 × 500 kW cho tải 1.000 kW |
| 2N | Hai nguồn độc lập hoàn chỉnh, phòng riêng | Bệnh viện giảng dạy, khu y tế lớn |

Song song cho nhiều hơn dự phòng: hai tổ ở 60 % thay vì một tổ 100 % giảm tiêu hao và tiếng ồn ban đêm, và bảo trì được một tổ trong khi tổ kia gánh tải. Bộ điều khiển của chúng tôi hỗ trợ chia tải, chia tải đẳng tốc và đồng bộ tự động, có thanh cái liên kết để tách một tổ.

Về chuyển nguồn, chốt sớm thời gian chuyển. Mạch an toàn tính mạng thường được mong có điện trong khoảng 10 giây; phòng mổ và hồi sức bù khoảng trống này bằng UPS hoặc chuyển nguồn tĩnh thay vì chờ máy phát tức thời. Kiểm tra toàn bộ trình tự — mất lưới, tín hiệu ATS, đề máy, tạo áp, đóng máy cắt, nhận tải — trên bệ thử, không phải đêm mất điện.

## 7. Tiếng ồn, vị trí và hàng xóm

Hai tổ máy trong bảng là loại bệ hở, 102 dB(A) ở 7 mét theo điểm tham chiếu LP7M. Đây là mức lớn, cỡ máy cưa xích. Chấp nhận được trong phòng máy cách âm tốt hoặc khu xa, không chấp nhận được ở 30 mét từ cửa sổ buồng bệnh.

Các lựa chọn theo chi phí:

- **Vỏ cách âm** — thường đưa tổ máy xuống khoảng 70–75 dB(A) ở 7 m.
- **Xử lý âm phòng** — bọc tiêu âm, cửa kín, sàn nổi và bộ tiêu âm gió vào ra tính đúng. Với tổ lớn, phòng thường là cách rẻ hơn để đạt giới hạn biên nghiêm ngặt.
- **Vị trí** — quay hướng thổi két giải nhiệt và ống khói ra xa mặt buồng bệnh, kiểm tra chiều cao ống khói so với cửa sổ mở gần nhất.

Kiểm tra giới hạn biên địa phương trước khi chọn vì khác nhau nhiều; nhiều nơi áp dụng khoảng 45–55 dB(A) tại điểm nhận nhạy cảm gần nhất vào ban đêm. Đừng cho rằng chỉ vỏ cách âm là đủ với máy 1,6 MW — không đủ.

## 8. Chi tiết lắp đặt quyết định thành bại

Đây là những thứ biến bảng dữ liệu đúng thành công trình chạy được:

- **Gió làm mát.** Két giải nhiệt cần cửa vào thông thoáng và cửa ra dẫn ống ra ngoài. Phòng có nan chớp cỡ hòm thư sẽ làm giảm định mức và nung nóng máy phát.
- **Áp ngược ống xả.** Tuyến dài, cút gấp và bộ tiêu âm nhỏ làm tăng áp ngược và mất công suất. Thiết kế với áp ngược tối đa nhà cung cấp cho phép trong tay.
- **Cách ly rung.** Đệm lò xo hoặc cao su dưới bệ, bù giãn ống xả và đầu nối nhiên liệu mềm. Không có chúng, tiếng ồn truyền qua sàn lên các khoa phía trên.
- **Tiết diện cáp.** Tính theo dòng định mức ở nhiệt độ thực và giữ cáp động lực và điều khiển ở máng riêng.
- **Nối đất và trung tính.** Xác nhận sơ đồ nối đất với kỹ sư điện bệnh viện: cách xử lý trung tính của máy phát phải khớp với hệ thống, không phải ngược lại.
- **Ngăn cháy.** Phòng máy phát là một khoang cháy có hệ thống phát hiện riêng và thường có chữa cháy riêng.
- **Lối tiếp cận.** Để trống đầu máy phát và hai bên động cơ: tổ máy không bảo trì được sẽ hỏng sớm.

## 9. Kiểm tra: phần đa số nhà cung cấp bỏ qua

Máy phát bệnh viện được đánh giá vào đêm cần đến nó. Vì vậy mọi tổ máy rời nhà máy Yangzhou của chúng tôi đều lên băng tải giả kỹ thuật số trước khi giao, theo trình tự cố định:

| Bước | Thời gian giữ | Nội dung kiểm tra |
|---|---|---|
| Không tải | — | Sấy máy, áp dầu, điện áp nạp |
| Tải 25 % | 30 phút | Ổn định áp và tần số, nhiệt độ khí xả |
| Tải 50 % | 30 phút | Phản ứng bộ điều tốc, tiêu hao, độ ồn |
| Tải 75 % | 60 phút | Hệ thống làm mát, nhiệt độ nước làm mát, độ căng dây đai |
| Tải 100 % | 60 phút | Công suất định mức đầy đủ, điều chỉnh áp trong ±1,5 % |
| Quá tải 110 % | 1 phút | Ngắt bảo vệ và kiểm tra báo động |

Sau khi chạy, chúng tôi kiểm tra điện trở cách điện và liên tục tiếp địa sau chu trình nhiệt, xác nhận mọi chức năng bảo vệ (quá tốc, nhiệt độ nước cao, áp dầu thấp, quá dòng, dừng khẩn) và kiểm tra trình tự ATS từ đầu đến cuối trên bệ. Báo cáo thử đi kèm tổ máy.

Nếu dự án cần thử có chứng kiến, báo cáo giám định bên thứ ba (BV, SGS hoặc TUV) hoặc quy trình FAT riêng cho công trình, phải đặt trước khi tổ máy vào sản xuất, không phải tuần trước khi giao.

## 10. Vì sao bệnh viện làm việc với Kaichen

Chúng tôi chế tạo tổ máy phát tại Dương Châu, Trung Quốc, từ 20 kVA đến 3.000 kVA, và mảng bệnh viện là phần quan trọng trong công việc. Ba điều quan trọng hơn ở phân khúc này.

**Chúng tôi tự làm máy phát.** Dòng KCI quấn dây đồng, cách điện cấp H, bảo vệ IP23, điều chỉnh AVR và sản xuất cùng cơ sở với dây chuyền lắp ráp. Khi bệnh viện cần đáp ứng quá độ cụ thể, chúng tôi thay máy phát chứ không đi mua ngoài.

**Chúng tôi thử đầy tải tại xưởng.** Băng tải giả kỹ thuật số 2 MW cho phép chứng minh tổ 1.600 kW ở 110 % trước khi giao, không chỉ chạy không tải ngoài sân.

**Chúng tôi làm tài liệu theo ngôn ngữ khách hàng.** Bảng dữ liệu, hướng dẫn vận hành và bảo trì, mô tả logic điều khiển và nhãn máy có thể cấp theo các ngôn ngữ chúng tôi xuất bản, giúp rút ngắn chạy thử khi đội công trường không nói tiếng Anh.

Tham chiếu bệnh viện của chúng tôi từ tổ 200 kW cho bệnh viện thành phố đến công trình cấp 1.600–1.800 kW cho khu bệnh viện khu vực, gồm những máy đã trực dự phòng nhiều năm với thử tải theo kế hoạch. Mỗi lô hàng kèm hồ sơ CE và ISO 9001, bộ phụ tùng cho kỳ bảo trì đầu và hỗ trợ kỹ thuật 24/7 trong chạy thử.

## Câu hỏi thường gặp

**Bệnh viện cần máy phát công suất bao nhiêu?**
Phụ thuộc thanh cái thiết yếu, không phụ thuộc số giường. Phòng khám có chiếu sáng phòng mổ, thiết bị hồi sức và hai thang máy thường cần 150–250 kW. Bệnh viện đa khoa 200 giường có chiller trên thanh cái thiết yếu thường rơi vào 400–600 kW. Khu bệnh viện khu vực có bếp, giặt là, chẩn đoán hình ảnh và hơn 15 thang máy thường cần 1.200–2.000 kW, thường hai tổ trở lên song song.

**Nhiên liệu nên đủ bao lâu?**
Quy định phổ biến yêu cầu 72 giờ ở tải xác định, đôi khi 96 giờ cho cơ sở trọng yếu. Tính bồn từ tiêu hao thực g/kWh ở tải trung bình dự kiến: tổ 200 kW nửa tải cần khoảng 1.700 L cho 72 giờ.

**Máy phát diesel có cấp được phòng mổ không?**
Có, nhưng không trực tiếp. Phòng mổ thường được cấp qua UPS hoặc chuyển nguồn tĩnh bù 10–30 giây đến khi máy phát nhận tải; sau đó máy phát giữ áp và tần số trong giới hạn thiết bị y tế chịu được.

**Dùng vỏ cách âm hay bệ hở cho bệnh viện?**
Cách âm cho mọi thứ nghe thấy từ buồng bệnh, nhân viên hoặc ranh giới. Bệ hở chỉ thực tế trong phòng máy cách âm tốt hoặc khu xa.

**Bao lâu thử máy phát bệnh viện một lần?**
Chạy không tải hoặc tải thấp hằng tháng cộng thử đầy tải hằng năm trên băng tải là nền tảng phổ biến; nhiều hệ thống chứng nhận yêu cầu thử hằng tháng có ghi chép và thử tải định mức hằng năm. Thử ATS cùng lúc, không tách riêng.

## Bước tiếp theo

Nếu bạn đang chỉ định tổ máy cho bệnh viện, gửi cho chúng tôi bảng phụ tải thanh cái thiết yếu và điều kiện công trường — độ cao, nhiệt độ môi trường, giới hạn ồn tại biên, thời lượng nhiên liệu yêu cầu — chúng tôi sẽ chọn công suất theo trường hợp khởi động thực thay vì quy tắc ngón tay. Xem cấp máy chúng tôi chế tạo tại trang [máy Cummins 200 kW cách âm](/vi/products/cummins-200kw-silent-diesel-generator/), [máy Yuchai 300 kW cách âm](/vi/products/yuchai-300kw-silent-diesel-generator/) và [máy Mitsubishi 1000 kW bệ hở](/vi/products/mitsubishi-1000kw-open-diesel-generator/), hoặc [liên hệ chúng tôi](/vi/contact/) kèm sơ đồ một sợi.
