# solarpy

Solarpy est une simulation de système solaire entièrement programmée entièrement en Python. Ce projet est un travail en collaboration avec un camarade.

Le programme vous permet d'observer le système solaire en vous déplacent dans l'espace grâce aux touches de votre clavier. Vous pouvez choisir au lancement du programme quelles planètes vous voulez afficher et la date à laquelle vous voulez les observer.
Lors du lancement de la simulation, vous êtes à une distance du soleil qui vous permet de voir la planète la plus éloignée. Vous pouvez ensuite zoomer pour afficher les planètes les plus proches du soleil. La taille des planètes ainsi que l'éloignement entre celles-ci est proportionnelle à la réalité. En revanche, la taille du soleil est adaptée.


# Prérequis pour lancer le programme:
  - Pillow (https://pillow.readthedocs.io/en/stable/installation.html)
  - Numpy (https://pypi.org/project/numpy/)
  - Pygame (https://pypi.org/project/pygame/)
  - pyOpenGL (http://pyopengl.sourceforge.net)
  - Skyfield (https://rhodesmill.org/skyfield/installation.html)
  
  
# Utilisation du programme:
  - Exécutez le programme "solarpy.py"
  - Vous arrivez sur une fenêtre de paramétrage comme celle ci-dessous où vous choisissez les paramètres d'affichages, les planètes que vous voulez afficher, la date du début de la simulation et la vitesse d'évolution de celle-ci. Vous pouvez aussi lancer la simulation à la date actuelle en cliquant sur le bouton prévu pour cette action.
  ![capture fenêtre simulation 1](https://user-images.githubusercontent.com/46789972/55513635-77ea2f80-5666-11e9-941e-88186a0a5124.png)
  - Lors du lancement de la simulation, une nouvelle fenêtre s'ouvre et le système solaire s'affiche avec les paramètres que vous avez précisé précédemment et un éloignement du centre suffisant pour voir la planète la plus éloignée du soleil. (Capture d'écran ci-dessous)
  ![capture fenêtre simulation 1](https://user-images.githubusercontent.com/46789972/55514387-39557480-5668-11e9-9c01-ee55d80fc8e9.png)
  - Vous pouvez ensuite zoomer ou effectuer des rotations autour du soleil grâce aux touches de votre clavier. (Exemples ci-dessous)
  ![capture fenêtre simulation 2](https://user-images.githubusercontent.com/46789972/55514598-d44e4e80-5668-11e9-8785-fac277b91845.png)
  ![capture fenêtre simulation 3](https://user-images.githubusercontent.com/46789972/55514614-ddd7b680-5668-11e9-8836-a3e8e01a300b.png)

# Remerciements:
  - Toutes les images et textures du logiciel sont issues du site: https://www.solarsystemscope.com/textures/
  - Travaux qui ont servi pour créer les sphères et les trajectoires: http://fab.cba.mit.edu/classes/864.11/people/Moritz_Kassner/
  - Forum qui a servi pour les textures: https://stackoverflow.com/questions/43033625/why-my-texture-is-not-showing-pyopengl/43038405#43038405
