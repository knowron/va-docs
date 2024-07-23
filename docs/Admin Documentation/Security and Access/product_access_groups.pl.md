# Grupy dostępu do produktów

!!! info "Ta funkcja nie jest domyślnie włączona"
    Jeśli chcesz wypróbować grupy dostępu do produktów w swojej organizacji, skontaktuj się z [us](https://smt.asmpt.com/en/products/software-solutions/virtual-assist).

Organizacje usługowe często mają różne zespoły, które muszą mieć dostęp do różnych typów dokumentów. Sprzedaż usług będzie wymagała cenników i broszur produktowych, technicy w terenie będą potrzebować instrukcji serwisowych i biuletynów technicznych, zespoły rozruchowe będą potrzebować instrukcji montażu itp.

Mówiąc najprościej, **użytkownicy będą mogli zobaczyć tylko linie produktów (oraz odpowiadające im dokumenty i jednostki treści), które są przypisane do grupy dostępu do produktów, do której należą.**

![Status Quo](https://i.imgur.com/VnLylKq.png)


Jeśli chcesz **ograniczyć dostęp** do niektórych informacji tylko do części organizacji usługowej, grupy dostępu do produktów są dla Ciebie. **Grupy dostępu do produktów nie są domyślnie aktywowane.**

Jeśli chcesz uzyskać więcej informacji na temat grup dostępu do produktów, zapoznaj się z poniższym przykładem.

??? przykład

    Wyobraźmy sobie firmę **3D Printers GmbH**. Produkują i sprzedają drukarki 3D na rynek przemysłowy. Korzystają z oprogramowania ASMPT Virtual Assist ze względu na swoje obszerne potrzeby w zakresie dokumentacji i dostarczania informacji. 3D Printers GmbH ma dwa oddziały w zależności od regionu: **EMEA** i **Ameryki**. Oba te działy podlegają **Global Management** z siedzibą w Monachium.

    Chandler jest globalnym kierownikiem ds. usług i odpowiada za koordynację wszystkich operacji serwisowych na całym świecie. Joey i Ross, szefowie służb odpowiednio na region EMEA i obie Ameryki, podlegają mu.

    Istnieją dwa rodzaje dokumentów, które firma Chandler chce udostępnić za pośrednictwem firmy ASMPT Virtual Assist:

    - Drukarki 3D (instrukcje montażu, schematy obwodów, instrukcje serwisowe itp.)
    - Dokumenty sprzedaży (broszury, cenniki, katalogi)

    ### Problem 
    Dokumenty sprzedaży różnią się w zależności od regionu: firmy europejskie są obciążane wyższymi opłatami niż firmy z Ameryki Południowej ze względu na koszty pracy. Same drukarki 3D są jednak wszędzie identyczne.

    ### Rozwiązanie
    Aby uniknąć dezorientacji zespołów serwisowych w każdym regionie, Chandler zdecydował się podzielić dokumenty sprzedaży na **Dokumenty sprzedaży (EMEA)** i **Dokumenty sprzedaży (Ameryki)**. 

    Nadal chce, aby wszyscy użytkownicy mieli dostęp do dokumentacji drukarki 3D, ale chce ograniczyć dostęp do dokumentów sprzedaży w zależności od regionu.

    Oto, w czym mogą pomóc **Grupy dostępu do produktów**: z pomocą firmy ASMPT Virtual Assist firma Chandler tworzy trzy różne grupy dostępu:

    - **Globalna grupa produktowa** dla Chandlera i jego zespołu w Monachium
    - **Grupa produktów EMEA** dla wszystkich członków zespołu EMEA
    - **Grupa produktów Americas** dla wszystkich członków zespołu Americas

    ![Status Quo](https://i.imgur.com/xq4Lbn4.png)

    ### Co to znaczy?

    Po prostu użytkownicy będą mogli zobaczyć tylko te linie produktów, które są przypisane do grupy dostępu do produktów, do której należą.

    Dla Joeya, szefa serwisu na region EMEA, wygląda to tak:

    ![Head of Service EMEA](https://i.imgur.com/B7JMtGo.png)

    Joey widzi dwie linie produktów, te, które są istotne dla jego pracy.

    Chandler widzi wszystkie linie produktów, ponieważ wszystkie linie produktów należą do globalnej grupy produktów.

    ![Global Head of Service](https://i.imgur.com/L4rfLfc.png)
