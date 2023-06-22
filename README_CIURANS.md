## Endpoints

### Articles de la col·lecció

El llistat d'articles que es mostra quan accedeixes a una col·lecció s'obté a
través d'un endpoint que accepta filtres.

Endpoint:

    /custom_api/collection_items/?page=4

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

    /custom_api/history_items/?page=4

Si no es passa el valor `page`, retornarà tots els items en tots els idiomes.
Pots saber el valor de page amb {{ self.id }} o {{ page.id }}.

### Vídeos a Qui Som

    /custom_api/video_items/?page=4

Si no es passa el valor `page`, retornarà tots els vídeos en tots els idiomes.
Pots saber el valor de page amb {{ self.id }} o {{ page.id }}.
