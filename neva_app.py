# -*- coding: utf-8 -*-
import streamlit as st
import os

# --- KONFIGURATION & NEVA STYLE ---
st.set_page_config(page_title="Neva Digital Menu", page_icon="🧿", layout="centered")

# Custom CSS für den "Neva Style" (Tiefblau & Gold)
st.markdown("""
    <style>
    .stApp {
        background-color: #174d80; /* Neva Tiefblau */
        color: #dee7ef;
    }
    h1, h2, h3 {
        color: #a6773b !important; /* Gold */
        font-family: 'Helvetica', sans-serif;
        font-weight: 300;
    }
    .stButton>button {
        background-color: #D4AF37;
        color: #0B1E3B;
        border-radius: 20px;
        border: none;
        font-weight: bold;
        width: 100%;
    }
    .card {
        background-color: #174d80;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 15px;
        border: 1px solid #a6773b;
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
    }
    .price {
        color: #a6773b; /* Terrakotta Akzent */
        font-weight: bold;
        float: right;
        font-size: 1.1em;
    }
    .tag {
        background-color: #dee7ef;
        border: 1px solid #E87E54;
        color: #a6773b;
        padding: 2px 8px;
        border-radius: 10px;
        font-size: 0.7em;
        margin-right: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ECHTE DATEN (Aus deinem PDF extrahiert) ---
menu_data = {
    "KALTE MEZE": [
        {"name": "CACIK", "desc": "Joghurt, Gurken, Minze, Knoblauch", "price": 7.50, "tags": ["G", "V"], "img": "https://github.com/buriber/neva-menu/blob/2f2235289b57c493903f5f82b58bd7218c1ceb04/images/cacik.jpeg"},
        {"name": "RED KISIR", "desc": "Bulgur, Paprika, Rote Bete, Petersilie", "price": 7.50, "tags": ["VE"], "img": "https://github.com/buriber/neva-menu/blob/2f2235289b57c493903f5f82b58bd7218c1ceb04/images/redkisir.jpeg"},
        {"name": "HUMUS", "desc": "Kichererbsen, Tahin, Knoblauch", "price": 7.50, "tags": ["G", "VE"], "img": "https://github.com/buriber/neva-menu/blob/2f2235289b57c493903f5f82b58bd7218c1ceb04/images/humus.jpeg"},
        {"name": "PIYAZ", "desc": "Bohnen, Zwiebeln, Tomaten", "price": 7.50, "tags": ["G", "VE"], "img": "https://github.com/buriber/neva-menu/blob/2f2235289b57c493903f5f82b58bd7218c1ceb04/images/piyaz.jpeg"},
           {"name": "LINSA", "desc": "Linsen, Bulgur, Zwiebeln", "price": 12.50, "tags": ["VE"], "img": "https://github.com/buriber/neva-menu/blob/2f2235289b57c493903f5f82b58bd7218c1ceb04/images/fishball.jpeg"},
           {"name": "TARAMA", "desc": "Fischrogen, Zwiebeln, Eier, Dill", "price": 12.50, "tags": ["G"], "img": "https://github.com/buriber/neva-menu/blob/2f2235289b57c493903f5f82b58bd7218c1ceb04/images/tarama.jpeg"},
           {"name": "ROASTIES", "desc": "Geröstete Auberginen, Paprika, Tomaten", "price": 12.50, "tags": ["G", "VE"], "img": "https://github.com/buriber/neva-menu/blob/2f2235289b57c493903f5f82b58bd7218c1ceb04/images/roasties.jpeg"},
        {"name": "LEVREK", "desc": "Wolfsbarsch, Sellerie, Orangen, Zwiebeln", "price": 7.50, "tags": ["G"], "img": "https://github.com/buriber/neva-menu/blob/2f2235289b57c493903f5f82b58bd7218c1ceb04/images/levrek.jpeg"},
        {"name": "GREEK FETA", "desc": "Schafskäse, Honigmelone", "price": 7.50, "tags": ["G", "V"], "img": "https://github.com/buriber/neva-menu/blob/2f2235289b57c493903f5f82b58bd7218c1ceb04/images/greekfeta.jpeg"},
    ],
    "WARME MEZE": [
        {"name": "Börek", "desc": "Teigröllchen mit Sauerkraut-Chili-Füllung", "price": 12.50, "tags": ["VE"], "img": "https://github.com/buriber/neva-menu/blob/2f2235289b57c493903f5f82b58bd7218c1ceb04/images/kadinbudu.jpeg"},
        {"name": "Manti", "desc": "Mit Käsefüllung, Joghurt, Chiliöl, Knoblauch", "price": 12.50, "tags": ["V"], "img": "https://github.com/buriber/neva-menu/blob/2f2235289b57c493903f5f82b58bd7218c1ceb04/images/manti.jpeg"},
        {"name": "Karides", "desc": "Garnelen, getr. Tomaten, Butter, Chili, Knoblauch", "price": 18.00, "tags": ["G", "Top-Seller"], "img": "https://github.com/buriber/neva-menu/blob/2f2235289b57c493903f5f82b58bd7218c1ceb04/images/karides.jpeg"},
        {"name": "Ahtapot (Octopus Pan)", "desc": "Oktopus, Tomaten, Paprika, Perlzwiebeln, Rotwein", "price": 18.00, "tags": ["G", "Premium"], "img": "https://github.com/buriber/neva-menu/blob/2f2235289b57c493903f5f82b58bd7218c1ceb04/images/octopuspan.jpeg"},
        {"name": "Çökertme Kebap", "desc": "Filetstreifen, Pommes Julienne, Knoblauchjoghurt", "price": 18.00, "tags": ["G", "Spezialität"], "img": "https://github.com/buriber/neva-menu/blob/2f2235289b57c493903f5f82b58bd7218c1ceb04/images/cokertme.jpeg"},
    ],
    "Neva Menüs (Sets)": [
        {"name": "Merhaba Menü", "desc": "Für 2 Gäste: 3 Kalte, 2 Warme, 1 Salat, 2 Desserts, 2 Mokka + Wasser-Flat", "price": 48.00, "tags": ["Best Value"], "img": "feast table"},
        {"name": "Sherefe Menü", "desc": "Wie Merhaba + 20cl Yeni Rakı oder 2 Gläser Wein", "price": 58.00, "tags": ["Rakı Lovers"], "img": "raki table"},
    ]
}

# --- SESSION STATE ---
if 'cart' not in st.session_state:
    st.session_state.cart = []

# --- APP HEADER ---
col1, col2 = st.columns([1, 5])
with col1:
    st.write("🧿")
with col2:
    st.title("Neva Meze Restaurant")
st.caption("Dein digitaler Begleiter am Tisch")

# --- TABS ---
tab1, tab2, tab3 = st.tabs(["📖 MENU", "🍷 PAIRING", "🛒 ORDER"])

with tab1:
    for category, items in menu_data.items():
        st.subheader(category)
        for item in items:
            
            raw_path = item['img']
            display_image = None
            
            # FALL A: Es ist eine Web-URL (http...)
            if raw_path.startswith("http"):
                # Automatischer Fix: Falls jemand den "blob" Link kopiert hat, machen wir "raw" draus
                if "github.com" in raw_path and "/blob/" in raw_path:
                    display_image = raw_path.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")
                else:
                    display_image = raw_path
                    
            # FALL B: Es ist eine lokale Datei (images/...)
            else:
                # Wir prüfen, ob die Datei da ist
                if os.path.exists(raw_path):
                    display_image = raw_path
                else:
                    # Debugging-Hilfe: Was sieht Python wirklich?
                    files_in_folder = os.listdir("images") if os.path.exists("images") else "Ordner 'images' fehlt!"
                    st.error(f"❌ Datei nicht gefunden: '{raw_path}'")
                    st.caption(f"📂 Inhalt des 'images' Ordners: {files_in_folder}")
                    display_image = "https://source.unsplash.com/800x600/?food,turkish" # Fallback

            with st.container():
                st.markdown(f"""
                <div class="card">
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <h3 style="margin:0;">{item['name']}</h3>
                        <span class="price">{item['price']:.2f} €</span>
                    </div>
                    <p style="font-style:italic; opacity:0.8; margin-top:5px;">{item['desc']}</p>
                    <div style="margin-top:10px;">
                        {' '.join([f'<span class="tag">{tag}</span>' for tag in item['tags']])}
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                c1, c2 = st.columns([3, 1])
                with c1:
                    if display_image:
                        st.image(display_image, use_container_width=True) 
                with c2:
                    st.write("") 
                    st.write("")
                    if st.button("➕", key=f"add_{item['name']}"):
                        st.session_state.cart.append(item)
                        st.toast(f"{item['name']} hinzugefügt!")



with tab2:
    st.header("Neva Pairing")
    st.info("Wähle dein Getränk, wir empfehlen die Meze.")
    drink = st.selectbox("Ich trinke...", ["Rakı", "Weißwein", "Rotwein", "Cocktail", "Wasser"])
    
    if drink == "Rakı":
        st.success("Klassisch! Dazu empfehlen wir **Cacık** (neutralisiert), **Greek Feta** (Salzbalance), **Fishball**, **Roasties** und **Levrek**.")
    elif "Weißwein" in drink:
        st.success("Dazu passt hervorragend etwas aus dem Meer: **Fishball**, **Piyaz**, **Tarama**, **Red Kisir**, **Karides** oder **Octopus**.")
    elif "Rotwein" in drink:
        st.success("Rotwein braucht kräftige Partner: **Fasoulya**, **Köfte'lein**, **Chicken Sote**, **Çökertme Kebap** oder **Red Kisir**.")
    else:
        st.success("Zu unseren Cocktails empfehlen wir unsere knusprigen **Börek**, **Greek Feta**, **Linsa**, **Mücver** und **Icli**.")

with tab3:
    st.header("Deine Auswahl")
    if st.session_state.cart:
        total = sum([x['price'] for x in st.session_state.cart])
        for item in st.session_state.cart:
            st.write(f"▪️ {item['name']} ({item['price']:.2f} €)")
        st.markdown("---")
        st.subheader(f"Gesamt: {total:.2f} €")
        if st.button("ZEIGE DIESE LISTE DEINER KELLNERIN"):
            st.balloons()
            st.success("BESTELLUNG DEM KELLNER ZEIGEN")
            st.session_state.cart = []
    else:
        st.write("Noch nichts ausgewählt.")
