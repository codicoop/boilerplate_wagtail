## Endpoints

El llistat d'articles que es mostra quan accedeixes a una col·lecció s'obté a
través d'un endpoint que accepta filtres.

Endpoint:

    /api/collection_items/

Per consultar quins filtres hi ha disponibles i com s'han de passar els paràmetres,
obre l'endpoint al navegador. En aquest projecte no hi ha cap Swagger que
resumeixi els endpoints ja que -de moment- només hi ha aquest.

Al navegador hauria d'aparèixer un botó Filters i allà en pots seleccionar diversos,
i veure com modifica la URL.

La imatge de cada article es genera en dues mides diferents, configurades així:

    image_thumbnail = "width-700"
    image_maximized = "width-1500"

