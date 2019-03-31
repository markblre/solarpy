# solarpy

Solarpy est une simulation de système solaire entièrement programmée en Python dans le cadre de l'épreuve du bac d'ISN. Ce projet est donc un travaille en collaboration avec un camarade.

Le programme vous permet d'observer le système solaire en vous déplacent dans l'espace grâce aux touches de votre clavier. Vous pouvez choisir au lancement du programme quelles planètes vous voulez afficher et la date à laquelle vous voulez les observer.
Lors du lancement de la simulation, vous êtes à une distance du soleil qui vous permet de voir la planète la plus éloignée. Vous pouvez ensuite zoomer pour afficher les planètes les plus proches du soleil. La taille des planètes ainsi que l'éloignement entre celles-ci est proportionnelle à la réalité. En revanche, la taille du soleil est adaptée.

Les modules utilisés sont:
  - tkinter
  - pyOpenGL
  - Pillow
  - numpy
  - pygame
  - skyfield
  
Ces modules sont donc nécessaires pour éxécuter correctement la simulation.

Pour lancer la simulation, il faut exécuter le programme "solarpy.py".
 
Les touches de déplacement sont:
    w --> zoom arrière
    x --> zoom avant
    e --> rotation négative sur l'axe X
    r --> rotation positive sur l'axe X
    d --> rotation négative sur l'axe Y
    f --> rotation positive sur l'axe Y
    c --> rotation négative sur l'axe Z
    v --> rotation positive sur l'axe Z
    
    (Ces touches sont modifiables dans le code "simulation.py")
 
Avertissements:
    - La simulation met du temps à charger les textures lors de son lancement. Un écran noir est affiché durant toute la durée du chargement. Il suffit d'attendre de voir les planètes s'afficher.


   /!\ Ne lancez pas le programme en plein écran après modification ou dès la première exécution car en cas d'erreur il sera impossible de quitter le programme. Pour désactiver le plein écran, décochez la case correspondante dans la première interface qui apparait.
