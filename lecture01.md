---
title: "Struktura a typy lékařských přístrojů"
author: "Tomáš Černík"
---

<div class="sections">


<div class="sectionbox">

### Vznik signálu
- **Vlastní činností organismu:**
	- Elektrická aktivita nervů a svalů
	- Srdeční činnost
	- Mozková aktivita
- **Vlivem vnějšího působení:**
	- Reakce na světlo, zvuk a tlak
	- Odpověď na elektrickou nebo mechanickou stimulaci

</div>

<div class="sectionbox">

## Vlastnosti biologickkých signálů
- **Amplituda**:
	- Velmi malé hodnoty, typicky jednotky miktovolt až $mV$
	- EEG  = desítky $\mathrm{\mu V}$
	- EKG  = cca 1 $\text{mV}$
	- EMG = jednotky $\mathrm{mV}$
	- klade poměrně velké nároky na kvalitu zesílení a potlačení rušení
- **Frekvenční rozsah:**
	- Velmi široký - setiny Hz až stovky Hz
	- EEG  = 0.1-100 Hz
	- EKG  = 0.05 - 150 Hz
	- EMG = až stovky Hz
	- vyšší frekvence jsou náchylné na šum
	- nižžší jsou náchuylné na pohybové artefakty
- **Výstupní odpor zdroje**
	- Velmi vysoký výstupní odpor - každý reálný zdroj lze nahradit ideálním zdrojem napětí s nějakým vnitřním odporem - biologický zdroj je např: přes buněčné membrány, přes tkáně s velkým odporem - čím větší R, tak tím menší proud zdroj dodá - často desítky $\text{k}\Omega$
	- **Příklad:**
		- Máme EKG, kde si srdce vytváří napětí 1 $\text{mV}$ a výstupní odpor zdroje je 30 $\text{k}\Omega.$ Připojím měřící přístroj s vstupním odporem 10 $\text{k}\Omega$. 
*<font style="color:orange">Pochopit odpor tkání a jejich měření</font>*

$$
\begin{align}
	\mathrm{R_{celkem} = R_Z + R_{měř} = 30 + 10 = 40} \\
	\mathrm{\text{Obvodem teče proud: } I = \frac{U_z}{R_{celk}} = \frac{1~mV}{40~k\Omega}} \\
	\mathrm{\text{Jaké napětí měříme? } U_{měř} = I \cdot R_{měř}} \\
	\mathrm{U_{měř} = \frac{U_z}{R_z + R_{měř}} \cdot R_{měř}}
\end{align}
$$

</div>


<div class="sectionbox">

### Artefakty

#### Definice:
- Složka zaznamenaného signálu, která nevznikla ve vyštřované části těla a nenese diagnostickou informaci
- Může mít větší amplitudu než vlastní signál
#### Proč jsou artefakty v medicíně kritické?
- Falešně pozitivní nálezy
- Falešně negativní nálezy
- Špatná klinická rozhodnutí
#### Rozdělení:
- **Technické - elektronika, prostředí**
	- **Elektrostatické artefakty:**
		- Způsobené elektrochemickými a elektrostatickými jevy na rozhraní
		- Mechanismus vzniku:
			- Změny na rozhraní elektroda - kůže
		- Příčiny:
			- Vyshlý gel, špatně přilepená elektroda
		- Projev signálu:
			- Pomalý drift zadní linie = pozvolná změna referenční úrovně signálu v čase, která nemá fyziologický původ
	- **Rušení elektrovodnou sítí (50 Hz):**
		- Mechanismu:
			- Kapacitní vazba
			- Elektromagnetická indukce
		- Projev:
			- Sinusový signál
	- **Impulsní rušení:**
		- Krátké náhlé poruchy signálu s velkou amplitudou
		- Zdroje:
			- Motory, relé, digitální obvody
		- Proč je to problém, když je poznám?
			- Impulsy mají široké frekvenšní spektrum a špatně se filtrují, tudíž mohou maskovat QRS komplex a vytvořit falešné špičky
		- Rušivá elektromagnetická pole
		- Šum elektronických prvků
			- Nelye odstranit, ale minimalizovat
			- Tepelný šum:
				- Vzniká pohybem nosičů nábojů - závisí na: 
				  teplotě, odporu
			- Šum polovodičů:
				- Tranzistorz a OZ
			- Kontaktní šum:
				- Přechody, konektory
	- **Biologické - jiné fyziologické procesy organismu:**
		- **Pohybové artefakty:**
			- Mechanismu:
				- Změny tlaku elektrod
				- Mechanické napětí kůže
			- Projev:
				- Vysokofrekvenční oscilace
				- Velká amplituda
			- U EKG při chůzi
			- Vzájemné ovlivňování biologických signálů:
				- EMG ruší EEG, pohyb ruší EEG
				- Biologické artefakty mohou vznikat při vzájemné interferenci fyziologických procesů
		- **Biologické rytmy:**
			- Časový rozsah:
				- $\mathrm{ms}$ - nervová aktivita
				- $\mathrm{s}$ - srdeční rytmus
				- $\mathrm{minuty/hodiny}$ - hormony
				- $\mathrm{dny/roky}$ - cirkadiánní a dlouhodobé rytmy

</div>

</div>

