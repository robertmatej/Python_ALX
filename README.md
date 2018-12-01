# Python_ALX" 



##PAKIETY python
można instalować nie róźne gotowe moduły, pisane przez innych userow

pip install warto podawać wersję programu gdzy coś stworzymy, po po rozwinięcu może być zgodności wstecznej

##Rysowanie wykresów
seaborn
bokeh




###Ciekawostki

www.kaggle.com
www.dane.gov.pl
python music21


##Sprawdzanie HELPa
metoda lub funkcja i ?
np. range()?
help (range)
najeżdzając na metodę z CTRL wchodzimy w funkcję metody


##Odpalanie innych programow z pythona



## Python logging
narzędzie do sporządani logów ze zdarzeń



## WEB scrapping
odpytywanie stron o zadaną frazę

Biblioteki:
pip install beautifulsoup4
pip install requests

POPST - zapytanie nasze danie nie są widoczne (są zaszyfrowane)
GET - przesyłamy zapytanie i jest widocznie (NIE zaszyfrowane)

RMB w przegldarce -> zbadaj element

Gdy strony są w Java Script i odpalenie następuje dopiero na stronie w przeglądarce GET
może sobie nie poradzić
można użyć selenium

##SQL Alchemy
kolejna biblioteka



## Wyrażenia regularne (RegExr)
https://regexr.com/   obrazuje działanie wyrażeń regularnych
wyszukuje numer 123-456-789
\d{3}-\d{3}-\d{3}

python regexr

Przeszukiwanie we wszystkich plikach projektu:
RMB na bootcamp -> find in path-> zaznaczamy regex i szuka


## DATETIME

## MATH
sinusy itp. 

#Dizś 01.12.2018 ostatni zjazd


## JUPYTER
w terminalu:
jupyter notebook    # i odpali się jupyter w przegldarce


##NUMPY
w jupyter instalacja modułów 
!pip install numpy
!pip install matplotlib

pip install numpy
pip install matplotlib
pip install jupyter
jupyter notebook w terminalu
!pip install opencv-python            # wykrzyknik tylko dla yupytera
ndimage.gaussian_filter?          # jupyter zapytanie o popis funkcji


a = np.array ([1,2,3],[2,3,4],)             # definiowanie tabliczy array z numpy
np.zeros((5,4))                         # tablica zainicjopwana zerami o rozmiarze 
a.arange(20)       #ablica 20 elementów jest  genrerowana
a.reshape(3,4)      zienia rozmiary wg wskazania
c= np.linespace(0,2,9)     # bierze przedział 0-2 i tworzy w tym przedziale 9 elementow
numpy ma wiele typów danych które zależnie od rozmiwau zmiennej alolkuje odpowiedno "miałą" zmienną aby ni3 zapychaćpamięći 
np.array([1,2,3],dtype='float').dtype     rzutujemy na float pomoiimoze całkowicte dtype wywołuje sprawdznie typu
a.astype(np.float)          całą tablicę a zamienamy na float
mozna stworzyc tablice z true i falsami
a.astype(np.bool)
b.max()    zwraca max wartosc z tablicy
i.info(np.int8)      # ?? ograniczmy do zmiennej typu intiger8?
a.itemsize     # sprawdzamy rozmiar obiektu w pamieci
A*B         # mnożenie elementów odpowiadajacyhc
A.dot(B)     # mnożenie macierzeowe
Broadcasting rozciąganie mniejszej macierzy
b=.sum(axis=0)   cumuje tylko wiersz 0
wybieranie elementu  z macierzy
b[2,3]     z wierasz 2 wybierze 3 element
b[1:2,2:2]   zakres danych wyubierze

układanie łączenie róźnych tablic - stacking
np.vstack([a,b])
np.hstack([a,b])

###### import obrazu
import cv2
im2 = cv2.imread("images/index.jpeg")


#! pip install scipy
from scipy import ndimage

im_rotate = ndimage.rotate(im1,90)
plt.imshow(im_rotate)

####### SciPhy
pip install scipy
dal macierzy żadkich smae 0 lub 1

plt.imshow(ndimage.gaussian_filter(im1,2))  # filtr gausowski


##Pandas - narzędzie do analizy danyhc
prowadzący pracował na pliku Wstep do Pandas - poszukać na githubie
www.pandas.pydata.org

pip install pandas
pip install xlrd
pip install openpyxl
import pandas as pd



!ls
folder_path = './files_pandas...'
po wczytaniu zbioru możemy wywołc pierwsze 5 wierszy
data.head()
data.tail()   # koniec zbioru

data.shape() rozmiar
data.info() opis funkcjonalności
data.describe()   #robi zestaw statystyk z danych
data.columns()      
data.types()
data[['name']]   #wybierze konkretną kolumnę o nazwie: xxx..
dir(df.Survived)         # survived to nazwa jednej z kolumn, wyświetla możliwe metody dla df
można też wczytać plik spakowany zip

wywoływanie przez labele loc[]
data.loc[5:10,Pclass:Age]       # wybiera od wierszy 5 do 10 kolumny od pclas do age
data.iloc[5:10, 3]              # to samo ale operuemy tylko numerami kolumn wierszy
data.columns.get_slice_bound("name", "left", 'id')

data2= pd.read_excell()
data3 = pd.read_pickle(os.pathc.join(foldr_path, nazwa_pliku.pickle))

Możliwośc wczytywania danych porcjami

uzupełnianie pustych wartośći
dta.Cabin.fillna("Deck")            puste wartości sią wypełniane zadaną wartośćią
dta.Age.fillna(data.Age.mean(), inplace = True)      puste wartości uzupełnia sie srednią wieku np
data.Embarket.fillna.??                   da się wyświetlić najczęściej występującą wartość

ROZWIAZANIA CWICZEN
cały czas działamy na titanic_train
Display passengers with Age above 50
#dane = df.loc[:,"Age"]>50
dane2=df[df.Age>50]
dane2

Display passengers that Embarked at location S and are female
df[(df.Embarked=="S") & (df.Sex == 'female')]

Display passengers that paid for ticket more than 50 and are not in first class
df[(df.Fare>50) & (df.Pclass <= 1)]      

Display all passengers with Names that contain 'Johnson' (it's a surname)
df[df.Name.str.contains("Johnson")]


Spsoby wyswitalania danch, pracujemy na macierzy:
df.DataFrame()
pd.Series()


data=pd.read_csv('files/matches.csv',parse_dates=['date'])     #parsuj daty
data.head()

Korzystając z pliku matches.csv zawierającego dane o rozgrywkach piłkarskich:
1.Znajdź wszystkie mecze pomiędzy dwoma wybranymi drużynami w latach 2010-2015.\
2.Znajdź 10 meczów z największą różnicą bramek.
3.Policz liczbę zdobytych i straconych bramek na sezon dla wybranej drużyny. Narysuj wykres obrazujący uzyskane wyniki.
4.Policz średnią liczbę bramek przypadającą na jeden mecz w każdej lidze. Narysuj wykres obrazujący uzyskane wyniki.

data=pd.read_csv('files/matches.csv',parse_dates=['date'])
data.head()

data[((data.home_team=="Legia Warszawa") | (data.away_team=="Lech Poznań"))]    #1. bez lat

data["concentrate_team"] = data['home_team']+data['away_team']    
data
data['goal_difference']=abs(data['home_team_goal']-data['away_team_goal'])   #zad 2
data.sort_values("goal_difference", ascending=False).head(10)

CWICZENIA:
jupyter iris_dataset_analize