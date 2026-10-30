#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kaybolan Çorapların Felsefi Yolculuğu
Bu script, çorapların kayboluşunu sorgular ama asla cevap vermez.
"""

import random
import time

def corap_renkleri():
    renkler = ["kırmızı", "mavi", "yeşil", "siyah", "beyaz", "kaybolmuş", "şüpheli gri", "paralel evren pembesi"]
    return random.choice(renkler)

def felsefi_soru(renk):
    sorular = [
        f"Bu {renk} çorap neden kayboldu? Acaba özgürlüğünü mü arıyordu?",
        f"{renk.capitalize()} çorabınız şu an nerede? Belki de bir kayyum tarafından el konuldu.",
        f"Eğer bir çorap kaybolursa ve kimse fark etmezse, gerçekten kaybolmuş mudur?",
        f"{renk} çorap, varoluşun anlamsızlığını mı temsil ediyor?",
        f"Çoraplar kaybolur, umutlar da. Ama {renk} olanınız özellikle inatçıdır."
    ]
    return random.choice(sorular)

def main():
    print("Kaybolan Çorapların Felsefi Yolculuğu başlıyor...")
    print("Bu kod size cevap vermeyecek. Sadece soracak. Sonsuza kadar.\n")
    
    for i in range(10):  # 10 kez, sonsuz değil ama yeterince uzun
        renk = corap_renkleri()
        soru = felsefi_soru(renk)
        print(f"Çorap #{i+1}: {soru}")
        time.sleep(random.uniform(0.5, 2.0))  # Dramatik bekleme
        
        # Gizli not (base64 benzeri ama düz):
        # a2F5eXVtIGJpciBndW4gYmlyIGNvcmlwIG9sdXIu (kayyum bir gün bir çorap olur.)
        
    print("\nİşte bu kadar. Cevap yok. Çoraplarınız hala kayıp. İyi günler.")
    print("Ctrl+C ile çıkın veya sonsuza kadar düşünün.")

if __name__ == "__main__":
    main()
