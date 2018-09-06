<h1>AI_Exercise</h1>
Codice in linguaggio Python atto ad implementare algoritmi di blind search ed heuristic search come risoluzione al problema che prevede di trovare il cammino minimo tra due punti in un piano nel quale sono presenti degli ostacoli poligonali convessi.
<h2>Come usare il codice</h2>
Il programma prevede come interfaccia utente un menù che sulla base del valore di input inserito permette di eseguire una funzionalià piuttosto che l’altra.  Il menù consente:
<ul>
<li>Inserendo  il  valore  1  di  eseguire  tutti  gli  algoritmi  implementati  su  una  stessa  istanza  del  problema.  Dopo l’esecuzione di ciascun algoritmo viene mostrata come output la simulazione dell’avanzamento del robot per via grafica nel processo che lo porta dallo stato iniziale allo stato obiettivo attraverso la sequenza di azioni relativa alla soluzione trovata (se appunto una soluzione viene trovata).  Se invece l’algoritmo non trova soluzione viene stampato il messaggio ’Soluzione non trovata’.</li>
<li>Inserendo il valore 2 di eseguire un certo algoritmo per un dato numero di volte, ciascuna volta su di una diversa istanza del problema.  Al termine dell’esecuzione dell’esperimento viene visualizzata come output la media dei seguenti parametri:  profondità e costo della soluzione, memoria utiizzata e tempo richiesto per calcolarla.</li>
<li>Inserendo qualsiasi valore diverso da 1 o da 2 di uscire e chiudere il programma.</li>
</ul>

