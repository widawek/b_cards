Używając dziedziczenia, rozdziel podstawową klasę wizytówki na dwie osobne:
pierwsza (BaseContact) powinna przechowywać podstawowe dane kontaktowe takie jak imię, nazwisko, telefon, adres e-mail. 
Za pomocą kolejnej klasy (BusinessContact) rozszerz klasę bazową o przechowywanie
informacji związanych z pracą danej osoby – stanowisko, nazwa firmy, telefon służbowy.
Oba typy wizytówek, powinny oferować metodę contact(),
która wyświetli na konsoli komunikat w postaci “Wybieram numer +48 123456789 i dzwonię do Jan Kowalski”. 
Wizytówka firmowa powinna wybierać służbowy numer telefonu, a wizytówka bazowa prywatny.
Oba typy wizytówek powinny mieć dynamiczny atrybut label_length,
który zwraca długość imienia i nazwiska danej osoby.
Stwórz funkcję create_contacts, która będzie potrafiła komponować losowe wizytówki. 
Niech ta funkcja przyjmuje dwa parametry: rodzaj wizytówki oraz ilość.
Wykorzystaj bibliotekę faker do generowania danych.