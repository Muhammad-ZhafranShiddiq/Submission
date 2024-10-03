import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

@st.cache_data
def load_data(file_path):
    return pd.read_csv(file_path)

def filter_data(data, status_list):
    return data[data['order_status'].isin(status_list)]

def calculate_sales(data):
    sales_count = data.groupby('product category').size().reset_index(name='total_sales')
    return sales_count.sort_values(by='total_sales', ascending=False)

def calculate_canceled(data):
    canceled_count = data.groupby('product category').size().reset_index(name='total')
    return canceled_count.sort_values(by='total', ascending=False)

def create_bar_chart(data, x_col, y_col, title, x_label, y_label, color='skyblue'):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(data[x_col], data[y_col], color=color)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    st.pyplot(fig)

def main():
    st.sidebar.title("Table of Contents")
    st.sidebar.write("[Top Product Categories by Sales](#top-product-categories-by-sales)")
    st.sidebar.write("[Product Categories With the Least Sales](#product-categories-with-the-least-sales)")
    st.sidebar.write("[Canceled Product Categories by Sales](#canceled-product-categories-by-sales)")
    st.sidebar.write("[Conclusion](#conclusion)")

    st.title('Product Sales and Cancellations (2017-2018) :rocket:')
    
    file_path = './main_data.csv'
    kategori_analysis = load_data(file_path)
    
    filtered_data = filter_data(kategori_analysis, ['delivered', 'shipped'])
    sorted_sales = calculate_sales(filtered_data)
    
    canceled_data = filter_data(kategori_analysis, ['canceled'])
    canceled_product = calculate_canceled(canceled_data)

    st.header('Top Product Categories by Sales')
    top_sales = sorted_sales.head()
    create_bar_chart(top_sales, 'product category', 'total_sales', 
                     'Top Product Categories by Sales (2017-10-17 until 2018-10-17)',
                     'Product Category', 'Total Sales', color='skyblue')
    st.write("Dari hasil visualisasi, terlihat sekali bagaimana perbandingan jumlah penjualan 5 kategori produk teratas dengan posisi terbanyak **bed_bath_table**, diikuti oleh **health_beauty**, **sports_leisure**, **computers_accessories**, dan **furniture_decor**.")

    st.header('Product Categories With the Least Sales')
    bad_sales = sorted_sales.tail()
    create_bar_chart(bad_sales, 'product category', 'total_sales', 
                     'Product Categories With the Least Sales (2017-10-17 until 2018-10-17)',
                     'Product Category', 'Total Sales', color='red')
    st.write("Kategori produk dengan penjualan terendah mencakup **fashion_childrens_clothes**, **la_cuisine**, **cds_dvds_musicals**, **fashion_sport**, dan **home_comfort_2**.")

    st.header('Canceled Product Categories by Sales')
    cancel_top = canceled_product.head()
    create_bar_chart(cancel_top, 'product category', 'total', 
                     'Canceled Product Categories by Sales (2017-10-17 until 2018-10-17)',
                     'Product Category', 'Total Canceled Orders', color='pink')
    st.write("Kategori produk yang paling sering dibatalkan ketika proses transaksi terjadi, diurutkan berdasarkan jumlah yang terbanyak yaitu **computers_accessories**, **sports_leisure**, **health_beauty**, **housewares**, dan **furniture_decor**.")

    st.header('Conclusion')
    st.subheader("Kategori produk dengan penjualan terbanyak dan terendah selama periode Oktober 2017 - Oktober 2018")
    st.write("Dari hasil analisis data yang mencakup rentang waktu satu tahun dari 2017-10-17 hingga 2018-10-17, terlihat dengan jelas perbandingan jumlah penjualan antara kategori produk. Kategori produk teratas dalam hal penjualan adalah **bed_bath_table**, diikuti oleh **health_beauty**, **sports_leisure**, **computers_accessories**, dan **furniture_decor**.\n\nSementara itu, kategori produk dengan penjualan terendah terdiri dari **fashion_childrens_clothes**, **la_cuisine**, **cds_dvds_musicals**, **fashion_sport**, dan **home_comfort_2**.\n\nHal ini menunjukkan adanya perbedaan signifikan dalam popularitas dan permintaan untuk berbagai kategori produk selama periode yang dianalisis. Dengan demikian, penjual bisa mengatur strategi pemasaran yang menarik seperti sistem bundling atau promo, serta melakukan pengembangan produk yang dapat difokuskan pada kategori teratas untuk meningkatkan penjualan. Selain itu, dengan tingginya permintaan konsumen akan barang tersebut, penjual dapat meningkatkan stok dengan tujuan agar dapat memenuhi permintaan pasar.\n\nSementara kategori dengan penjualan terendah mungkin memerlukan evaluasi lebih lanjut untuk memahami faktor-faktor yang memengaruhi performa penjualan kategori tersebut. Hal ini dapat mencakup analisis lebih dalam mengenai preferensi konsumen, tren pasar, serta daya saing produk di kategori tersebut. Selain itu, penjual juga dapat mempertimbangkan untuk melakukan survei konsumen atau analisis umpan balik untuk menggali lebih jauh mengenai alasan rendahnya minat terhadap produk-produk ini. Dengan pendekatan yang tepat, diharapkan dapat memperbaiki strategi pemasaran dan meningkatkan kinerja kategori yang masih kurang optimal.")

   
    st.subheader("Dalam periode penjualan bulan Oktober 2017 - Oktober 2018, kategori produk apa saja yang paling sering dibatalkan pembeliannya?")
    st.write("Dari hasil analisis selama satu tahun yang mencakup periode 2017-10-17 hingga 2018-10-17, dapat disimpulkan bahwa terdapat lima kategori produk yang sering dibatalkan selama proses transaksi. Kategori-kategori tersebut, diurutkan berdasarkan jumlah pembatalan terbanyak, adalah **computers_accessories**, **sports_leisure**, **health_beauty**, **housewares**, dan **furniture_decor**.\n\nTingginya angka pembatalan dalam kategori-kategori ini menunjukkan adanya masalah yang mungkin terkait dengan pengalaman konsumen, seperti harga, ketersediaan produk, atau mungkin ketidakpuasan terhadap kualitas atau deskripsi produk. Oleh karena itu, penting bagi penjual untuk melakukan analisis lebih lanjut mengenai penyebab pembatalan ini.\n\nDengan memahami faktor-faktor yang menyebabkan pembatalan, penjual dapat merumuskan strategi yang lebih efektif, seperti meningkatkan transparansi informasi produk, memperbaiki layanan pelanggan, atau menawarkan insentif untuk menyelesaikan transaksi. Upaya ini diharapkan dapat mengurangi tingkat pembatalan dan meningkatkan kepuasan serta loyalitas pelanggan.")
if __name__ == '__main__':
    main()
