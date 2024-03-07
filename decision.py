import numpy as np
import pandas as pd
from sklearn import tree

#Using the scikit-learn library for decision trees, evaluating job applications with artificial intelligence.
#scikit-learn kütüphanesi decision tree kullanarak iş başvurularının yapay zeka ile değerlendirilmesi


df = pd.read_csv("datas/DecisionTreesClassificationDataSet.csv") #verilerin okunması

#print(df.head())

#Decision Tree'nin düzgün çalışması için herşeyin rakamsal  olması gerekiyor. Bu yüzden veri setimizdeki Y ve N değerlerini 0 ve 1 olarak düzeltiyoruz.
duzeltme_mapping = {'Y': 1, 'N': 0}  #df setindeki Y - N  harflerini sayısal değerlere eşitledik.
duzeltme_mapping_egitim = {'BS': 0, 'MS': 1 , 'PhD':2 } #df egitim seviyesi çıktısını bs(lisans mezun), ms(master mezun) ve PhD(doktora mezun) olarak kısaltma yaparak yeniden düzenledik.


df['IseAlindi'] = df['IseAlindi'].map(duzeltme_mapping)
df['StajBizdeYaptimi?'] = df['StajBizdeYaptimi?'].map(duzeltme_mapping)
df['Top10 Universite?'] = df['Top10 Universite?'].map(duzeltme_mapping)
df['SuanCalisiyor?'] = df['SuanCalisiyor?'].map(duzeltme_mapping)
df['Egitim Seviyesi'] = df['Egitim Seviyesi'].map(duzeltme_mapping_egitim)

#print(df.head())

y = df['IseAlindi']
x = df.drop(['IseAlindi'], axis=1)

#print(y)

#Decision Tree oluşturuyoruz
clf  = tree.DecisionTreeClassifier()  
clf = clf.fit(x, y)   							
#5 yıl deneyimli, aktif çalışan , 3 eski şirkette çalışmış, eğitim seviyesi bs(lisans), top10 okuldan mezun değil, stajı bizde yapmamış olan bir kişi
print(clf.predict([[5, 1, 3, 0 ,0 ,0]]))

#çıktı olarak [1] verdi yani ai bu kişiyi işe aldı.

print(clf.predict([[2,0,7,0,1,0]]))

#[0] ai bu kişiyi işe almadı


