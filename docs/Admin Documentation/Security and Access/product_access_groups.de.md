# Produktzugriffsgruppen

!!! info "Diese Funktion ist standardmäßig nicht aktiviert"
    Wenn Sie Produktzugriffsgruppen für Ihre Organisation ausprobieren möchten, wenden Sie sich bitte an asm-support.df@asmpt.com.

Service-Organisationen haben oft verschiedene Teams, die auf unterschiedliche Arten von Dokumenten zugreifen müssen. Der Vertrieb benötigt Preislisten und Produktbroschüren, Techniker vor Ort benötigen Serviceanleitungen und technische Bulletins, Inbetriebnahme-Teams benötigen Montageanleitungen usw.

Kurz gesagt, **Benutzer können nur Produktlinien (und ihre entsprechenden Dokumente und Inhaltsmodule) sehen, die der Produktzugriffsgruppe zugewiesen sind, der sie angehören.**

![Status Quo](https://i.imgur.com/VnLylKq.png)

Wenn Sie den Zugriff auf bestimmte Informationen nur auf Teile Ihrer Service-Organisation beschränken möchten, sind Produktzugriffsgruppen das Richtige für Sie. Produktzugriffsgruppen sind standardmäßig nicht aktiviert.

Wenn Sie sich für weitere Details zu Produktzugriffsgruppen interessieren, lesen Sie das folgende Beispiel.

??? example
    Stellen Sie sich ein Unternehmen vor, **3D-Drucker GmbH**. Sie produzieren und vermarkten 3D-Drucker für den industriellen Markt. Sie nutzen ASMPT Virtual Assist für ihre umfangreichen Dokumentations- und Informationsbereitstellungsbedürfnisse. 3D-Drucker GmbH hat zwei regionale Abteilungen: **EMEA** und **Americas**. Beide Abteilungen stehen unter **Global Management**, mit Sitz in München.

    Chandler ist Global Service Manager und verantwortlich für die Koordination aller Service-Operationen weltweit. Joey und Ross, die Leiter des Servicebereichs für EMEA bzw. Americas, berichten an ihn.

    Es gibt zwei Arten von Dokumenten, auf die Chandler über ASMPT Virtual Assist zugreifen möchte:

    - 3D-Drucker (Montageanleitungen, Schaltpläne, Serviceanleitungen usw.)
    - Vertriebsdokumente (Broschüren, Preislisten, Kataloge)

    ### Problem
    Die Vertriebsdokumente variieren je nach Region: Europäische Unternehmen zahlen aufgrund der Lohnkosten mehr als südamerikanische Unternehmen. Die 3D-Drucker selbst sind jedoch überall identisch.

    ### Lösung
    Um die Service-Teams für jede Region nicht durcheinander zu bringen, beschließt Chandler, die Vertriebsdokumente in **Vertriebsdokumente (EMEA)** und **Vertriebsdokumente (Americas)** aufzuteilen.

    Er möchte immer noch, dass alle Benutzer Zugang zur 3D-Drucker-Dokumentation haben, aber den Zugriff auf die Vertriebsdokumente nach Region beschränken.

    Hier können **Produktzugriffsgruppen** helfen: Mit der Hilfe von ASMPT Virtual Assist erstellt Chandler drei verschiedene Zugriffsgruppen:

    - **Globale Produktgruppe** für Chandler und sein Team in München
    - **EMEA Produktgruppe** für alle im EMEA-Team
    - **Americas Produktgruppe** für alle im Americas-Team

    ![Status Quo](https://i.imgur.com/xq4Lbn4.png)

    ### Was bedeutet das?

    Ganz einfach: Die Benutzer können nur die Produktlinien sehen, die der Produktzugangsgruppe zugeordnet sind, der sie angehören.

    Für Maximilian, Serviceleiter für EMEA, sieht das so aus:

    ![Head of Service EMEA](https://i.imgur.com/B7JMtGo.png)

    Joey kann zwei Produktlinien sehen, nämlich diejenigen, die für seine Arbeit relevant sind.

    Chandler kann alle Produktlinien sehen, da alle Produktlinien zur Produktgruppe Global gehören.

    ![Globaler Serviceleiter](https://i.imgur.com/L4rfLfc.png)
