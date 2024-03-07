# Job Application Decision System

## Introduction

This project employs a Decision Tree Classifier from the scikit-learn library to automate the evaluation of job applications. By analyzing various factors such as education level, work experience, and previous internships, the system predicts whether an applicant is a suitable candidate for the job.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)
- [Contributors](#contributors)

## Installation

To run this project, you will need Python 3.6 or later. It is recommended to use a virtual environment for Python projects to manage dependencies efficiently.

1. Clone the repository to your local machine.
2. Install the required dependencies:

```bash
pip install numpy pandas scikit-learn
```

## Usage

To evaluate job applications, execute the script with Python:

```bash
python decision.py
```

Ensure that the dataset `DecisionTreesClassificationDataSet.csv` is located in the `data` folder relative to the script.

## Features

- Conversion of categorical data into numerical format for model training.
- Training a decision tree model to predict the suitability of a job applicant.
- Evaluation of applicants based on education, work experience, and other relevant factors.

## Dependencies

- numpy
- pandas
- scikit-learn

## Configuration

No additional configuration is needed to run this script as provided. Ensure that the dataset path is correct in the script:

```python
df = pd.read_csv("data/DecisionTreesClassificationDataSet.csv")
```

## Examples

The script includes two examples of predictions:

1. An applicant with 5 years of experience, currently employed, with a bachelor's degree, not from a top 10 university, and without an internship in the company is predicted to be hired (`[1]`).
2. An applicant with 2 years of experience, not currently employed, with a PhD, from a top 10 university, without an internship in the company is predicted not to be hired (`[0]`).

## Troubleshooting

If you encounter any issues with running the script, ensure that:

- The Python version is 3.6 or later.
- All dependencies are correctly installed.
- The dataset file is located in the correct directory and named properly.

## Contributors

Emircan Yüksel

# İş Başvurusu Karar Sistemi

## Giriş

Bu proje, scikit-learn kütüphanesinden Bir Karar Ağacı Sınıflandırıcısı kullanarak iş başvurularının otomatik değerlendirilmesini sağlar. Eğitim seviyesi, iş tecrübesi ve önceki stajlar gibi çeşitli faktörleri analiz ederek, bir başvuru sahibinin iş için uygun olup olmadığını tahmin eder.

## İçindekiler

- [Kurulum](#kurulum)
- [Kullanım](#kullanım)
- [Özellikler](#özellikler)
- [Bağımlılıklar](#bağımlılıklar)
- [Konfigürasyon](#konfigürasyon)
- [Örnekler](#örnekler)
- [Sorun Giderme](#sorun-giderme)
- [Katkıda Bulunanlar](#katkıda-bulunanlar)


## Kurulum

Bu projeyi çalıştırmak için Python 3.6 veya daha yeni bir sürümüne ihtiyacınız olacak. Python projelerinde bağımlılıkları etkin bir şekilde yönetmek için sanal bir ortam kullanılması önerilir.

1. Yerel makinenize repoyu klonlayın.
2. Gerekli bağımlılıkları yükleyin:

```bash
pip install numpy pandas scikit-learn
```

## Kullanım

İş başvurularını değerlendirmek için scripti Python ile çalıştırın:

```bash
python decision.py
```

`DecisionTreesClassificationDataSet.csv` veri setinin, scripte göre `data` klasöründe yer aldığından emin olun.

## Özellikler

- Model eğitimi için kategorik verilerin sayısal formata dönüştürülmesi.
- Bir iş başvuru sahibinin uygunluğunu tahmin etmek için bir karar ağacı modelinin eğitilmesi.
- Başvuru sahiplerinin eğitim, iş tecrübesi ve diğer ilgili faktörlere göre değerlendirilmesi.

## Bağımlılıklar

- numpy
- pandas
- scikit-learn

## Konfigürasyon

Bu script, sağlandığı şekilde çalıştırmak için ek bir konfigürasyona ihtiyaç duymaz. Scriptteki veri seti yolunun doğru olduğundan emin olun:

```python
df = pd.read_csv("data/DecisionTreesClassificationDataSet.csv")
```

## Örnekler

Script, tahminlerin iki örneğini içerir:

1. 5 yıl tecrübeli, halen çalışan, lisans derecesine sahip, ilk 10 üniversiteden mezun olmayan ve şirkette staj yapmamış bir başvuru sahibinin işe alınacağı tahmin edilmektedir (`[1]`).
2. 2 yıl tecrübeli, şu anda çalışmayan, doktora derecesine sahip, ilk 10 üniversiteden mezun olan ve şirkette staj yapmamış bir başvuru sahibinin işe alınmayacağı tahmin edilmektedir (`[0]`).

## Sorun Giderme

Scripti çalıştırırken herhangi bir sorunla karşılaşırsanız, şunlardan emin olun:

- Python sürümünüzün 3.6 veya daha yeni olduğu.
- Tüm bağımlılıkların doğru bir şekilde yüklendiği.
- Veri seti dosyasının doğru dizinde ve uygun şekilde adlandırıldığı.

## Katkıda Bulunanlar

Emircan Yüksel




