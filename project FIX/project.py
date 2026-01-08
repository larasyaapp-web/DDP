import streamlit as st
import pandas as pd
import time

st.set_page_config(
    page_title="Aplikasi Gizi Harian",
    page_icon="🥗",
    layout="wide"
)

def transition():
    with st.spinner("⏳ Memuat halaman..."):
        time.sleep(0.5)

def set_bg(url, overlay=0.88):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{url}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        .block-container {{
            background: rgba(255,255,255,{overlay});
            padding: 2rem;
            border-radius: 25px;
            animation: fadeIn 0.8s ease-in;
        }}
        @keyframes fadeIn {{
            from {{opacity:0; transform: translateY(25px);}}
            to {{opacity:1; transform: translateY(0);}}
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

st.markdown("""
<style>
.card {
    background: linear-gradient(135deg,#ffffff,#f1f8e9);
    padding: 25px;
    border-radius: 22px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    margin-bottom: 20px;
}
.metric {
    background: linear-gradient(135deg,#ff7043,#66bb6a);
    color: #FAFAFA ;
    padding: 20px;
    border-radius: 18px;
    text-align: center;
    transition: 0.3s;
}
.metric:hover { transform: scale(1.08); }
button { border-radius: 12px ; }
.menu-item {
    background: #FAFAFA ;
    padding: 15px;
    border-radius: 12px;
    margin: 10px 0;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    transition: 0.3s;
}
.menu-item:hover {
    transform: translateY(-5px);
    box-shadow: 0 6px 12px rgba(0,0,0,0.15);
}
.welcome-title {
    font-size: 3.5rem;
    font-weight: bold;
    text-align: center;
    color: #2e7d32;
    margin-bottom: 20px;
}
.welcome-subtitle {
    font-size: 1.5rem;
    text-align: center;
    color: #558b2f;
    margin-bottom: 30px;
}
html, body, [class*="css"] {
    color: #4B4B4B;
}
h1, h2, h3, h4, h5, h6 {
    color: #4B4B4B;
}
label, span, p, div {
    color: #4B4B4B;
}
section[data-testid="stSidebar"] * {
    color: #4B4B4B;
}
.metric {
    color: #f5f5f5;
}
</style>
""", unsafe_allow_html=True)

for k in ["welcome","login","nama","jk","kategori","menu_dipilih"]:
    if k not in st.session_state:
        if k == "menu_dipilih":
            st.session_state[k] = {}
        elif k == "welcome":
            st.session_state[k] = True
        else:
            st.session_state[k] = None

MENU_MAKANAN = {
    "Sarapan": [
        {"nama": "Nasi Goreng", "kalori": 450, "protein": 15, "lemak": 18, "karbo": 55},
        {"nama": "Roti Bakar + Telur", "kalori": 320, "protein": 18, "lemak": 12, "karbo": 35},
        {"nama": "Bubur Ayam", "kalori": 280, "protein": 12, "lemak": 8, "karbo": 42},
        {"nama": "Nasi Uduk", "kalori": 380, "protein": 14, "lemak": 16, "karbo": 48},
        {"nama": "Omelet + Roti", "kalori": 350, "protein": 20, "lemak": 15, "karbo": 30},
        {"nama": "Pancake + Madu", "kalori": 400, "protein": 10, "lemak": 12, "karbo": 65},
        {"nama": "Nasi Kuning", "kalori": 420, "protein": 16, "lemak": 14, "karbo": 58},
        {"nama": "Lontong Sayur", "kalori": 340, "protein": 13, "lemak": 11, "karbo": 50},
        {"nama": "Mie Goreng", "kalori": 430, "protein": 14, "lemak": 17, "karbo": 52},
        {"nama": "Sandwich Isi", "kalori": 360, "protein": 19, "lemak": 13, "karbo": 38},
        {"nama": "Nasi + Ayam Goreng", "kalori": 480, "protein": 22, "lemak": 19, "karbo": 50},
        {"nama": "Bubur Kacang Hijau", "kalori": 290, "protein": 11, "lemak": 7, "karbo": 48},
        {"nama": "Nasi + Telur Dadar", "kalori": 370, "protein": 17, "lemak": 14, "karbo": 45},
        {"nama": "Oatmeal + Buah", "kalori": 310, "protein": 12, "lemak": 8, "karbo": 52},
        {"nama": "Nasi + Ikan Asin", "kalori": 390, "protein": 18, "lemak": 15, "karbo": 46},
        {"nama": "Roti Gandum + Selai", "kalori": 330, "protein": 10, "lemak": 9, "karbo": 55},
    ],
    "Makan Siang": [
        {"nama": "Nasi + Ayam Bakar", "kalori": 520, "protein": 35, "lemak": 18, "karbo": 55},
        {"nama": "Nasi + Ikan Goreng", "kalori": 480, "protein": 32, "lemak": 16, "karbo": 52},
        {"nama": "Nasi + Rendang", "kalori": 600, "protein": 28, "lemak": 28, "karbo": 58},
        {"nama": "Nasi + Sate Ayam", "kalori": 550, "protein": 33, "lemak": 20, "karbo": 54},
        {"nama": "Nasi + Gulai", "kalori": 580, "protein": 26, "lemak": 25, "karbo": 60},
        {"nama": "Nasi + Capcay", "kalori": 420, "protein": 15, "lemak": 12, "karbo": 62},
        {"nama": "Nasi + Ayam Geprek", "kalori": 540, "protein": 30, "lemak": 22, "karbo": 53},
        {"nama": "Nasi + Pecel Lele", "kalori": 490, "protein": 28, "lemak": 20, "karbo": 50},
        {"nama": "Nasi + Tempe Penyet", "kalori": 450, "protein": 18, "lemak": 16, "karbo": 58},
        {"nama": "Nasi + Ayam Kecap", "kalori": 510, "protein": 31, "lemak": 17, "karbo": 56},
        {"nama": "Nasi + Ikan Bakar", "kalori": 470, "protein": 33, "lemak": 14, "karbo": 51},
        {"nama": "Nasi + Sop Ayam", "kalori": 430, "protein": 24, "lemak": 13, "karbo": 54},
        {"nama": "Nasi + Beef Teriyaki", "kalori": 590, "protein": 34, "lemak": 23, "karbo": 57},
        {"nama": "Nasi + Udang Goreng", "kalori": 500, "protein": 29, "lemak": 18, "karbo": 53},
        {"nama": "Nasi + Cumi Saus Pedas", "kalori": 520, "protein": 27, "lemak": 21, "karbo": 55},
        {"nama": "Nasi + Tahu Tempe Bacem", "kalori": 440, "protein": 16, "lemak": 14, "karbo": 60},
    ],
    "Makan Malam": [
        {"nama": "Nasi + Sayur Asem", "kalori": 380, "protein": 12, "lemak": 10, "karbo": 60},
        {"nama": "Nasi + Sayur Lodeh", "kalori": 420, "protein": 14, "lemak": 15, "karbo": 58},
        {"nama": "Nasi + Soto Ayam", "kalori": 450, "protein": 22, "lemak": 14, "karbo": 55},
        {"nama": "Nasi + Pecel", "kalori": 410, "protein": 15, "lemak": 16, "karbo": 52},
        {"nama": "Nasi + Gado-Gado", "kalori": 430, "protein": 17, "lemak": 18, "karbo": 50},
        {"nama": "Nasi + Opor Ayam", "kalori": 520, "protein": 26, "lemak": 22, "karbo": 54},
        {"nama": "Sup Ayam + Roti", "kalori": 390, "protein": 20, "lemak": 11, "karbo": 48},
        {"nama": "Nasi + Ikan Kuah Kuning", "kalori": 440, "protein": 24, "lemak": 13, "karbo": 56},
        {"nama": "Nasi + Tumis Kangkung", "kalori": 360, "protein": 11, "lemak": 9, "karbo": 58},
        {"nama": "Nasi + Perkedel", "kalori": 400, "protein": 13, "lemak": 14, "karbo": 55},
        {"nama": "Nasi + Sayur Bening", "kalori": 340, "protein": 10, "lemak": 8, "karbo": 60},
        {"nama": "Bubur Ayam", "kalori": 320, "protein": 15, "lemak": 9, "karbo": 48},
        {"nama": "Nasi + Ayam Suwir", "kalori": 460, "protein": 23, "lemak": 15, "karbo": 53},
        {"nama": "Nasi + Telur Balado", "kalori": 420, "protein": 18, "lemak": 17, "karbo": 50},
        {"nama": "Nasi + Ikan Pindang", "kalori": 410, "protein": 21, "lemak": 12, "karbo": 54},
        {"nama": "Nasi + Tahu Isi", "kalori": 380, "protein": 14, "lemak": 13, "karbo": 52},
    ],
    "Buah": [
        {"nama": "Apel (1 buah)", "kalori": 52, "protein": 0.3, "lemak": 0.2, "karbo": 14},
        {"nama": "Pisang (1 buah)", "kalori": 89, "protein": 1.1, "lemak": 0.3, "karbo": 23},
        {"nama": "Jeruk (1 buah)", "kalori": 62, "protein": 1.2, "lemak": 0.2, "karbo": 15},
        {"nama": "Mangga (1 potong)", "kalori": 60, "protein": 0.8, "lemak": 0.4, "karbo": 15},
        {"nama": "Pepaya (1 potong)", "kalori": 43, "protein": 0.5, "lemak": 0.1, "karbo": 11},
        {"nama": "Semangka (1 potong)", "kalori": 30, "protein": 0.6, "lemak": 0.2, "karbo": 8},
        {"nama": "Anggur (1 mangkok)", "kalori": 69, "protein": 0.7, "lemak": 0.2, "karbo": 18},
        {"nama": "Melon (1 potong)", "kalori": 34, "protein": 0.8, "lemak": 0.2, "karbo": 8},
        {"nama": "Strawberry (5 buah)", "kalori": 32, "protein": 0.7, "lemak": 0.3, "karbo": 8},
        {"nama": "Nanas (1 potong)", "kalori": 50, "protein": 0.5, "lemak": 0.1, "karbo": 13},
        {"nama": "Pir (1 buah)", "kalori": 57, "protein": 0.4, "lemak": 0.1, "karbo": 15},
        {"nama": "Alpukat (1/2 buah)", "kalori": 160, "protein": 2, "lemak": 15, "karbo": 9},
        {"nama": "Kiwi (1 buah)", "kalori": 42, "protein": 0.8, "lemak": 0.4, "karbo": 10},
        {"nama": "Jambu Biji (1 buah)", "kalori": 37, "protein": 1.4, "lemak": 0.5, "karbo": 8},
        {"nama": "Salak (3 buah)", "kalori": 82, "protein": 0.4, "lemak": 0.4, "karbo": 21},
        {"nama": "Durian (1 potong)", "kalori": 147, "protein": 1.5, "lemak": 5, "karbo": 27},
    ],
    "Minuman": [
        {"nama": "Air Putih (1 gelas)", "kalori": 0, "protein": 0, "lemak": 0, "karbo": 0},
        {"nama": "Teh Manis (1 gelas)", "kalori": 90, "protein": 0, "lemak": 0, "karbo": 23},
        {"nama": "Teh Tawar (1 gelas)", "kalori": 2, "protein": 0, "lemak": 0, "karbo": 0.5},
        {"nama": "Kopi Hitam (1 gelas)", "kalori": 5, "protein": 0.3, "lemak": 0, "karbo": 1},
        {"nama": "Kopi Susu (1 gelas)", "kalori": 120, "protein": 6, "lemak": 4, "karbo": 15},
        {"nama": "Susu Sapi (1 gelas)", "kalori": 149, "protein": 8, "lemak": 8, "karbo": 12},
        {"nama": "Jus Jeruk (1 gelas)", "kalori": 112, "protein": 2, "lemak": 0.5, "karbo": 26},
        {"nama": "Jus Apel (1 gelas)", "kalori": 114, "protein": 0.3, "lemak": 0.3, "karbo": 28},
        {"nama": "Jus Mangga (1 gelas)", "kalori": 128, "protein": 1, "lemak": 0.5, "karbo": 31},
        {"nama": "Smoothie Pisang (1 gelas)", "kalori": 180, "protein": 4, "lemak": 2, "karbo": 38},
        {"nama": "Es Teh Manis (1 gelas)", "kalori": 95, "protein": 0, "lemak": 0, "karbo": 24},
        {"nama": "Yogurt Drink (1 botol)", "kalori": 110, "protein": 5, "lemak": 2, "karbo": 18},
        {"nama": "Infused Water (1 gelas)", "kalori": 5, "protein": 0, "lemak": 0, "karbo": 1},
        {"nama": "Susu Kedelai (1 gelas)", "kalori": 80, "protein": 7, "lemak": 4, "karbo": 4},
        {"nama": "Jus Wortel (1 gelas)", "kalori": 94, "protein": 2, "lemak": 0.4, "karbo": 22},
        {"nama": "Teh Hijau (1 gelas)", "kalori": 3, "protein": 0.5, "lemak": 0, "karbo": 0.5},
    ]
}

DATA = {
    "Remaja": {
        "Aktivitas":[
            "🚶 Jalan kaki / sepeda 15-30 menit",
            "🏃 Olahraga ringan 30-45 menit",
            "⚽ Bermain aktif / olahraga tim",
            "🏀 Basketball / Badminton / Futsal"
        ]
    },
    "Dewasa": {
        "Aktivitas":[
            "🏃 Jogging / Lari 30-45 menit",
            "🏋️ Latihan kekuatan otot",
            "🧘 Yoga / Stretching / Relaksasi",
            "🚶 Jalan santai / Aktivitas ringan",
            "🏊 Renang / Bersepeda"
        ]
    }
}

def hitung_total_dari_pilihan():
    """Menghitung total gizi dari menu yang dipilih user"""
    total = {"Kalori":0,"Protein":0,"Lemak":0,"Karbo":0}
    
    for waktu in ["Sarapan", "Makan Siang", "Makan Malam", "Buah", "Minuman"]:
        if waktu in st.session_state.menu_dipilih:
            menu = st.session_state.menu_dipilih[waktu]
            total["Kalori"] += menu["kalori"]
            total["Protein"] += menu["protein"]
            total["Lemak"] += menu["lemak"]
            total["Karbo"] += menu["karbo"]
    
    return total

def status_gizi(kal):
    """Menentukan status gizi berdasarkan total kalori harian"""
    if kal < 1200: return "🔴 Kurang"
    elif kal <= 2000: return "🟢 Cukup"
    elif kal <= 2500: return "🟡 Sedikit Berlebih"
    else: return "🟠 Berlebih"

if st.session_state.welcome:
    set_bg("https://images.unsplash.com/photo-1490645935967-10de6ba17061", 0.80)
    
    st.markdown("<div class='welcome-title'>🥗 Selamat Datang di Aplikasi Gizi Harian</div>", unsafe_allow_html=True)
    st.markdown("<div class='welcome-subtitle'>Monitor Nutrisi Anda Setiap Hari</div>", unsafe_allow_html=True)
    
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("### Tentang Aplikasi")
        st.write("""
        Aplikasi ini membantu Anda untuk:
        - 🍽️ **Memilih menu makanan** yang sehat dan bergizi
        - 📊 **Menghitung total gizi** dari makanan yang Anda konsumsi
        - 🏃 **Rekomendasi aktivitas fisik** sesuai kategori usia
        - ✅ **Monitoring status gizi** harian Anda
        """)
        
        st.markdown("### Fitur Aplikasi")
        st.write("""
        ✅ Pilihan menu makanan lengkap (Sarapan, Makan Siang, Makan Malam)
        ✅ Pilihan buah dan minuman dengan kandungan gizi
        ✅ Perhitungan otomatis total kalori, protein, lemak, karbohidrat
        ✅ Grafik visualisasi kandungan gizi
        ✅ Rekomendasi aktivitas fisik
        """)
        
        st.markdown("---")
        
        if st.button("🚀 Mulai Sekarang", type="primary", use_container_width=True):
            st.session_state.welcome = False
            st.rerun()
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style='text-align: center; margin-top: 30px; color: #666;'>
        <p>© 2025 Aplikasi Gizi Harian | Dibuat dengan kelompok 2 menggunakan Streamlit</p>
    </div>
    """, unsafe_allow_html=True)

elif not st.session_state.login:
    set_bg("https://images.unsplash.com/photo-1490645935967-10de6ba17061",0.85)

    st.markdown("<div class='card'>",unsafe_allow_html=True)
    st.header("🔐 Login Aplikasi Gizi")

    nama = st.text_input("👤 Nama")
    jk = st.radio("⚧️ Jenis Kelamin",["Laki-laki","Perempuan"])
    kategori = st.selectbox(
        "📊 Kategori Usia",
        ["Remaja", "Dewasa"]
    )

    if st.button("🚀 Masuk"):
        if nama:
            st.session_state.login = True
            st.session_state.nama = nama
            st.session_state.jk = jk
            st.session_state.kategori = kategori
            st.rerun()
        else:
            st.error("Mohon isi nama Anda terlebih dahulu!")

    st.markdown("</div>",unsafe_allow_html=True)

else:
    # Sidebar 
    st.sidebar.title("📌 MENU NAVIGASI")
    
    menu = st.sidebar.radio(
        "Pilih Halaman:",
        [
            "👤 Data Pengguna",
            "🍽️ Pilih Menu Makanan",
            "📊 Total Gizi",
            "🏃 Aktivitas Fisik"
        ]
    )
    
    st.sidebar.markdown("---")
    
    # Tombol logout
    if st.sidebar.button("🚪 Logout", type="primary", use_container_width=True):
        st.session_state.clear()
        st.session_state.welcome = True
        st.rerun()

    transition()
    data_user = DATA[st.session_state.kategori]

    # DATA PENGGUNA
    if menu == "👤 Data Pengguna":
        set_bg("https://images.unsplash.com/photo-1504674900247-0877df9cc836")
        st.header("👤 Profil Pengguna")
        
        col1, col2 = st.columns(2)
        with col1:
            st.success(f"**Nama:** {st.session_state.nama}")
            st.info(f"**Jenis Kelamin:** {st.session_state.jk}")
        with col2:
            st.info(f"**Kategori:** {st.session_state.kategori}")
            total_menu = len(st.session_state.menu_dipilih)
            st.success(f"**Menu Terpilih:** {total_menu}/5")

    # MENU MAKANAN
    elif menu == "🍽️ Pilih Menu Makanan":
        set_bg("https://images.unsplash.com/photo-1498837167922-ddd27525d352")
        st.header("🍽️ Pilih Menu Makanan Harian")
        
        # waktu makan
        tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "🌞 Sarapan", 
            "🍱 Makan Siang", 
            "🌙 Makan Malam",
            "🍎 Buah",
            "🥤 Minuman"
        ])
        
        # SARAPAN
        with tab1:
            st.subheader("Pilih Menu Sarapan")
            
            if "Sarapan" in st.session_state.menu_dipilih:
                menu_terpilih = st.session_state.menu_dipilih["Sarapan"]
                st.success(f"✅ Menu terpilih: **{menu_terpilih['nama']}** ({menu_terpilih['kalori']} kal)")
            
            cols = st.columns(3)
            for idx, menu_item in enumerate(MENU_MAKANAN["Sarapan"]):
                with cols[idx % 3]:
                    with st.container():
                        st.markdown(f"""
                        <div class='menu-item'>
                            <h4>{menu_item['nama']}</h4>
                            <p>🔥 {menu_item['kalori']} kal | 🥩 {menu_item['protein']}g<br>
                            🧈 {menu_item['lemak']}g | 🍚 {menu_item['karbo']}g</p>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        if st.button(f"Pilih", key=f"sarapan_{idx}"):
                            st.session_state.menu_dipilih["Sarapan"] = menu_item
                            st.rerun()
        
        # MAKAN SIANG
        with tab2:
            st.subheader("Pilih Menu Makan Siang")
            
            if "Makan Siang" in st.session_state.menu_dipilih:
                menu_terpilih = st.session_state.menu_dipilih["Makan Siang"]
                st.success(f"✅ Menu terpilih: **{menu_terpilih['nama']}** ({menu_terpilih['kalori']} kal)")
            
            cols = st.columns(3)
            for idx, menu_item in enumerate(MENU_MAKANAN["Makan Siang"]):
                with cols[idx % 3]:
                    with st.container():
                        st.markdown(f"""
                        <div class='menu-item'>
                            <h4>{menu_item['nama']}</h4>
                            <p>🔥 {menu_item['kalori']} kal | 🥩 {menu_item['protein']}g<br>
                            🧈 {menu_item['lemak']}g | 🍚 {menu_item['karbo']}g</p>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        if st.button(f"Pilih", key=f"siang_{idx}"):
                            st.session_state.menu_dipilih["Makan Siang"] = menu_item
                            st.rerun()
        
        # MAKAN MALAM
        with tab3:
            st.subheader("Pilih Menu Makan Malam")
            
            if "Makan Malam" in st.session_state.menu_dipilih:
                menu_terpilih = st.session_state.menu_dipilih["Makan Malam"]
                st.success(f"✅ Menu terpilih: **{menu_terpilih['nama']}** ({menu_terpilih['kalori']} kal)")
            
            cols = st.columns(3)
            for idx, menu_item in enumerate(MENU_MAKANAN["Makan Malam"]):
                with cols[idx % 3]:
                    with st.container():
                        st.markdown(f"""
                        <div class='menu-item'>
                            <h4>{menu_item['nama']}</h4>
                            <p>🔥 {menu_item['kalori']} kal | 🥩 {menu_item['protein']}g<br>
                            🧈 {menu_item['lemak']}g | 🍚 {menu_item['karbo']}g</p>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        if st.button(f"Pilih", key=f"malam_{idx}"):
                            st.session_state.menu_dipilih["Makan Malam"] = menu_item
                            st.rerun()
        
        # BUAH
        with tab4:
            st.subheader("Pilih Buah")
            
            if "Buah" in st.session_state.menu_dipilih:
                menu_terpilih = st.session_state.menu_dipilih["Buah"]
                st.success(f"✅ Buah terpilih: **{menu_terpilih['nama']}** ({menu_terpilih['kalori']} kal)")
            
            cols = st.columns(3)
            for idx, menu_item in enumerate(MENU_MAKANAN["Buah"]):
                with cols[idx % 3]:
                    with st.container():
                        st.markdown(f"""
                        <div class='menu-item'>
                            <h4>🍎 {menu_item['nama']}</h4>
                            <p>🔥 {menu_item['kalori']} kal | 🥩 {menu_item['protein']}g<br>
                            🧈 {menu_item['lemak']}g | 🍚 {menu_item['karbo']}g</p>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        if st.button(f"Pilih", key=f"buah_{idx}"):
                            st.session_state.menu_dipilih["Buah"] = menu_item
                            st.rerun()
        
        # MINUMAN
        with tab5:
            st.subheader("Pilih Minuman")
            
            if "Minuman" in st.session_state.menu_dipilih:
                menu_terpilih = st.session_state.menu_dipilih["Minuman"]
                st.success(f"✅ Minuman terpilih: **{menu_terpilih['nama']}** ({menu_terpilih['kalori']} kal)")
            
            cols = st.columns(3)
            for idx, menu_item in enumerate(MENU_MAKANAN["Minuman"]):
                with cols[idx % 3]:
                    with st.container():
                        st.markdown(f"""
                        <div class='menu-item'>
                            <h4>🥤 {menu_item['nama']}</h4>
                            <p>🔥 {menu_item['kalori']} kal | 🥩 {menu_item['protein']}g<br>
                            🧈 {menu_item['lemak']}g | 🍚 {menu_item['karbo']}g</p>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        if st.button(f"Pilih", key=f"minuman_{idx}"):
                            st.session_state.menu_dipilih["Minuman"] = menu_item
                            st.rerun()

    # TOTAL
    elif menu == "📊 Total Gizi":
        set_bg("https://images.unsplash.com/photo-1512621776951-a57141f2eefd")
        st.header("📊 Total Gizi Sehari")
        
        if len(st.session_state.menu_dipilih) == 0:
            st.warning("⚠️ Anda belum memilih menu makanan. Silakan pilih menu terlebih dahulu.")
        else:
            # menu yang dipilih
            st.subheader("Menu Anda Hari Ini:")
            
            col1, col2, col3, col4, col5 = st.columns(5)
            
            with col1:
                if "Sarapan" in st.session_state.menu_dipilih:
                    menu = st.session_state.menu_dipilih["Sarapan"]
                    st.info(f"**🌞 Sarapan**\n\n{menu['nama']}\n\n{menu['kalori']} kal")
                else:
                    st.warning("Belum pilih")
            
            with col2:
                if "Makan Siang" in st.session_state.menu_dipilih:
                    menu = st.session_state.menu_dipilih["Makan Siang"]
                    st.info(f"**🍱 Siang**\n\n{menu['nama']}\n\n{menu['kalori']} kal")
                else:
                    st.warning("Belum pilih")
            
            with col3:
                if "Makan Malam" in st.session_state.menu_dipilih:
                    menu = st.session_state.menu_dipilih["Makan Malam"]
                    st.info(f"**🌙 Malam**\n\n{menu['nama']}\n\n{menu['kalori']} kal")
                else:
                    st.warning("Belum pilih")
            
            with col4:
                if "Buah" in st.session_state.menu_dipilih:
                    menu = st.session_state.menu_dipilih["Buah"]
                    st.info(f"**🍎 Buah**\n\n{menu['nama']}\n\n{menu['kalori']} kal")
                else:
                    st.warning("Belum pilih")
            
            with col5:
                if "Minuman" in st.session_state.menu_dipilih:
                    menu = st.session_state.menu_dipilih["Minuman"]
                    st.info(f"**🥤 Minuman**\n\n{menu['nama']}\n\n{menu['kalori']} kal")
                else:
                    st.warning("Belum pilih")
            
            st.markdown("---")
            
            # total
            total = hitung_total_dari_pilihan()
            df = pd.DataFrame.from_dict(total,orient="index",columns=["Jumlah"])

            st.subheader("Total Kandungan Gizi:")
            c1,c2,c3,c4 = st.columns(4)
            for c,(k,v) in zip([c1,c2,c3,c4],total.items()):
                c.markdown(f"<div class='metric'>{k}<br><h2>{v:.1f}</h2></div>",unsafe_allow_html=True)

            st.subheader("📈 Grafik Kandungan Gizi")
            st.bar_chart(df)

            st.success(f"**Status Gizi:** {status_gizi(total['Kalori'])}")

    # AKTIVITAS
    elif menu == "🏃 Aktivitas Fisik":
        set_bg("https://images.unsplash.com/photo-1554284126-aa88f22d8b74")
        st.header("🏃 Rekomendasi Aktivitas Fisik")
        
        st.info(f"Aktivitas yang direkomendasikan untuk **{st.session_state.kategori}**:")
        
        for i, aktivitas in enumerate(data_user["Aktivitas"], 1):
            st.markdown(f"### {i}. {aktivitas}")
        
        st.markdown("---")
        st.subheader("💡 Tips Tambahan:")
        tips = [
            "💧 Minum air putih minimal 8 gelas per hari",
            "😴 Tidur cukup 7-8 jam setiap malam",
            "🥗 Konsumsi makanan bergizi seimbang",
            "🏃 Rutin berolahraga minimal 30 menit per hari",
            "🚫 Hindari makanan tinggi gula dan lemak jenuh",
            "🧘 Lakukan peregangan sebelum dan sesudah olahraga",
            "📱 Batasi waktu screen time / gadget"
        ]
        
        for tip in tips:
            st.write(f"- {tip}")