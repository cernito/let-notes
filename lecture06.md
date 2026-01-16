---
title: "**Zesilovače biologických signálů**"
author: "Tomáš Černík"
---

<div class="sections">


-   Typicky mají signály velmi malé amplitudy a jsou snadno rušitelné

-   Příklady:

-   EKG -- amplituda 0.5-5 mV

-   EEG -- amplituda řádově mikrovolty

-   EMG -- amplituda 0.1-10 mV

<div class="sectionbox">

## Požadavky na zesilovače


-   Dostatečné zesílení

-   Potlačení souhlasného signálu

-   Rušení, které se objeví stejně na obou vstupech (síťové)

-   Vysoký vstupní odpor

-   Aby zesilovač nezatěžoval zdroj signálu a neovlivnil měření

-   Požadovaný frekvenční rozsah

-   Odolnost proti rušení

-   Odolnost proti špatnému připojení elektrod


</div>

<div class="sectionbox">

## Operační zesilovač -- základní prvek


-   Univerzální integrovaný zesilovač

-   Má dva vstupy -- invertující a neinvertující

-   Jeden výstup

-   Pracuje se zpětnou vazbou

-   Je napájen nejčastěji symetrickým napětím +- Ucc

-   **Ideální operační zesilovač**

-   Nekonečné zesílení rozdílového napětí

-   Nulové zesílení souhlasného napětí

-   Nulový vstupní odpor

-   Nulové vstupní proudy

-   **Reálný OP**

-   Zesílení je konečné

-   Zesílení souhlasného signálu není nulové

-   Vstupní odpor je velmi velký, ale konečný

-   Existují vstupní proudy

-   **Napájení**

-   Nejčastěji symetrické +- 3V až 15

-   Rozsah napájení určuje:

-   Povolený rozsah vstupních napětí

-   Maximá


</div>

<div class="sectionbox">

## Zapojení


1)  **Invertující**

![Obsah obrázku diagram, skica, řada/pruh, Technický výkres Obsah
generovaný pomocí AI může být
nesprávný.](media/image1.png){width="1.9009820647419073in"
height="1.4533672353455818in"}

2)  **Neinvertující zesilovač**

![Obsah obrázku diagram, skica, Technický výkres, Plán Obsah generovaný
pomocí AI může být
nesprávný.](media/image2.png){width="2.701496062992126in"
height="1.5183103674540683in"}


</div>

<div class="sectionbox">

## Hlavní zdroje chyb


-   Nenulové vstupní proudy

-   Napěťový offset

![Obsah obrázku diagram, skica, řada/pruh, Technický výkres Obsah
generovaný pomocí AI může být
nesprávný.](media/image3.png){width="2.868218503937008in"
height="1.940265748031496in"}


</div>

<div class="sectionbox">

## Kompenzace chyb


![](media/image4.png){width="2.9178455818022746in"
height="1.0593853893263343in"}![Obsah obrázku diagram, řada/pruh,
Technický výkres, skica Obsah generovaný pomocí AI může být
nesprávný.](media/image5.png){width="3.7481780402449694in"
height="2.3437740594925636in"}

-   Druhý zdroj chyby je napěťový offset Uoff a ten je dán vnitřní
nesymetrií OZ

-   Řeší se dle výrobce OZ -- pomocí trimru


</div>

<div class="sectionbox">

## Odstranění vlivu odporu zdroje


![Obsah obrázku text, diagram, řada/pruh, Technický výkres Obsah
generovaný pomocí AI může být
nesprávný.](media/image6.png){width="3.463742344706912in"
height="1.869811898512686in"}

-----------------------------------------------------------------------

</div>

<div class="sectionbox">

## Typ chyby**        **Lze kompenzovat rezistorem?** **Proč

-------------------- ------------------------------- ------------------
Vstupní proudy OZ    ✅ ano                          jsou vlastností OZ

Napěťový offset      ⚠️ částečně                     trimr / typ OZ

Vnitřní odpor zdroje ❌ ne                           je mimo OZ
-----------------------------------------------------------------------


</div>

<div class="sectionbox">

## Měření rozdílových signálů


-   Měří se jako rozdíl napětí mezi 2 elektrodami v biologických
signálech a na obou elektrodách se objevuje užitečný signál a rušení
společně pro oba vstupy

-   Cílem je zesílit rozdíl a potlačit souhlasnou složku

-   Musí platit Au+ = Au-

![Obsah obrázku diagram, skica, Technický výkres, Plán Obsah generovaný
pomocí AI může být
nesprávný.](media/image7.png){width="2.880893482064742in"
height="1.6942825896762905in"}

![](media/image8.png){width="2.4331397637795273in"
height="0.6376038932633421in"}![Obsah obrázku text, diagram, Písmo,
řada/pruh Obsah generovaný pomocí AI může být
nesprávný.](media/image9.png){width="3.0071620734908135in"
height="1.994915791776028in"}


</div>

<div class="sectionbox">

## Souhlasný a rozdílový signál -- definice


-   Souhlasný signál -- napětí, které je na obou vstupech stejné

