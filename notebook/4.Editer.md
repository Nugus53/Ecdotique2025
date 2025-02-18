Une fois la transcription éffectué, puis l’alignement on souhaites pourvoir éditer le contenus en choissant la leçons retuenu ou encore ajouter des notes.


---

## TEI Universe

---
### Oxygen branch
> **OxygenXML**
> > **Lien** :[www.oxygenxml.com](https://www.oxygenxml.com/)

Ajout spécifique :

> **ediarum**
> > **Lien** :[https://www.ediarum.org/module.html](https://www.ediarum.org/module.html)
---
### XmlMind branch

> **XmlMind**
> > **Lien** :[www.xmlmind.com](https://www.xmlmind.com/xmleditor/)

Ajout spécifique :
> **XMLmind-editor pour l’édition critique**
> > **Lien** :[https://mrsh.unicaen.fr/editer-des-sources-avec-apparat-critique/](https://mrsh.unicaen.fr/editer-des-sources-avec-apparat-critique/)


---
### Autres Outils 

> **Apatosaurus**
> > **Lien** :[https://apatosaurus.io](https://apatosaurus.io)


> **TEI Critical Apparatus Toolbox**
> > **Lien** :[http://teicat.huma-num.fr/](http://teicat.huma-num.fr/)

---

> **ChrysoCollate**
> > **Lien** :[https://cental.uclouvain.be/chrysocollate/](https://cental.uclouvain.be/chrysocollate/)


> **Classical Text Editor**
> > **Lien** :[https://cte.oeaw.ac.at](https://cte.oeaw.ac.at)

Introduction à Latex

c'est un fichier qui est compiler à la l'aide d'un processeur :

- pdfTEX
- LaTeX
- XeLaTeX
- LuaLaTex

En fonction de votre système d'exploitation vous pouvez intaller les outils suivant pour éditer Latex


template pour les outils :

## Outils pour éditer LaTeX selon votre système d'exploitation

---

> **TeXworks**  
> > **Description** : Éditeur simple et intégré pour LaTeX  
> > **Lien** : [https://www.tug.org/texworks/](https://www.tug.org/texworks/)  

> **TeXstudio**  
> > **Description** : Environnement de développement LaTeX avec nombreuses fonctionnalités avancées  
> > **Lien** : [https://www.texstudio.org/](https://www.texstudio.org/)  

> **MiKTeX**  
> > **Description** : Distribution LaTeX complète avec éditeur intégré  
> > **Lien** : [https://miktex.org/](https://miktex.org/)  

> **TeXShop**  
> > **Lien** : [https://pages.uoregon.edu/koch/texshop/](https://pages.uoregon.edu/koch/texshop/)  

> **MacTeX**   
> > **Lien** : [https://tug.org/mactex/](https://tug.org/mactex/)

> **MiKTeX**  
> > **Lien** : [https://miktex.org/](https://miktex.org/)  

> **Kile**  
> > **Lien** : [https://kile.sourceforge.io/](https://kile.sourceforge.io/)  

> **Gummi**   
> > **Lien** : [https://github.com/alexandervdm/gummi](https://github.com/alexandervdm/gummi)  

> **TeXmaker**   
> > **Lien** : [https://www.xm1math.net/texmaker/](https://www.xm1math.net/texmaker/)  

> **MiKTeX**    
> > **Lien** : [https://miktex.org/](https://miktex.org/)  
---

### **editeur en Ligne :**

> **Overleaf**  
> > **Lien** : [www.overleaf.com](https://www.overleaf.com)  

> **PLMLatex**  
> > **Lien** : [plmlatex.math.cnrs.fr](https://plmlatex.math.cnrs.fr/)


template de base :
```latex
 \documentclass{book}
 \begin{document}
 
 \end{document}
```

- **Environnement** : Un environnement délimité par `\begin{}` et `\end{}`.
- **Commande** : Une instruction qui commence par un antislash (`\`) pour réaliser une action spécifique.
- **Arguments** : entre `{}` pour ceux qui sont obligatoire  et entre `[]` pour les optionel

```latex
%Ceci est un Environnement
\begin{}
\end{}

%Examples:
\begin{itemize}
    \item Premier élément
    \item Deuxième élément
\end{itemize}
```

```latex
%Ceci est une Commande 
\command

%Examples:
\textbf{Texte en gras}
\textit{Texte en italique}
```


Onpeux venir ajoter des paquets spécifiques 
```latex
\documentclass{book}
\usepackage{}
```


[↳Sortie en PDF](pdf/demo_simple.pdf) [↳Fichier .Tex](latex/simple.tex)

### **Pour débuter:**
> > **Lien** : [overleaf-learn](https://www.overleaf.com/learn)

### **package specifique :**

> **ekdosis**  
> > **Lien** : [www.ekdosis.org](https://www.ekdosis.org/fr/)

[↳Sortie en PDF](pdf/demo_1.pdf) [↳Fichier .Tex](latex/demo_1.tex)

> **bibleref-french**  
> > **Lien** : [bibleref-french](https://ctan.org/pkg/bibleref-french/)
> > 
> > **Lien** : [bibleref](https://ctan.org/pkg/bibleref)

[↳Sortie en PDF](pdf/demo_bibleref.pdf) [↳Fichier .Tex](latex/demo_bibleref.tex)



Combiné les package :

[↳Sortie en PDF](pdf/demo_2.pdf) [↳Fichier .Tex](latex/demo_2.tex)
