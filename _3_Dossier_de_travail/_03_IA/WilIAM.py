# (X1 ; Y1) = les coordonée de l'alpha
# (X2 ; Y2) = les coordonée du loup à déplacer

X1 =  # position x de l'Alpha
Y1 =  # position y de l'Alpha
X2 =  # position x du loup qui se déplace
Y2 =  # position y du loup qui se déplace

if Y1 > Y2 + 1:
    Y2 = Y2 + 1
if Y1 < Y2 - 1:
    Y2 = Y2 - 1

if Y1 == Y2 + 1:
    if  # il y a au moins 3 loups sur la ligne Y1-1, et toujours plus de trois loup après que les déplacement précédement enregistré ou futur
       if  # il y a plus de loup du coté de l'alphe, droite ou gauche, du loup à déplacer que de l'autre, et ce, toujours après que les déplacement précédement enregistré ou futur
           if  # le loup est le plus à l'extrémité
              Y2 = Y2 + 1

if Y1 == Y2 - 1:
    if  # il y a déjà au moins 3 loups sur la ligne Y1+1, et toujours plus de trois loup après que les déplacement précédement enregistré ou futur
       if  # il y a plus de loup du coté de l'alphe, droite ou gauche, du loup à déplacer que de l'autre, et ce, toujours après que les déplacement précédement enregistré ou futur
           if  # le loup est le plus d'un l'extrémité
              Y2 = Y2 - 1

if Y1 == Y2:
    # il y a deux loup du coté même coté (X) de l'alpha, et ce, toujours après que les déplacement précédement enregistré ou futur
    if
       # il y a plus de loup en haut (Y > Y1) que en bas (Y < Y1), et ce, même aprèes les déplacement précédement enregistré ou futur
       if
          Y2 = Y2 - 1
        else:
            Y2 = Y2 + 1

if X1 > X2 + 1:
    X2 = X2 + 1
if X1 < X2 - 1:
    X2 = X2 - 1

if X1 == X2 + 1:
    if  # il y a au moins 3 loups sur la ligne X-1, et toujours plus de trois loup après que les déplacement précédement enregistré ou futur
       if  # il y a plus de loup du coté de l'alphe, droite ou gauche, du loup à déplacer que de l'autre, et ce, toujours après que les déplacement précédement enregistré ou futur
           if  # le loup est le plus d'un l'extrémité
              X2 = X2 + 1

if X1 == X2 - 1:
    if  # il y a déjà au moins 3 loups sur la ligne X1+1, et toujours plus de trois loup après que les déplacement précédement enregistré ou futur
       if  # il y a plus de loup du coté de l'alphe, droite ou gauche, du loup à déplacer que de l'autre, et ce, toujours après que les déplacement précédement enregistré ou futur
           if  # le loup est le plus d'un l'extrémité
              X2 = X2 - 1

if X1 == X2:
    # il y a deux loup du coté même coté (y) de l'alpha, et ce, toujours après que les déplacement précédement enregistré ou futur
    if
       if  # il y a plus de loup en haut (x > x1) que en bas (x < x1), et ce, toujours après que les déplacement précédement enregistré ou futur
          X2 = X2 - 1
        else:
            X2 = X2 + 1
