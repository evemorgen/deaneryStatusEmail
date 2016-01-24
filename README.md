# deaneryStatusEmail

Ponieważ wirtualny dziekanat na AGH jest bardzo ubogi w funkcjonalności, postanowiłem stworzyć skrypt który wysle wiadomość email w momencie pojawienia się nowej oceny końcowej. Szczególnie przydane, gdy ktoś sprawdza status dziekanatu co 10 minut w oczekiwaniu na wynik egzaminu. 


Wymagania:
 - dostęp no jakiegoś serwera (np  uczelnianego) (np konto na serwerze student.agh.edu.pl)
 - zainstalowany python w wersji 2.X na serwerze
 - dostęp do Crona na serwerze
 - zainstalowany sendmail na serwerze


INSTRUKCJA DO "INSTALACJI" skryptu.

1) wrzuć  paczkę na serwer ( scp paczka.zip twojlogin@student.agh.edu.pl:~/ ) </ br>
2) zaloguj się na serwer i rozpakuj paczkę (ssh twojlogin@student.agh.edu.pl oraz unzip paczka.zip)</ br>
3) ustaw prawa dostępu dla całego folderu chmod -R 755 pythonDeaneryStatus</ br>
4) wyedytuj swoim ulubionym edytorem plik run.sh (np nano run.sh) i wstaw swoj login do studenta tam gdzie trzeba </ br>
5) wyedytuj swoim ulubionym edytorem plik sekret.py i wstaw odpowiednie dane (spokojnie, nikt nie będzie miał do nich dostępu) </ br>
6) uruchom polecenie crontab -e i wklej następującą linijkę: </ br>
* * * * * /home/eaiibgrp/<--tu wstaw swoj login-->/pythonDeaneryStatus/run.sh
7) po około minucie powinieneś zauważyć że w folderze są dwa pliki sekret.py oraz sekret.pyc, dla nich należy wykonać polecenie chmod 700 </ br>
chmod 700 sekret.py
chmod 700 sekret.pyc

Dzięki temu nikt nie będzie miał dostępu do Twoich danych

8) profit? </ br>
9) jeśli chcesz sprawdzić czy skrypt działa ok to w głównym katalogu Twojego konta (tj. ~/ ) powinien znajdować się plik "stare.csv", usuń z niego jakąś ocenę i czekaj na email. Jeżeli wszystko działa tak jak trzeba to po około minucie powinieneś dostać email z oceną. </ br>
10) Jeżeli coś nie działa to możesz odpalić skrypt samodzielnie i sprawdzić output </ br>
python2.6 getFromWeb.py