<h2>Implementazione</h2>
Il codice del programma `e suddiviso in 4 file: 'Robot.py’, ’search.py’, ’utils.py’ e ’main.py’.
<h3>Search.py</h3>
Tale file contiene l’implementazione delle classi Problem e Node, le quali forniscono l’interfaccia di base del 
problema e dei nodi, e delle varie funzioni che implementano gli algoritmi di searching .
Per quanto riguarda tali algoritmi, sono implementati:  breadth first tree,  breadth
first graph, depth first tree, depth first graph, depth limited, iterative deepening, greedy best first graph
ed A*.  Per l'implementazione, sono definite due funzioni generiche tree_search(problem,fringe) e graph_search(problem,fringe) che definiscono il codice per l'esecuzione degli algoritmi di ricerca su albero e su grafo. Tali funzioni sono poi 
invocate dalle funzioni relative ai vari algoritmi sopra citati, le quali, a seconda della tecnica da questi prevista, passano come parametro un tipo di coda piuttosto che un'altra. (BFS usa una coda FIFO, DFS stack, e cosi via). Le classi relative alle code sono definite nel file utils.py.

Le  classe  Problem  ha  due  attributi,  lo  stato  inziale  e  quello  obiettivo,  e  fornisce  l’implementazione
di default dei metodi successor(self,state) , goaltest(self, state) e pathcost(self, c, state1, action, state2), il quale restituisce il costo c incrementato di 1.  

La classe Node ha gli attributi state, parent, action, depth
e  pathcost  che  caratterizzano  ciascun  nodo  e  fornisce  l’implementazione  dei  metodi __repr__(self), path(self) che ricostruisce il cammino che porta dal nodo iniziale al nodo in questione ed infine il metodo expand(self, problem) il quale
restituisce un array contenente tutti i nodi successori del nodo in questione (generati attraverso chiamata
al metodo successor(self,state) definito nella classe Robot in ’Robot.py’).

Per la compilazione di tale file sono necessari i package: psutil, sys, os e time.


<h3>Robot.py</h3>
In questo file sono definite le classi Robot e RoboState.

La classe Robot eredita dalla classe Problem presente definita nel file search.py. Tale classe possiede anche un attributo
dictActions che è un dizionario che associa ad ogni punto un array contenente tutti i suoi punti vicini. 
Nella classe vi è una ridefinizione dei metodi goal_test(self, state) in cui il confronto confronta le coordinate degli 
stati e path_cost(self, c, state1, action, state2) in cui il costo dell'azione action (che rappresenta il punto in cui 
l'agente si sposta) è considerato come la distanza in linea d'area  tra lo stato state1 e lo stato state2 (calcolata usando la funzione distance in utils.py). (L'azione è rappresentata dal punto in cui ci si sposta eseguendo l'azione stessa).
Il metodo getActions(self,state), riceve un oggetto RobotState state e ricerca in dictActions il punto associato
a state per poi restituire l'array di punti vicini ad esso associato; h(self,node) restituisce la distanza tra il punto
associato a node ed quello associato al goal, invocando il metodo h definito nella classe RobotState; successor(self,state)
restituisce le coppie (actions,nexts) per ogni stato nexts generato attraverso l'azione actions.

La classe RobotState definisce lo stato del robot contraddistinto dalle coordinate x ed y del piano. Implementa i metodi move(self,point) che restituisce il nuovo stato avente point come coordinate ed h(self,goal) che calcola il valore della funzione euristica: distanza in linea d'area tra il punto relativo allo stato ed il goal.

<h3>Utils.py<h3>
In questo file sono definite le classi ed i metodi ausiliari. Più precisamente, vi sono le implementazioni relative alle code (vedere fonti) ed ad alcuni metodi utili al fine di generare gli elementi necessari per l'istanziazione del problema ed a stampare i risultati per via grafica.

Per gli elementi necessari ad istanziare il problema vi sono le seguenti funzioni:
<ul>
  <li>generateRandomPoints(num,min=0,max=10): restituisce array con num punti generati casualmente aventi range [min,max]</li>
  <li>searchInitialPoint(points) e searchGoalPoint(points): ricevuti i punti points generati, restituiscono come punto inziale quello avente ascissa minore e come goal quello avente ascissa maggiore.></li>
  <li>createDict(points,vertices): ricevuto un oggetto del tipo dell'oggetto restituito dal metodo Delauney della libreria scipy.spatial, restituisce un dizionario che associa a ciascun punto di points un array contenente tutti i suoi vicini secondo la suddivisione del piano effettuata dal metodo Delauney.</li>
</ul>

Per la stampa dei risultati: printResult(dictlines,result,algoritmo,points,problem) esegue una stampa dei risultati mostrando una simulziaone dell'avanzamento del robot per via grafica. Usa le funzioni searchMinX, searchMaxX, searchMinY e searchMaxY, il dizionario dictlines che associa a ciascun punto i suoi vicini ed appunto points contenente l'array dei vari punti, per generare il piano con presenti i vari poligoni convessi che lo suddividono. Attraverso pyplot della libreria matplotlib, si aggiungono iterativamente le linee relative allo spostamento del robot secondo la soluzione trovata, la quale è specificata dal parametro results.

Per la compilazione di tale file sono necessari i package: math,bisect,random e matplotlib.

<h3>Main.py</h3>

In tale file vi è l' implementazione del menù il cui funzionamento è spiegato nel paragrafo relativo all'utilizzo del codice. Si noti che nonostante in Robot.py vi sia l'implementazione dell'algoritmo DFS Tree, questo non viene invocato dalla classe main poichè per il problema in questione questo raramente riesce a trovare una soluzione.

Si noti inoltre che per creare gli ostacoli oligonali convessi e dividere così il piano, viene usato il metodo Delauney della libreria scipy.spatial. 

Per compilare il file è quindi necessario il package scipy.spatial, oltre a: os, time e psutil. 


<h2>Sources</h2>
Per l'implementazione delle classi Problem e Node nel file search.py, per quelle relative all'implementazione degli algoritmi di searching nello stesso file ed anche per quella delle code nel file utils.py, si è fatto riferimento al codice presente al link http://ai.dinfo.unifi.it/teaching/ai_2017.html. 
