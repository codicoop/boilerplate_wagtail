## Endpoints

### Articles de la col·lecció

El llistat d'articles que es mostra quan accedeixes a una col·lecció s'obté a
través d'un endpoint que accepta filtres.

Endpoint:

    /api/[ca|es]/collection_items/?page=4

Si no es passa el valor `page`, retornarà tots els articles de totes les col·leccions.

Per consultar quins filtres hi ha disponibles i com s'han de passar els paràmetres,
obre l'endpoint al navegador. En aquest projecte no hi ha cap Swagger que
resumeixi els endpoints ja que -de moment- només hi ha aquest.

Al navegador hauria d'aparèixer un botó Filters i allà en pots seleccionar diversos,
i veure com modifica la URL.

La imatge de cada article es genera en dues mides diferents, configurades així:

    image_thumbnail = "width-700"
    image_maximized = "width-1500"

### Items de la Història a Qui som

    /api/history_items/

### Vídeos a Qui Som

    /api/video_items/

### Posts d'Instagram

    /api/instagram_posts/

## Translations of CollectionItems

CollectionItem hauria d'haver estat un model amb TranslationMixin, però no ha
pogut ser degut a la complexitat de fer el canvi des del punt on és ara el projecte.
També tinc dubtes de si és compatible això amb els ClusterableModel.

L'únic camp que cal en els 2 idiomes és títol, així que l'hem duplicat per poder
tenir la traducció però al marge del sistema de Wagtail.
Els acabats i tipologies, ja va bé que es quedin seleccionats segons la versió
en català, ja que el que fem és mostrar l'acabat o tipologia en l'idioma que toqui.
D'aquesta manera, no cal que tots els articles de cada col·lecció es reassignin
a altres acabats o tipologies.
