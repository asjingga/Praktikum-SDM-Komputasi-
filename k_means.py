# -*- coding: utf-8 -*-
"""K-means.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1smFAzQR1yuzpvHH4agXTqjfpHEYV08xt

# (1) PRAKTIKUM CLUSTERING

## NAMA:Bisma Ridho Pambudi

## NIM:10319002

***Catatan:***
1. Praktikum bersifat individual, namun berdiskusi secukupnya di dalam grup masing-masing
2. **Laporan final dalam format PDF** sebagai hasil konversi Notebook ke PDF dan disubmit di edunex. Bila ada slot informasi yang dapat dientry di edunex, tuliskan tautan ke Google Colab Notebook tersebut.

## Prinsip dasar (secara intuitif)
1. **Pilih** (secara acak untuk loop pertama; tidak perlu dari dataset) atau **hitung** (mulai dari loop kedua) sebanyak *K* titik-titik pusat cluster
2. Masukkan setiap titik dataset **hanya** ke salah satu cluster berdasarkan kriteria jarak terdekat ke titik-titik pusat cluster
3. Catat pergeseran setiap titik pusat cluster (mulai dari loop kedua)
4. Ulangi hingga konvergen

## Potensi masalah pada nilai awal centroid yang acak
1. Inisialisasi centroid acak tidak selamanya membawa sukses
2. Pada praktikum ini akan dicoba langsung pakai KMeans++ sebagai solusi yang ditawarkan Scikit Learn

## Metode siku (Elbow) untuk memilih jumlah cluster yang tepat
**Within Cluster Sum of Squares** (**WCSS**, atau istilah lainnya adalah **inersia**) adalah jumlah kuadrat jarak setiap titik data ke cluster terdekat. WCSS pada awalnya bernilai sangat besar dan dapat terus mengecil dengan semakin bertambahnya nilai parameter jumlah cluster. Dalam plot, seringkali terlihat penurunan ini sangat signifikan serupa tekukan siku, dan setelahnya nilai WCSS terus menurun secara melandai menuju nilai 0. Sifat seperti ini memungkinkan kita untuk memutuskan bahwa pada titik siku tersebut peningkatan jumlah cluster tidak lagi menurunkan nilai WCSS secara signifikan. Di titik siku itulah titik ideal jumlah cluster dapat dipilih.

__Dalam perspektif kalkulus: jumlah cluster ideal diperoleh dengan memaksimalkan turunan kedua dari WCSS__

### Perhatian:
Pada contoh kasus di bawah ini, akan dipelajari clustering pelanggan mall berdasarkan variabel ***penghasilan tahunan*** (indeks fitur ke-3) vs ***skor pengeluaran*** (indeks fitur ke-4)
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('/content/Mall_Customers.csv')
X = df.iloc[:, [3, 4]].values

# Cek tampilan beberapa baris atas dataframe
df

"""#### Di sini kita akan menggunakan k-means++"""

from sklearn.cluster import KMeans

fig = plt.figure(figsize=(10, 8))
WCSS = []
for i in range(1, 11):
    clf = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    clf.fit(X)
    WCSS.append(clf.inertia_) # inertia is another name for WCSS

plt.plot(range(1, 11), WCSS)
plt.title('Elbow Method')
plt.ylabel('WCSS')
plt.xlabel('Jumlah cluster')
plt.show()

"""#### Berdasarkan titik siku yang tampak di plot, berapakah jumlah cluster yang disarankan?
*(Jawab dan tulis di sel ini: n_clusters = 5 )*
"""

clf = KMeans(n_clusters=5, init='k-means++', max_iter=300, n_init=10,  random_state=0)
y_kmeans = clf.fit_predict(X)

fig = plt.figure(figsize=(10, 8))
plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], color='red', s=60, label='Cluster 1', edgecolors='black')
plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], color='green', s=60, label='Cluster 2', edgecolors='black')
plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], color='blue',s=60, label='Cluster 3', edgecolors='black')
plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3, 1], color='yellow',s=60, label='Cluster 4', edgecolors='black')
plt.scatter(X[y_kmeans == 4, 0], X[y_kmeans == 4, 1], color='pink',s=60, label='Cluster 5', edgecolors='black')
#plt.scatter(X[y_kmeans == 5, 0], X[y_kmeans == 5, 1], color='grey',s=60, label='Cluster 5', edgecolors='black')
#cluster centres
plt.scatter(clf.cluster_centers_[:, 0], clf.cluster_centers_[:, 1], color='magenta', s=100, label='Centroid',edgecolors='black')
plt.legend()
plt.title('Clustering menggunakan K-Means')
plt.ylabel('Pendapatan Tahunan (ribu dollar)')
plt.xlabel('Skor Pengeluaran (1-100)')
plt.show()

"""### Tugas:

Coba Anda temukan ide lain untuk clustering selain dari penghasilan tahunan vs skor pengeluaran. Kerjakan secara lengkap seperti contoh latihan di atas.
"""

df = pd.read_csv('/content/insurance.csv')
X = df.iloc[:, [2, 6]].values

# Cek tampilan beberapa baris atas dataframe
df.head()

from sklearn.cluster import KMeans

fig = plt.figure(figsize=(10, 8))
WCSS = []
for i in range(1, 11):
    clf = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    clf.fit(X)
    WCSS.append(clf.inertia_) # inertia is another name for WCSS

plt.plot(range(1, 11), WCSS)
plt.title('Elbow Method')
plt.ylabel('WCSS')
plt.xlabel('Jumlah cluster')
plt.show()

"""Jumlah cluster yang didapatkan adalah k=3"""

clf = KMeans(n_clusters=3, init='k-means++', max_iter=300, n_init=10,  random_state=0)
y_kmeans = clf.fit_predict(X)

fig = plt.figure(figsize=(10, 8))
plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], color='red', s=60, label='Cluster 1', edgecolors='black')
plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], color='green', s=60, label='Cluster 2', edgecolors='black')
plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], color='blue',s=60, label='Cluster 3', edgecolors='black')
#plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3, 1], color='yellow',s=60, label='Cluster 4', edgecolors='black')
#plt.scatter(X[y_kmeans == 4, 0], X[y_kmeans == 4, 1], color='pink',s=60, label='Cluster 5', edgecolors='black')
#plt.scatter(X[y_kmeans == 5, 0], X[y_kmeans == 5, 1], color='grey',s=60, label='Cluster 5', edgecolors='black')
#cluster centres
plt.scatter(clf.cluster_centers_[:, 0], clf.cluster_centers_[:, 1], color='magenta', s=100, label='Centroid',edgecolors='black')
plt.legend()
plt.title('Clustering menggunakan K-Means')
plt.ylabel('Charges')
plt.xlabel('Body Mass Index')
plt.show()