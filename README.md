# Tank-U
Uni Projekt
Praxisprojekt Softwareentwicklung




Projekt: Netzwerkfähiges Mehrspieler Python Game (NMPG)




Titel: TANK-U

V: 1.0




Entwickelt von: Hannes Sattler (804846), Willi Siedlaczek (805374), Konrad Firley (804764)




------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




Was ist TANK-U?




Tank-U ist ein netzwerkfähiges Mehrspieler Videospiel geschrieben in Python. Das Spiel basiert

vom Prinzip auf altbekannten Panzer Spielen wie Tank Wars oder neueren Titeln wie Shellshock Live.

Inspiriert davon haben wir hier, im Rahmen unseres Praxisprojekts, ein 2D Panzer Kampf spiel gebaut.

Das Ziel im Spiel ist es als erster den Gegnerischen Panzer zu zerstören und somit die Schlacht zu

gewinnen. Wir wünschen ihnen viel Spaß beim Zocken!




------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




Das brauch ich, um Tank-U zu spielen...




- Python             3.8

- pygame	         2.1.2

- button	         0.0.3

- pip	             22.0.4

- python-dateutil	 2.8.2

- setuptools	     58.1.0

- six	             1.16.0

                 (oder jeweils eine neuere)




------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




Um TANK-U zu starten, muss ich...




(Das Spiel befindet sich aktuell im Ordner "prototyp python test2 von Hannes" das ist deswegen da wir dort als erstes

den Server plus Client zum Laufen bekommen haben und wir dort mit der Zeit weiter gecoded haben)

 ...als erstes den Ordner "prototyp python test2 von Hannes" öffnen

 ...dort muss ich in der Datei "tank_server" und in "tank_network" die IP vom Computer eingeben welcher sich im selben

    Netzwerk befindet und auf dem der Server Laufen soll. (PS: am besten einfach einen Computer auf dem man dann zockt.)

 (Info: beide Computer müssen bei sich die gleiche IP eintragen, man kann aber auch tank_client zweimal ausführen)

 ... jetzt kann man den server starten

 ... anschließend tank_client starten

 ...schon kann man zocken

 ...nach jedem match muss man Server und Clients neustarten




Viel Spaß!




------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Datum: 07.07.2022

Aktuelle bekannte Bugs:

- Hitboxen sind nicht ganz auf der gleichen Position wie die Bilder der Panzer

- Flackern der Spieler, wegen server logic

- Winkel Einstellung etwas fehlerhaft, bleibt stecken --> quickfix reset button auf R

- Flackern von Winner und Loser Screen




Bugs die behoben werden bis zur Präsentation:

- Hitboxen und Bild werden besser mit einander verbunden