![Obsah obrázku Písmo, text, bílé, typografie Obsah generovaný pomocí AI
může být nesprávný.](media/image10.png){width="1.7176607611548556in"
height="0.5962128171478566in"}

-   Rozdílový signál -- užitečný signál

![Obsah obrázku typografie, Písmo, kaligrafie, rukopis Obsah generovaný
pomocí AI může být
nesprávný.](media/image11.png){width="1.5073720472440946in"
height="0.38000984251968506in"}

![Obsah obrázku Písmo, text, bílé, design Obsah generovaný pomocí AI
může být nesprávný.](media/image12.png){width="1.8391338582677166in"
height="1.0466119860017498in"}

![](media/image13.png){width="0.5545702099737533in"
height="0.3455391513560805in"}![](media/image14.png){width="1.226809930008749in"
height="0.30225721784776904in"}**Zesílení souhlasné a rozdílové složky**

![Obsah obrázku text, Písmo, diagram, snímek obrazovky Obsah generovaný
pomocí AI může být
nesprávný.](media/image15.png){width="3.3204494750656166in"
height="1.5822637795275591in"}


</div>

<div class="sectionbox">

## Potlačení souhlasné složky


-   Míra potlačení souhlasného signálu se určuje parametrem CMMR

-   ![Obsah obrázku Písmo, text, bílé, kaligrafie Obsah generovaný
pomocí AI může být
nesprávný.](media/image16.png){width="1.7329286964129484in"
height="0.5096850393700787in"}

-   Čím větší, tím lepší zesilovač

-   Prakticky alespoň 80 dB


</div>

<div class="sectionbox">

## Vliv odporů elektrod Ri1 a Ri2


![Obsah obrázku diagram, Technický výkres, Plán, řada/pruh Obsah
generovaný pomocí AI může být
nesprávný.](media/image17.png){width="3.999446631671041in"
height="1.8448151793525809in"}

Řešení pomocí oddělení vstupů sledovačem signálu nebo neinvertujícím
zesilovačem:

![Obsah obrázku diagram, Technický výkres, Plán, řada/pruh Obsah
generovaný pomocí AI může být
nesprávný.](media/image18.png){width="5.877038495188102in"
height="3.4153160542432195in"}

-   A1 a A2 zapojeny jako sledovače napětí

-   Zesílení Aa1 = Aa2 = 1

-   Díky A1 a A2 jsou Ri1 a Ri2 odděleny od zbytku zesilovače

![Obsah obrázku diagram, Technický výkres, Plán, schématické Obsah
generovaný pomocí AI může být
nesprávný.](media/image19.png){width="6.3in"
height="3.1284722222222223in"}

-   A1 a A2 jsou vstupní zesilovače zapojeny jako neinvertující a jejich
úloha je zesílit signál ještě přes rozdílovým zesilovačem

-   A3 je rozdílový zesilovač a provádí vlastní odečtení signálu a při
volbě R1=R3 a R2=R4 má rozdílové napětí: ADif, A3 = R2/R1

-   Při symetrické volbě rezistorů:

![Obsah obrázku text, Písmo, rukopis, bílé Obsah generovaný pomocí AI
může být nesprávný.](media/image20.png){width="2.9713363954505687in"
height="0.789167760279965in"}


</div>

<div class="sectionbox">

## Přístrojový zesilovač


-   Zesilovač určený pro přesné měření velmi malých rozdílových signálů
-- EKG, EEG, EMG

-   **Vlastnosti:**

-   Vysoký vstupní odpor

-   Potlačení souhlasné složky

-   Stabilní a přesně definované zesílení

![](media/image21.png){width="1.4470975503062118in"
height="0.36585520559930007in"}![](media/image22.png){width="2.161851487314086in"
height="0.5079538495188102in"}![Obsah obrázku text, diagram, Plán,
Technický výkres Obsah generovaný pomocí AI může být
nesprávný.](media/image23.png){width="3.8052668416447943in"
height="2.61794728783902in"}

-   Elegantní řešení -- zesílení se mění jedním prvkem a je zachována
dokonalá symetrie vstupů

pletysmografie

-   Metoda měření změn objemu tkání, nejčastěji vlivem:

-   Průtoku krve

-   Dýchání

-   **Fotopletysmografie**

-   Optická varianta

-   Sleduje změny odrazu nebo průchodu světla tkání a odraz se liší
v závislosti na prokrvení tkáně dle tepu a barvě krve dle
okysličení

-   Pulzní oxymetrie

-   Dvě vlnové délky (červená a infračervená)

-   Sleduje se změna absorpce podle okysličení krve

-   Otický snímač

-   Tvořen infračervenou LED a fotodiodou (detektor)

-   Pracuje v hradlovém režimu (fotoproudovém) -- při osvětlení
dodává proud úměrný intenzitě světla

-   Proud z fotodiody nelze měřit přímo napěťovým zesilovačem --
proto přiveden jako převodník proud-napětí

-   Strmost převodu je dána hodnotami 100 kohm, 220, 320

-   Kondenzátor ve zpětné vazbě zlepšuje stabilitu


</div>

</div>