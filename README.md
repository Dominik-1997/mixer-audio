## mixer-audio
# Idea i założenia projektu

Celem tego projektu było stworzenie praktycznego urządzenia, które będę mógł wykorzystywać w codziennym życiu. Zdecydowałem się zaprojektować mikser audio.
Kontrolowanie poziomów głośności bywa uciążliwe, kiedy korzysta się z kilku aplikacji jednocześnie. W trybie pełnoekranowym najpierw klikamy windows key, potem wykonujemy 4 kolejne kliknięcia, w trakcie scrollując jeszcze przez ustawienia dźwięku (Windows 11), a fizyczny mikser sprawia, że wszystkie te ustawienia są dosłownie pod ręką.
Sam projekt jest w miarę prosty, a jego najważniejsze części to mikrokontroler i potencjometry.

# Części

- 2 x Płytka stykowa (wystarczyłaby jedna ale chciałem mieć więcej miejsca)
- 1 x Lolin32 lite (ESP32)
- 5 x Potencjometr obrotowy 1k ohm
- 1 x Kabel micro USB to USB
- 22 x Kabel male-to-male

# Budowa

Po przejściu szkolenia BHP w Makerspace, zlutowałem swój mikrokontroler (udało się to zrobić bez problemów mimo, że lutowałem pierwszy raz od czasu zajęć z techniki w gimnazjum) i zbudowałem projekt na płytce stykowej.
Jeden potencjometr steruje głównym poziomem głośności i cztery potencjometry sterują głośnościami 4 dowolnych aplikacji (lub grup aplikacji) np.: 1. Przeglądarki, 2. Komunikatory, 3. Multimedia, 4. Gry.
Początkowo potencjometry miały być suwakowe, ale ostatecznie zdecydowałem się na obrotowe (są kilkukrotnie tańsze i mniejsze).
Potencjometry są bezpośrednio podłączone do pinów ADC mikrokontrolera, a sam mikrokontroler podłączony kablem USB do komputera.

Kod znajduje się w dwóch miejscach:

1. Mikrokontroler czyta wartości potencjometrów i wysyła je do komputera.
2. Aplikacja na komputerze czyta przesyłane wartości oraz steruje poziomami głośności.
