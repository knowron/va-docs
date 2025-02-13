# Rollen und Berechtigungen

!!! tip "Brauchen Sie mehr Optionen? Sprechen Sie mit uns!"

    Das System von ASMPT Virtual Assist ist auf maximale Modularität für Unternehmenskunden ausgelegt. Wenn Sie andere Rollen oder einen anderen Satz von Berechtigungen benötigen, lassen Sie es uns wissen - kontaktieren Sie uns einfach [us](https://smt.asmpt.com/en/products/software-solutions/virtual-assist).

Mit ASMPT Virtual Assist können Sie wählen, welche Funktionen und welchen Zugriff jeder einzelne Benutzer erhält. Einige Benutzer, wie z.B. jüngere Kollegen, werden hauptsächlich Informationen **konsumieren**, während erfahrenere Benutzer viel davon **erstellen und kuratieren**.

Jeder Benutzer hat eine **Rolle**. Diese Rolle bestimmt, welche Aktionen sie durchführen können und sogar auf welche Funktionen sie Zugriff haben. Benutzer können derzeit eine von drei Rollen haben: 

- [Admin](#admin)
- [Editor](#editor)
- [Contributor](#contributor)
- [Viewer](#viewer)

Für jede Systemkomponente gibt es **Berechtigungen**, die festlegen, ob eine Rolle eine bestimmte Aktion ausführen darf. Jede der oben aufgeführten Rollen hat eine einzigartige Kombination von Berechtigungen. Im Folgenden finden Sie weitere Informationen zu den einzelnen Rollen.

## Rollen

### Admin

Admins sind **Systemadministratoren**. Sie sind oft Service- oder Engineering-Manager, die daran interessiert sind, dass ihre Kollegen die bestmögliche Arbeit auf die effizienteste Weise leisten. 

Sie können alles im System lesen und schreiben und können entscheiden, was andere Benutzer sehen können.

!!! warning "Mit großer Macht kommt große Verantwortung"

    Admins haben Zugang zu allen Komponenten und potenziell sensiblen Daten. Vergewissern Sie sich, dass Sie der Person, die Sie zum Administrator ernennen, vertrauen!

|                         | Erstellen | Bearbeiten | Löschen | Anzeigen |
|-------------------------|-----------|-----------|---------|----------|
| **Insights-Dashboard**  | ✅        | ✅        | ✅      | ✅        |
| **Suche**               | ➖        | ➖        | ➖      | ✅        |
| **Artikel**             | ✅        | ✅        | ✅      | ✅        |
| **Tutorials**           | ✅        | ✅        | ✅      | ✅        |
| **Dokumente**           | ✅        | ✅        | ✅      | ✅        |
| **Expertenantworten**   | ✅        | ✅        | ✅      | ✅        |
| **Produktlinien**       | ✅        | ✅        | ✅      | ✅        |
| **Maschinenbestand**    | ✅        | ✅        | ✅      | ✅        |
| **Logbuch**             | ✅        | ✅        | ✅      | ✅        |
| **Benutzer**            | ✅        | ✅        | ✅      | ✅        |

### Editor

Editors sind **Inhaltsmanager**. Sie sind oft eher Support-Ingenieure der ersten Ebene, erfahrene Außendiensttechniker, die mit ihrem Fachwissen einen großen Beitrag leisten können. Sie sind daran interessiert, dass ihre Kollegen die richtigen Informationen zur richtigen Zeit erhalten. 

Sie können alle **Inhaltseinheiten** (Anleitungen, Dokumente und Produktlinien) erstellen, bearbeiten und lesen. Sie können auch Feedback-Schleifen erstellen, um die Suche zu verbessern.

Editors sind **nicht** berechtigt, globale Einstellungen zu ändern oder andere Kollegen auf die Plattform einzuladen. Sie können auch keine Einstellungen anderer Benutzer ändern.

|                         | Erstellen | Bearbeiten | Löschen | Anzeigen |
|-------------------------|-----------|-----------|---------|----------|
| **Insights-Dashboard**  | ✅        | ✅        | ✅      | ✅        |
| **Suche**               | ➖        | ➖        | ➖      | ✅        |
| **Artikel**             | ✅        | ✅        | ✅      | ✅        |
| **Tutorials**           | ✅        | ✅        | ✅      | ✅        |
| **Dokumente**           | ✅        | ✅        | ✅      | ✅        |
| **Expertenantworten**   | ✅        | ✅        | ✅      | ✅        |
| **Produktlinien**       | ❌        | ✅        | ❌      | ✅        |
| **Maschinenbestand**    | ✅        | ✅        | ✅      | ✅        |
| **Logbuch**             | ✅        | ✅        | ✅      | ✅        |
| **Benutzer**            | ❌        | ❌        | ❌      | ❌        |

### Contributor

Contributors sind Viewer-Nutzer mit **erweiterten Rechten zur Inhaltserstellung**. Häufig handelt es sich um Mitarbeitende in der Produktion, die neue Entwürfe für Tutorials oder Artikel hochladen können. Diese Entwürfe müssen jedoch von einem Editor oder Admin validiert werden, bevor sie veröffentlicht werden.

|                         | Erstellen        | Bearbeiten                         | Löschen                            | Anzeigen |
|-------------------------|------------------|------------------------------------|-------------------------------------|----------|
| **Insights-Dashboard**  | ❌              | ❌                                  | ❌                                   | ❌        |
| **Search**              | ➖              | ➖                                  | ➖                                   | ✅        |
| **Articles**            | 🟧 (nur Entwürfe) | 🟧 (nur Entwürfe & wenn Besitzer)   | 🟧 (nur Entwürfe & wenn Besitzer)    | ✅        |
| **Tutorials**           | 🟧 (nur Entwürfe) | 🟧 (nur Entwürfe & wenn Besitzer)   | 🟧 (nur Entwürfe & wenn Besitzer)    | ✅        |
| **Documents**           | ❌              | ❌                                  | ❌                                   | ✅        |
| **Expert Answers**      | ❌              | ❌                                  | ❌                                   | ✅        |
| **Product Lines**       | ❌              | ❌                                  | ❌                                   | ✅        |
| **Machine Inventory**   | ❌              | ❌                                  | ❌                                   | ✅        |
| **Logbook**             | ✅              | ✅ (wenn Besitzer)                  | ✅ (wenn Besitzer)                   | ✅        |
| **Users**               | ❌              | ❌                                  | ❌                                   | ❌        |


### Viewer

Viewers sind **normale Benutzer**. Sie machen den Großteil der ASMPT Virtual Assist Nutzer aus. Sie sind oft Service-Ingenieure und Außendiensttechniker, die schnell auf Informationen zugreifen müssen. Sie haben nicht immer die Zeit oder das Fachwissen, um Inhalte zu erstellen oder zu ändern, daher ist es ihnen nicht erlaubt.

Sie können alle **Inhaltseinheiten** (Anleitungen, Dokumente und Produktlinien) sehen und natürlich auch suchen.

|                         | Erstellen | Bearbeiten           | Löschen             | Anzeigen |
|-------------------------|-----------|----------------------|---------------------|----------|
| **Insights-Dashboard**  | ❌        | ❌                   | ❌                  | ❌        |
| **Suche**               | ➖        | ➖                   | ➖                  | ✅        |
| **Artikel**             | ❌        | ❌                   | ❌                  | ✅        |
| **Tutorials**           | ❌        | ❌                   | ❌                  | ✅        |
| **Dokumente**           | ❌        | ❌                   | ❌                  | ✅        |
| **Expertenantworten**   | ❌        | ❌                   | ❌                  | ✅        |
| **Produktlinien**       | ❌        | ❌                   | ❌                  | ✅        |
| **Maschinenbestand**    | ❌        | ❌                   | ❌                  | ✅        |
| **Logbuch**             | ✅        | ✅ (wenn Besitzer)    | ✅ (wenn Besitzer)   | ✅        |
| **Benutzer**            | ❌        | ❌                   | ❌                  | ❌        |

## Wie man die Rolle eines Benutzers ändert

!!! warning "Nur Admins können diese Aktion ausführen"

    Standardmäßig können nur Administratoren die Rollen anderer Benutzer ändern. Wenn Sie kein Administrator sind und eine Rollenänderung benötigen, wenden Sie sich bitte an Ihren Manager.

<p align="center"><img src="https://i.imgur.com/CdsfoEC.gif" width="100%"></p>