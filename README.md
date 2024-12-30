# Prätherapeutisches Tumorboard für Prostatakarzinompatienten

Dieser Algorithmus dient der automatischen Generierung von Empfehlungen für das prätherapeutische Tumorboard.
Es handelt sich hierbei um Patienten mit einem histologisch gesicherten Prostatakarzinom, wo die weitergehende Diagnostik und Therapie multidisziplinär besprochen werden soll.

Das Modell basiert auf einem multivariablen Random Forest mit einem multilabel Outcome mit den Inputvariablen Alter, PSA, DRU (Digital Rektale Untersuchung), ISUP-Kategorie, Anzahl positiver Stanzen, Gesamtzahl der Stanzen und dem Vorliegen bestimmter Vorerkrankungen (Arterielle Hypertonie, Diabetes mellitus, Koronare Herzerkrankung, Adipositas, Voroperationen).
Als Outcomevariablen wurden die entsprechenden Tumorboardempfehlungen in die Empfehlungen für ein PSMA-PET konventionelles Staging (CT und Knochenszintigraphie), Aktive Überwachung und lokale Therapie (radikale Prostatektomie und perkutane Strahlentherapie) in eine Multilabel-Variable konvertiert. Die Outcomevariable wird nach der Prädiktion in den entsprechenden Empfehlungstext konvertiert.

Die App benutzt das Streamlit Framework als Frontend und läuft als Server über die [Streamlit Community Cloud](https://ukd-uro-pretb-full.streamlit.app).


> [!Warning]
> Es handelt sich um ein Projekt in Entwicklung ohne entsprechende Zulassung als Medizinprodukt und ist daher nur für den experimentellen Einsatz geeignet.
