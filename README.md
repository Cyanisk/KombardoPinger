# KombardoPinger

## Anvendelse
Bliv notificeret når udsolgte afgange med [Bornholmslinjen](https://www.bornholmslinjen.dk/) bliver ledige.

1. Vælg transport og en række datoer

![Screenshot from 2022-09-11 17-53-17](https://user-images.githubusercontent.com/101006560/189537425-acfc6e17-fc24-48af-90f8-3c932f27cdf8.png)

2. Vælg tidsintervaller, enten for de individuelle datoer eller generelt for alle valgte datoer

![Screenshot from 2022-09-11 17-54-54](https://user-images.githubusercontent.com/101006560/189537486-49c438e7-c93d-41fe-8b4b-799b17475110.png)

3. Vælg en email a sende notifikationer til

![Screenshot from 2022-09-11 17-55-03](https://user-images.githubusercontent.com/101006560/189537702-78d29740-1cdf-473b-b8b0-67b0d4a56565.png)

4. Hold computeren tændt og hold øje med mail om nye ledige afgange

![Screenshot from 2022-09-11 17-55-19](https://user-images.githubusercontent.com/101006560/189537760-c4f96c1f-ff5f-40c1-a189-b60add58dbd9.png)
![Screenshot from 2022-09-11 18-17-45](https://user-images.githubusercontent.com/101006560/189538177-84659482-83ec-4ccd-925c-85fbcbd091ad.png)

## Opsætning
De vigtigste forudsætninger for at kunne bruge KombardoPinger er
- Python3 (jeg bruger 3.10)
- PyQt5
- Selenium (til python)
- [Gecko Driver](https://github.com/mozilla/geckodriver/releases) (så KombardoPinger kan interagere med Bornholmslinjens bookingsystem)
- Udfyld variables.txt
  - For at sende notifikationer, skal KombardoPinger bruge en mailaddresse at sende fra
  - Udfyld ```smtp_server```, ```port```, ```sender``` og ```password``` med gyldige værdier
