import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Judul
st.title("📊 Simulasi Model Antrian M/M/1")

st.markdown("Masukkan parameter berikut untuk menghitung model antrian:")

# Input user
λ = st.number_input("Rata-rata kedatangan (λ) pelanggan/jam", value=15.0)
μ = st.number_input("Rata-rata layanan (μ) pelanggan/jam", value=20.0)

if λ >= μ:
    st.error("⚠️ Sistem tidak stabil (λ ≥ μ). Pastikan λ < μ")
else:
    # Perhitungan
    ρ = λ / μ
    L = λ / (μ - λ)
    Lq = λ**2 / (μ * (μ - λ))
    W = 1 / (μ - λ)
    Wq = λ / (μ * (μ - λ))

    # Hasil
    st.markdown("### 📈 Hasil Perhitungan")
    st.write(f"**Utilisasi server (ρ):** {ρ:.2f}")
    st.write(f"**Jumlah rata-rata pelanggan dalam sistem (L):** {L:.2f}")
    st.write(f"**Jumlah rata-rata pelanggan dalam antrean (Lq):** {Lq:.2f}")
    st.write(f"**Waktu rata-rata dalam sistem (W):** {W*60:.2f} menit")
    st.write(f"**Waktu rata-rata menunggu dalam antrean (Wq):** {Wq*60:.2f} menit")

    # Diagram Antrian
    st.markdown("### 🧭 Diagram Antrian")

    fig, ax = plt.subplots(figsize=(8, 3))
    ax.axis("off")

    # Gambar elemen antrian
    ax.text(0.1, 0.5, "Kedatangan λ", fontsize=12, ha='center')
    ax.arrow(0.2, 0.5, 0.2, 0.0, head_width=0.05, head_length=0.05, fc='blue', ec='blue')

    ax.add_patch(plt.Rectangle((0.45, 0.4), 0.1, 0.2, fill=True, color='lightgray'))
    ax.text(0.5, 0.5, "Antrian", fontsize=10, ha='center')

    ax.arrow(0.55, 0.5, 0.2, 0.0, head_width=0.05, head_length=0.05, fc='blue', ec='blue')

    ax.add_patch(plt.Rectangle((0.75, 0.4), 0.1, 0.2, fill=True, color='orange'))
    ax.text(0.8, 0.5, "Server\n(μ)", fontsize=10, ha='center')

    ax.arrow(0.85, 0.5, 0.2, 0.0, head_width=0.05, head_length=0.05, fc='green', ec='green')
    ax.text(1.08, 0.5, "Keluar", fontsize=12, ha='center')

    st.pyplot(fig)
