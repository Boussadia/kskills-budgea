From : http://www.kskills.com/Tests/PublicProblem/2949

Vous souhaitez analyser vos revenus et dépenses passés afin de déterminer quels sont les mouvements récurrents chaque mois.

 

Pour cela, vous avez extrait tous les mouvements de chacun des derniers mois. Chaque mouvement est composé d'un nom et d'un montant. Un mouvement est considéré comme récurrent s'il est présent dans chaque relevé mensuel (le nom et le montant doivent être identiques chaque mois).

 

Attention : Une ou plusieurs des dernières lettres d'un nom peuvent être remplacées par un point. Ces noms doivent alors être considérés comme identiques. Il y a obligatoirement au moins 3 lettres avant le point, il n'y a un seul point possible par nom et il sera toujours situé en fin de nom.

Par exemple, le nom "salaire" est considéré comme identique aux noms suivants : salair. salai. sala. sal.

Par contre, il n'est pas considéré comme identique aux noms suivants : sale. (ne commence pas pareil) salaire. (Un point remplace obligatoirement 1 ou plusieurs caractères) sala (pas de point à la fin)

Les mouvements sont triés par nom (ordre alphabétique) puis par montant croissant (si noms identiques).

Vous décidez d'écrire un programme qui prend en entrée la liste des mouvements mensuels et renvoie en sortie le nombre de mouvements récurrents chaque mois, ainsi que la somme de ces mouvements.
Par exemple, si vous avez récupéré les mouvements des 3 derniers mois :

Mois 1:

loyer : -485.00 €
restaurant : -32.50 €
retrait : -40.00 €
salaire : 2300.00 €
Mois 2 :

loyer : -485.00 €
remboursement : 45.68 €
retrait : -60.00 €
retrait : -30.00 €
sal. : 2300.00 €
virement : 700.00 €

Mois 3 :

loyer : -485.00 €
retrait : -40.00 €
salai. : 2300.00 €
Votre fonction devra retourner qu'il y a 2 mouvements récurrents (salaire et loyer) et que la somme de ces mouvements est de 1815.00€ (-485 + 2300). "salaire" est considéré comme récurrent car il y a pour chaque mois une des opérations suivantes :

salaire : 2300.00 €
sal. : 2300.00 €
salai. : 2300.00 €
Programmation Orientée Object appréciée ;)

Entrée de la fonction
La 1ère ligne contient un nombre entier N compris entre 1 et 12 inclus, représentant le nombre de mois d'historique que vous allez analyser.

S'en suivent N lignes contenant les mouvements de chaque mois sous la forme suivante :

Chaque ligne est composée d'entre 1 et 30 mouvements séparés par un espace.
Chaque mouvement est composé d'un nom et d'un montant séparés par un point-virgules tels que :
Le nom du mouvement est composé d'une chaîne de caractères comprenant entre 1 et 30 lettres minuscules et potentiellement 1 point (pas d'espaces ni d'autres caractères de ponctuation que le point, maximum 1 point par chaîne de caractères)
Le montant du mouvement est sous la forme d'un nombre à 2 décimales compris entre -9999.99 et 9999.99 inclus. Le séparateur décimal est un point et les 2 décimales sont toujours affichées, même si le montant est rond (ex. 800.00).
Exemple d'une ligne de mois d'historique : salaire;2300.00 loyer;-485.00 retr.;-40.00

Sortie de la fonction
Votre fonction doit retourner le nombre de mouvements récurrents ainsi que la somme de ces mouvements, séparés par un point-virgule, tels que :

Le nombre de mouvements récurrents doit être un nombre entier égal ou supérieur à 0.
La somme des mouvements doit être un nombre à 2 décimales systématiquement affichées et un point comme séparateur décimal.

Exemple de sortie: 2;1815.00

Exemple

Entrée
3
loyer;-485.00 restaurant;-32.50 retrait;-40.00 salaire;2300.00
loyer;-485.00 remboursement;45.68 retrait;-60.00 retrait;-30.00 sal.;2300.00 virement;700.00
loyer;-485.00 retrait;-40.00 salai.;2300.00

Sortie
2;1815.00
