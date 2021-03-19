# Générateur

![code size](https://img.shields.io/github/languages/code-size/Madjakul/ESILV-PTS/tree/main/generator)
___

Considérons un arbre où à la racine, se trouve l'état résolu du cube. A partir de cette racine, nous pouvons générer 8 états voisins. Un voisin est un  état du cube ateignable à l'aide d'une seule rotation. En effet, nous n'avons qu'a modifier chacun des 4 sommets de la face opposée à celle résolue lors de la phase 1. Chaque sommet peut tourner dans deux sens différents, nous avons donc 8 états voisin à générer. Ces 8 états voisins seront donc de nouveaux noeuds du graph, qui seront reliés (de manière non-orienté) à la racine (qui devient de fait le parent de ces 8 nouveaux noeuds).  On répète l'opération pour chaque noeud jusqu'à arriver à  1 632 960 noeuds uniques.

![](assets/images/graph.png)


## Prérequis

* Python 3.8+


## Utiliser notre générateur

### Linux et MAC OS

A partir du dossier ```generateur```
```bash
python3 treeCreator.py
```


### Windows

A partir du dossier ```generateur``` , via votre terminal favori
```shell
py treeCreator.py
```


### Docker

A partir du dossier ```generateur``` , via votre terminal favori
```bash
docker build -t treeCreator:latest .
docker run -it miniproblem1
```


[TLimnavong]: https://github.com/TLimnavong
[MIT]: https://github.com/Madjakul/ESILV-DataAnalysis/blob/main/LICENSE