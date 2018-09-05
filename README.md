<h1>AI_Exercise</h1>
Codice atto ad implementare algoritmi di blind search ed heuristic search come risoluzione del problema che prevede di trovare il cammino minimo tra due punti in un piano nel quale sono presenti degli ostacoli poligonali convessi.
<h2>Come usare il codice</h2>
Il programma prevede come interfaccia utente un menù che sulla base del valore di input inserito permette di eseguire una funzionalià piuttosto che l’altra.  Il menù consente:
<ul>
<li>Inserendo  il  valore  1  di  eseguire  tutti  gli  algoritmi  implementati  su  una  stessa  istanza  del  problema.  Tale istanza prevede una suddivisione del piano attraverso il metodo Delauney della libreria scipy.spatial  usando  un  insieme  di  punti  generati  casualmente  ed  il  cui  numero  e  range  di  valori delle coordinate sono immessi come input dall’utente.  Dopo l’esecuzione di ciascun algoritmo viene mostrata come output la simulazione dell’avanzamento del robot per via grafica nel processo che lo porta dallo stato iniziale allo stato obiettivo attraverso la sequenza di azioni relativa alla soluzione trovata (se appunto una soluzione viene trovata).  Se invece l’algoritmo non trova soluzione viene stampato il messaggio ’Soluzione non trovata’.</li>
<li>Inserendo il valore 2 di eseguire un certo algoritmo per un dato numero di volte, ciascuna volta su di una diversa istanza del problema il quale per ogni esperimento viene istanziato allo stesso modo del punto sopra.  Al termine dell’esecuzione dell’esperimento viene visualizzata come output la media dei seguenti parametri:  profondità e costo della soluzione, memoria utiizzata e tempo richiesto.</li>
<li>Inserendo qualsiasi valore diverso da 1 o da 2 di uscire e chiudere il programma.</li>
</ul>

<h2>Implementazione</h2>
Il codice del programma `e suddiviso in 4 file:  Robot.py’ ’search.py’, ’utils.py’ e ’main.py’.
<h3>Search.py</h3>
Tale file contiene l’implementazione delle classi Problem e Node che forniscono l’interfaccia di base del 
problema e dei nodi e le varie funzioni che implementano gli algoritmi di searching.Le  classe  Problem 
ha  due  attributi,  lo  stato  inziale  e  quello  obiettivo,  e  fornisce  l’implementazione
di default dei metodi successor(self,state) che fornisce i successori dello stato state, goaltest(self, state)
che confronta state col goal per verificare se state `e un obiettivo pathcost(self, c, state1, action, state2)
che restituisce il costo c incrementato di 1.  La classe Node ha gli attributi state, parent, action, depth
e  pathcost  che  caratterizzano  ciascun  nodo  e  fornisce  l’implementazione  dei  metodirepr(self)  che
fornisce la stringa di output da fornire nel caso in cui si stampi un nodo,  path(self) che ricostruisce il
cammino che porta dal nodo iniziale al nodo in questione, d infine il metodo expand(self, problem) il quale
restituisce un array contenente tutti i nodi successori del nodo in questione (generati attraverso chiamata
al metodo successor(self,state) definito nella classe Robot in ’Robot.py’).
Per quanto riguarda gli algoritmi di search,  si `e scelto di implementare:  breadth first tree,  breadth
first graph, depth firsttree, depth first graph, depth limited, iterative deepening, greedy best first graph
ed A*.  Si sono definite due funzioni generiche treesearch(problem,fringe) e graphsearch(problem,fringe)
che definiscono  i generici algoritmi di ricerca su albero e su grafo.  Si  sono poi  definite  le funzioni che
le utilizzano passandogli una coda piuttosto che un’altra cos`ı da implementare una DFS (attraverso una
coda  di  tipo  Stack())  piuttosto  che  una  BFS  (con  coda  FIFO).  Per  gli  algoritmi  di  heuristic  search ho
utilizzato  una  coda  con  priorit`a.   L’implementazione  delle  code  si  trova  nel  file  ’utils.py’,  quindi  per
approndidre su di essa si rimanda al paragrafo relativo a tale file.

<h3>Robot.py</h3>
In questo file sono definite le classi Robot e RoboState.

La classe Robot eredita dalla classe Problem presente definita nel file search.py. Tale classe possiede anche un attributo
dictActions che è un dizionario che associa ad ogni punto un array con i suoi punti vicini. 
Nella classe vi è una ridefinizione dei metodi goal_test(self, state) in cui il confronto confronta le coordinate degli 
stati e path_cost(self, c, state1, action, state2) in cui il costo dell'azione action (che rappresenta il punto in cui 
l'agente si sposta) è considerato come la distanza in linea d'area tra lo stato state1 e lo stato state2,
distanza calcolato usando la funzione distance in utils.py.
Il metodo getActions(self,state), riceve un oggetto RobotState state e ricerca in dictActions il punto associato
a state per poi restituire l'array di punti vicini ad esso associato; h(self,node) restituisce la distanza tra il punto
associato a node ed quello associato al goal, invocando il metodo h definito nella classe RobotState; successor(self,state)
restituisce le coppie (actions,nexts) per ogni stato nexts generato attraverso l'azione actions.
