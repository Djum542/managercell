import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu từ tập tin CSV
df = pd.read_excel('thongke.xlsx')

# Vẽ biểu đồ đường
df.plot(kind='line', x='Hãng', y='Số lượng')

# Đặt tên cho trục x và trục y
plt.xlabel('Hãng')
plt.ylabel('Số lượng')

# Hiển thị biểu đồ
plt.show()
